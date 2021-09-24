from tkinter import *
from tkinter import filedialog

process = True
i, ending, adress = 0, "", ""
word = ""
end = ["jpg", "jpeg", "png", "bmp", "raw", "tiff", "gif", "psd"]
kwords = []


def UploadAction(event=None):
    global adress, ending
    filename = filedialog.askopenfilename()
    ending = filename.split('.')[-1]
    adress = filename


def clicked():
    global kwords
    kwords = txt.get().split(",")


def info():
    if ending in end:
        for key, val in enumerate(kwords):
            print(key, val)
            kwords[key] = kwords[key].replace(" ", "")
        print(adress)
        print(kwords)


root = Tk()
root.geometry("500x500")

lbl = Label(root, text="Upload file", font=("Arial Bold", 15))
lbl.grid(column=0, row=0)

btn1 = Button(root, text='Upload', width=10, font=("Arial Bold", 12), command=(UploadAction))
btn1.grid(column=1, row=0)

lbl = Label(root, text="Key words:   ", font=("Arial Bold", 15))
lbl.grid(column=0, row=1)

txt = Entry(root, width=25)
txt.grid(column=1, row=1)

btn2 = Button(root, text="Add", font=("Arial Bold", 12), command=clicked)
btn2.grid(column=2, row=1)

btn3 = Button(root, text="Generate", font=("Arial Bold", 12), command=info)
btn3.grid(column=0, row=10)

root.mainloop()
