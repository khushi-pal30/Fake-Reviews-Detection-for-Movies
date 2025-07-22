from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *
import joblib 

# Create your views here.

def index(request):
    return render(request,'index.html')

def login_page(request):
    error=""
    if request.method == "POST":
        ur = request.POST['uname']
        pd = request.POST['pwd']
        user = auth.authenticate(username=ur,password=pd)
        try:
            if user.is_staff:
                auth.login(request,user)
                error = "no"
            elif user is not None:
                auth.login(request,user)
                return redirect('user_home')
                error = "not"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'login_page.html',d)

def signup(request):
    error = ""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        p = request.POST['pwd']
        gen = request.POST['gender']
        i=request.FILES['image']
        addr=request.POST['address']
        d=request.POST['dob']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Signup.objects.create(user=user,mobile=con,image=i,gender=gen,address=addr,dob=d)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signup.html',d)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    return render(request,'admin_home.html')

def user_home(request):
    return render(request,'user_home.html')

def logout(request):
    auth.logout(request)
    return redirect('/') 

def view_user(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    data = Signup.objects.all()
    d = {'data':data}
    return render(request,'view_user.html',d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_page')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_user')

def add_movie(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    error=""
    if request.method=='POST':
        n = request.POST['mname']
        p = request.POST['hname']
        rt = request.POST['hiname']
        s = request.POST['rdate']
        i = request.FILES['poster']
        try:
            Movie.objects.create(movi_name=n,hero_name=p,heroin_name=rt,rdate=s,image=i)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_movie.html',d)

def view_movie_admin(request):
    data=Movie.objects.all()
    d={'data':data}
    return render(request,'view_movie_admin.html',d)

def view_movie_user(request):
    data=Movie.objects.all()
    d={'data':data}
    return render(request,'view_movie_user.html',d)

def delete_movie(request,id):
    data=Movie.objects.get(id=id)
    data.delete()
    return redirect('view_movie_admin')

def edit_movie(request,id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    data =Movie.objects.get(id=id)
    if request.method=='POST':
        n = request.POST['roomno']
        p = request.POST['hero']
        rt = request.POST['heroin']
        s = request.POST['rdate']
        data.movi_name = n
        data.hero_name = p
        data.heroin_name = rt
        data.rdate = s
        try:
            data.save()
            error="no"
        except:
            error="yes"
    d = {'data':data,'error':error}
    return render(request,'edit_movie.html',d)

def change_poster(request,id):
    if not request.user.is_authenticated:
        return redirect('login_page')
    error=""
    data = Movie.objects.get(id=id)
    if request.method == 'POST':
        l = request.FILES['image']
        data.image = l
        try:
            data.save()
            error="no"
        except:
            error="yes"
    d = {'error': error,'data':data}
    return render(request,'change_poster.html',d)

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passwordadmin.html',d)

def feedback(request):
    if not request.user.is_authenticated:
        return redirect('feedback')
    error=""
    if request.method=='POST':
        n = request.POST['fname']
        p = request.POST['fphone']
        e = request.POST['femail']
        c = request.POST['fcomment']
        try:
            Feedback.objects.create(feedback_name=n,feedback_contact=p,feedback_email=e,feedback_comment=c)
            error = "no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'feedback.html',d)

def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passworduser.html',d)

def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    user = request.user
    data = Signup.objects.get(user=user)
    error=""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        con=request.POST['contact']
        gen=request.POST['gender']

        data.user.first_name = f
        data.user.last_name = l
        data.mobile = con
        data.gender = gen

        try:
            data.save()
            data.user.save()
            error="no"
        except:
            error="yes"

        try:
            i = request.FILES['image']
            data.image = i
            data.save()
            error="no"
        except:
            pass
    d = {'data':data,'error':error}
    return render(request,'user_profile.html',d)

def add_review_user(request,id):
    user=request.user
    data=Movie.objects.get(id=id)
    error=""
    if request.method=='POST':
        s=request.POST['star']
        r=request.POST['review']
        f=user.first_name+' '+user.last_name
        e=user.username
        m=data.movi_name
        if 'not clear' in r or 'audible' in r or 'poor quality' in r or 'dubbing' in r:
            fk='Fake'
        else:
            fk='Real'
        try:
            Review.objects.create(mname=m,fake=fk,star=s,review=r,rname=f,remail=e,rid=id)
            error="no"
        except:
            error="yes"
    d={'data':data,'error':error}
    return render(request,'add_review_user.html',d)

def view_review_user(request,id):
    data=Movie.objects.get(id=id)
    data2=Review.objects.all()
    a=0
    b=0
    for i in data2:
        if int(i.rid)==id:
            a=int(i.star)+a
            b+=1
    a=a//b
    d={'data':data,'data2':data2,'a':a}
    return render(request,'view_review_user.html',d)

def view_feedback(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    data = Feedback.objects.all()
    data2 = Contact.objects.all()
    d = {'data':data,'data2':data2}
    return render(request,'view_feedback.html',d)

def delete_contact(request,id):
    if not request.user.is_authenticated:
        return redirect('login_page')
    feedback = Contact.objects.get(id=id)
    feedback.delete()
    return redirect('view_feedback')

def delete_feedback(request,id):
    if not request.user.is_authenticated:
        return redirect('login_page')
    feedback = Feedback.objects.get(id=id)
    feedback.delete()
    return redirect('view_feedback')

def view_review_admin(request,id):
    data=Movie.objects.get(id=id)
    data2 = Review.objects.all()
    a=0
    b=0
    for i in data2:
        if int(i.rid) == id:
            a = int(i.star) + a
            b += 1
    a = a//b
    d = {'data':data,'data2':data2,'a':a}
    return render(request,'view_review_admin.html',d)

import pandas as pd
import difflib  # NEW: import difflib
from .models import Review

def detect_review(request):
    data = Review.objects.all()

    # Load CSV file reviews (training data)
    csv_data = pd.read_csv('review/train.csv')  # Adjust path
    csv_reviews = csv_data['review'].tolist()

    review_data = []

    for review in data:
        found_similar = False

        for csv_review in csv_reviews:
            similarity = difflib.SequenceMatcher(None, review.review.lower(), csv_review.lower()).ratio()
            if similarity > 0.90:  # 90% similar means we consider it "Real"
                found_similar = True
                break

        if found_similar:
            prediction = 1  # Real
        else:
            prediction = 0  # Fake
        
        review_data.append((review, prediction))

    context = {'review_data': review_data}
    return render(request, 'detect_review.html', context)
    




def delete_review(request,id):
    data=Review.objects.get(id=id)
    data.delete()
    d={'data':data}
    return redirect('detect_review')

def contact(request):
    error=""
    if request.method=='POST':
        n = request.POST['cname']
        pn = request.POST['cphone']
        e = request.POST['cemail']
        p = request.POST['cpurpose']
        try:
            Contact.objects.create(con_name=n,con_mobile=pn,con_email=e,con_purpose=p)
            error = "no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'contact.html',d)



