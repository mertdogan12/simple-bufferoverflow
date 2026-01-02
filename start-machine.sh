#!/bin/sh
qemu-system-x86_64 -hda datadrct/debian \
	-boot d \
	-m 2048 \
	-virtfs local,path=.,mount_tag=shared,security_model=mapped-xattr
