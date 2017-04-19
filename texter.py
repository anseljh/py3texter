"""
Send SMS from Python 3 using a little USB GSM modem!
https://github.com/anseljh/py3texter
"""

import serial
import sys


class Texter:

    def __init__(self, path):
        self.path = path
        # Establish serial connection:
        self.serial_connection = serial.Serial(path, timeout=1)

    def send(self, number, text):
        # Set text mode:
        self.serial_connection.write(bytes('AT+CMGF=%d\r' % 1, 'UTF-8'))
        # Set number:
        self.serial_connection.write(bytes('AT+CMGS="%s"\r' % number, 'UTF-8'))
        # Send message:
        self.serial_connection.write(bytes('%s\x1a' % text, 'UTF-8'))
        # Close connection:
        # self.serial_connection.close()


# Example
if __name__ == '__main__':
    instance = Texter('/dev/ttyUSB1')
    message = "Hello from Python!"
    if len(sys.argv) > 1:
        message = sys.argv[1]
    recipient = input("Phone number to send to? (Format like +12125551212) ")
    instance.send(recipient, message)
    print("Sent: \"%s\"" % message)
