from math import ceil
import argparse
import os
import select
import sys

from PIL import Image, ImageDraw, ImageOps
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter

STYLE = "inkpot"
MAIN_COLOR = "#1E1E26"
MAIN_COLOR_TUPLE = (30, 30, 38)

DEFAULT_BACKGROUND_COLOR = "#D7ACB9"
COLORS = ["#D7ACB9", '#87FFCC', '#E4E6E8', '#5EBA7D', '#848689']


def generate_code(code: str):
    formatter = ImageFormatter(font_size=25, style="inkpot", line_number_bg="#1E1E26")  # font_name="Ubuntu Mono",
    with open("6bdaf8da92a088eb74885f97c8310cfeec949661a5f19bf060599cff55172418", "wb+") as f:
        highlight(code, PythonLexer(), formatter, f)
    im = Image.open("6bdaf8da92a088eb74885f97c8310cfeec949661a5f19bf060599cff55172418")
    os.remove('6bdaf8da92a088eb74885f97c8310cfeec949661a5f19bf060599cff55172418')
    return im


def generate_im(code: str, filename_out: str = "image.png", background_color: str = DEFAULT_BACKGROUND_COLOR):
    im_from_pygments = generate_code(code)

    window_im_size = (im_from_pygments.size[0] + 40, im_from_pygments.size[1] + 70)

    window_im = Image.new('RGBA', window_im_size, MAIN_COLOR)
    box = (window_im.size[0] - im_from_pygments.size[0]) // 2, (window_im.size[1] - im_from_pygments.size[1]) // 2
    window_im.paste(im_from_pygments, box)

    background = Image.new("RGBA", window_im_size, (*MAIN_COLOR_TUPLE, 0))
    draw = ImageDraw.Draw(background)
    draw.rounded_rectangle(((0, 0), window_im_size), 20, (*MAIN_COLOR_TUPLE, 255))

    background.paste(im_from_pygments, box)

    full_im = Image.new('RGBA', (ceil(window_im_size[0] * 2), ceil(window_im_size[1] * 1.4)), background_color)
    box = (full_im.size[0] - window_im.size[0]) // 2, (full_im.size[1] - window_im.size[1]) // 2

    full_im.paste(background, box, background)
    full_im.save(filename_out)


def main():
    parser = argparse.ArgumentParser(description='generate beautiful image of python code')
    parser.add_argument('file', nargs='?', action="store", help='filename to generate from')
    parser.add_argument('-f', '--file_out', action="store", help='filename to store in')
    parser.add_argument('-c', '--color', action="store",
                        help='background color, default is {}'.format(DEFAULT_BACKGROUND_COLOR))
    args = parser.parse_args()
    color = None
    if not args.color:
        color = DEFAULT_BACKGROUND_COLOR
    else:
        color = args.color

    try:
        idx = int(color)
    except ValueError:
        pass
    else:
        color = COLORS[idx]

    pipe = None
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        pipe = sys.stdin.read()
    if pipe:
        code = pipe
    elif args.file:
        code = open(args.file, 'r').read()
    else:
        print("Error, no file or pipe specified")
        sys.exit(1)

    generate_im(code, args.file_out if args.file_out else 'image.png', color)


if __name__ == "__main__":
    main()
