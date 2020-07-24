# import the packages listed below
from os import system
import os
import cv2
import progressBar
import time
import random

# this code is supposed to append all the array values of the 20k images
# it has added progress bars to show the progress so far
# this file is also for the model to be added below the pre-processing
# pre-processing couldn't be in another file because creating binary .npy files made it to large to push to github

# directories with 256 x 256 grayscale images
# Pranav Directories
newWithoutDir = 'C:/Users/Singaraju/Desktop/Face Mask Detection Data/20k_faces/new_without_mask/'
newWithDir = 'C:/Users/Singaraju/Desktop/Face Mask Detection Data/20k_faces/new_with_mask/'

# Lavik Directories
# newWithoutDir = 'D:/Face Mask Detection Dataset/new_without_mask/'
# newWithDir = 'D:/Face Mask Detection Dataset/new_with_mask/'

# declare an empty data list
images = []

# time, counter, i = 0
totalTime = 0.0
counter = 0
i = 0

print('Program Started... ')  # print that the program started
time.sleep(1)  # wait for 1 second
system('cls')  # clear the screen/console on call
start = time.time()  # start the timer

# bar method with reading the image for the 10k images with a mask
progressBar.barMethod1(0, 1000, prefix='Loading Faces... ', suffix='Complete', length=50, time=0)

# loop in order to append all new mask image values
for image in os.listdir(newWithDir):
    # every 10 increments, update the bar
    if counter % 10 == 0:
        progressBar.barMethod1(i + 1, 1000, prefix='Loading Faces... ', suffix='Complete', length=50,
                               time=float(totalTime))
        i += 1
    imageMain = cv2.imread(newWithDir + image)  # read the image from the directory
    images.append((imageMain, 1))  # append the list of image value and label to the data list
    counter += 1  # increment counter by 1
    end = time.time()  # end time
    totalTime = float(end - start)  # totalTime now equals the end value minus beginning value

# time, counter, i = 0
totalTime = 0.0
counter = 0
i = 0
start = time.time()  # start the timer

# bar method with reading the image for the 10k images with a mask
progressBar.barMethod1(0, 1000, prefix='Optimizing Images... ', suffix='Complete', length=50, time=0)

# loop in order to append all new without mask image values
for image in os.listdir(newWithoutDir):
    # every 10 increments, update the bar
    if counter % 10 == 0:
        progressBar.barMethod1(i + 1, 1000, prefix='Optimizing Images... ', suffix='Complete', length=50,
                               time=float(totalTime))
        i += 1
    imageMain = cv2.imread(newWithoutDir + image)  # read the image from the directory
    images.append((imageMain, 0))  # append the list of image value and label to the data list
    counter += 1  # increment counter by 1
    end = time.time()  # end time
    totalTime = float(end - start)  # totalTime now equals the end value minus beginning value

# shuffle the list in place
random.shuffle(images)

# declare the data and target lists
data = []
labels = []

# split the finalSet into data and labels
# no mask = 0 & mask = 1
for i in images:
    data.append(i[0])
for i in images:
    labels.append(i[1])
