"""Timeout handler"""

import math
from time import sleep

# Cool Terminal Colors
from rich import print
from rich.progress import track


def timeout(time, step, action):
    """Function to handle timeouts"""

    step = math.ceil(step * 0.1)

    print(f">> [dim]Waiting for the next [bold]{action}[/bold]![/dim]\n")

    for _ in track(
        range(0, time, step),
        description="Waiting...",
        get_time=False,
        style="red",
        complete_style="green",
        finished_style="green",
    ):
        sleep(step)
