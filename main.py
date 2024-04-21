from machine import ADC
from utime import sleep

pot = ADC(26)

print("Beginning Check:")

def convert_to_percentage(value):
    return (value / 65535) * 100

while True:
    actual = pot.read_u16()
    print("Pos is: ", str(actual), " | Perc is: ", str(convert_to_percentage(actual)))
    sleep(0.1)