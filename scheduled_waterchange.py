###make sure all of the signposts are the appropriate INTEGERS
###they will be going through a switch-case so no strings

# Cron will initiate this file at the specified times to start a water change
# when this script runs it's supposed to immediately start the water change process

import serial    # allows Pi to read serial data
import time    # allows Pi to keep track of time
import csv    # for writing turbidity readings to CSV
from datetime import datetime    # for recording the time a turbidity reading was taken
ready = "no"    # indicates when the next water change can start (assuming only one at a time for now)
waiting = 0    # keeps track of how many tanks are ready to start the water change cycle
# list containing numbers for each tank chamber
# numbers will be removed from the array as water changes are completed on each chamber
chambers = list(range(1,24))   # array containing the number of chambers

### I need to learn more about arrays. I should have an array that contains every chamber that has done
### a water change this cycle and the randomizer refers to it before picking the next chamber

if __name__ == '__main__':    #defines this file as primary module
    # calls the serial monitor using serial.Serial at port 'ttyACM0' (change if needed),
      # sets the baud rate (needs to be the same as the Arduino), and sets a
      # timeout so that if the Arduino stops sending info the Pi doesn't
      # get stuck in a loop
    # each Arduino has been assigned a symlink in the Raspberry Pi's udev rules,
      # see README for more information
    ser1 = serial.Serial('/dev/arduino1', 9600, timeout = 1)
    #ser2 = serial.Serial('/dev/arduino2', 9600, timeout = 1)
    #ser3 = serial.Serial('/dev/arduino3', 9600, timeout = 1)
    #ser4 = serial.Serial('/dev/arduino4', 9600, timeout = 1)
    #ser5 = serial.Serial('/dev/arduino5', 9600, timeout = 1)
    #ser6 = serial.Serial('/dev/arduino6', 9600, timeout = 1)
    #ser7 = serial.Serial('/dev/arduino7', 9600, timeout = 1)
    #ser8 = serial.Serial('/dev/arduino8', 9600, timeout = 1)
    # clearing buffer
    ser1.flush()
    #ser2.flush()
    #ser3.flush()
    #ser4.flush()
    #ser5.flush()
    #ser6.flush()
    #ser7.flush()
    #ser8.flush()
    # short delay before first read request
    time.sleep(2)
    
    while True:    # creates an infinite loop because this should always
                   # be the primary module
        # asking all of the Arduinos what the turbidity readings are for each tank chamber
        if start == "yes":
            ser1.write(b"1~NA\n")
            #ser2.write(b"1~NA\n")
            #ser3.write(b"1~NA\n")
            #ser4.write(b"1~NA\n")
            #ser5.write(b"1~NA\n")
            #ser6.write(b"1~NA\n")
            #ser7.write(b"1~NA\n")
            #ser8.write(b"1~NA\n")
            start = "no"
        
        # checks if something is in Serial
        if ser1.in_waiting > 0:
            # readline() reads all bytes in a line from serial monitor
            # decode() converts the bytes from their raw form to their
              # intended string
            # rstrip() removes "trailing characters" and excess white space from
              # the beginning/end of a line
            #I'll need a parser here to decide if an Arduino message is a sensor reading or a "finished" message
            #IF SENSOR READING the first two characters will be c1, c2 or c3 followed by a ~ and the voltage reading
              #c1 = chamber 1, c2 = chamber 2, c3 = chamber 3. Parser will have to deal with that
            received = ser1.readline().decode('utf-8').rstrip()
            when = datetime.now()
            print(received)
            #'signpost' used by the parser to determine the type of message
              # 'check' signposts are just used to received a printout
              # 'chamber' indicates which tank chamber the message is coming from
              # 'message' is the rest of the data received from the Arduino
                # can be sensor reasing or status printout
            signpost,chamber,message = received.split("~")
            # prints turbidity reading for visibility
            print("Signpost -" + signpost + "- from chamber " + chamber + ".  Message: " + message)
            # turbidity reading from Tank 1 Chamber 1
            if signpost == "t":
                with open("Turbidity_Record.csv", "a") as fileA:
                    # row format: tank number, chamber number, datetime, turbidity reading
                    datarow = ["1", chamber, when, message]
                    writer = csv.writer(fileA)
                    writer.writerow(datarow)  #not sure this line is necessary
                    waiting += 1
            # recording the time of water change for each tank chamber
            elif signpost == "w":
                with open ("Waterchange_Record.csv", "a") as file:
                    # row format: tank number, chamber number, datetime
                    datarow = ["1", chamber, when]
                    writer = csv.writer(file_b)
                    writer.writerow(datarow)
                    ready = "yes"
                    chambers.remove(int(message))
        
        # begins the water change cycle after all chambers have sent turbidities
        if waiting == 24 and once == "no":
            #math to calculate the clear water to add to each tank
            #just going to have three clearwater variables in total because
            #there are only three chambers per tank and each tank has its own
            #Serial to contend with
            ser1.write(b"2~" + clear1 + "\n")
            time.sleep(0.5)
            ser1.write(b"3~" + clear2 + "\n")
            time.sleep(0.5)
            ser1.write(b"4~" + clear3 + "\n")
            
            #the same math
            #ser2.write(b"2~" + clear1 + "\n")
            #time.sleep(0.5)
            #ser2.write(b"3~" + clear2 + "\n")
            #time.sleep(0.5)
            #ser2.write(b"4~" + clear3 + "\n")
            
            #math again
            #ser3.write(b"2~" + clear1 + "\n")
            #time.sleep(0.5)
            #ser3.write(b"3~" + clear2 + "\n")
            #time.sleep(0.5)
            #ser3.write(b"4~" + clear3 + "\n")
            
            #math again
            #ser4.write(b"2~" + clear1 + "\n")
            #time.sleep(0.5)
            #ser4.write(b"3~" + clear2 + "\n")
            #time.sleep(0.5)
            #ser4.write(b"4~" + clear3 + "\n")
            
            #math again
            #ser5.write(b"2~" + clear1 + "\n")
            #time.sleep(0.5)
            #ser5.write(b"3~" + clear2 + "\n")
            #time.sleep(0.5)
            #ser5.write(b"4~" + clear3 + "\n")
            
            #math again
            #ser6.write(b"2~" + clear1 + "\n")
            #time.sleep(0.5)
            #ser6.write(b"3~" + clear2 + "\n")
            #time.sleep(0.5)
            #ser6.write(b"4~" + clear3 + "\n")
            
            #math again
            #ser7.write(b"2~" + clear1 + "\n")
            #time.sleep(0.5)
            #ser7.write(b"3~" + clear2 + "\n")
            #time.sleep(0.5)
            #ser7.write(b"4~" + clear3 + "\n")
            
            #so much of the same math
            #ser8.write(b"2~" + clear1 + "\n")
            #time.sleep(0.5)
            #ser8.write(b"3~" + clear2 + "\n")
            #time.sleep(0.5)
            #ser8.write(b"4~" + clear3 + "\n")
            
            # prevents Pi from sending clearwater values more than once
            once = "yes"
                    
            #and then a function that randomly picks chambers without repeats until all chambers are done
                    