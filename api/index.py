from flask import Flask, request, render_template_string, jsonify
from flask_cors import CORS
from hugg_search import hugg_chat_query  # Importing the hugg_chat_query function

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '''
        <form action="/chat" method="get">
            <input type="text" name="query" placeholder="Enter search query">
            <input type="submit" value="Search">
        </form>
    '''

@app.route('/chat', methods=['GET'])
def hugg_chat():
    query = request.args.get('query', '')
    try:
        response = hugg_chat_query(query)
        # Ensure response is a string and encode to bytes
        if not isinstance(response, str):
            response = str(response)
        return response.encode('utf-8')
    except Exception as e:
        # Handle exceptions and return error message
        return f"Error occurred: {str(e)}".encode('utf-8')

if __name__ == '__main__':
    app.run(debug=True)