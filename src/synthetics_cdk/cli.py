import pathlib
import yaml

import click


@click.command()
@click.argument(
    "config",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=pathlib.Path))
def cli(config):
    with config.open() as config_file:
        config_data = yaml.safe_load(config_file)
