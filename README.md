# rpi-power-button

Combined Power on / off Button for Raspberry Pi

You can wire GPIO 3 and a second GPIO connected together and to ground through a switch
Using GPIO 3 for power up and second GPIO for shutdown
By default, the software assumes the switch is connected to pin BCM 24. The pin can be changed in the Python source file.

## Installation

1. [Connect to your Raspberry Pi via SSH](https://howchoo.com/g/mgi3mdnlnjq/how-to-log-in-to-a-raspberry-pi-via-ssh)
1. Clone this repo: `git clone https://github.com/lihak/pi-power-button.git`
1. Run the setup script: `./rpi-power-button/script/install`

## Uninstallation

If you need to uninstall the power button script:

1. Run the uninstall script: `./rpi-power-button/script/uninstall`

## Hardware

A full list of what you'll need can be found [here](https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi#parts-list). At a minimum, you'll need a normally-open (NO) power button, some jumper wires, and a soldering iron. If you _don't_ have a soldering iron or don't feel like breaking it out, you can use [this prebuilt button](https://howchoo.com/shop/product/prebuilt-raspberry-pi-power-button) instead.

Connect the power button to Pin 5 (BCM3 - SCL) and Pin 18 (BCM24) and any GND Pin shown in this diagram:

![Connection Diagram](https://raw.githubusercontent.com/lihak/pi-power-button/master/diagrams/pinout.png)
