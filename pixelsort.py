#!/usr/bin/env python

from PIL import Image
import time


def sort_by_row(image):
    """
    Sorts each row of the specified image
    Modifies the image object in place.
    """
    data = image.load()
    width, height = image.size
    for j in range(height):
        splice = sorted([data[i, j] for i in range(width)])
        for i in range(width):
            data[i, j] = splice[i]


def sort_by_column(image):
    """
    Sorts each column of the specified row.
    Modifies the image object in place.
    """
    data = image.load()
    width, height = image.size
    for j in range(width):
        splice = sorted([data[j, i] for i in range(height)])
        for i in range(height):
            data[j, i] = splice[i]


def sort_by_npx(image, numpx=50):
    """
    Treats the specified image data as a 1D list and s`orts by every N pixels.
    Modifies the image object in place.
    """
    data = list(image.getdata())  # Pull image data and convert to list
    for i in range(0, len(data) - numpx, numpx):
        section = sorted(data[i + j] for j in range(numpx))
        for k in range(numpx):
            data[i + k] = section[k]
    image.putdata(data)  # Push the sorted data back to the original image

def sort_by_sumrgb(image):
    """
    Sorts by the sum of red, green, and blue values of the pixels
    """
    data = list(image.getdata())
    sort = sorted([(sum(i), i) for i in data])
    for i in range(len(sort)):
        data[i] = sort[i][1]
    image.putdata(data)


if __name__ == '__main__':
    image = Image.open('yukon.jpg')
    start = time.clock()
    sort_by_column(image)
    end = time.clock()
    elapsed = '%.2f' % (end - start)
    print 'Image Sorted in ' + elapsed + ' seconds!'
    image.save('output.' + image.format.lower())
