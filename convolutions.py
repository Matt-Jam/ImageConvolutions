from PIL import Image;

conv = [[0.04,0.04,0.04,0.04,0.04],
        [0.04,0.04,0.04,0.04,0.04],
        [0.04,0.04,0.04,0.04,0.04],
        [0.04,0.04,0.04,0.04,0.04],
        [0.04,0.04,0.04,0.04,0.04]]

filename = "ImageConvolutions\shrek.jpg"
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
    apply_convolution(conv,loadIm)
