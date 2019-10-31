from PIL import Image

def rd_file(file_name):
    with open (file_name, "r") as f:
        data = f.readlines()
        stext = ""
        for line in data:
            stext += str(line)
        strout = str(stext).replace(chr(10) + chr(32), chr(10))
        if strout[0] == chr(32):
            print("ok")
            strout = strout[1:]
        return strout

def wr_file(file_name, data):
    with open (file_name, "w") as f:
        f.write(data)

def string2pixelsRGB(text_str, file_name):
    text = text_str
    if len(text.encode()) % 3 == 2:
        text += chr(0)
    if len(text.encode()) % 3 == 1:
        text += 2* chr(0)

    pixs = len(text.encode()) // 3
    height = int(input(f"Ilość pixeli = {pixs}.\nMożliwe wymiary: {findfactors(pixs)} \n"
                   f"Podaj wysokość: "))
    width = pixs // height
    if width * height != pixs:
        print("Rozmiar obrazka nieprawidłowy: ".upper() + str((width // 3 ) * height) +
              " pixeli. Przywrócono ustawienia domyślne")
        print(findfactors(pixs) + "\n")
        height = 1
        width = len(text.encode()) // 3 // height
    else:
        print("Rozmiar obrazka: {0} x {1}\nLiczba pixeli: {2}".format(str(width), str(height), str(pixs)))

    im2 = Image.frombytes('RGB', (width, height), text.encode())
    im2.save(file_name, "PNG", optimize=True)
    return text

def string2pixelsCMYK(text_str, file_name):
    text = text_str

    if len(text.encode()) % 4 == 3:
        text += 1* chr(0)
    if len(text.encode()) % 4 == 2:
        text += 2* chr(0)
    if len(text.encode()) % 4 == 1:
        text += 3* chr(0)

    print("\nIlość bajtów do zakodowania:", len(text.encode()))

    pixs = len(text.encode()) // 4
    height = int(input(f"Ilość pixeli = {pixs}.\nMożliwe wymiary: {findfactors(pixs)} \n"
                       f"Podaj wysokość: "))
    width = pixs // height
    if width * height != pixs:
        print("Rozmiar obrazka nieprawidłowy: ".upper() + str(
            (width // 4) * height) + " pixeli. Przywrócono ustawienia domyślne")
        print(findfactors(pixs) + "\n")
        height = 1
        width = len(text.encode()) // 4 // height
    else:
        print("Rozmiar obrazka: {0} x {1}\nLiczba pixeli: {2}".format(str(width), str(height), str(pixs)))


    im2 = Image.frombytes('CMYK', (width, height), text.encode())
    im2.save(file_name, "TIFF", optimize=True)
    return text

def pixels2string(image_name):
    im3 = Image.open(image_name, 'r')
    p = im3.tobytes().decode()
    print(list(im3.getdata()))
    pstring = p.replace(chr(0), "")
    return pstring

def printarray(arr):
    for k, i in enumerate(range(0, len(arr), 3)):
        print(k, arr[i:i + 3])

def findfactors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            dimention = str(num // i) + " x " + str(i)
            factors.append(dimention)
    return  "Możliwe wymiary dla {} to {}".format(num, factors)

choice = int(input("Podaj wariant : 1 - RGB, 2 - CMYK :"))
file_in = "in.txt"
file_out = "out.txt"
print("Dane WE:", rd_file(file_in))

if choice == 1:
    file_n = "out.png"
    string2pixelsRGB(rd_file(file_in),file_n)
elif choice == 2:
    file_n = "out.tiff"
    string2pixelsCMYK(rd_file(file_in),file_n)

wr_file(file_out, pixels2string(file_n))
print("\nDane WY:\n",rd_file( file_out))