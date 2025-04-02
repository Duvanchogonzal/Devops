from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Duvan",
        "lastname": "Gonzalez",
        "socialMedia":
        {
            "facebookUser": "duvanchogonzal",
            "instagramUser": "duvanchogonzal",
            "xUser": "duvanchogonzal",
            "linkedin": "duvanchogonzal",
            "githubUser": "duvanchogonzal"
        },
        "blog": "https://duvan",
        "author": "Duvan Gonzalez",
    }

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)