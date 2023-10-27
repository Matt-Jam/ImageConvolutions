import math
from PIL import Image

conv = [[1/273,4/273,7/273,4/273,1/273],
        [4/273,16/273,26/273,16/273,4/273],
        [7/273,26/273,41/273,26/273,7/273],
        [4/273,16/273,26/273,16/273,4/273],
        [1/273,4/273,7/273,4/273,1/273]]

filename = "sonic.jpg"

def guass(x,mu,sigma):
    y = (x-mu)/sigma
    return math.exp(-0.5*y*y)

def generate2DGaussianFilter(dimensions):
    mu = dimensions // 2
    sigma = mu/2
    s = 0
    kernel = [[0 for i in range(dimensions)] for j in range(dimensions)]
    for row in range(dimensions):
        for col in range(dimensions):
            a = guass(row,mu,sigma) * guass(col,mu,sigma)
            s += a
            kernel[row][col] = a
    kernel = [[val/s for val in row] for row in kernel]
    return kernel





#Unused currently
def getPixelCol(x,y,img):
    if ((y<0) or (y>img.size[1])):
        return (0,0,0)
    if ((x<0) or (x<img.size[0])):
        return (0,0,0)
    return img[x,y]

def clamp0255(val):
    if val < 0:
        return 0
    if val>255:
        return 255
    return int(val)

def scaleCol(scale,col):
    newCol = [0,0,0]
    for i in range(0,3):
        newCol[i] = clamp0255(col[i]*scale)
    return tuple(newCol)

            
def apply_convolution(conv,img):
    #Assumes conv in a 2D square array with odd side length
    rows = len(conv)
    indent = rows // 2
    targetimg = Image.new("RGBA",(img.size[0]-(rows-1),img.size[1]-(rows-1)),(0,0,0))
    targetimgPixels = targetimg.load()
    imgPixels = img.load()
    for x in range(indent,img.size[0]-indent):
        for y in range(indent,img.size[1]-indent):
            newcol = (0,0,0)
            for i in range(-indent,indent+1):
                for j in range(-indent,indent+1):
                    newcol = tuple(map(lambda a,b:a+b,scaleCol(conv[i+indent][j+indent],imgPixels[x+i,y+j]),newcol))
            targetimgPixels[x-indent,y-indent] = newcol
    targetimg.show()

if __name__ == "__main__":
    loadIm = Image.open(filename)
    apply_convolution(generate2DGaussianFilter(7),loadIm)
