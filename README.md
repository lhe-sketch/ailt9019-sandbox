# ailt9019-sandbox

Small Flask page that converts Hong Kong dollars (HKD) to US dollars (USD).

## Run locally

Requires Python 3.10 or newer.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser.

Enter an HKD amount and click **Convert**. The live rate is fetched from a public FX API; if that request fails, the app uses the HKD currency-board peg (~7.80 HKD per USD).

Stop the server with `Ctrl+C`.

## Agent conventions

See [AGENTS.md](AGENTS.md) for code style, git, and commit conventions.
