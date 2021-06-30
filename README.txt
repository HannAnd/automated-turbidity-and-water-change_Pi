(incomplete)

Primary script is "scheduled_waterchange.py". All other files
are either .csv record files or code test files.

Goal for completed project is to utilize cron to initiate
scheduled, automated water changes which will be able to
1) record the turbidity of at multiple points in time
of a water change, 2) complete a fully automated water change,
3) control the turbidity of the water in a tank chamber
during water changes, 4) lower water in tank chambers to
appropriate levels to film fish behavior while minimizing
movement along the z-axis.

Symbolic links are used to create persistent names for each of
the Arduino used. The Vendor ID, Product ID and Serial Number
are used to identify the individual Arduinos. (These values
can be found by entering the console command
"udevadm info -n /dev/[tty port occupied by the Arduino]". To
create the symbolic link a custom udev file "99-usb-serial.rules"
was created in the directory "/etc/udev/rules.d". The file
followed the below format:

SUBSYSTEM=="tty", ATTRS{idVendor}=="[Vendor ID]", 
ATTRS{idProduct}=="[Product ID]",
ATTRS{serial}=="[Serial Number]",
SYMLINK+="[persistent name]", MODE=="0777"

With the above script repeated for each Arduino.


In development:
waterchange_test.py
scheduled_waterchange.py