# Import required libraries
import openai
from flask import Flask, render_template, request, jsonify
from config import OPENAI_API_KEY

# Initializes a Flask application. The template_folder and static_folder parameters specify the 
# locations of HTML templates and static files (like CSS or images).
app = Flask(__name__, template_folder='statics/templates', static_folder='statics')

# Set your OpenAI API key
openai.api_key = "sk-proj-cghAcPFX8C2XMWXWfllGT3BlbkFJX85pm9qgLXoh8IsWrS7m"

# Function to interact with the ChatGPT model
def chat_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    """
    Interact with the ChatGPT model to generate keywords.

    Parameters:
    - prompt (str): The user's input prompt.
    - model (str): The OpenAI GPT model to use. Defaults to "gpt-3.5-turbo".

    Returns:
    dict: The generated keywords in JSON format.
    """
    # System prompt to guide the behavior of the model
    system_prompt = 'You are a helpful assistant. Please make sure that you only return a JSON format that looks like ' \
                    '{"keywords": <list of keywords>}. Ensure the JSON is valid and do not write anything before ' \
                    'or after the JSON structure provided and any new line character.'

    # Make a request to OpenAI's ChatCompletion API
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract and evaluate the model's response
    message = eval(response['choices'][0]['message']['content'])
    print(message)
    return message

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling keyword generation
@app.route('/generate_keywords', methods=['POST'])
def generate_keywords():
    if request.method == 'POST':
        # Use request.form.get() to safely retrieve form data
        url_link = request.form.get('inputValue')
        n_keywords = 5

        if url_link:
            # Formulate a question for the model based on the input
            question = f"Write me {n_keywords} keywords given "
            input_text = question + url_link

            # Call the function to interact with the ChatGPT model and get keywords
            keywords = chat_with_chatgpt(input_text)
            print(keywords)
            
            # Return the generated keywords in JSON format
            return jsonify(keywords)

    # Handle the case where the form is not submitted correctly
    return "Invalid request"

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0')
