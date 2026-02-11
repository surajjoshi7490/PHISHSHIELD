from flask import Flask, request, render_template, redirect, url_for, session
import numpy as np
import warnings
import pickle
import time

from convert import convertion
from feature import FeatureExtraction

warnings.filterwarnings("ignore")

# ---------------- LOAD MODEL ----------------
with open("newmodel.pkl", "rb") as file:
    gbc = pickle.load(file)

app = Flask(__name__)
app.secret_key = "phishshield-secret-key"  # REQUIRED for session

# ---------------- HOME (GET ONLY) ----------------
@app.route("/", methods=["GET"])
def home():
    # Pop result so refresh clears it
    result = session.pop("result", None)
    return render_template("index.html", name=result)

# ---------------- SCAN (POST ONLY) ----------------
@app.route("/scan", methods=["POST"])
def scan():
    url = request.form.get("name")
    if not url:
        return redirect(url_for("home"))

    start_time = time.time() 
    # Feature extraction + prediction
    obj = FeatureExtraction(url)
    x = np.array(obj.getFeaturesList()).reshape(1, 30)
    y_pred = gbc.predict(x)[0]
    result = convertion(url, int(y_pred))
    processing_time = time.time() - start_time 
    print(f"[PHISHSHIELD] Scan completed in {processing_time:.2f} seconds")

    # Normalize result safely
    session["result"] = {
        "url": result[0],
        "status": result[1] if len(result) > 1 else "Unknown",
        "button": result[2] if len(result) > 2 else "Open",
        "safe": bool(result[3]) if len(result) > 3 else False
    }

    # 🔴 CRITICAL: Redirect to HOME (no POST page)
    return redirect(url_for("home"))
@app.route("/know-more")
def know_more():
    return render_template("know_more.html")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True) 