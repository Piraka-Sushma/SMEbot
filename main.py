import openai

# Set your OpenAI GPT-3 API key
api_key = "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"
openai.api_key = api_key

# Define a function to interact with the OpenAI API
def get_openai_response(user_input):
    # Construct the conversation with system and user messages
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input},
    ]

    # Make an API call to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Extract and return the assistant's reply
    reply = response['choices'][0]['message']['content']
    return reply

# Example usage
user_question = input("Ask a question: ")
response = get_openai_response(user_question)
print("Assistant:", response)

# openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#   ]
# )