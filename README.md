# raspi-ansible
Automated management for the Raspberry Pi.

## external-storage.yml

Configure the Raspberry Pi to use external USB storage.
Connect a storage device before running this playbook,
and /etc/fstab will be configured to automatically mount
the device.

See [this guide](https://www.raspberrypi.org/documentation/configuration/external-storage.md)

## security.yml

Configure the Raspberry Pi to require key-based authentication for ssh.

See [this guide](https://www.raspberrypi.org/documentation/configuration/security.md)
