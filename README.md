# Guess-a-Number (MVC) - Tiny Python Console App

A small console-based **Guess-a-Number** game written as an MVC (Model / View / Controller) exercise.

Copyright &copy; (c) Dick Donohue, 2026

- **Controller** drives the game loop.
- **View** handles all console input/output.
- **Model** persists results to a JSON file and computes simple player statistics.

## Requirements

- Python 3.8+ (older versions may work, but the project is tested conceptually with modern Python).

## Run

From the `guess_number_MVC` folder:

```bash
python guess_number.py
```

## Project Layout

- `guess_number.py`  
  Entry point.

- `guess_number_controller.py`  
  Game flow and coordination between View and Model.

- `guess_number_view.py`  
  Console UI and rendering.

- `guess_number_model.py`  
  JSON persistence and statistics calculations.

- `guess_number.json`  
  Game history (created/updated when you play).  
  If you don't want to commit game history to Git, delete it or add it to `.gitignore`.

## Data Persistence

Each completed round is appended to `guess_number.json` with:

- player name
- timestamp
- win/loss flag (`y` / `n`)
- number of guesses taken

When you stop playing, the app prints per-player statistics based on records matching your name.

## Notes / Ideas

- This is intentionally a learning project. For multi-user or concurrent use, consider a database or file locking.
- Consider adding input validation (e.g., enforce guesses are within range).
- Consider adding unit tests for the Model (stats and persistence are straightforward to test).
