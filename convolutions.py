from PIL import Image;
conv = [[0.1,0.1,0.1],
        [0.1,0.1,0.1],
        [0.1,0.1,0.1]]

filename = ""
#Unneccesary right now, but could be helpful in the future if I want more complex behaviour
#in the edge cases
def getPixelCol(x,y,img):
    if ((y<0) or (y>img.size[1])):
        return (0,0,0,0)
    if ((x<0) or (x<img.size[0])):
        return (0,0,0,0)
    return img[x,y]

def clamp0255(val):
    if val < 0:
        return 0
    if val>255:
        return 255
    return val

def scaleCol(scale,col):
    newCol = [0,0,0,0]
    for i in range(0,4):
        newCol[i] = clamp0255(col[i]*scale)
    return tuple(newCol)


def apply_convolution(conv,img):
    #Assumes conv in a 2D square array with odd side length
    rows = len(conv)
    indent = rows // 2
    targetimg = Image.new("RGBA",(img.size[0],img.size[1]),(0,0,0))
    for x in range(indent,img.size[0]-indent):
        for y in range(indent,img.size[1]-indent):





