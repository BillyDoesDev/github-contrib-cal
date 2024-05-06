from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/raccoon", methods=["GET"])
@cross_origin()
def home():
    print(request.args.get("apple"))
    data = "hello world"
    return jsonify({"data": data})


if __name__ == "__main__":
    app.run(debug=True)
