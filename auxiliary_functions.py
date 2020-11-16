# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:18:44 2020

@author: sebas
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.io.wavfile import read
from scipy.fft import fft, fftfreq, fftshift

def read_signals(grabaciones):
    for i in grabaciones:
        data = "./grabaciones/"+i+"g.wav"
        print(data)
        fs,data_signal=read(data)
        t=np.arange(len(data_signal))/fs
        plt.figure(figsize=(15,8))
        plt.plot(t,data_signal)
        plt.title("Temperatura :"+"%s"%i+" ºC   en el dominio del tiempo")
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()
    
        Nmuestras = len(data_signal)
        yff = scipy.fft.fft(data_signal)
        xff = fftfreq(len(data_signal), 1/fs)[:Nmuestras//2]

        plt.plot(xff, 2.0/Nmuestras * np.abs(yff[0:Nmuestras//2]))
        plt.grid()
        plt.title("Temperatura :"+"%s"%i+" ºC  en el Dominio de la frecuencia")
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude')
        plt.show()
        print(fs)