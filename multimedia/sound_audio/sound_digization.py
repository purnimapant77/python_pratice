import sounddevice as sd
import matplotlib.pyplot as plt
duration = 3  
fs = 44100     
print("Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
print("Done")
plt.plot(audio)
plt.title("Waveform")
plt.show()