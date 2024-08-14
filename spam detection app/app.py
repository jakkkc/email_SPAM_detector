import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and vectorizer
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("Spam Detection App")

user_input = st.text_area("Enter the message to classify")

if st.button("Classify"):
    if user_input:
        # Vectorize the user input
        input_vector = vectorizer.transform([user_input])
        
        # Predict using the model
        prediction = model.predict(input_vector)
        result = "Spam" if prediction == 1 else "Not Spam"
        
        st.write(f"The message is: **{result}**")
    else:
        st.write("Please enter a message to classify.")


import pickle

# Save the trained model
with open('spam_model.pkl', 'wb') as model_file:
    pickle.dump(trained_model, model_file)

# Save the vectorizer
with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)
  
  
  
  
  
