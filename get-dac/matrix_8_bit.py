import display_8_bit


  
pix_arr = []
for i in range (256):
    tmp_arr = []
    for j in range(256):
        tmp_arr.append(1)
    pix_arr.append(tmp_arr)
pix_arr1 = []
for i in range (256):
    tmp_arr = []
    for j in range(256):
        tmp_arr.append((i+j)%2)
    pix_arr.append(tmp_arr)


if __name__ == "__main__":
    display = display_8_bit.DISPLAY_8_BIT()
    try:
        while True:
            display.matrix(pix_arr)
    finally:
        display.deinit()