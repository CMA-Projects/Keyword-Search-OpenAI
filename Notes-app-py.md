# App.py
### Create the Flask application
Initializes a Flask application. The template_folder and static_folder parameters specify the locations of HTML templates and static files (like CSS or images).

```
app = Flask(__name__, template_folder='statics/templates', static_folder='statics')
```

### Function to interact with the ChatGPT model
- chat_with_chatgpt is a function that interacts with OpenAI's ChatGPT model. It takes a user prompt and an optional model parameter as inputs.
- The system_prompt provides instructions to the model, guiding its behavior during the conversation.
- A request is made to OpenAI's ChatCompletion API using openai.ChatCompletion.create(). It sends the system prompt and user prompt to generate a model response.
- The response is then extracted and evaluated, and the resulting message (keywords) is returned.
```
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
```

### Route to the homepaage
- @app.route('/') is a decorator that associates the function index() with the root URL ('/'). When a user visits the root URL, the index() function is called, and it renders the HTML template 'index.html'.
```
@app.route('/')
def index():
    return render_template('index.html')
```

### Route to Generate Keywords
- @app.route('/generate_keywords', methods=['POST']) is another route decorator, associated with the '/generate_keywords' URL. It specifies that this route accepts POST requests.

- Inside generate_keywords(), it checks if the request method is POST. If true, it retrieves the form data ('inputValue') safely and sets the number of desired keywords (n_keywords).

- It then formulates a question based on the input and calls the chat_with_chatgpt function to interact with the ChatGPT model.

- The generated keywords are printed and returned in JSON format using Flask's jsonify function.
```
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
```

### Run the Application
- if __name__ == '__main__': ensures that the Flask application runs only if the script is executed directly, not if it's imported as a module.

- app.run(host='0.0.0.0') starts the Flask development server, making the web application accessible at the specified host and port. The host '0.0.0.0' means it's accessible from any IP address.
```if __name__ == '__main__':
    app.run(host='0.0.0.0')
```