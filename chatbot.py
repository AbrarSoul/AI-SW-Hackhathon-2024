import openai
import streamlit as st

# Set up OpenAI API key
openai.api_key = "you_open_api_key"

# Initialize session state variables if they don’t already exist
if "response_text" not in st.session_state:
    st.session_state.response_text = ""
if "show_chatbox" not in st.session_state:
    st.session_state.show_chatbox = False
if "response_generated" not in st.session_state:
    st.session_state.response_generated = False

# Close button to hide the chatbox
if st.session_state.show_chatbox:
    if st.button("Close Chatbox"):
        st.session_state.show_chatbox = False
        st.session_state.response_text = ""

# Streamlit app setup
st.title("Chat GPT-4o-Mini")

# User input for chatbot prompt
user_input = st.text_input("Ask a question:")

# Generate a response only when there’s user input
if user_input:
    try:
        # Call OpenAI API with the gpt-4 model
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        chatbot_response = response['choices'][0]['message']['content']

        # Store the response and set the chatbox to show
        st.session_state.response_text = chatbot_response
        st.session_state.show_chatbox = True

    except Exception as e:
        st.error("An error occurred while generating a response. Please try again.")

# Display the chatbot response
if st.session_state.show_chatbox:
    st.write("Chatbot Response:")
    st.markdown(
        f"""
        <div style="max-height: 300px; overflow-y: auto; padding: 10px; background-color: #f9f9f9; border-radius: 5px;">
            {st.session_state.response_text}
        </div>
        """,
        unsafe_allow_html=True
    )
