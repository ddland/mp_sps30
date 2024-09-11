import serial
import time

ser1 = serial.Serial('/dev/ttyACM0')

output = 'datafile.csv'

fh = open(output, 'a')
run = True
while run:
    try:
        data = ser1.readline().decode().strip()[1:-1].split(',')
        data = [float(ii) for ii in data]
        data_str = ''
        for val in data:
            data_str += '%4.3f,' %val
        data_str = data_str[:-1] # remove extra ,
        data_str = str(time.time()) + ',' + data_str + '\n'
        fh.write(data_str)
        fh.flush()
        print(data_str[:-1])
    except KeyboardInterrupt:
        run = False
    except Exception as err:
        print(err)
fh.close()


