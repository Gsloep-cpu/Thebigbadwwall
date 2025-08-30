from flask import Flask, request, abort

app = Flask(__name__)

# List of allowed paths
ALLOWED_PATHS = [
    "/",  # root
    "/You1can2stick3a4fricking5dildo6in7your8asshole9you10fucking11piece12of13shit14get15recked16and17die18data.lua"
]

@app.before_request
def check_request():
    path = request.path
    if path not in ALLOWED_PATHS:
        # Block everything else
        abort(403)

@app.route("/")
def index():
    return "Firewall is active.", 200

@app.route("/You1can2stick3a4fricking5dildo6in7your8asshole9you10fucking11piece12of13shit14get15recked16and17die18data.lua")
def lua_data():
    return "Lua endpoint allowed.", 200

if __name__ == "__main__":
    # Run on port 80 or any port you choose
    app.run(host="0.0.0.0", port=80)
