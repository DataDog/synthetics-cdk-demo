import pathlib
import yaml

import click

from . import loader, stack


@click.command()
@click.argument("config", type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=pathlib.Path))
def cli(config):
    with config.open() as config_file:
        config_data = yaml.safe_load(config_file)
    app, tests_stack = stack.build_stack()
    loader.build_tests(config_data, tests_stack)
    app.synth()
