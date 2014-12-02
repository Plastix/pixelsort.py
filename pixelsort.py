#!/usr/bin/env python

import cv2
import click
import sorts
import time


@click.group()
@click.option('-i', '--src', nargs=1, default='Lenna.png',
              help='Input file to pixelsort.', type=click.Path(exists=True))
@click.option('-o', '--out', nargs=1, default='output.png',
              help='Sorted file to output.')
@click.version_option(version=0.1)
@click.pass_context
def cli(ctx, src, out):
    """Sort pixels from the CLI."""
    ctx.obj['i'] = cv2.imread(src)
    ctx.obj['o'] = out
    ctx.obj['start'] = time.clock()


@cli.command()
@click.pass_context
def column(ctx):
    """Sorts each column of the image."""
    sort = sorts.sort_by_column(ctx.obj['i'])
    save_image(ctx.obj['o'], sort, ctx.obj['start'])


@cli.command()
@click.pass_context
def row(ctx):
    """Sorts each row of the image."""
    sort = sorts.sort_by_row(ctx.obj['i'])
    save_image(ctx.obj['o'], sort, ctx.obj['start'])


@cli.command()
@click.argument('numpx', nargs=1, type=click.INT,
                metavar="<Number of Pixels>", default=50)
@click.pass_context
def npixel(ctx, numpx):
    """Sorts every N-pixels of the image."""
    sort = sorts.sort_by_npx(ctx.obj['i'], numpx)
    save_image(ctx.obj['o'], sort, ctx.obj['start'])


@cli.command()
@click.pass_context
def sumrgb(ctx):
    """Sorts by sum of the RGB channels."""
    sort = sorts.sort_by_sumrgb(ctx.obj['i'])
    save_image(ctx.obj['o'], sort, ctx.obj['start'])

@cli.command()
@click.argument('chan', nargs=1, type=click.INT,
                metavar="<Channel #>", default=0)
@click.pass_context
def chan(ctx, chan):
    """Sorts by the specified color channel."""
    sort = sorts.sort_by_chan(ctx.obj['i'], chan)
    save_image(ctx.obj['o'], sort, ctx.obj['start'])


def save_image(filename, data, start):
    cv2.imwrite(filename, data)
    ellapsed = time.clock() - start
    click.secho('Sorted image in %.2f seconds!' % ellapsed, fg='green')


if __name__ == '__main__':
    # Pass in a dictionary object to save the context
    cli(obj={})
