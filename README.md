# wifiStatPy
A Python Library for the WifiStat

The wifiStat is an inexpensive thermostat sold on e-bay. Based on the work of a redditor 
reverse engineering the protocol I have started creating a python library for it. This is no frills,
no error handling, no class, and especially no brains. Error handling is on you, as I am only publishing this
because some other person may be interested. So far the interaction with the wifiStat is slow and sometimes clunky.
After a couple of requests the thermostat seems to stop responding. This will work for now, I may do something 
different in the future, so at that time I don't expect to continue development of this library.

Reddit Post https://www.reddit.com/r/homeautomation/comments/5e0550/presumably_chinese_wifi_thermostat_protocol/


To use this library
```sh
import wifiStat as stat
import time

wifistat_ip = IP Address of wifistat
wifistat_port = int(8899)
wifistat_password = 'what ever you have set as a password'
epoch = int(time.time())
day = '6' #day of the week start with sunday
schedule = 'W,4,30,67,70;L,6,30,60,65;R,19,0,67,70;S,22,0,60,65' # Check reddit post on this

seccode = str(stat.login(wifistat_ip, wifistat_port, wifistat_password))
stat.set_time(wifistat_ip, wifistat_port, seccode, str(epoch))
stat.send_schedule(wifistat_ip, wifistat_port, seccode, day, schedule))
```
