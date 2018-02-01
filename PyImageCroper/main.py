""""
Written by Alec Bellinghausen Pagliarussi
Transform a table of images, into separate images according to the number of rows ans cols on that table,
then using trace2scad images are transformed into scad files, then those files are modified and the scad files
are rendered and exported as an stl file.

DEPENDENCIES
ImageMagick - sudo apt-get install imagemagick
Potrace - sudo apt-get install potrace
Openscad - sudo apt-get install openscad
Opencv - sudo apt-get install opencv
"""
import cv2
import numpy as np
import os
import sys

first_arg = sys.argv[1]
second_arg = sys.argv[2]
third_arg = sys.argv[3]

filePath = str(first_arg)
rowsConf = int(second_arg) #5
colsConf = int(third_arg) #16


def crop(imgToCrop, cols, rows, sizeX, sizeY):
    divx = sizeX/cols
    divy = sizeY/rows
    image = imgToCrop
    counter = 0
    fileName = filePath
    fileName=fileName.replace(".png", "")
    fileName=fileName.replace(".jpg", "")
    fileName=fileName.replace(".jpeg", "")
    fileName=fileName.replace(".gif", "")
    scriptPath = str(os.path.realpath(__file__))
    scriptPath=scriptPath.replace("main.py", "")
    try:
        #os.makedirs(scriptPath+fileName)
        pass
    except:
        print "directory already exist"
    #os.chdir(fileName)
    for y in range(rows):
        for x in range(cols):
            imgName = fileName+str(counter)
            imgName2 = imgName+".png"
            croppedImg = image[y*divy:(y+1)*divy, x*divx:(x+1)*divx]
            #cv2.imshow(imgName2, croppedImg)
            cv2.imwrite(imgName2, croppedImg)
            print "path1 "+"./trace2scad -f 0 "+imgName2
            os.system("./trace2scad -f 0 "+imgName2)
            with open(imgName+".scad", "a") as txt:
                print "Opening File"
                txt.write("scale([8.5,8.5,1])\n{\ndifference()\n{\ntranslate([0, 0, 1.5])cube([1.5, 2, .5], center=true);\ntranslate([0, 0, -.01])scale([2, 2, 5])"+imgName+"();\n}\n}")
                txt.close()
            print "path2: "+"openscad --render -o "+imgName+".stl "+imgName+".scad"
            os.system("openscad -o "+imgName+".stl "+imgName+".scad")
            counter += 1


img = cv2.imread(filePath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)
sizeY, sizeX = img.shape
print img.shape
# cv2.imshow("Image loaded", img)
crop(img, colsConf, rowsConf, sizeX, sizeY)
cv2.waitKey(0)
