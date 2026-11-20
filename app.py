import os

from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "letter-dev-secret")
app.config["DESK_CODE"] = os.environ.get("DESK_CODE", "LETTER-8830")

EXAMPLES = [
    {
        "recipient": "the shop volunteers",
        "sender": "Maya",
        "note": "Thanks for staying late to cut the acrylic. The rover panel fits.",
    },
    {
        "recipient": "Jordan",
        "sender": "Devon",
        "note": "Thanks for covering the Thursday screening booth.",
    },
]

LAYOUT = """
<article class="letter">
  <p class="dear">Dear {{ recipient }},</p>
  <div class="body">
NOTE
  </div>
  <p class="sign">— {{ sender }}</p>
</article>
"""


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/")
def home():
    return render_template("home.html", examples=EXAMPLES, result=None, error=None)


@app.post("/")
def compose():
    recipient = (request.form.get("recipient") or "").strip()
    sender = (request.form.get("sender") or "").strip()
    note = request.form.get("note") or ""
    if not recipient or not sender or not note.strip():
        return render_template(
            "home.html",
            examples=EXAMPLES,
            result=None,
            error="Recipient, sender, and a note are required.",
        ), 400
    source = LAYOUT.replace("NOTE", "{{note}}")
    try:
        rendered = app.jinja_env.from_string(source).render(
            recipient=escape(recipient),
            sender=escape(sender),
            note=escape(note)
        )
    except Exception:
        return render_template(
            "home.html",
            examples=EXAMPLES,
            result=None,
            error="That note could not be laid out.",
        ), 400
    return render_template("home.html", examples=EXAMPLES, result=rendered, error=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "3000")))
