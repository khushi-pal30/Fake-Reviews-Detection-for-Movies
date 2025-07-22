import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load the CSV data
data = pd.read_csv('review/training_data.csv')

# Features and labels
X = data['review']
y = data['label']

# Split into training and testing (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize text data
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Build the model
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

# Predict on test set
y_pred = model.predict(X_test_vectorized)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the model and vectorizer
joblib.dump(model, 'review/fake_review_model.pkl')
joblib.dump(vectorizer, 'review/vectorizer.pkl')

print("✅ Model and vectorizer saved successfully!")
