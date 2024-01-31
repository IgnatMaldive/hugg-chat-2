from flask import Flask, request
from flask_cors import CORS
from hugchat import hugchat
from hugchat.login import Login

# Log in to huggingface and grant authorization to huggingchat
sign = Login("ignatiusmaldive@gmail.com", "hu&LO8f&e34")
cookies = sign.login()

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    # A simple form for entering search queries
    return '''
        <form action="/search" method="get">
            <input type="text" name="query" placeholder="Enter search query">
            <input type="submit" value="Search">
        </form>
    '''

@app.route('/search', methods=['GET'])
def search():
    try:
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict()) 

        user_query = request.args.get('query', '')

        response = chatbot.query(user_query)

        if not isinstance(response, str):
            response = str(response)
            return response.encode('utf-8')
    except Exception as e:
        # Handle exceptions and return error message
            return f"Error occurred: {str(e)}".encode('utf-8')
    








if __name__ == '__main__':
    app.run(debug=True)
