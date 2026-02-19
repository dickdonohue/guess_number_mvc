"""guess_number.py

Entry point for the Guess-a-Number MVC example.
"""

from __future__ import annotations

from guess_number_controller import GuessNumberController


def main() -> None:
    """Create a controller and run the game."""
    controller = GuessNumberController()
    controller.run()


if __name__ == "__main__":
    main()
