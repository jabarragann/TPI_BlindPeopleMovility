import bluetooth

target_name = "DR-BTN200"
target_address = None
port = 0x1001

def search(searchTime):
  devices = bluetooth.discover_devices(duration=searchTime, lookup_names = True)
  return devices


if __name__=="__main__":

  print("Start discovering....")
  results = search(5);

  if results is not None:
    print("The following devices were found:")
    for addr, name in results:
      print("{0} - {1}".format(addr, name))

      if target_name == bluetooth.lookup_name( addr):
        target_address = addr
        break
      else:
        print ("nothing found!")


  if target_address == None:
    print("No devices found")
  else:
    print("Connecting")
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((target_address, port))
