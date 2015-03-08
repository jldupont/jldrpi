
Raspberry Pi command line tools

@author: Jean-Lou Dupont


* jldrpi-input : detect events on GPIO input pins and output JSON on stdout


## jldrpi-input

Use the `-p` option to define pin(s).

`jldrpi-input -p 25:FU 26:DR` defines pin 25 with internal pull-up and falling edge detection, pin 26 with pull-down and rising edge detection.


History
=======

0.1 : initial release

