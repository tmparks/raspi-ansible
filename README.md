# raspi-ansible
Automated management for the Raspberry Pi.

## boot-folder.yml

Configure the Raspberry Pi before first boot.
[Image](https://www.raspberrypi.org/blog/raspberry-pi-imager-imaging-utility)
a microSD card with the latest version of
[Raspberry Pi OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/).
Insert the microSD card into your computer (not the Raspberry Pi)
before running this playbook, and the Raspberry Pi will be configured to
enable headless operation via WiFi and remote access via SSH.

See [this guide](https://www.raspberrypi.org/documentation/configuration/boot_folder.md)
and [this guide](https://www.raspberrypi.org/documentation/configuration/config-txt/)

## cacti.yml

Configure the Raspberry Pi to monitor your home network using cacti.

## external-storage.yml

Configure the Raspberry Pi to use external USB storage.
Connect a storage device to the Raspberry Pi before running this playbook,
and /etc/fstab will be configured to automatically mount the device.

See [this guide](https://www.raspberrypi.org/documentation/configuration/external-storage.md)

## security.yml

Configure the Raspberry Pi to require key-based authentication for ssh.

See [this guide](https://www.raspberrypi.org/documentation/configuration/security.md)
