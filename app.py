from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


from app.service import Services

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/emoji": {"origins": "*"}})


@app.route('/')
def doc():
    with open("app/doc.html", "r") as f:
        return f.read()

@app.route('/emoji', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def emoji():
    
    services = Services()
    request_data = request.get_json()
    after = services.date_str_to_unix(request_data.get('after', '2020-01-01'))
    before = services.date_str_to_unix(request_data.get('before', '2020-01-01'))
    subreddit = request_data.get('subreddit')
    limit = int(request_data.get('limit', 100))

    resp = services.get_emoji_frequency_for_range(after=after, before=before, subreddit=subreddit, limit=limit)

    return jsonify(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')