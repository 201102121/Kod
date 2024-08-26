from tkinter import *

# Create the main window
tk = Tk()
tk.title("Rim raqamlari")
tk['bg'] = 'green'
tk['padx'] = 10
tk['pady'] = 5

label = Label(tk, text='Ozgartiruvchi', width=120, height=3, bg='green', fg='white')
label.pack()


text = Text(tk, width=90, height=1)
text.pack()


label1 = Label(tk, text='', height=3, bg='green', fg='white')
label1.pack()


def changer():
    son = text.get("1.0", END).strip()
    
    if son.isdigit():
        son = int(son)
        if 0 < son < 100000000:
            result = ""

            # 100 lar
            if son >= 900:
                result += "CM"
                son -= 900
            elif son >= 500:
                result += "D"
                son -= 500
            elif son >= 400:
                result += "CD"
                son -= 400
            elif son >= 100:
                result += "C" * (son // 100)
                son %= 100

            # 10 lar
            if son >= 90:
                result += "XC"
                son -= 90
            elif son >= 50:
                result += "L"
                son -= 50
            elif son >= 40:
                result += "XL"
                son -= 40
            elif son >= 10:
                result += "X" * (son // 10)
                son %= 10

            # 1 lar
            if son >= 9:
                result += "IX"
                son -= 9
            elif son >= 6:
                result += "V" + "I" * (son-5)
                son -= 8
            elif son >= 5:
                result += "V"
                son -= 5
            elif son >= 4:
                result += "IV"
                son -= 4
            elif son >= 1:
                result += "I" * son

            label1.config(text=result)
        else:
            label.config(text="Son 1 va 100000000 oralig'ida bo'lishi kerak.")
    else:
        label.config(text="Iltimos, to'g'ri son kiriting.")


button = Button(tk, text='Ozgartirish', command=changer, bg='yellow', height=2, width=15, pady=5)
button.pack()


tk.mainloop()
