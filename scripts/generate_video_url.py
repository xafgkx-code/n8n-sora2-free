
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def gen():
    t = request.json.get('text','demo')
    return jsonify({
        "videoUrl": f"https://example.com/videos/{t.replace(' ','_')}.mp4"
    })

app.run(host='0.0.0.0', port=5000)
