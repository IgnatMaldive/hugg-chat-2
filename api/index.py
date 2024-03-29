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
    query = request.args.get('query', '')
    try:
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict()) 

        
        query_result = chatbot.query(query)
        if isinstance(query_result, str):
            return query_result.encode('utf-8')
        else:
            # Handle non-string response appropriately
            return str(query_result).encode('utf-8')
    except GeneratorExit:
        # Handle GeneratorExit exception
        pass
    except Exception as e:
        # Handle other exceptions
        pass







if __name__ == '__main__':
    app.run(debug=True)
