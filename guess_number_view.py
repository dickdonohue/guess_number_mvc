"""guess_number_view.py

View layer for the Guess-a-Number MVC example.

All user interaction (I/O) is contained here so the Controller can remain free
of direct calls to ``print`` and ``input``.
"""

from __future__ import annotations

import os
from typing import Any, Dict


class GuessNumberView:
    """Console-based user interface for the Guess-a-Number game."""

    @staticmethod
    def show_banner() -> None:
        """Clear the screen and display the game banner."""
        GuessNumberView._clear_screen()
        print("---------------------------------------")
        print("                                   v2.0")
        print("   The 'Guess-a-Number' Game ")
        print(" ")
        print("---------------------------------------")
        print(" ")

    @staticmethod
    def get_name() -> str:
        """Prompt the user for their name.

        Returns:
            The trimmed name string (may be empty).
        """
        return input("Hello! What is your name? ").strip()

    @staticmethod
    def display_welcome_message(name: str) -> None:
        """Display a greeting to the user.

        Args:
            name: Player name.
        """
        print(f"Welcome, {name}!")

    @staticmethod
    def display_number_range(low: int, high: int) -> None:
        """Display the current guessing range for the round.

        Args:
            low: Lower bound (inclusive).
            high: Upper bound (inclusive).
        """
        print(" ")
        print(f"I am thinking of a number between {low} and {high}.")
        print("Can you guess it in 7 tries or less?")

    @staticmethod
    def get_guess() -> int:
        """Prompt the user for a guess.

        Returns:
            The parsed integer guess.
        """
        while True:
            guess = input("Take a guess: ")
            try:
                return int(guess)
            except ValueError:
                print("I don't understand. Please enter a valid integer.")

    @staticmethod
    def display_higher_number(guess: int) -> None:
        """Tell the player the target number is higher than their guess."""
        print(f"My number is higher than {guess}")

    @staticmethod
    def display_lower_number(guess: int) -> None:
        """Tell the player the target number is lower than their guess."""
        print(f"My number is lower than {guess}")

    @staticmethod
    def display_congratulations(name: str, guesses: int) -> None:
        """Display the 'you won' message.

        Args:
            name: Player name.
            guesses: Number of guesses taken.
        """
        print(f"Congratulations, {name}! You guessed my number in {guesses} guesses!")

    @staticmethod
    def display_game_over(name: str, number: int) -> None:
        """Display the 'you lost' message.

        Args:
            name: Player name.
            number: The secret number.
        """
        print(f"Sorry, {name}. The number I was thinking of was {number}.")

    @staticmethod
    def play_again() -> str:
        """Ask whether the user wants to play another round.

        Returns:
            The user's response in lowercase. Typical values are ``'y'`` or ``'n'``.
        """
        print(" ")
        return input("Want to play again (Y/N)?  ").lower().strip()

    @staticmethod
    def display_farewell_message(name: str) -> None:
        """Display an exit message."""
        print(" ")
        print(f"Thanks for playing, {name}!")

    @staticmethod
    def display_statistics(statistics: Dict[str, Any]) -> None:
        """Render per-player statistics to the console.

        Args:
            statistics: A statistics dictionary produced by
                :meth:`guess_number_model.GuessNumberStatsModel.calculate_statistics`.
        """
        print(" ")
        print(f"Game statistics for {statistics['name']}:")
        print(f"  Total games played....: {statistics['total_games']:>4}")
        print(f"  Total games won.......: {statistics['total_games_won']:>4}   {statistics['win_percentage']}")
        print(f"  Total games lost......: {statistics['total_games_lost']:>4}   {statistics['lost_percentage']}")
        print(f"  Avg number of guesses.: {statistics['average_guess']:>7.2f}")

        if statistics["total_games_won"] > 0:
            print("  Of the games you've won, you guessed it in:")
            for guesses, count in statistics["guesses_distribution"].items():
                percentage = (count / statistics["total_games_won"]) * 100
                label = "guess" if guesses == 1 else "guesses"
                times_label = "time" if count == 1 else "times"
                output = f"	{guesses} {label}:  {count:3.0f} {times_label}"
                if percentage > 0.00:
                    output += f" {percentage:6.2f}%"
                print(output)

    @staticmethod
    def _clear_screen() -> None:
        """Clear the terminal screen in a cross-platform way."""
        os.system("cls" if os.name == "nt" else "clear")
