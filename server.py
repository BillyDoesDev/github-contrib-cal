from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from scripts.imgtochart import get_chart

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/raccoon", methods=["GET"])
@cross_origin()
def home():
    rows, cols = [int(_) for _ in request.args.get("cal_dim").split("-")]
    return jsonify({"data": get_chart("assets/text.png", rows=rows, cols=cols)})


if __name__ == "__main__":
    app.run(debug=True)
