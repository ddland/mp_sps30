import machine
import time

from sps30 import SPS30

if __name__ == "__main__":
    sda = machine.Pin(0)
    scl = machine.Pin(1)
    i2c = machine.I2C(0, sda=sda, scl=scl, freq=100000)
    sps30 = SPS30(i2c, print_output=True)
    time.sleep(5)
    sps30.start_measurement()
    run = True
    errors = 0
    while run:
        try:
            sps30.read_data()
            print(sps30.last_measurement)
            time.sleep(5)
            errors = 0
        except OSError as err:
            errors += 1
            print(err, errors)
        except KeyboardInterrupt:
            run = False
