from flask import Flask, request, render_template_string
from tavily import TavilyClient
from flask_cors import CORS

app = Flask(__name__)

# Initialize Tavily client with your API key
tavily = TavilyClient(api_key="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")

CORS(app)

def json_to_htmx(data):
    # Convert JSON data to HTMX (HTML)
    htmx_tags = ''
    for result in data['results']:
        htmx_tags += f"<div data-score='{result['score']}'>"
        htmx_tags += f"<h1>{result['title']}</h1>"
        htmx_tags += f"<p>{result['content']}</p>"
        htmx_tags += f"<a href='{result['url']}'>Link</a>"
        htmx_tags += '</div>'
    return htmx_tags

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
    return('manola')

if __name__ == '__main__':
    app.run(debug=True)
