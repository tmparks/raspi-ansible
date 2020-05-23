#!/bin/bash
# Turn USB power off and on.

if [ $(id --user) -ne 0 ]
then
	echo "Please execute $0 as root!"
	exit 1
fi

DEVICE=$(find /sys/devices -name buspower)
if [ -z "$DEVICE" ]
then
	echo "buspower device not found!"
	exit 1
fi

case "$1" in
off)
	shopt -s nullglob
	MOUNT_POINTS="/media/pi/* /mnt/*"
	if [ -n "$MOUNT_POINTS" ]
	then
		umount --verbose $MOUNT_POINTS
	fi
	echo 0 > $DEVICE
	;; 
on)
	echo 1 > $DEVICE
	;;
*)
	echo "Usage: $0 {off|on}"
	exit 1
	;;
esac

cat $DEVICE
