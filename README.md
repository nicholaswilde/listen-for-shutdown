# Listen For Shutdown

A combined power on / off button for the [Turing Pi](https://turingpi.com/)

You can wire GPIO 3 and a second GPIO connected together and to ground through a switch
Using GPIO 3 for power up and second GPIO for shutdown.

By default, the software assumes the switch is connected to pin BCM 24. The pin can be changed in the Python source file.
## Prerequisites
1. Python3
1. gpiozero

## Installation

1. [Connect to your Raspberry Pi via SSH](https://howchoo.com/g/mgi3mdnlnjq/how-to-log-in-to-a-raspberry-pi-via-ssh)
1. Clone this repo: `git clone https://github.com/lihak/rpi-power-button.git`
1. Run the setup script: `./rpi-power-button/script/install`

## Uninstallation

If you need to uninstall the power button script:

1. Run the uninstall script: `./rpi-power-button/script/uninstall`

## Hardware

Connect the power button to Pin 5 (BCM3 - SCL) and Pin 18 (BCM24) and any GND Pin shown in this diagram:

![Connection Diagram](https://raw.githubusercontent.com/lihak/pi-power-button/master/diagrams/pinout.png)
