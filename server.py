from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import sys
import os
from scripts.imgtochart import get_frames

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/raccoon", methods=["GET"])
@cross_origin()
def home():
    rows, cols = [int(_) for _ in request.args.get("cal_dim").split("-")]
    return jsonify(get_frames(os.path.join(sys.argv[1]), rows=rows, cols=cols, inv=bool(sys.argv[2])))


if __name__ == "__main__":
    try:
        print(sys.argv[1])
        print(sys.argv[2])
    except IndexError:
        print("Please provide a valid path and mode to the folder containing your images you want to display.")
        print("[Usage]")
        print("\tMode 0 means do not invert image, 1 means invert image")
        print("\tpython server.py /path/to/your/folder 1")
        exit(1)

    app.run(debug=True)
