from flask import Flask
from tavily import TavilyClient
from flask_cors import CORS
from hugchat import hugchat
from hugchat.login import Login

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
    return('holamanola')

if __name__ == '__main__':
    app.run(debug=True)
