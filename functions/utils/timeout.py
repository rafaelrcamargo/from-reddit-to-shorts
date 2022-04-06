"""Timeout handler"""

from time import sleep


def timeout(time, steps, action):
    """Function to handle timeouts"""
    total = time
    while total > 0:
        print(f"\n>> [red]Waiting for the next [bold]{action}[/bold]![/red]")
        print(f">> [red]Time left: {str(total)} seconds[/red]")
        sleep(steps)
        total -= steps
