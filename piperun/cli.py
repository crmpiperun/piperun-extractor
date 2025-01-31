#!/usr/bin/env python3
import os
import re
import unicodedata
from datetime import datetime
from typing import Iterator

import click
import pandas

from piperun.extractor import PipeRunExtractor

EXTENSION_PARQUET = 'parquet'
EXTENSION_JSONL = 'jsonl'


def validate_token(ctx: click.core.Context, param: click.core.Option, value: str):
    """Validates that the input is a 32-character hexadecimal string."""
    if value and (len(value) != 32 or not all(c in '0123456789abcdefABCDEF' for c in value)):
        raise click.BadParameter(f"{param.name} must be a valid 32-character hexadecimal string.")
    return value


def validate_method(ctx: click.core.Context, param: click.core.Option, value: str):
    """Validates the method parameter."""
    value = unicodedata.normalize('NFKD', value or '').encode('ascii', 'ignore').decode('ascii').lower()

    if not re.match(r"^[a-z_][a-z0-9_]*$", value):
        raise click.BadParameter(f"Invalid character on method '{value}'")

    return value


def assert_output(method: str, extension: str, output: str) -> None:
    """Validates the output location."""
    if method == 'all':
        if not os.path.isdir(output):
            raise click.BadParameter(f"--output for the 'all' method must be a directory. '{output}' is not a valid directory.")
    elif not output.endswith(f".{extension}"):
        raise click.BadParameter(f"--output '{output}' must be a file with the '{extension}' extension for the '{method}' method.")



def write_itens(items: Iterator, extension: str, output_file: str) -> int:
    count = 0

    def wrapper() -> Iterator:
        nonlocal count
        for item in items:
            count += 1
            yield item

    df = pandas.DataFrame(wrapper())

    if extension == EXTENSION_JSONL:
        df.to_json(output_file, orient='records', lines=True)
    elif extension == EXTENSION_PARQUET:
        df.to_parquet(output_file, compression='zstd')
    else:
        raise NotImplementedError

    return count


def execute_all(piperun: PipeRunExtractor, after: datetime, extension: str, output_dir: str) -> int:
    count = 0
    for name, method in piperun.all(after=after):
        items = method()
        output_file = os.path.join(output_dir, f"{name}.{extension}")
        count += write_itens(items, extension, output_file)

    return count


def execute_one(piperun: PipeRunExtractor, method: str, after: datetime, extension: str, output_file: str) -> int:
    method_attr = getattr(piperun, method)
    items = method_attr(after=after)
    return write_itens(items, extension, output_file)


@click.command()
@click.argument('method', callback=validate_method)
@click.option('-t', '--token', show_envvar=True, required=True,
              callback=validate_token,
              help='User Token')
@click.option('-a', '--after', show_envvar=True, required=True,
              type=click.DateTime(['%Y-%m-%dT%H:%M:%S']),
              help='Date to start filter')
@click.option('-e', '--ext', show_envvar=True, required=True, default=EXTENSION_JSONL, show_default=True,
              type=click.Choice([EXTENSION_JSONL, EXTENSION_PARQUET]),
              help='Output Extension')
@click.option('-o', '--output', show_envvar=True, required=True,
              help='Output Location')
@click.option('--throttle', show_envvar=True, required=False,
              callback=validate_token,
              help='Throttle Token')
@click.option('--log', show_envvar=True, required=False, default='warning', show_default=True,
              type=click.Choice(['critical', 'error', 'warning', 'info', 'debug']),
              help='Log level')
@click.option('--origin', show_envvar=True, required=False,
              type=click.STRING,
              help='Origin URL')
@click.option('--url', show_envvar=True, required=False, default='https://api.pipe.run/v1', show_default=True,
              type=click.STRING,
              help='PipeRun API')
def main(token, throttle, log, origin, url, after, ext, output, method: str):
    assert_output(method, ext, output)

    piperun = PipeRunExtractor(
        token=token,
        token_throttle=throttle,
        log_level=log,
        origin=origin,
        base_url=url,
    )

    if method.startswith('_') or not hasattr(piperun, method):
        raise click.BadParameter(f"method must be one of: {', '.join([name for name, _ in piperun.all(after)])}")

    start_time = datetime.now()

    if method == 'all':
        count = execute_all(piperun, after, ext, output)
    elif callable(getattr(piperun, method)):
        count = execute_one(piperun, method, after, ext, output)
    else:
        raise click.BadParameter('Invalid method')

    elapsed_time = datetime.now() - start_time

    click.echo(f"{count} {method} in {elapsed_time} = {(elapsed_time.seconds / (count / 100))}")


if __name__ == '__main__':
    main(auto_envvar_prefix='PIPERUN')
