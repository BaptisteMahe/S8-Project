from PIL import Image, ImageDraw
from random import randrange
from time import time
import os

# global variables

size = 90
resolution = 10
num = int(size / resolution)
grid = []
databasePath = os.path.dirname(os.path.abspath(__file__)) + "\\database\\"
imgId = str(int(open(databasePath + "tracks.txt", "r").read()))
nbImgs = 2

t = time()

for n in range(0, nbImgs):

    imgId = str(int(imgId) + 1)

    # generating a random grid

    grid = [[randrange(0, 2) for i in range(0, num)] for j in range(0, num)]

    # set up the drawing

    img = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(img)

    # draw a black rectangle for every 1 in the grid

    for i in range(0, num):
        for j in range(0, num):
            if grid[i][j] == 1:
                x0, y0 = i * resolution, j * resolution
                x1, y1 = (i + 1) * resolution, (j + 1) * resolution
                draw.rectangle([x0, y0, x1, y1], fill='black')

    # name and save the result

    file = databasePath + imgId + "img.png"
    img.save(file)

# update the tracking

open(databasePath + "tracks.txt", "w").write(imgId)

# img.show()

print("total time : " + str(round((time() - t) * 1000)) + "ms")
