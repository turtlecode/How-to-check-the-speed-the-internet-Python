import speedtest
wifi  = speedtest.Speedtest()
print("Wifi Download Speed is ", wifi.download()/1024/1024)
print("Wifi Upload Speed is ", wifi.upload()/1024/1024)