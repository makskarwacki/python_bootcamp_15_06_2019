
def copy_file(src, dest, bufor=10000):
    with open(src, "rb") as f1, open(dest, "wb") as f2:
        while True:
            buf = f1.read(bufor)
            f2.write(buf)
            if not buf:
                break
        f2.flush()

copy_file("out.bin", "out-kopia.bin")
