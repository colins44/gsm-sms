gsm-sms
=======

A small python script that allows you to send, receive and delete SMS's using a USB GSM dongle modem

I created this using a HUAWEI E220 modem and a vodaphone sim card, not sure but i gues it should work with other modems

first find and install the driver software for your particular modem

Next set up and connect to your modem within network settings, set the APN to your network (Look up your networks APN online) set the phone number ( you can use default #99*, or your number no country code) and chose GPRS 3G as modem type

Next find the USB directory that your modem is plugged into by running $ ls /dev/tty* within terminal. Find the path to your modem and set that to the modem path within the sms.py file

run the sms.py file in your shell

to send sms type:


sendsms('number','text that you want to send')

eg:

sendsms('0711100011','this is the message im sending')

to read all sms's on your sim card:

read_all_sms()

To read just the read sms's:

read_read_sms()

To read the unread sms's on your sim card:

read_unread_sms()

to delete all sms's from the sim card:

delete_all_sms()

to delete just the read sms's from the sim card:

delete_read_sms()
