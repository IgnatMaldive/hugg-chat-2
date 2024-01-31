from flask import Flask, request, render_template_string
from tavily import TavilyClient
from flask_cors import CORS

app = Flask(__name__)

# Initialize Tavily client with your API key
tavily = TavilyClient(api_key="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")

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
    return('manolaffff')

if __name__ == '__main__':
    app.run(debug=True)
