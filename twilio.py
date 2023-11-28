import streamlit as st
from twilio.rest import Client

# Streamlit app configuration
st.title("Send us your queries")

# Twilio credentials
TWILIO_ACCOUNT_SID = "AC57b15b2f874c753f76cd667a0712be0b"
TWILIO_AUTH_TOKEN = "3c6a2c68dac0650b79d119f9195581f3"
TWILIO_PHONE_NUMBER = "+19897109806"

# Initialize the Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Streamlit app content
default_message = "Hello from Tanishq Ravula.Send us any queries or doubts if you like to contact me."
message = st.text_area("Message", default_message)

if st.button("Send Notification"):
    if not message:
        st.warning("Please enter message.")
    else:
        try:
            # Send the SMS notification
            message = client.messages.create(
                to='+917702337176',
                from_=TWILIO_PHONE_NUMBER,
                body=message
            )
            st.success(f"Notification sent successfully to {message.to}!")
        except Exception as e:
            st.error(f"Error sending notification: {e}")
