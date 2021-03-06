import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
#from IPython.display import Audio
from numpy.fft import fft, ifft
#%matplotlib inline
import random
import copy
import multiprocessing
from playsound import playsound
import math
import sys
import os
import time

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')



def laugh():
    for x in range(10):
        clearScreen()
        print(chr(0x1f602))
        time.sleep(.2)
        clearScreen()
        print(chr(0x1f60a))
        time.sleep(.2)

def listAllEmojisAndDoSomeOtherShit():
    x = chr(593)
    y = 0x1f600
    print(x)
    for z in range(80):
        print(z, " ", chr(y+z))
    print(x.encode("unicode_escape"))
    print(ord(x))
    #laugh()

def buildDict():
    engToIPADict = dict()
    f = open("en_US.txt", 'r')
    for line in f:
        splitline = line.split("\t")
        splitline[1] = splitline[1][:-1]
        engToIPADict[splitline[0]] = splitline[1]
    f.close()
    return engToIPADict

def stringToIPA(string):
    string = "zero one two three four five six seven eight nine"
    outstring = ""
    words = string.split(" ")
    IPADict = buildDict()
    for word in words:
        wordToAdd = IPADict[word]
        wordToAdd = wordToAdd.split("/")
        outstring += wordToAdd[1] + " "
    return outstring

def IPAStringToWAV(string):
    out = np.empty([])
    for ch in string:
        if ch == '\'':
            pass
            # do something to make next sound more emphasized- maybe like i dunno increase amplitude or length of next sound
        if ch == ' ':
            out = np.concatenate((out, np.zeros(10000)), axis=None)
        else:
            if ord(ch) == 609:
                ch = 'g'
            try:
                fileName = "sounds/" + ch + ".wav"
                Fs, data = read(fileName)
                data = data[:,0]
                out = np.concatenate((out, data[:5000]), axis=None)
                
            except:
                print("failed char: ", ch)
    write("out.wav", Fs, out.astype(np.int32))
    playsound("out.wav")
    
        


def main():
    IPAString = stringToIPA("hello")    
    print(IPAString)
    IPAStringToWAV(IPAString)
    # needs to first convert string to IPA using .txt dictionary i found on github
    # then needs to convert IPA to speech using dictionary that maps IPA characters to recorded waveforms from synth
    # for each letter, append to numpy array until done


if __name__ == "__main__":
    main()
