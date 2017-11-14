import sounddevice as sd
import scipy.io.wavfile as wav


fileName="Partita_E_major.wav"

fs,data=wav.read(fileName)

sd.play(data,fs)
sd.wait()

print("*"*40)
print(" "*15+"Finished"+" "*15)
print("*"*40)


