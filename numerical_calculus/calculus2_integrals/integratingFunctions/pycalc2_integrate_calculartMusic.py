"""Calculart! Create "music" from equations

COURSE: Master calculus 2 using Python: integration, intuition, code
SECTION: Integrating functions
LECTURE: Calculart! Create "music" from equations
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

### New!
from scipy.io import wavfile

# # Calculart 1: Make a simple sound

# sampling rate (44.1 kHz)
fs = 44100

# time vector
t = np.arange(0, 3-1/fs, 1/fs)

freq1 = 261.6   # middle C
freq2 = 329.628 # E

# create the sound (C+E)
sound = np.sin(2*np.pi*freq1*t) + np.sin(2*np.pi*freq2*t)

# and play it
Audio(sound, rate=fs)

# left and right channels (right channel is AM)
left  = 1*np.sin(2*np.pi*freq1*t)
right = np.sin(2*np.pi*freq2*t) * np.sin(2*np.pi*2*t)

# play that
Audio([left, right], rate=fs)

# need to scale to -1/+1
mono2write = (sound-np.min(sound))*2 / (np.max(sound)-np.min(sound)) - 1
print(np.min(sound), np.max(sound))
print(np.min(mono2write), np.max(mono2write))

# stereo needs to be a numpy array of size [samples X channels]
stereo = np.vstack((left, right)).T

# scaling
stereo2write = (stereo-np.min(stereo))*2 / (np.max(stereo)-np.min(stereo)) - 1

# write to wav file
wavfile.write('humanMusic_mono.wav', fs, mono2write)
wavfile.write('humanMusic_stereo.wav', fs, stereo2write)

print(f'Size of monochan matrix: {mono2write.shape}')
print(f'Size of stereo matrix:   {stereo2write.shape}')

# # Calculart 2: Make AM and FM sounds

# AM
t = np.arange(-np.pi, np.pi, 1/fs)

a = 1.5
AM = (1-a)+np.cos(a*t) + np.log(np.abs(t)+.001)
AM = 2*(AM-np.min(AM)) / (np.max(AM)-np.min(AM))
sound = AM * np.sin(2*np.pi*440*t)

plt.plot(t, AM)

# and play it
Audio(sound, rate=fs)

# FM

# Parameters
fc = 440 # carrier frequency
bw = 75  # bandwidth

# modulating signal
modsig = np.sin(2*np.pi*5*t)

# integrate the modulating signal and scale
modint = bw * np.cumsum(modsig) / fs

# FM signal
sound = np.cos(2*np.pi*(fc*t + modint))

Audio(sound, rate=fs)

# # Calculart 3: Make some mathy art noise

# and now for something weird

# FM part
FM = np.sin(2*np.pi*1.5*t) + np.log(np.abs(t)*2)
modint = bw * np.cumsum(FM) / fs

# AM part
AM = 1-np.linspace(-1, 1, len(t))**2

# create the sound
sound = AM * np.cos(2*np.pi*(fc*t + modint))

# visualize the FM modulation
_, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(t, FM, 'k', linewidth=2)
axs[0].set(xlabel='Time (s)', xlim=t[[0, -1]], yticks=[], ylabel='Frequency modulation (a.u.)', title='FM component')

axs[1].plot(t, AM, 'k', linewidth=2)
axs[1].set(xlabel='Time (s)', xlim=t[[0, -1]], yticks=[], ylabel='Amplitude modulation (a.u.)', title='AM component')

plt.tight_layout()
plt.show()

# # Calculart 4: Go crazy!

