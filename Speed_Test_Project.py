
import speedtest
wifi  = speedtest.Speedtest()
import time

counter= 0

print("Speed Test is Running - Please Wait")

DownloadSpeed = round(wifi.download(), 2)

for counter, x in enumerate(list(range(101))):
    counter += 1
    time.sleep(0.08)
    if counter == 101:
        break
    print("Gathering Download Speed:", counter,"%", end="\r")

print("\n")
print("Finalizing Speed Test - Please Wait")

UploadSpeed = round(wifi.upload(), 2)

for counter, x in enumerate(list(range(101))):
    counter += 1
    time.sleep(0.08)
    if counter == 101:
        break
    print("Gathering Upload Speed:", counter,"%", end="\r")

print("\n")

#1000000 is represented as 1 million kbs which equates to 1  gbs

Download_Speed = DownloadSpeed // 1000000
Upload_Speed = UploadSpeed // 1000000 

print("Wifi Download Speed is ", Download_Speed, "GB's")
print("Wifi Upload Speed is ", Upload_Speed, "GB's")
