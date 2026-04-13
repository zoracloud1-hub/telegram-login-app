from flask import Flask
import os

app = Flask(__name__)

# 모든 경로에 대해 빈 HTML 반환
@app.route("/")
def blank_page():
    return "<html><body></body></html>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT", 5000))
