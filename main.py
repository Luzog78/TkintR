from tkinter import *
from random import randint

tk = Tk()

tk.title("Mon Application Tkinter")
tk.geometry("720x480")
tk.iconbitmap("src/icon.ico")
tk.configure(background="gray", highlightthickness=16)


###################
###################


card_frame = Frame(tk, height=240, width=240, highlightthickness=1, highlightbackground="black")
card_frame.pack(side="top", anchor="w", padx=8, pady=8)
card_frame.pack_propagate(0)

card_l2 = Label(card_frame, text=" -  -  - ", width=8, bg="green", fg="lime")
card_l2.place(relx=0.5, rely=0.55, anchor=CENTER)

def card_handler(text: str = None, bg=None, fg=None):
    if text: card_l2.configure(text=text)
    else: card_l2.configure(text=" -  -  - ", bg="green", fg="lime")
    if fg: card_l2.configure(fg=fg)
    if bg: card_l2.configure(bg=bg)

# Cardinal Button Configuration
bconf = {"width": 7, "height": 1, "anchor": CENTER}

card_n = Button(card_frame, text="Nord", **bconf, command=lambda: card_handler("Nord", "blue", "deep sky blue"))
card_n.pack(side='top')

card_w = Button(card_frame, text="Ouest", **bconf, command=lambda: card_handler("Ouest", "dark orange", "yellow"))
card_w.pack(side='left')

card_e = Button(card_frame, text="Est", **bconf, command=lambda: card_handler("Est", "firebrick1", "red4"))
card_e.pack(side='right')

card_s = Button(card_frame, text="Sud", **bconf, command=lambda: card_handler("Sud", "green3", "lawn green"))
card_s.pack(side='bottom')

card_r = Button(card_frame, text="Reset", **bconf, command=lambda: card_handler())
card_r.place(relx=0.5, rely=0.7, anchor=CENTER)

card_l1 = Label(card_frame, text="Points Cardinaux", width=12, bg="green", fg="lime")
card_l1.place(relx=0.5, rely=0.45, anchor=CENTER)


###################
###################


cookie_count = 0

def update_cookie_btn():
    global cookie_count
    cookie_btn.configure(bg="#{:0>2}".format(str(hex(randint(0, 255)))[2:]) + "{:0>2}".format(str(hex(randint(0, 255)))[2:]) + "{:0>2}".format(str(hex(randint(0, 255)))[2:]))
    cookie_label.configure(text=f"{cookie_count} cookies",
                           bg="#{:0>2}".format(str(hex(randint(0, 255)))[2:]) + "{:0>2}".format(str(hex(randint(0, 255)))[2:]) + "{:0>2}".format(str(hex(randint(0, 255)))[2:]))
    cookie_count += 1

cookie_label = Label(tk, width=30)
cookie_label.place(relx=0.55, rely=0.2)

cookie_btn = Button(tk, width=30, text="Click", command=update_cookie_btn)
cookie_btn.place(relx=0.55, rely=0.3)

update_cookie_btn()


###################
###################


chekout_frame = Frame(tk, padx=20, pady=20, height=200)
chekout_frame.pack(side="bottom", fill="x", padx=16, pady=16)
chekout_frame.grid_propagate(0)
chekout_frame.pack_propagate(0)  # 'Cause the last widjet is packing

chk_in = Entry(chekout_frame, width=35)
chk_in.grid(column=0, row=0, columnspan=3)

r1_label = Label(chekout_frame, text="Vous aimez :")
r1_label.grid(column=0, row=1, columnspan=3)
r1_btn_vals = IntVar()
r1_btn_vals_table = ["Rien de Ouf", "Ta Mère", "Ton Père", "Ton Frère"]
r1_btn_1 = Radiobutton(chekout_frame, text=r1_btn_vals_table[1], variable=r1_btn_vals, value=1)
r1_btn_1.grid(column=0, row=2)
r1_btn_2 = Radiobutton(chekout_frame, text=r1_btn_vals_table[2], variable=r1_btn_vals, value=2)
r1_btn_2.grid(column=1, row=2)
r1_btn_3 = Radiobutton(chekout_frame, text=r1_btn_vals_table[3], variable=r1_btn_vals, value=3)
r1_btn_3.grid(column=2, row=2)

r2_label = Label(chekout_frame, text="Vous n'aimez pas :")
r2_label.grid(column=0, row=3, columnspan=3)
r2_btn_vals = IntVar()
r2_btn_vals_table = ["Prsn Miskinnn", "Ton Oncle", "Ta Tante", "Ta Grand-Mère"]
r2_btn_1 = Radiobutton(chekout_frame, text=r2_btn_vals_table[1], indicatoron=0, variable=r2_btn_vals, value=1)
r2_btn_1.grid(column=0, row=4)
r2_btn_2 = Radiobutton(chekout_frame, text=r2_btn_vals_table[1], indicatoron=0, variable=r2_btn_vals, value=2)
r2_btn_2.grid(column=1, row=4)
r2_btn_3 = Radiobutton(chekout_frame, text=r2_btn_vals_table[1], indicatoron=0, variable=r2_btn_vals, value=3)
r2_btn_3.grid(column=2, row=4)

imgg = PhotoImage(file="src/Python.png").subsample(int(2048/128), int(2048/128))
chk_img = Label(chekout_frame, image=imgg, height=128, width=128, padx=120)
chk_img.grid(column=3, row=0, rowspan=5, padx=18, sticky="news")  # Not "news" like newsletters x) ... More like "North East West Sud" And here, it's not verry necessary.

def chk_reset():
    chk_in.delete(0, 'end')
    r1_btn_vals.set(0)
    r2_btn_vals.set(0)
    chk_label.configure(text="")

chk_reset_btn = Button(chekout_frame, width=16, height=2, text="Reset.", command=chk_reset)
chk_reset_btn.grid(column=4, row=0, rowspan=2)

def chk():
    chk_label.configure(text=f"Heyy\n{chk_in.get()} !\nU like ur\n{r1_btn_vals_table[r1_btn_vals.get()]}\nbut not ur\n{r2_btn_vals_table[r2_btn_vals.get()]}\n...")

chk_done_btn = Button(chekout_frame, width=16, height=2, text="Done !", command=chk)
chk_done_btn.grid(column=4, row=3, rowspan=5)

chk_label = Label(chekout_frame, width=12, bg="SteelBlue1", fg="magenta2")
chk_label.pack(side="right", fill="y")


###################
###################


tk.mainloop()
