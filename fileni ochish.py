from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile

tk = Tk()

lugat = {'А': 'A', 'Б': 'B', 'Ч': 'Ch', 'Д': 'D', 'Е': 'E', 'Ф': 'F', 'Г': 'G', 'Ғ': "G'", 'Ҳ': 'H', 'И': 'I', 'Ж': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'Ў': "O'", 'П': 'P', 'Қ': 'Q', 'Р': 'R', 'С': 'S', 'Ш': 'SH', 'Т': 'T', 'У': 'U', 'В': 'V', 'Х': 'X', 'Й': 'Y', 'З': 'Z', 'A': 'А', 'B': 'Б', 'CH': 'Ч', 'D': 'Д', 'E': 'Е', 'F': 'Ф', 'G': 'Г', "G'": 'Ғ', 'H': 'Ҳ', 'I': 'И', 'J': 'Ж', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О', "O'": 'Ў', 'P': 'П', 'Q': 'Қ', 'R': 'Р', 'S': 'С', 'SH': 'Ш', 'T': 'Т', 'U': 'У', 'V': 'В', 'X': 'Х', 'Y': 'Й', 'Z': 'З'}


def krill_to_lotin():
    global txt
    result = ""
    i = 0   
    text = txt.get(1.0, END)

    while i < (len(text) - 1):
        harf = text[i]

        if text[i] + text[i+1] == "Sh":
            harf = "Sh"
            i += 1
        elif text[i] + text[i+1] == "sh":
            harf = "sh"
            i += 1
        elif text[i] + text[i+1] == "Ch":
            harf = "Ch"
            i += 1
        elif text[i] + text[i+1] == "ch":
            harf = "ch"
            i += 1
        elif text[i] + text[i+1] == "O'":
            harf = "O'"
            i += 1
        elif text[i] + text[i+1] == "o'":
            harf = "o'"
            i += 1
        elif text[i] + text[i+1] == "G'":
            harf = "G'"
            i += 1
        elif text[i] + text[i+1] == "g'":
            harf = "g'"
            i += 1
        elif text[i] + text[i+1] == "Q":
            harf = "Q"
            i += 1
        elif text[i] + text[i+1] == "q":
            harf = "q"
            i += 1


        try:
            if harf.islower():
                result += lugat[harf.upper()].lower()
            else:
                result += lugat[harf.upper()]
        except:
            result += harf
        i += 1
    txt.delete(1.0, END)
    txt.insert(1.0, result)

def open_file():
    global txt
    mask = \
        [("Text and Python files", "*.txt *.py *.pyw"),
         ("HTML files", "*.htm"),
         ("All files", "*.*")]
    file = askopenfile(initialdir="", filetypes=mask, mode='r')
    text = file.name
    text2 = open(text)
    txt.delete(1.0, END)
    txt.insert(1.0, text2.read())
    text2.close()

def save_file():
    global txt
    mask = \
        [("Text and Python files", "*.txt *.py *.pyw"),
         ("HTML files", "*.htm"),
         ("All files", "*.*")]
    file = asksaveasfile(mode='w', filetypes=mask, defaultextension=".txt", initialdir="")
    text3 = file.name
    text = open(text3, 'w')
    text2 = txt.get(1.0, END)
    text.write(text2)
    text.close()


txt = Text(tk)
txt.grid(row=0)
Button(tk, text="O'tkazish", command=krill_to_lotin).grid(row=1, column=0)
Button(tk, text="Open file", command=open_file).place(x=80, y=414)
Button(tk, text="Save file", command=save_file).place(x=470, y=414)



tk.mainloop()
