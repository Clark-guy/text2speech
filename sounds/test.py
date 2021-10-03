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


def plotWav(data):
    plt.figure()
    plt.plot(data)
    plt.xlabel("index")
    plt.ylabel("Amplitude")
    plt.title("waveform of audio")
    plt.show()

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
    filename = "g.wav"
    playsound("g.wav")
    Fs, data = read(filename)
    data = data[:,0]
    out = np.empty([])
    out = np.concatenate((out, data), axis=None)
    plotWav(data)
    plotWav(out)
    out = np.delete(out, 0)
    print(np.array_equal(data, out))
    print(data.shape)
    print(out.shape)
    write("out.wav", Fs, out.astype(np.int32))
    playsound("out.wav")



if __name__ == "__main__":
    main()
