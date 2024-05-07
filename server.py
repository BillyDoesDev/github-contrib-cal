from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import argparse
from scripts.imgtochart import get_frames

parser = argparse.ArgumentParser(
    description="Draw tf out on the world's best canvas - GitHub Contribution Calendar.",
    epilog="Version 0.0.1",
    usage="%(prog)s [options] directory_path",
)

parser.add_argument("directory_path", help="Path to the directory where your images are", type=str)
parser.add_argument("--inv", help="Invert images", action="store_true", default=False)
parser.add_argument(
    "--reload_cache", help="Disable using cache [generates frames again]", action="store_true", default=False
)

args = parser.parse_args()

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/raccoon", methods=["GET"])
@cross_origin()
def home():
    rows, cols = [int(_) for _ in request.args.get("cal_dim").split("-")]
    return jsonify(
        get_frames(
            args.directory_path,
            rows=rows,
            cols=cols,
            inv=args.inv,
            cache_reload=args.reload_cache,
        )
    )


if __name__ == "__main__":
    app.run(debug=True)
