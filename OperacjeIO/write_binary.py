

frame = bytearray()
frame.append(0x41) # 16*4 + 1
frame.append(0x42)
frame.append(0x43)
frame.append(0x44)

with open("out.bin", "wb+") as f:
    f.write(frame)
    f.seek(0)
    line = f.read()
    print(line.decode())

