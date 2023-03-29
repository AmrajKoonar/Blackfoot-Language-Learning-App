#2022/11/16


#import statements
import random
import cmpt120image

# This line has exactly 100 characters (including the period), use it to keep each line under limit.

#function that changed the color of image
def recolorImage(img,color):
    newImg = cmpt120image.getBlackImage(len(img),len(img))
    for row in range(len(img)):
        for col in range(len(img[row])):

            #test if the rgb value is any number that is larger then 230
            if (img[row][col][0] > 230) and (img[row][col][1] > 230) and (img[row][col][2] > 230):
                newImg[row][col] = [255,255,255]

            else:

                newImg[row][col] = color



    return newImg


#function that minimizes the image by getting average rgb of 2x2 pixels
def minify(img):
    rowAdd = 0
    miniImg = cmpt120image.getBlackImage(len(img)//2,len(img)//2)
    for row in range(0,len(img),+2):
        colAdd = 0
        for col in range(0,len(img),+2):
            red_avg = (img[row][col][0] + img[row+1][col][0] +
                                                                img[row+1][col+1][0] +
                                                                img[row][col+1][0])/4
            green_avg = (img[row][col][1] + img[row+1][col][1] +
                                                                img[row+1][col+1][1] +
                                                                img[row][col+1][1])/4
            blue_avg = (img[row][col][2] + img[row+1][col][2] +
                                                                img[row+1][col+1][2] +
                                                                img[row][col+1][2])/4

            miniImg[rowAdd][colAdd] = [red_avg, green_avg, blue_avg]
            colAdd += 1
        rowAdd += 1

    return miniImg


#function that flips or mirrors the image
def mirror(img):
    mirrorImg = cmpt120image.getBlackImage(len(img),len(img))
    for row in range(len(img)):
        count = len(img)-1
        for col in range(len(img)):
            mirrorImg[row][col] = img[row][count]
            count -= 1

    return mirrorImg

#function that draws the image at a certain position
def drawItem(img,item,row,col):
    newCanvas = img
    for i in range(len(item)):
        for j in range(len(item)):
            #test if the rgb value is any number that is larger then 230
            if (item[i][j][0] > 230) and (item[i][j][1] > 230) and (item[i][j][2] > 230):

                newCanvas[i][j] = img[i][j]

            else:
                newCanvas[i+row][j+col] = item[i][j]


    return newCanvas

#function that draws randomized amounts of the image
def distributeItems(img,item,n):
    newDrawing = img

    for i in range(n):
        newDrawing = drawItem(newDrawing,item,random.randint(0,len(newDrawing)
                                                                            -len(item)),
                                                                            random.randint(0,len
                                                                            (newDrawing)-len
                                                                            (item)))
    return newDrawing


##################################################################################################################################3
