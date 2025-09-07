import os
import requests
from flask import Flask, request, abort, Response

app = Flask(__name__)

# Target server (interne server.py)
TARGET_SERVER = "http://127.0.0.1:10001"

# List of allowed paths
ALLOWED_PATHS = [
    "/",  # root
    "/You1can2stick3a4fricking5dildo6in7your8asshole9you10fucking11piece12of13shit14get15recked16and17die18data.lua"
]

@app.before_request
def check_request():
    # Normaliseer path: verwijder trailing slash
    path = request.path.rstrip("/")
    allowed = [p.rstrip("/") for p in ALLOWED_PATHS]

    # Ping-route mag altijd
    if path == "/ping":
        return

    if path not in allowed:
        # Block alles wat niet expliciet toegestaan is
        abort(403)

@app.route("/", methods=["GET", "HEAD"])
def index():
    return "Firewall is active.", 200

@app.route("/You1can2stick3a4fricking5dildo6in7your8asshole9you10fucking11piece12of13shit14get15recked16and17die18data.lua", methods=["GET"])
def lua_data():
    # Forward request to internal server.py
    try:
        resp = requests.get(f"{TARGET_SERVER}{request.path}", timeout=10)
        return Response(resp.content, status=resp.status_code, mimetype=resp.headers.get("Content-Type"))
    except requests.RequestException as e:
        return Response(f"-- error connecting to internal server: {str(e)}", status=500)

@app.route("/ping", methods=["GET"])
def ping():
    # Simpel antwoord om de server wakker te houden
    return "pong", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)
