import sounddevice as sd
import scipy.io.wavfile as wav
import subprocess

def connectDevice():
  connect = subprocess.Popen(['./bluetoothConnection.sh'],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)

def checkDeviceConnection():
  cat = subprocess.Popen(['./deviceInformation.sh'],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
  
  grep = subprocess.Popen(['grep', 'Connected'],
                          stdin=cat.stdout,
                          stdout=subprocess.PIPE,)
  
  end_of_pipe = grep.stdout
  
  
  for line in end_of_pipe:
    info1=str(line).strip()
    info1=info1[4:-3]
    return info1

def playWavFile():
  fileName="Partita_E_major.wav"
  fs,data=wav.read(fileName)
  sd.play(data,fs)
  sd.wait()

if __name__ == "__main__":
  
  print("Checking Device Connection")
  connected=checkDeviceConnection().split(" ")[1].strip()
  
  if connected=="no":
    print("Device is not connected beginning connection")
    connectDevice()
    connected=checkDeviceConnection().split(" ")[1].strip()
    
    if connected=="yes":
      print("Connection successful")
    else:
      print("Can not connect with the device")
      
  else:    
    print("Your device is connected.")
  
  if connected=="yes":
    print("Lets play a wav File...!")
    playWavFile()
  
  
  
      