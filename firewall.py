import requests
from flask import Flask, request, Response, abort

app = Flask(__name__)

# Interne server waar de requests naartoe moeten
TARGET_SERVER = "http://127.0.0.1:10001"

# Alleen deze paden zijn toegestaan
ALLOWED_PATHS = [
    "/",
    "/You1can2stick3a4fricking5dildo6in7your8asshole9you10fucking11piece12of13shit14get15recked16and17die18data.lua"
]

@app.before_request
def check_request():
    if request.path not in ALLOWED_PATHS:
        # Alles wat niet is toegestaan wordt geblokkeerd
        abort(403)

def proxy_request(path):
    # Forward de request naar de interne server
    resp = requests.get(f"{TARGET_SERVER}{path}")
    return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def handle(path):
    # Alleen toegestaan pad wordt doorgestuurd
    return proxy_request("/" + path)

if __name__ == "__main__":
    # Firewall luistert op poort 80
    app.run(host="0.0.0.0", port=80)
