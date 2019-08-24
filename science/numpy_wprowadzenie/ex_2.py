import argparse

import numpy as np
from scipy import ndimage

import bmp


def parse_args():
    parser = argparse.ArgumentParser('Process BMP file')
    parser.add_argument('--input', help='input file', required=True)
    parser.add_argument('--output', help='output file', required=True)
    parser.add_argument('--rotate', help='rotate image', type=int)
    parser.add_argument('--blur', help='blur image', action='store_true')
    parser.add_argument('--black-white', help='black-white filter', action='store_true')
    parser.add_argument('--color', help='choose single color (RED, GREEN, BLUE)', type=str)
    return parser.parse_args()


def main():
    args = parse_args()
    data = bmp.read_bmp(args.input)

    if args.rotate:
        data = ndimage.rotate(data, angle=args.rotate)
    if args.blur:
        data = ndimage.gaussian_filter(data, sigma=3)
    if args.black_white:
        sum_array = data.sum(axis=2, keepdims=True) / 3
        data = np.ones(3) * sum_array
    if args.color:
        data = data * np.array([args.color == 'BLUE', args.color == 'GREEN', args.color == 'RED'])

    bmp.write_bmp(args.output, data)


if __name__ == '__main__':
    main()
