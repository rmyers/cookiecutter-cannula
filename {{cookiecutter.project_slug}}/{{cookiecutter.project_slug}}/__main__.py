import click
import uvicorn

from .config import config


@click.group()
def cli():  # pragma: no cover
    pass


@click.command()
def initdb():  # pragma: no cover
    click.echo("Initialized the database")
    # import asyncio
    # asyncio.run(create_tables(config.engine))


@click.command()
def run():  # pragma: no cover
    uvicorn.run(
        "{{cookiecutter.project_slug}}.main:app",
        port=config.port,
        host=config.host,
        reload=config.debug,
    )


cli.add_command(initdb)
cli.add_command(run)

if __name__ == "__main__":  # pragma: no cover
    cli()
