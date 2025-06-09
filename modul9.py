from termcolor import colored, cprint
import time
import os

def loading () :
    persen = [10, 35, 40, 55, 75, 90, 100]
    for p in (persen) :
        os.system("cls")
        cprint ("Selamat datang di Aplikasi-KU", "cyan", attrs=["bold"])
        cprint (f"\nLoading {p}%", "red")
        time.sleep(1)

def logo():
    icon = [
        "    **    ",
        "   ****   ",
        "  **  **  ",
        " **    ** ",
        "  **  **  ",
        "   ****   ",
        "    **    ",
    ]
    print()

    for i in icon:
        baris = ""
        for j in i :
            if j == "*":
                baris += colored(" ", on_color="on_magenta")  
            else:
                baris += colored(" ", on_color="on_black") 
        print(baris)

loading()
logo()
cprint ("\nSelamat menggunakan Aplikasi-KU!!", "cyan", attrs=["bold"])
