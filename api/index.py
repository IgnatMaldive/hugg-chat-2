from flask import Flask, request, render_template_string
from flask_cors import CORS

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
    return('pasitos')

if __name__ == '__main__':
    app.run(debug=True)
