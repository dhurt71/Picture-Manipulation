 
# CSUF CPSC 305
# Mini-Project 3
#
# Group Members:
#   Devon Hurt
#   

file = pickAFile()
pict = makePicture(file)

#call functions to show effect of each one
def negativeTest():
  negative(pict)
  show(pict)

def maxBlueTest():
  maxBlue(pict)
  show(pict)

def blacktopTest():
  blacktop(pict)
  show(pict)

def mirrorUpHalfTest():
  mirrorUpHalf(pict)
  show(pict)


#function definitions
def negative(picture):
  for px in getPixels(picture):
    red = getRed(px)
    green = getGreen(px)
    blue = getBlue(px)
    negColor = makeColor(255-red, 255-green, 255-blue)
    setColor(px, negColor)
  
def maxBlue(picture):
  for p in getPixels(picture):
    value = getBlue(p)
    setBlue(p, value = 255)

def blacktop(picture):
   pixels = getPixels(picture)
   for index in range(0, len(pixels)/2):
     pixel = pixels[index]
     valueRed = getRed(pixel)
     setRed(pixel, value = 0)
     valueGreen = getGreen(pixel)
     setGreen(pixel, value = 0)
     valueBlue = getBlue(pixel)
     setBlue(pixel, value = 0)

def mirrorUpHalf(picture):
  pixels = getPixels(picture)
  target = len(pixels)/2
  for index in range(len(pixels)/2, len(pixels) - 1):
    pixel1 = pixels[index]
    color1 = getColor(pixel1)
    pixel2 = pixels[target]
    setColor(pixel2, color1)
    target = target - 1




    
