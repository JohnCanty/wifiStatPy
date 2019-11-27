#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:16:22 2019

@author: John
"""
import socket
import re

def wifistat_send(ip, port, command):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(command)
    data = s.recv(1024)
    s.close()
    sdata = data.decode('utf-8')
    return sdata

def login(ip, port, password):
    command = str('*GUP' + password + '*L_I')
    response = str(wifistat_send(ip, port, str.encode(command)))
    if re.search("(sucessfully)", response) is not None:
        seccode = str(re.findall('(\d{4})', response))
    else:
        seccode = 666
    return seccode

def send_schedule(ip, port, seccode, day, schedule):
    command = str(day + ';' + schedule + ':' + seccode + '*W_S')
    response = str(wifistat_send(ip, port, str.encode(command)))
    if re.search("(W_S1)", response) is not None:
        status = 0
    else:
        status = 1
    return status

def set_time(ip, port, seccode, time):
    command = str(time + ':' + seccode + '*S_T')
    response = str(wifistat_send(ip, port, str.encode(command)))
    print(response)
    if re.search("(S_T1)", response) is not None:
        status = 0
    else:
        status = 1
    return status




# Get the security code from the thermostat. This is usually a 4 digit number that lets the thermostat
# Know that you have logged in sucessfully.

#seccode = str(login('10.10.11.54', int(8899), 'test'))

# Send a schedule to the thermostat
#W,6,0,67,70; W is wake The first digit is the Hour the second the minute Followed by the temp setpoints.
#W - Wake
#L - Leave
#R - Return
#S - Sleep
#To Write a schedule for Friday Day = 6
#W,4,30,67,70;L,7,0,60,65;R,19,0,67,70;S,22,0,60,65

#print(send_schedule('10.10.11.54', int(8899), seccode, '6', 'W,4,30,67,70;L,6,30,60,65;R,19,0,67,70;S,22,0,60,65'))
