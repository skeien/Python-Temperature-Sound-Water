# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 11:00:33 2020

@author: sebas
"""




from numpy import argmax
from IPython.display import Audio
from auxiliary_functions import read_signals


    
grabaciones =["29","35","37","40","48","50","51","55","58","59","63","68","73","76","78","80"]
read_signals(grabaciones)

# sos = signal.butter(5, 7000, fs=44100, output='sos')
# filtered = signal.sosfilt(sos, data_signal)
# plt.plot(t, filtered)
# plt.title('Signal with filter passlow 100Hz')
# plt.xlabel('Time [seg]')
# plt.ylabel('Amplitude')
# plt.show()

# Nmuestras = len(filtered)
# yff = scipy.fft.fft(filtered)
# xff = fftfreq(len(filtered), 1/fs)[:Nmuestras//2]

# plt.plot(xff, 2.0/Nmuestras * np.abs(yff[0:Nmuestras//2]))
# plt.grid()
# plt.title('Domain of frequency')
# plt.xlabel('Frequency [Hz]')
# plt.ylabel('Amplitude')
# plt.show()

# write("temperature_filter.wav", fs, filtered)
# Audio(filtered, rate=fs)
