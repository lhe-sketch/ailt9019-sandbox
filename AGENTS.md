# Agent conventions

Follow these rules for this repo. Cursor also loads `.cursor/rules/`.

## Code style

- Keep the app a small Flask service: `app.py` plus templates. Do not add extra frameworks unless asked.
- Use Python 3.10+ typing (`tuple[float, str]`, not `Tuple`).
- Prefer the standard library (`urllib`, `json`) over new HTTP clients.
- Validate user input and return JSON errors with HTTP 400 for bad amounts.
- Keep a documented fallback FX rate if the live API fails.
- HTML lives in `templates/`. CSS lives in `static/style.css` and follows `prefers-color-scheme`.
- Match existing naming: `fetch_rate`, `FALLBACK_RATE`, `RATE_URL`.

```python
# Good: typed helper, narrow except, fallback
def fetch_rate() -> tuple[float, str]:
    try:
        ...
    except (urllib.error.URLError, TimeoutError, KeyError, ValueError, json.JSONDecodeError):
        return FALLBACK_RATE, "peg fallback"
```

## Git and commits

- Branch names: `cursor/short-description` (example: `cursor/hkd-usd-converter`).
- Do not commit unless asked. Do not push unless asked.
- Do not commit `.venv/`, `__pycache__/`, secrets, or `.env`.
- Commit messages: 1–2 sentences on **why**, imperative mood, no trailer noise.

```
Add a small Flask page to convert HKD to USD.
```

- Never update git config, skip hooks, force-push, or amend published history.

## Product notes

- Verify UI changes in the browser (convert a known amount end to end).
- Do not expand scope (extra currencies, auth, deploy) unless requested.
