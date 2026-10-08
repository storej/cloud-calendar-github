"""Лабораторна робота №2, варіант 1 — Календар."""

from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask

app = Flask(__name__)


@app.route("/")
def calendar():
    # Дата обчислюється для кожного запиту з урахуванням часового поясу Києва.
    today = datetime.now(ZoneInfo("Europe/Kyiv"))
    formatted_date = today.strftime("%d.%m.%Y")

    return f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Календар</title>
    </head>
    <body>
        <h1>Календар</h1>
        <p>Сьогоднішня дата: <strong>{formatted_date}</strong></p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    # Render використовує цю адресу для перевірки працездатності.
    return {"status": "ok"}


@app.after_request
def disable_cache(response):
    # Браузер має запитувати актуальну дату замість збереженої сторінки.
    response.headers["Cache-Control"] = "no-store"
    return response


if __name__ == "__main__":
    # Для локальної перевірки; на Render застосунок запускає Gunicorn.
    app.run()
