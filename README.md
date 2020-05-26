# raspberry-lcd-1602a
A basic python API for LCD screen 1602a on a raspberry pi 3 B+

## 1. Installation

Only one, run `sudo ./install.sh` to install i2c support and python3 smbus module

You can use `./remote_install.sh` to install all stuff on a remote (LAN) raspberry pi through ssh [TODO]

At every update run `python3 setup.py install` to update module [TODO]

## 2. Tests

There are some various tests to run on `./tests/`

## 3. Usage

```python3
import lcd
lcd_print("Hello !")
```