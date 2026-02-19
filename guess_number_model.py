"""guess_number_model.py

Model layer for the Guess-a-Number MVC example.

This module is responsible for:
- Persisting game results to a JSON file stored alongside the code.
- Computing per-player statistics from the stored results.

Notes:
    The JSON file is intentionally simple and human-readable because this is a
    learning/demo project. For a multi-user or concurrent environment, you would
    typically use a database or add file locking.
"""

from __future__ import annotations

import datetime
import json
import os
from typing import Any, Dict


class GuessNumberModel:
    """Persist and retrieve game results.

    The data is stored in a JSON file in the same directory as this module.

    Attributes:
        json_file_path: Absolute path to the JSON persistence file.
    """

    JSON_FILE = "guess_number.json"

    def __init__(self) -> None:
        """Build an absolute path to the JSON file next to this module."""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.json_file_path = os.path.join(script_dir, self.JSON_FILE)

    def load_data(self) -> Dict[str, Dict[str, Any]]:
        """Load all game records from disk.

        Returns:
            A dictionary keyed by record id (e.g., ``game_1``) where each value is
            a game record dictionary.

        Behavior:
            If the JSON file does not exist, an empty dict is returned.
        """
        try:
            with open(self.json_file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self, name: str, guessed: str, guesses: int) -> None:
        """Append a new game record and save to disk.

        Args:
            name: Player name as entered in the UI.
            guessed: ``'y'`` if the player guessed the number, otherwise ``'n'``.
            guesses: Number of guesses taken during the round.

        Notes:
            Record keys are created sequentially as ``game_<n>`` based on the
            current number of records.
        """
        data = self.load_data()
        index = len(data) + 1
        record_key = f"game_{index}"

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data[record_key] = {
            "name": name,
            "played_at": current_time,
            "guessed": guessed,
            "guesses": guesses,
        }

        with open(self.json_file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)


class GuessNumberStatsModel:
    """Compute statistics from stored game data."""

    def __init__(self, data: Dict[str, Dict[str, Any]]) -> None:
        """Create a stats calculator.

        Args:
            data: All stored game records as returned by :meth:`GuessNumberModel.load_data`.
        """
        self.data = data

    def calculate_statistics(self, name: str) -> Dict[str, Any]:
        """Calculate per-player statistics.

        Args:
            name: Player name to filter the stored records by.

        Returns:
            A dictionary containing totals, percentages, and a per-guess distribution.
        """
        # Select only the records for this player.
        user_data = {key: value for key, value in self.data.items() if value.get("name") == name}

        total_games = len(user_data)
        total_games_won = sum(1 for record in user_data.values() if record.get("guessed") == "y")
        total_games_lost = sum(1 for record in user_data.values() if record.get("guessed") == "n")

        if total_games > 0:
            win_percentage = (total_games_won / total_games) * 100
            lost_percentage = (total_games_lost / total_games) * 100
            win_percentage_formatted = f"{win_percentage:6.2f}%" if win_percentage != 0 else ""
            lost_percentage_formatted = f"{lost_percentage:6.2f}%" if lost_percentage != 0 else ""
        else:
            win_percentage_formatted = "N/A"
            lost_percentage_formatted = "N/A"

        total_guesses_in_wins = sum(
            int(record.get("guesses", 0)) for record in user_data.values() if record.get("guessed") == "y"
        )
        average_guess = (total_guesses_in_wins / total_games_won) if total_games_won > 0 else 0

        statistics: Dict[str, Any] = {
            "name": name,
            "total_games": total_games,
            "total_games_won": total_games_won,
            "total_games_lost": total_games_lost,
            "win_percentage": win_percentage_formatted,
            "lost_percentage": lost_percentage_formatted,
            "average_guess": average_guess,
            "guesses_distribution": {
                guesses: sum(
                    1
                    for record in user_data.values()
                    if int(record.get("guesses", 0)) == guesses and record.get("guessed") == "y"
                )
                for guesses in range(1, 8)
            },
        }

        return statistics
