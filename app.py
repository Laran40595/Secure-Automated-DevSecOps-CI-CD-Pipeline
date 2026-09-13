from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevSecOps Demo</title>
        </head>
        <body>
            <h1>🚀 DevSecOps Pipeline</h1>
            <p>Application deployed successfully.</p>
            <p>CI/CD • Docker • Security • AWS • Monitoring</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "DevSecOps Demo",
        "version": "1.0.0"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)