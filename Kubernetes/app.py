from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    response = {
        "foo": "bar",
        "built_at": 1616337212,
        "deployed_at": 1222037111
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


