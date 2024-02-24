import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='statics/templates', static_folder='statics')
# Set your OpenAI API key
openai.api_key = "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"


def chat_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    systemp_prompt = 'You are a helpful assistant.  Please make sure that you only return a JSON format that look like ' \
                     'this: {"keywords": <list of keywords>}. Ensure the JSON is valid and do not write anything before' \
                     ' or after the JSON structure provided and any new line character.'
    response = openai.ChatCompletion.create(
        model=model,  # Specifies the GPT model to use

        # Create a conversational context for the model
        messages=[
            {"role": "system", "content": systemp_prompt},
            {"role": "user", "content": prompt},
        ],

        max_tokens=100,  # Specifies the maximum number of tokens (words or characters) in the generated completion
        n=1,  # Requests only 1 completion from the model
        stop=None,  # Specifies a stopping condition for the model. 'None' means it will hit max_token as the limit
        temperature=0.5,  # Controls the randomness of the model's output. Lower = more focused, Higher = more random
    )

    # Picks the first and only choice in the list
    # 'text.strip' removies leading and trailing whitespaces
    message = eval(response['choices'][0]['message']['content'])
    print(message)
    return message


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_keywords', methods=['POST'])
def generate_keywords():
    if request.method == 'POST':
        # Use request.form.get() to avoid KeyError
        url_link = request.form.get('inputValue')
        n_keywords = 5
        if url_link:
            question = f"Write me {n_keywords} keywords given "
            input_text = question + url_link

            # Call your function to get keywords
            keywords = chat_with_chatgpt(input_text)
            print(keywords)
            return jsonify(keywords)

    # Handle the case where the form is not submitted correctly
    return "Invalid request"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
