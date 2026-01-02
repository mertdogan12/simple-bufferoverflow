#!/bin/sh
qemu-img create -f raw datadrct/debian 50G
qemu-system-x86_64 -hda datadrct/debian -cdrom cdromimg/debian-13.2.0-amd64-netinst.iso -boot d -m 2048
