"""Send greetings."""
import time

import arrow
import click


@click.command()
@click.argument("tz")
@click.option("--repeat", "-r", default=1, type=int)
@click.option("--interval", "-i", default=3, type=int)
def greet(tz, repeat=1, interval=3):
    """Parse a timezone and greet a location a number of times."""
    for i in range(repeat):
        if i > 0:  # no delay needed on first round
            time.sleep(interval)
        now = arrow.now(tz)
        friendly_time = now.format("h:mm a")
        seconds = now.format("s")
        location = tz.split("/")[-1].replace("_", " ")
        print(f"Hello, {location}!")
        print(f"The time is {friendly_time} and {seconds} seconds.\n")
