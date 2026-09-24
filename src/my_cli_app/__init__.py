import click


@click.command()
@click.option("--name", default="world", help="name to greet.")
def main(name: str) -> None:
    """A simple CLI greeting app."""
    click.echo(f"Hello, {name}!")

    if __name__ == "__main__":
        main()
