
import streamlit as st
import joblib

st.title("Email Spam Detection")
st.write("Enter an email message to check it.")

@st.cache_resource
def load_model():
    return joblib.load("email_spam_model.joblib")

email_model = load_model()
email = st.text_area("Email message")

if st.button("Check Email"):
    if email.strip():
        result = email_model.predict([email])[0]
        if result == "spam":
            st.error("This email may be SPAM!")
        else:
            st.success("This email looks legitimate.")
    else:
        st.warning("Please enter an email message.")
      
