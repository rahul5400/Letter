# Letter

Thank-you notes for one club. Type a recipient, your name, and the note. Letter sets it as a card.

Flask and Jinja templates. No database.

## Features

- Compose a short note
- Two recent example notes
- Health check at `/health`

## Run locally

Python 3.11+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:3000.

## Run with Docker

```bash
docker compose up --build
```

The app listens on port 3000.

## Project layout

```
app.py                 Routes and the note layout
templates/home.html    Form and recent notes
static/style.css
```

## Assignment notes

Host this somewhere your classmates and instructor can reach. Walk the running app until you can explain:

- what is stored versus what is rendered
- which fields become part of the card
- how the example notes differ from a note you just set
- what `app.py` does with the note before it is shown

Then look for a security defect in the running system, document how to trigger it, and patch it without breaking a normal note. Submit the hosted URL, a short architecture sketch, the writeup, and the patched repo.
