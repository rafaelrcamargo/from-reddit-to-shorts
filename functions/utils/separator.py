"""String separator"""


def separator(size=21):
    """Separator"""

    separator_string = "\n"

    for i in range(0, size):
        if i % 2 == 0:
            separator_string += "[red]-[/red] "
        else:
            separator_string += "[yellow]-[/yellow] "

    return separator_string
