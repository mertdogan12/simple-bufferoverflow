all: build

build:
	gcc -std=c89 -fno-stack-protector -z execstack -no-pie -g main.c

exp:
	(cat payload.bin && cat) | ./a.out
