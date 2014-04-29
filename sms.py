import serial
from curses import ascii



##set serial
ser = serial.Serial()

##Set port connection to USB port GSM modem 
ser.port = '/dev/tty.HUAWEIMobile-Pcui'

## set older phones to a baudrate of 9600 and new phones and 3G modems to 115200
ser.baudrate = 115200
ser.timeout = 1
ser.open()

## Important understand the difference between PDU and text mode, in PDU istructions are sent to the port as numbers eg: 0,1,2,3,4 and in TEXT mode as text eg: "ALL", "REC READ" etc
## following line sets port into text mode, all instructions have to be sent to port as text not number
ser.write('AT+CMGS=1\r\n')
##Important positive responses from the modem are always returned as OK

##you may want to set a sleep timer between sending texts of a few seconds to help the system process

def sendsms(number,text):
    ser.write('AT+CMGF=1\r\n')
    ser.write('AT+CMGS="%s"\r\n' % number)
    ser.write('%s' % text)
    ser.write(ascii.ctrl('z'))
    print "Text: %s  \nhas been sent to: %s" %(text,number)

def read_all_sms():
    ser.write('AT+CMGS=4\r\n')
    ser.read(100)
    ser.write('AT+CMGL="ALL"\r\n')
    ser.read(1)
    a = ser.readlines()
    for x in a:
        print x

def read_unread_sms():
    ##returns all unread sms's on your sim card
    ser.write('AT+CMGS=0\r\n')
    ser.read(100)
    ser.write('AT+CMGL="REC UNREAD"\r\n')
    ser.read(1)
    a = ser.readlines()
    for x in a:
        print x

def read_read_sms():
    ##returns all unread sms's on your sim card
    ser.write('AT+CMGS=1\r\n')
    ser.read(100)
    ser.write('AT+CMGL="REC READ"\r\n')
    ser.read(1)
    a = ser.readlines()
    for x in a:
        print x

def delete_all_sms():
    ##this changes modem back into PDU mode and deletes all texts then changes modem back into text mode
    ser.write('AT+CMGF=0\r\n')
    ser.write('AT+CMGD=0,4\r\n')
    ser.write('AT+CMGF=1\r\n')

def delete_read_sms():
    ##this changes modem back into PDU mode and deletes read texts then changes modem back into text mode
    ser.write('AT+CMGF=0\r\n')
    ser.write('AT+CMGD=0,1\r\n')
    ser.write('AT+CMGF=1\r\n')
    
