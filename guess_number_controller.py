"""guess_number_controller.py

Controller layer for the Guess-a-Number MVC example.

This module coordinates the Model and View:
- It drives the game loop.
- It delegates all user I/O to the View.
- It delegates persistence and statistics calculations to the Model.
"""

from __future__ import annotations

import random
from typing import Optional

from guess_number_model import GuessNumberModel, GuessNumberStatsModel
from guess_number_view import GuessNumberView


class GuessNumberController:
    """Orchestrates the Guess-a-Number game.

    Attributes:
        model: Persistence and statistics backend.
        view: Console I/O front-end.
    """

    def __init__(self) -> None:
        """Initialize the controller with default Model and View instances."""
        self.model = GuessNumberModel()
        self.view = GuessNumberView()

    def run(self) -> None:
        """Run the interactive game loop.

        Flow:
            1. Display a banner and ask the player for their name.
            2. Play one or more rounds.
            3. Persist each round's result.
            4. When the player stops, display per-player statistics and exit.
        """
        self.view.show_banner()
        name = self.view.get_name()
        self.view.display_welcome_message(name)

        playing = True
        while playing:
            # Round state
            guesses_taken = 0
            low = 1
            high = 100
            target = random.randint(low, high)
            last_guess: Optional[int] = None

            self.view.display_number_range(low, high)

            # Up to 7 attempts
            while guesses_taken < 7:
                guess = self.view.get_guess()
                last_guess = guess
                guesses_taken += 1

                if guess < target:
                    self.view.display_higher_number(guess)
                elif guess > target:
                    self.view.display_lower_number(guess)
                else:
                    break

            guessed = 'y' if (last_guess == target) else 'n'
            if guessed == 'y':
                self.view.display_congratulations(name, guesses_taken)
            else:
                self.view.display_game_over(name, target)

            # Persist round result. For losses, we still store the number of guesses
            # that were taken (rather than 0), because it tends to be more useful
            # for analysis.
            self.model.save_data(name=name, guessed=guessed, guesses=guesses_taken)

            play_again = self.view.play_again()
            if play_again != 'y':
                playing = False
                data = self.model.load_data()
                stats_model = GuessNumberStatsModel(data)
                statistics = stats_model.calculate_statistics(name)
                self.view.display_statistics(statistics)
            else:
                self.view.show_banner()

        self.view.display_farewell_message(name)
