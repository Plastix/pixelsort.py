#!/usr/bin/env python

import cv2
import click
import sorts
# import time
# import sys


@click.group()
# TODO: Change these to filepath arguments later
@click.option('--src', nargs=1, default="Lenna.png", help="File to pixelsort")
@click.option('--out', nargs=1, default="output.png", help="File to output")
@click.pass_context
def pixelsort(ctx, src, out):
    """Sort pixels from the CLI"""
    ctx.obj['src'] = cv2.imread(src)
    ctx.obj['out'] = out


@click.command()
@click.pass_context
def column(ctx):
    """Sorts each column of the image"""
    sort = sorts.sort_by_column(ctx.obj['src'])
    save_image(ctx.obj['out'], sort)


@click.command()
@click.pass_context
def row(ctx):
    """Sorts each row of the image"""
    sort = sorts.sort_by_row(ctx.obj['src'])
    save_image(ctx.obj['out'], sort)


@click.command()
@click.argument('numpx', nargs=1, type=click.INT, metavar="<Number of pixels>", default=50)
@click.pass_context
def npixel(ctx, numpx):
    """Sorts every N-pixels of the image"""
    sort = sorts.sort_by_npx(ctx.obj['src'], numpx)
    save_image(ctx.obj['out'], sort)


def save_image(filename, data):
    cv2.imwrite(filename, data)
    print 'Sorted image!'


pixelsort.add_command(row)
pixelsort.add_command(column)
pixelsort.add_command(npixel)

if __name__ == '__main__':
    pixelsort(obj={})
    # if len(sys.argv) > 1:
    #     filename = sys.argv[1]
    # else:
    #     filename = "Lenna.png"
    # image = cv2.imread(filename)
    # start = time.clock()
    # image = sorts.sort_by_npx(image)
    # end = time.clock()
    # elapsed = '%.2f' % (end - start)
    # print 'Image Sorted in ' + elapsed + ' seconds!'
    # name = filename.split('.')
    # cv2.imwrite(name[0] + '_output' + '.' + name[1], image)
