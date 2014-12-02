#!/usr/bin/env python

import cv2
import click
import sorts
import time


@click.group()
@click.option('--src', nargs=1, default="Lenna.png",
              help="File to pixelsort", type=click.Path(exists=True))
@click.option('--out', nargs=1, default="output.png", help="File to output")
@click.version_option(version=0.1)
@click.pass_context
def cli(ctx, src, out):
    """Sort pixels from the CLI"""
    ctx.obj['src'] = cv2.imread(src)
    ctx.obj['out'] = out
    ctx.obj['start'] = time.clock()


@cli.command()
@click.pass_context
def column(ctx):
    """Sorts each column of the image"""
    sort = sorts.sort_by_column(ctx.obj['src'])
    save_image(ctx.obj['out'], sort, ctx.obj['start'])


@cli.command()
@click.pass_context
def row(ctx):
    """Sorts each row of the image"""
    sort = sorts.sort_by_row(ctx.obj['src'])
    save_image(ctx.obj['out'], sort, ctx.obj['start'])


@cli.command()
@click.argument('numpx', nargs=1, type=click.INT,
                metavar="<Number of Pixels>", default=50)
@click.pass_context
def npixel(ctx, numpx):
    """Sorts every N-pixels of the image"""
    sort = sorts.sort_by_npx(ctx.obj['src'], numpx)
    save_image(ctx.obj['out'], sort, ctx.obj['start'])


@cli.command()
@click.pass_context
def sumrgb(ctx):
    """Sorts by sum of the RGB channels"""
    sort = sorts.sort_by_sumrgb(ctx.obj['src'])
    save_image(ctx.obj['out'], sort, ctx.obj['start'])


def save_image(filename, data, start):
    cv2.imwrite(filename, data)
    ellapsed = time.clock() - start
    click.secho('Sorted image in %.2f seconds!' % ellapsed, fg='green')


if __name__ == '__main__':
    # Pass in a dictionary object to save the context
    cli(obj={})
