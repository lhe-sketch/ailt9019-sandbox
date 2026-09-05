import json
import urllib.error
import urllib.request

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

FALLBACK_RATE = 0.1282  # ~7.80 HKD per USD (currency board peg)
RATE_URL = "https://open.er-api.com/v6/latest/HKD"


def fetch_rate() -> tuple[float, str]:
    try:
        with urllib.request.urlopen(RATE_URL, timeout=5) as resp:
            data = json.loads(resp.read().decode())
        rate = float(data["rates"]["USD"])
        date = str(data.get("time_last_update_utc", "live"))
        return rate, date
    except (urllib.error.URLError, TimeoutError, KeyError, ValueError, json.JSONDecodeError):
        return FALLBACK_RATE, "peg fallback"


@app.route("/")
def index():
    rate, source = fetch_rate()
    return render_template("index.html", rate=rate, source=source)


@app.post("/convert")
def convert():
    payload = request.get_json(silent=True) or {}
    try:
        hkd = float(payload.get("hkd", 0))
    except (TypeError, ValueError):
        return jsonify({"error": "Enter a valid HKD amount."}), 400
    if hkd < 0:
        return jsonify({"error": "Amount cannot be negative."}), 400
    rate, source = fetch_rate()
    return jsonify({"hkd": hkd, "usd": round(hkd * rate, 2), "rate": rate, "source": source})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
