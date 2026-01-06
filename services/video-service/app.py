from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def gen():
    text = request.json.get("text", "demo")
    return jsonify({
        "videoUrl": f"https://example.com/videos/{text.replace(' ', '_')}.mp4"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
