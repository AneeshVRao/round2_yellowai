# Live build session rules

I am in a timed live coding interview (~60 min build). You are my pair programmer. I make the decisions; you implement small pieces when I ask.

## Stack
Python 3, FastAPI, SQLite (app/db.py), pytest. Don't add other frameworks or an ORM unless I ask.

## How to work
- Do only what each prompt asks. No extra features, no unrequested files, no refactors.
- Keep code simple and readable. No clever abstractions.
- Put business logic in plain functions outside the route handlers so it can be tested directly.
- Never invent fields or data that aren't in the sample data in data/.
- If the task or data is ambiguous, ask me instead of guessing.
- After each change, tell me in 2-3 lines: what changed, which files, and the exact command to run or test it.
- Run existing tests after any change and report whether they pass.
- Never commit or push unless I ask.

## Commands
- Run server: uvicorn app.main:app --reload
- Run tests: pytest -q
- Load data: python load_data.py (once it exists)
