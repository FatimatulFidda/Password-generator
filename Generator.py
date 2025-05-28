import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit UI
st.set_page_config(page_title="Password Generator", page_icon="🔐")
st.title("🔐 Password Generator")

st.sidebar.header("Customize Your Password")
length = st.sidebar.slider("Password Length", min_value=8, max_value=20, value=12)
use_digits = st.sidebar.checkbox("Include Numbers", value=True)
use_special = st.sidebar.checkbox("Include Special Characters", value=True)

if st.sidebar.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"Generated Password: `{password}`")
    
    # Copy to Clipboard Button
    st.button("Copy to Clipboard", on_click=lambda: st.write("Copy manually for now!"))

st.markdown("\n**Tip:** Use a mix of letters, numbers, and special characters for a strong password.")
st.markdown("**👨‍💻 Made by Fatima Tul Fidda**")