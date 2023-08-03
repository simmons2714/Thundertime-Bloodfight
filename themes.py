import questionary
from questionary import Style
from questionary import Separator
from questionary import Choice

custom_style_pretty = Style(
    [
        ("separator", "fg:#cc5454"),
        ("qmark", "fg:#2196f3 bold"),
        ("question", ""),
        ("selected", "fg:#cc5454"),
        ("pointer", "fg:#FF9D00 bold"),
        ("highlighted", "fg:#FF9D00 bold"),
        ("answer", "fg:#f44336 bold"),
        ("disabled", "fg:#858585 italic"),
    ]
)