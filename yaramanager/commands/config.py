import io

import click
from rich.console import Console

from yaramanager.config import load_config, config_file, init_config, write_config
from yaramanager.utils import open_file

CONFIG = load_config()


@click.group(help="Review and change yaramanager configuration.")
def config():
    pass


@config.command(help="Get single config entry by key")
@click.argument("key")
def get(key):
    pass


@config.command(help="Edit your config with an external editor.")
def edit():
    open_file(config_file, status="Config file opened in external editor...")


@config.command()
def dump():
    c = Console()
    with io.open(config_file) as fh:
        c.print(fh.read())


@config.command()
def reset():
    write_config(init_config)