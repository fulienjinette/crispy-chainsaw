from PIL import Image
import numpy
import sys
import itertools

image = Image.open(sys.argv[1]).convert('1')
data = numpy.asarray(image)

strings = ["B"]
counter = 0
for val in data.flat:
    if counter == 8:
        counter = 0
        strings.append("B")
    strings[-1] += "1" if val else "0"
    counter += 1

for i, s in enumerate(strings):
    if i > 0 and i % 16 == 0:
        print()
    print(s, end="")
    if i != len(strings) - 1:
        print(", ", end="")

