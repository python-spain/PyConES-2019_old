from flask import Flask, render_template, jsonify

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

# @app.route('/')
# def index():
#     return render_template("index.html")
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route('/v1/keynoters')
def keynoters():
    response = {
        "gurl": "Microsoft",
        "fj": "StyleSage"
    }
    return jsonify(response)
