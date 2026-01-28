all: build

build:
	gcc -std=c89 -fno-stack-protector -z execstack -no-pie -g main.c
