from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10,null=True)
    dob = models.DateField()
    address = models.CharField(max_length=50,null=True)
    def _str_(self):
        return self.user.username

class Movie(models.Model):
    movi_name = models.CharField(max_length=20,null=True)
    hero_name = models.CharField(max_length=30, null=True)
    heroin_name = models.CharField(max_length=10,null=True)
    rdate = models.CharField(max_length=15,null=True)
    image = models.FileField(null=True)

class Review(models.Model):
    mname = models.CharField(max_length=20, null=True)
    fake = models.CharField(max_length=20, null=True)
    star = models.CharField(max_length=20, null=True)
    review = models.CharField(max_length=30, null=True)
    rname = models.CharField(max_length=30, null=True)
    remail = models.CharField(max_length=30, null=True)
    rid = models.CharField(max_length=30, null=True)
def __str__(self):
        return f"{self.mname} - {self.review}"
def __str__(self):
        # Return a meaningful string representation of the review object
    return f'Review by {self.rname} for {self.mname}: {self.review}'
    
class Feedback(models.Model):
    feedback_name = models.CharField(max_length=20,null=True)
    feedback_contact = models.CharField(max_length=30, null=True)
    feedback_email = models.CharField(max_length=10,null=True)
    feedback_comment = models.CharField(max_length=15,null=True)

class Contact(models.Model):
    con_name = models.CharField(max_length=20,null=True)
    con_mobile = models.CharField(max_length=30, null=True)
    con_email = models.CharField(max_length=10,null=True)
    con_purpose = models.CharField(max_length=15,null=True)


