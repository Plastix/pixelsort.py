#!/usr/bin/env python

import cv2
import click
import sorts
# import time
# import sys


@click.group()
# TODO: Change these to filepath arguments later
@click.option('--src', nargs=1, default="Lenna.png", help="File to pixelsort")
@click.option('--out', nargs=1, default="Lenna_out.png", help="File to output")
def pixelsort(src, out):
    pass


@click.command()
def column(ctx):
    """Sorts each column of the image"""
    pass


@click.command()
def row():
    """Sorts each row of the image"""
    pass


@click.command()
def npixel():
    """Sorts every N-pixels of the image"""
    pass


def save_image(filename, data):
    cv2.imwrite(filename, data)


def load_image(filename):
    return cv2.imread(filename)

pixelsort.add_command(row)
pixelsort.add_command(column)
pixelsort.add_command(npixel)

if __name__ == '__main__':
    pixelsort({})
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
