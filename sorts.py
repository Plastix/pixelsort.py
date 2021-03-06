#!/usr/bin/env python
import numpy
import click


def sort_by_row(image):
    """
    Sorts each row of the specified image
    Returns the sorted image.
    """
    return numpy.sort(image, axis=1)


def sort_by_column(image):
    """
    Sorts each column of the specified image.
    Returns the sorted image.
    """
    return numpy.sort(image, axis=0)


def sort_by_npx(image, numpx):
    """
    Splits the image into segments of N pixels and sorts each one
    Returns the sorted image.
    """
    depth = image.shape[2]
    # Convert the 3D array into 2D
    # Squeeze trims the enapsulating arrays left over from reshape
    flat = numpy.reshape(image, (-1, 1, depth)).squeeze()
    new_width = flat.shape[0]
    remainder = new_width % numpx
    split_index = new_width - remainder

    # Transform the 2D array into a 3D array of N pixel segments
    # Because N pixels won't evenly divide into our array evenly every time we
    # have to split the array at split_index and sort the other part separately
    reshaped = numpy.reshape(flat[:split_index], (-1, numpx, depth))
    sort1 = numpy.sort(reshaped, axis=1)
    sort1 = numpy.reshape(sort1, (-1, 1, depth)).squeeze()

    sort2 = numpy.sort(flat[split_index:], axis=1)

    # Combine the parts back together and reshape back into original image size
    sort_final = numpy.vstack((sort1, sort2))
    return numpy.reshape(sort_final, image.shape)


def sort_by_sumrgb(image):
    """
    Sorts by the sum of red, green, and blue values of the pixels
    Returns the sorted image.
    """
    # Reshape to 2D array
    flat = numpy.reshape(image, (-1, 1, image.shape[2])).squeeze()
    # Sum RGB values
    sums = numpy.sum(image, axis=2).flatten()
    # Calculate sort indicies then sort by them
    sort_indices = numpy.argsort(sums)
    return flat[sort_indices].reshape(image.shape)


def sort_by_chan(image, chan):
    """
    Sorts by the specified channel
    Returns the sorted image.
    """
    if chan > image.shape[2] - 1:
        raise click.BadParameter('Image does not have %s channels!' % chan)
    # Reshape to 2D array
    flat = numpy.reshape(image, (-1, 1, image.shape[2])).squeeze()
    # Get specified Channel
    channel = image[:, :, chan].flatten()
    # Calculate sort indicies then sort by them
    sort_indices = numpy.argsort(channel)
    return flat[sort_indices].reshape(image.shape)
