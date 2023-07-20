import questionary
from questionary import ValidationError, Validator

class SpecialValidator(Validator):
    def __init__(self, special_stats, stat_name):
        self.special_stats = special_stats
        self.stat_name = stat_name

    def validate(self, document):
        try:
            current_points = int(document.text)
            if not (1 <= current_points <= 10):
                raise ValidationError(
                    message="Please enter a valid number between 1 and 10",
                    cursor_position=0,
                )

            temp_stats = self.special_stats.copy()
            temp_stats[self.stat_name] = current_points
            total_points = sum(temp_stats.values())
            if total_points > 40:
                raise ValidationError(
                    message="Total points allocated cannot exceed 40",
                    cursor_position=0,
                )
        except (ValueError, TypeError):
            raise ValidationError(
                message="Please enter a valid number between 1 and 10",
                cursor_position=0,
            )
def get_special_stats():
    answers = {}
    special_stats = {
        "Strength": 1,
        "Perception": 1,
        "Endurance": 1,
        "Charisma": 1,
        "Intelligence": 1,
        "Agility": 1,
        "Luck": 1,
    }

    # List of stat names in the order they will be asked
    stat_names = list(special_stats.keys())
    for stat_name in stat_names:
        questions = questionary.text(
            f'{stat_name}:',
            validate=SpecialValidator(special_stats, stat_name),
            default='1'
        ).ask()
        answers.update({stat_name: questions})

        special_stats[stat_name] = int(answers[stat_name])

    print("\nYour chosen SPECIAL stats:")
    for stat, value in special_stats.items():
        print(f"{stat}: {value}")

    unused_points = 40 - sum(special_stats.values())
    print(f"\nUnused stat points: {unused_points}")

    # Ask the player if they like the stats
    like_stats = questionary.confirm("Do you like these stats?").ask()

    if like_stats:
        print("Great! Your character's SPECIAL stats are finalized.")
    else:
        print("Feel free to adjust your character's SPECIAL stats.")

    return special_stats.values()
