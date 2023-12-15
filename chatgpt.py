import streamlit as st

# Function to generate AI response
def generate_response(user_input):
    # This is a placeholder for the actual AI response generation
    # In a real scenario, this would interact with an AI model (like GPT-3)
    # For demo purposes, echoing the user input as a response
    return f"AI: I received '{user_input}'"

# Streamlit UI
st.title("ChatGPT - Streamlit")

conversation = []

user_input = st.text_input("You:", key="user_input")
if st.button("Send"):
    if user_input:
        # Add user input to the conversation history
        conversation.append(f"You: {user_input}")

        # Generate AI response and add it to the conversation history
        ai_response = generate_response(user_input)
        conversation.append(ai_response)

        # Display conversation history in the text area
        st.text_area("Chat History", "\n".join(conversation), height=400, max_chars=None, key="chat_history")
    else:
        st.warning("Please enter a message!")

# Add a separator and a space for better UI
st.markdown("---")
st.write("")  # Empty sp
