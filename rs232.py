from serial import *
import time
import keyboard
from tkinter import *
import threading

root = Tk()
root.title("rs232 바코드")
root.geometry("500x500")
ser = Serial(port="COM6", bytesize=8, baudrate=9600, stopbits=STOPBITS_ONE, timeout=1)

e = Entry(root, width=30)
e.pack()



def run_serial():
    while ser.is_open == True:
        receive=ser.readline().decode("ascii")
        e.insert(0,receive)        
        

        if len(receive) > 0:
            e.delete(len(receive),'end')
            


        # if e.get() != receive:
        #     e.insert(0, receive)
        #     #e.delete(3)

        # elif e.get() == receive:
        #     e.delete(13)
        #     e.insert(0, receive)


        print("e.get값 : {}".format(e.get()))
        print("receive값 : {}".format(receive))
        print("e.get 자리수 : {}".format(len(e.get())))
        print("receive 자리수 : {}".format(len(receive)))
        #print("num 자리수값 : {}".format(num))                


def del_barcode():
    e.delete(0,"end")
    

def check_serial_state():
    if ser.is_open == False:
        print("오픈상태")
    else:
        print("클로즈상태")
                              

a = threading.Thread(target=run_serial)
a.start()

btn1 = Button(root, text="초기화", command=del_barcode)
btn1.pack()

btn2 = Button(root, text="통신상태체크", command=check_serial_state)
btn2.pack()


root.mainloop()











