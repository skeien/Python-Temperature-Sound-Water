# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 11:00:33 2020

@author: sebas
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
import scipy
from scipy.fft import fft, fftfreq, fftshift
from scipy import fftpack, signal
from numpy import argmax
from IPython.display import Audio


fs,data_signal=read("hola_hola.wav")
t=np.arange(len(data_signal))/fs
plt.figure(figsize=(15,8))
plt.plot(t,data_signal)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

Nmuestras = len(data_signal)
yff = scipy.fft.fft(data_signal);
xff = fftfreq(len(data_signal), 1/fs)[:Nmuestras//2];

plt.plot(xff, 2.0/Nmuestras * np.abs(yff[0:Nmuestras//2]))
plt.grid()
plt.title('Señal Original en el Dominio de la Frecuencia')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.show()
print(fs)
sos = signal.butter(5, 7000, fs=44100, output='sos')
filtered = signal.sosfilt(sos, data_signal)
plt.plot(t, filtered)
plt.title('Señal con Filtro Paso Bajas de 7000Hz')
plt.xlabel('Tiempo [seg]')
plt.ylabel('Amplitud')
plt.show()

Nmuestras = len(filtered)
yff = scipy.fft.fft(filtered);
xff = fftfreq(len(filtered), 1/fs)[:Nmuestras//2];

plt.plot(xff, 2.0/Nmuestras * np.abs(yff[0:Nmuestras//2]))
plt.grid()
plt.title('Dominio de la Frecuencia')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.show()

write("Voz_filtrada.wav", fs, filtered)
Audio(filtered, rate=fs)