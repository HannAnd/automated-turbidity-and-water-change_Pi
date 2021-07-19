#Serial format from Pi: signpost~message
#Serial format from Arduino: signpost~chamber#~sensor reading

import serial
from datetime import datetime
import time
import csv    # for writing turbidity readings to CSV

waiting = "no"    # so the test doesn't start until the turbidity readings have been taken
signpost = "NA"
chamber = "NA"
reading = "NA"
start = "yes"
ready = 0
once = "no"


if __name__ == '__main__':
    # each Arduino has been assigned a symlink in the Pi's udev rules
        #see README for more information
    ser1 = serial.Serial('/dev/arduino7', 9600, timeout = 1)
    # clearing buffer
    ser1.flush()
    # short delay before first read request
    time.sleep(2)
    
    while True:
        if start == "yes":  # sending the request only once
            # requesting turbidity reading from Arduino
            ser1.write(b"1~NA\n")
            start = "no"
        if ready == 3 and once == "no":
            # sending the calibrated clear water values for each of the three tank chambers
            ser1.write(b"2~620\n")  # chamber 1
            time.sleep(1)
            ser1.write(b"3~769\n")  # chamber 2, calibrated to 12cm
            time.sleep(1)
            ser1.write(b"4~629\n")  # chamber 3
            time.sleep(1)
            once = "yes"
        
        # checks if something is in Serial
        if ser1.in_waiting > 0:
            received = ser1.readline().decode('utf-8').rstrip()
            when = datetime.now()
            #print("Received: " + received)
            # 'signpost' used by the parser to determine the type of message
              # 'check' signposts are just used to received a printout
            # 'chamber' indicates which tank chamber the message is coming from
            # 'message' is the rest of the data received from the Arduino
              # can be sensor reasing or status printout
            signpost,chamber,message = received.split("~")
            # prints turbidity reading for visibility
            print("Signpost -" + signpost + "- from chamber " + chamber + ".  Message: " + message)
            # "t" messages contain turbidity readings
            if signpost == "t":
                # adds turbidity readings to "test_readings.csv" without deleting present values
                with open("test_readings.csv", "a") as file_a:
                    # row format: tank number, chamber number, datetime, turbidity reading
                    datarow = ["1", chamber, when, message]
                    writer = csv.writer(file_a)
                    # sends amount of clearwater to be added to each tank chamber
                      #since this is test code we'll just give arbitrary amounts for clearwater/blackwater
                    ready += 1
                    #if chamber == "1":
                        #ser1.write(b"2~620\n")
                        #time.sleep(1)
                        #ready += 1
                    #if chamber == "2":
                        #ser1.write(b"3~640\n")
                        #time.sleep(1)
                        #ready += 1
                    #if chamber == "3":
                        #ser1.write(b"4~629\n")
                        #time.sleep(1)
                        #ready +=1
            
            # "r" messages indicate Arduino is ready for water changes
            elif signpost == "r":
                # starts water changes
                #at the moment we're only going to mess around with a single chamber
                #in the real thing there will be some randomization going on
                # value after ~ tells Arduino which chamber to run
                  # values 1-3 represent a turbid water change on chambers 1, 2 or 3, respectively
                  # values 4-5 represent a clearwater only water change on chambers 1, 2 or 3, respectively
                  #since we're only doing one chamber at the moment we only need chamber 1
                ser1.write(b"5~1\n")
                waiting = "no"
                
            # "w" messages indicate a water change is complete
            elif signpost == "w":
                # recording the time the water change is completed for each chamber
                with open ("test_record.csv", "a") as file_b:
                    # row format: tank number, chamber number, datetime
                    datarow = ["1", message, when]
                    writer = csv.writer(file_b)
                    writer.writerow(datarow)
                    ready = "yes"
                    #chambers.remove(int(message))
                
                        
                        
