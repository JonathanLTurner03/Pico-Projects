from machine import ADC
from utime import sleep

pot = ADC(26)

print("Beginning Check:")

def convert_to_percentage(value):
    return (value / 65535) * 100

max = 10000
counter = 0
previous = 0

while counter < max:
    actual = pot.read_u16()
    conversion = int(convert_to_percentage(actual))
    if (conversion % 2 == 0):
        print("Pos is: ", str(actual), " | Perc is: ", str(conversion))
    sleep(0.1)
    counter+=1