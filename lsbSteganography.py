import sys
import numpy as np
from PIL import Image
np.set_printoptions(threshold=sys.maxsize) # To use full representation instead of summarization

def encode(src, message, destination):
    # OPEN AND CREATE AN ARRAY OF THE SOURCE IMAGE
    sourceImage = Image.open(src,'r')
    width,height = sourceImage.size
    array = np.array(list (sourceImage.getdata()))


    if sourceImage.mode == 'RGB':
        n=3
    elif sourceImage.mode == 'RGBA':
        n = 4
    
    totalPixels = array.size//n

    message += "$END" #STOP FLAG TO SIGNIFY THAT THE MESSAGE IS DONE
    binaryMessage = ''.join([format(ord(i), "08b") for i in message]) #BINARY CONVERSION OF STRING
    requiredPixels = len(binaryMessage)

    if requiredPixels > totalPixels:
        print("Image size not sufficient for the message, try a larger image file")

    else:
        i = 0
        for p in range(totalPixels):
            for q in range(0,3):
                if i < requiredPixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + binaryMessage[i], 2) # bin() returns "0b--numbertobinary--" so the [2:9] is there to eliminate the "0b"
                    i += 1

        array = array.reshape(height,width,n)
        encryptedImage = Image.fromarray(array.astype('uint8'), sourceImage.mode)
        encryptedImage.save(destination)
        print("Image encoding successful...")


def decode(src):

    sourceImage = Image.open(src,'r')
    array = np.array(list(sourceImage.getdata()))

    if sourceImage.mode == 'RGB':
        n = 3
    elif sourceImage.mode == 'RGBA':
        n = 4

    totalPixels = array.size//n

    hiddenBits = ""
    for p in range(totalPixels):
        for q in range(0, 3):
            hiddenBits += (bin(array[p][q])[2:][-1])

    hiddenBits = [hiddenBits[i:i+8] for i in range(0, len(hiddenBits), 8)]# this makes the hiddenbits string into 8 bit groups

    message = ""
    for i in range(len(hiddenBits)):
        if message[-4:] == "$END":
            break
        else:
            message += chr(int(hiddenBits[i], 2))#convert each 8 bit to a char
    if "$END" in message:
        print("Payload:", message[:-4]) 
    else:
        print("No Hidden Message Found")


def main():
    print("LSB STEGANOGRAPHY TOOL")
    print("Enter 1 to encode an image")
    print("Enter 2 to decode an image")
    while True:
        userInput = input()

        if userInput == "1":
            print("Enter the source path of the image to encode:")
            src = input()
            print("Enter message to be hidden: ")
            message = input()
            print("Enter the destination path of your image: ")
            destination = input()

            encode(src,message,destination)

        elif userInput == "2":
            print("Enter source path of the image you wish to decode: ")
            src = input()
            
            decode(src)
        else:
            print("There was an unknown error, try again...")

main()
