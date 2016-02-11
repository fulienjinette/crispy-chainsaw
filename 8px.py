from PIL import Image
import numpy
import sys

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

print(", ".join(strings))


