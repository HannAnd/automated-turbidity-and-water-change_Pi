# Cron will initiate this file at the specified times to start a water change
# when this script runs it's supposed to immediately start the water change process

import serial    # allows Pi to read serial data
import time    # allows Pi to keep track of time
import csv    # for writing turbidity readings to CSV
from datetime import datetime    # for recording the time a turbidity reading was taken
import random  # allows Pi to randomize list order
ready = "no"    # indicates when the next water change can start (assuming only one at a time for now)
waiting = 0    # keeps track of how many tanks are ready to start the water change cycle
t1 = 0  # counter to keep track of which number on the randomized list the waterchanges have reached
t2 = 0
t3 = 0
t4 = 0
# list of water change messages for each tank chamber by Arduino#
wchange = ["5~1\n", "5~2\n", "5~3\n", "5~1\n", "5~2\n", "5~3\n"]
# holds variables that randomly decide between each pair of Arduinos
    # 0-2 represent the first Arduino of the pair and 3-5 the second
r1_2 = [0, 1, 2, 3, 4, 5]
r3_4 = [0, 1, 2, 3, 4, 5]
r5_6 = [0, 1, 2, 3, 4, 5]
r7_8 = [0, 1, 2, 3, 4, 5]

#tank chambers need to be divided into four groups:
    #Arduinos 1 & 2, Arduinos 3 & 4,
    #Arduinos 5 & 6, Arduinos 7 & 8
#only one pump from each chamnber may be permitted to run at a time
###put a script here that randomizes the order of tank chambers in each of those groups

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
            
        #below if-statment is main body of code. Should determine if we want to keep it
            #here or dump it at the bottom of the file
        # begins the water change cycle after all chambers have sent turbidities
        if waiting == 24 and once == "no":
            #math to calculate the clear water to add to each tank
            #just going to have three clearwater variables in total because
            #there are only three chambers per tank and each tank has its own
            #Serial to contend with
            #values going to arbitrary for now until calibrations can be done
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
            
            
            
        
        # all code below deals with responses to Arduino messages
        
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
            
            
            # all code below responds to messages based on the signpost
            
            # turbidity reading from Tank 1 Chamber 1
            if signpost == "t":
                # appends turbidity readings to existing csv without deleting old entries
                with open("Turbidity_Record.csv", "a") as fileA:
                    # row format: tank number, chamber number, datetime, turbidity reading
                    datarow = ["1", chamber, when, message]
                    writer = csv.writer(fileA)
                    writer.writerow(datarow)  #not sure this line is necessary
                    waiting += 1
            # an Arduino registering it is ready for water changes
            # when all 24 chambers are ready water changes will start
            elif signpost == "r":
                timetostart += 1
                # starting the first set of four water changes
                if timetostart == 24:
                    # randomizing water change order
                    random.shuffle(r1_2)
                    random.shuffle(r3_4)
                    random.shuffle(r5_6)
                    random.shuffle(r7_8)
                    # values 0-2 represent Arduino 1 (the first of the pair) and 3-5 Arduino 2 (the second of the pair)
                    if r1_2[t1] <= 2:
                        i = r1_2[0]
                        ser1.write(bytes(wchange[i], 'utf-8'))
                        t1 += 1
                    if r1_2[t1] >= 3:
                        i = r1_2[0]
                        ser2.write(bytes(wchange[i], 'utf-8'))
                        t1 += 1
                    if r3_4[t2] <= 2:
                        i = r1_2[0]
                        ser3.write(bytes(wchange[i], 'utf-8'))
                        t2 += 1
                    if r3_4[t2] >= 3:
                        i = r1_2[0]
                        ser4.write(bytes(wchange[i], 'utf-8'))
                        t2 += 1
                    if r5_6[t3] <= 2:
                        i = r1_2[0]
                        ser5.write(bytes(wchange[i], 'utf-8'))
                        t3 += 1
                    if r5_6[t3] >= 3:
                        i = r1_2[0]
                        ser6.write(bytes(wchange[i], 'utf-8'))
                        t3 += 1
                    if r7_8[t4] <= 2:
                        i = r1_2[0]
                        ser7.write(bytes(wchange[i], 'utf-8'))
                        t4 += 1
                    if r7_8[t4] >= 3:
                        i = r1_2[0]
                        ser8.write(bytes(wchange[i], 'utf-8'))
                        t4 += 1
                    timetostart == 25


            # recording the time of water change for each tank chamber and then starting the next waterchange
            elif signpost == "w":
                with open ("Waterchange_Record.csv", "a") as file:
                    # row format: tank number, chamber number, datetime
                    datarow = ["1", chamber, when]
                    writer = csv.writer(file_b)
                    writer.writerow(datarow)
                    ready = "yes"
                    #keep in mind that all of this is still just for Arduino 1
                    if r1_2[t1] <= 2:
                        i = r1_2[t1]
                        ser1.write(bytes(wchange[i], 'utf-8'))
                        t1 += 1
                    if r1_2[t1] >= 3:
                        i = r1_2[t1]
                        ser2.write(bytes(wchange[i], 'utf-8'))
                        t1 += 1
        
        
                    
            #and then a function that randomly picks chambers without repeats until all chambers are done
                    