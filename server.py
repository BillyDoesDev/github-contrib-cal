from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import sys
import os
from scripts.imgtochart import get_chart

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/raccoon", methods=["GET"])
@cross_origin()
def home():
    rows, cols = [int(_) for _ in request.args.get("cal_dim").split("-")]
    return jsonify({"data": get_chart(os.path.join(sys.argv[1]), rows=rows, cols=cols)})


if __name__ == "__main__":
    try:
        print(sys.argv[1])
    except IndexError:
        print("Please provide a valid path to the image you want to display.")
        print("[Usage]")
        print("\tpython server.py /path/to/your/image.ext")
        exit(1)

    app.run(debug=True)
