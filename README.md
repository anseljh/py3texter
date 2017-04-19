# py3texter
Send SMS from Python 3 using a little USB GSM modem

## Dependencies
* [pyserial](https://pypi.python.org/pypi/pyserial)

## Example Usage
```python
from texter import Texter

t = Texter('/dev/ttyUSB1')
recipient = input("Phone number to send to? (Format like +12125551212) ")
message = input("Message? ")
t.send(recipient, message)
```

## Tested with
* Raspberry Pi Zero W
* [ZTE MF190](http://amzn.to/2oKEUt2) USB GSM modem

## License
* MIT License
