"""String separator"""


def separator(size=40):
    """Separator"""

    separator_string = ""

    for i in range(0, size):
        if i % 2 == 0:
            separator_string += "[red]-[/red] "
        else:
            separator_string += "[yellow]-[/yellow] "

    return separator_string
