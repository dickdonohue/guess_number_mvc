# Guess-a-Number (MVC) 

## A small Python command-line game

This is a little command-line-based **Guess-a-Number** game written using MVC (Model / View / Controller) approach.

Copyright &copy; Dick Donohue, 2026

- **Controller** drives the game loop.
- **View** handles all console input/output.
- **Model** persists results to a JSON file and computes player statistics.

## Requirements

- Python 3.8+ (older versions may work, but the project is tested conceptually with modern Python).

## Run

From the `guess_number_mvc` folder:

```bash
python guess_number.py
```

## Project Layout

- `guess_number.py`  
  Entry point.

- `guess_number_controller.py` (Controller)  
  Game flow and coordination between View and Model.

- `guess_number_view.py`  (View)  
  Console UI and rendering.

- `guess_number_model.py`  (Model)  
  JSON persistence and statistics calculations.

- `guess_number.json`  
  Game history data file (created/updated when you play).  
  This file is purposely included in `.gitignore`. I've included a `sample_guess_number.json` to give you an idea of the format of this file. 

## Data Persistence

Each completed round is appended to `guess_number.json` with:

- player name
- timestamp
- win/loss flag (`y` / `n`)
- number of guesses taken

When you stop playing, the app prints per-player statistics based on records matching your name.

## Notes / Future enhancements

- This is intentionally a learning project. 
It is not intended to be a multi-user game or support concurrent use, otherwise, I'd consider using a database and/or file locking.
- Consider adding input validation (e.g., enforce guesses are within range).
- Consider adding unit tests for the Model (in theory, stats and persistence should be straightforward to test).
