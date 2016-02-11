from PIL import Image
import numpy
import sys

def chop(iterator, size):
    group = []
    finished = False
    iterator = iter(iterator)
    while not finished:
        for i in range(size):
            try:
                group.append(next(iterator))
            except StopIteration:
                finished = True
                break
        else:
            yield group
            group = []

if __name__ == "__main__":
    image = Image.open(sys.argv[1]).convert('1')
    data = numpy.asarray(image)
    groups = chop(data.flat, 8)

    strings = ["B" + ''.join('1' if val else '0' for val in group) for group in groups]

    for segment in chop(strings, 16):
        print(', '.join(segment))
