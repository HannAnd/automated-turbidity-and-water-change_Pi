import serial
import csv
import time

readyA = "yes"
readyB = "no"


if __name__ == '__main__':
    ser1 = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)  #change tty port as necessary
    # clearing buffer
    ser1.flush()
    # short delay before first read request
    time.sleep(2)
    
    while True:
        if readyA == "yes":
            ser1.write(b"a~1\n")
            readyA = "no"
        if readyB == "yes":
            ser1.write(b"b~1.3\n")
            readyB = "no"
        #ser1.write(b"a~1\n")
        
        # checks if something is in Serial
        if ser1.in_waiting > 0:
            received = ser1.readline().decode('utf-8').rstrip()
            print("Received: " + received)
            signpost,message = received.split("~")
            # prints turbidity reading for visibility
            print("Signpost: " + signpost + "  Message: " + message)
            time.sleep(2)
            if signpost == "a":
                readyB = "yes"
            if signpost == "b":
                readyA = "yes"