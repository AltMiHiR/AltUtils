import questionary

from typing import Optional, Union, Sequence, Dict, Any
from questionary import Choice


class Questionary:
    def __init__(self):
        self.QMARK = "[-]"
        self.SELECTED_POINTER = "»"
        self.CUSTOM_STYLES = questionary.Style([
            ('qmark', 'fg:#FF9D00 bold'),    # Question mark
            ('question', 'fg:#00FF00 bold'), # Question text
            ('answer', 'fg:#0000FF bold'),   # Selected answer
            ('pointer', 'fg:#FF0000 bold'),  # Pointer to the current selection
            ('highlighted', 'fg:#FFFF00 bold'),  # Highlighted options
            ('selected', 'fg:#00FFFF bold'), # Selected options when using checkboxes
        ])
        self.INSTRUCTION = "(Use arrow keys to navigate, Enter to select, Ctrl+C to quit)"

    def make_choices(self, choices: list, indexed: bool = False) -> list:
        new_choices = []
        for ind, choice in enumerate(choices):
            if indexed:
                new_choices.append(Choice(title=f"[{ind + 1}] {choice}", value=ind + 1))
            else:
                new_choices.append(Choice(title=choice, value=ind + 1))
        return new_choices

    def select(
            self,
            question_text: str,
            choices: Sequence[Union[str, Choice, Dict[str, Any]]],
            default: Optional[Union[str, Choice, Dict[str, Any]]] = None
        ):
        return questionary.select(
            question_text,
            choices=choices,
            default=default,
            qmark=self.QMARK,
            pointer=self.SELECTED_POINTER,
            style=self.CUSTOM_STYLES,
            instruction=self.INSTRUCTION
        ).ask()
