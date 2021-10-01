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

def IPAStringToWAV(string):
    Fs = 44100
    out = np.empty([])
    for ch in string:
        try:
            fileName = "sounds/" + ch + ".wav"
            print(fileName)
            Fs, data = read(fileName)
            data = data[:,0]
            out = np.concetenate((out, data), axis=None)
        except:
            print("failed char")
    write("out.wav", Fs, out)
    playAudio("out.wav")

def main():
    filename = "k.wav"
    Fs, data = read(filename)
    out = np.empty([])
    for x in range(10):
        out = np.concatenate((out, data), axis=None)
    write("out.wav", Fs, out)
    playsound("out.wav")
    
if __name__ == "__main__":
    main()
