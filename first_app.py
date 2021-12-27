from tkinter import *
from random import randint

class FirstApp(Tk):
    def __init__(self):
        super().__init__()

        ###################
        ###################

        self.title("Mon Application Tkinter")
        self.geometry("720x480")
        self.iconbitmap("src/icon.ico")
        self.configure(background="gray", highlightthickness=16)


        ###################
        ###################


        self.card_frame = Frame(self, height=240, width=240, highlightthickness=1, highlightbackground="black")
        self.card_frame.pack(side="top", anchor="w", padx=8, pady=8)
        self.card_frame.pack_propagate(0)

        self.card_l2 = Label(self.card_frame, text=" -  -  - ", width=8, bg="green", fg="lime")
        self.card_l2.place(relx=0.5, rely=0.55, anchor=CENTER)

        # Cardinal Button Configuration
        self.bconf = {"width": 7, "height": 1, "anchor": CENTER}

        self.card_n = Button(self.card_frame, text="Nord", **self.bconf, command=lambda: self.card_handler("Nord", "blue", "deep sky blue"))
        self.card_n.pack(side='top')

        self.card_w = Button(self.card_frame, text="Ouest", **self.bconf, command=lambda: self.card_handler("Ouest", "dark orange", "yellow"))
        self.card_w.pack(side='left')

        self.card_e = Button(self.card_frame, text="Est", **self.bconf, command=lambda: self.card_handler("Est", "firebrick1", "red4"))
        self.card_e.pack(side='right')

        self.card_s = Button(self.card_frame, text="Sud", **self.bconf, command=lambda: self.card_handler("Sud", "green3", "lawn green"))
        self.card_s.pack(side='bottom')

        self.card_r = Button(self.card_frame, text="Reset", **self.bconf, command=lambda: self.card_handler())
        self.card_r.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.card_l1 = Label(self.card_frame, text="Points Cardinaux", width=12, bg="green", fg="lime")
        self.card_l1.place(relx=0.5, rely=0.45, anchor=CENTER)


        ###################
        ###################


        self.cookie_count = 0

        self.cookie_label = Label(self, width=30)
        self.cookie_label.place(relx=0.55, rely=0.2)

        self.cookie_btn = Button(self, width=30, text="Click", command=self.update_cookie_btn)
        self.cookie_btn.place(relx=0.55, rely=0.3)

        self.update_cookie_btn()


        ###################
        ###################


        chekout_frame = Frame(self, padx=20, pady=20, height=200)
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

        chk_reset_btn = Button(chekout_frame, width=16, height=2, text="Reset.", command=self.chk_reset)
        chk_reset_btn.grid(column=4, row=0, rowspan=2)

        chk_done_btn = Button(chekout_frame, width=16, height=2, text="Done !", command=self.chk)
        chk_done_btn.grid(column=4, row=3, rowspan=5)

        chk_label = Label(chekout_frame, width=12, bg="SteelBlue1", fg="magenta2")
        chk_label.pack(side="right", fill="y")
    
    def start(self):
        self.mainloop()
        return self
    
    def end(self):
        self.quit()
        return self
    
    def start_an_other(self):
        return FirstApp().start()

    def card_handler(self, text: str = None, bg=None, fg=None):
            if text: self.card_l2.configure(text=text)
            else: self.card_l2.configure(text=" -  -  - ", bg="green", fg="lime")
            if fg: self.card_l2.configure(fg=fg)
            if bg: self.card_l2.configure(bg=bg)

    def update_cookie_btn(self):
            global cookie_count
            self.cookie_btn.configure(bg="#{:0>2}".format(str(hex(randint(0, 255)))[2:]) + "{:0>2}".format(str(hex(randint(0, 255)))[2:]) + "{:0>2}".format(str(hex(randint(0, 255)))[2:]))
            self.cookie_label.configure(text=f"{self.cookie_count} cookies",
                                        bg="#{:0>2}".format(str(hex(randint(0, 255)))[2:]) + "{:0>2}".format(str(hex(randint(0, 255)))[2:]) + "{:0>2}".format(str(hex(randint(0, 255)))[2:]))
            self.cookie_count += 1

    def chk_reset(self):
            self.chk_in.delete(0, 'end')
            self.r1_btn_vals.set(0)
            self.r2_btn_vals.set(0)
            self.chk_label.configure(text="")
    
    def chk(self):
            self.chk_label.configure(text=f"Heyy\n{self.chk_in.get()} !\nU like ur\n{self.r1_btn_vals_table[self.r1_btn_vals.get()]}\nbut not ur\n{self.r2_btn_vals_table[self.r2_btn_vals.get()]}\n...")
