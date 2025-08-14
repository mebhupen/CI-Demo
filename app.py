from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "CI/CD demo app running"}), 200

@app.route("/add")
def add_numbers():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return jsonify({"sum": a +b}), 200
    except ValueError:
        return jsonify({"erroe": "invalid input"}), 400
    
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)