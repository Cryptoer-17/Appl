from tkinter import  *
from PIL import ImageTk, Image
from gif import ImageLabel
import metodi_calc
import tkinter as tk
from tkinter import font
from itertools import count, cycle
import pygame
import sqlite3
import io
import  binascii
class Application(Frame):
    """ A GUI application with three buttons. """


    def __init__ (self,master):
        """ Initialized the frame"""
        Frame.__init__(self,master,borderwidth=5)
        self.grid()
        self.create_widgets()
        self.IsPaused = False
        self.IsEmpty = True
        self.mainloop()



    def create_widgets(self):

        """Create 3 buttons that to do nothing"""
        # create first label
        self.conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
        self.c = self.conn.cursor()
        self.c.execute("select immagini from File_inseriti")
        self.res = self.c.fetchall()
        self.conn.commit()
        self.write_file(self.res[0][0],r"C:\Users\39347\Desktop\Appl\venv\Foto_database\universo.jpg")
        self.write_file(self.res[1][0], r"C:\Users\39347\Desktop\Appl\venv\Foto_database\Nature_gif.gif")
        self.write_file(self.res[3][0], r"C:\Users\39347\Desktop\Appl\venv\Foto_database\Stai Zitto INSTRUMENTAL (Reprod. by GR8).wav")
        self.write_file(self.res[2][0], r"C:\Users\39347\Desktop\Appl\venv\Foto_database\Welcome.wav")
        self.Label_1 = Label(self,text="Benvenuta! Inserisci prima i due numeri, "
                              "succesivamente scegli l'operazione desiderata",
                         font=("Arial Black",15))
        self.Label_1.grid(row=0, column=0, sticky="W",padx=150,pady=10)

        self.lbltxt_2 = Label(self, text="Primo carattere:",font=("Caladea", 11),bg="red",relief=RAISED)
        self.lbltxt_2.place(x = 175,y = 40)

        self.lbltxt_2 = Label(self, text="Secondo carattere:", font=("Caladea", 11),bg="red",relief=RAISED)
        self.lbltxt_2.place(x=290, y=40)
        #create first button add
        self.Button_1 = Button(self,text= "addition", command=lambda : metodi_calc.addition(self.n1_input,self.n2_input,self.testo))
        self.Button_1.grid(row = 2, column = 0,sticky = "W")
        self.Button_1.config(height=2, width=10)
        # create second button sub
        self.Button_2 = Button(self, text="substation", font=("Caladea",10), command=lambda : metodi_calc.subtraction(self.n1_input,self.n2_input,self.testo))
        self.Button_2.grid(row = 2, column = 0,sticky = "W",padx=90)
        self.Button_2.config(height=2, width=10)
        # create fird button mul
        self.Button_3 = Button(self, text="multiplication",font=("Caladea",10), command=lambda : metodi_calc.multiplication(self.n1_input,self.n2_input,self.testo))
        self.Button_3.grid(row = 3, column = 0,sticky = "W",pady=5)
        self.Button_3.config(height=2, width=10)
        # create fourth button div
        self.Button_4 = Button(self, text="division", font=("Caladea",10),command=lambda : metodi_calc.division(self.n1_input,self.n2_input,self.testo))
        self.Button_4.grid(row = 3, column = 0,sticky = "W",padx=90)
        self.Button_4.config(height=2, width=10)

        self.Button_5 = Button(self, text="potenza",font=("Caladea",10),command=lambda: metodi_calc.power(self.n1_input, self.n2_input, self.testo))
        self.Button_5.grid(row=4, column=0, sticky="W",pady=5)
        self.Button_5.config(height=2, width=10)


        self.Button_6 = Button(self, text="exponential",font=("Caladea",10),command=lambda : metodi_calc.exponential(self.n1_input,self.n2_input,self.testo))
        self.Button_6.grid(row=4, column=0, sticky="W", padx=90)
        self.Button_6.config(height=2, width=10)

        self.Button_7 = Button(self, text="equals string", font=("Caladea", 10),command=lambda: metodi_calc.equals(self.n1_input,self.n2_input, self.testo))
        self.Button_7.grid(row=5, column=0, sticky="W", pady=5)
        self.Button_7.config(height=2, width=10)

        self.Button_8 = Button(self, text="concatena", font=("Caladea", 10),command=lambda: metodi_calc.concat(self.n1_input, self.n2_input, self.testo))
        self.Button_8.grid(row=5, column=0, sticky="W", padx=90)
        self.Button_8.config(height=2, width=10)

        self.Button_9 = Button(self, text="Minore di", font=("Caladea", 10),command=lambda: metodi_calc.lt(self.n1_input, self.n2_input, self.testo))
        self.Button_9.grid(row=6, column=0, sticky="W", pady=5)
        self.Button_9.config(height=2, width=10)

        self.Button_10 = Button(self, text="n1 << n2bit", font=("Caladea", 10),command=lambda: metodi_calc.shift(self.n1_input, self.n2_input, self.testo))
        self.Button_10.grid(row=6, column=0, sticky="W", padx=90)
        self.Button_10.config(height=2, width=10)

        self.Button_11 = Button(self, text="lunghezza", font=("Caladea", 10),command=lambda: metodi_calc.length(self.n1_input, self.n2_input, self.testo))
        self.Button_11.grid(row=7, column=0, sticky="W", pady=5)
        self.Button_11.config(height=2, width=10)

        self.Button_12 = Button(self, text="matr moltip", font=("Caladea", 10),command=lambda: metodi_calc.matmul(self.n1_input, self.n2_input, self.testo))
        self.Button_12.grid(row=7, column=0, sticky="W", padx=90)
        self.Button_12.config(height=2, width=10)

        self.Button_13 = Button(self, text="matr add", font=("Caladea", 10),
                                command=lambda: metodi_calc.addmul(self.n1_input, self.n2_input, self.testo))
        self.Button_13.grid(row=8, column=0, sticky="W", pady=5)
        self.Button_13.config(height=2, width=10)

        self.Button_14 = Button(self, text="matr sub", font=("Caladea", 10),
                                command=lambda: metodi_calc.submul(self.n1_input, self.n2_input, self.testo))
        self.Button_14.grid(row=8, column=0, sticky="W", padx=90)
        self.Button_14.config(height=2, width=10)

        self.Button_15 = Button(self, text="sommatoria", font=("Caladea", 10),
                                command=lambda: metodi_calc.sommatoria(self.n1_input, self.n2_input, self.testo))
        self.Button_15.grid(row=9, column=0, sticky="W", pady=5)
        self.Button_15.config(height=2, width=10)
        self.Button_15.place( y = 449)

        self.Button_15 = Button(self, text="radic quadr", font=("Caladea", 10),
                                command=lambda: metodi_calc.squareroot(self.n1_input, self.n2_input, self.testo))
        self.Button_15.grid(row=9, column=0, sticky="W")
        self.Button_15.config(height=2, width=10)
        self.Button_15.place(y=449,x=90)


        self.Button_ans = Button(self, text="ans", font=("Arial Black", 8),command=lambda: metodi_calc.ans(self.n1_input, self.n2_input, self.testo))
        self.Button_ans.grid(row=9, column=0, sticky="W")
        self.Button_ans.config(height=2, width=10)
        self.Button_ans.place(y=449,x=180)

        self.Button_exit = Button(self, text="Quit",font=("Arial Black",9), command=lambda: metodi_calc.exit(),bg="red")
        self.Button_exit.grid(row=1, column=0, sticky="N")
        self.Button_exit.place(x=940,y = 48)
        self.Button_exit.config(height=3, width=10)

        # create first Entry
        self.n1_input = Entry(self,width=10)
        self.n1_input.grid(row=1,column=0, sticky="W", padx=210,pady=12)
        # create second Entry
        self.n2_input = Entry(self, width=10)
        self.n2_input.grid(row=1,column=0, sticky="W", padx=340)
        # create first Text
        self.testo = Text(self)
        self.testo.place(x = 430,y = 50,width=385, height=63)

        self.musica = Button(self, text="Prima di cominciare clicca su questo bottone!",font=("Arial Black",10), command=lambda: metodi_calc.music())
        self.musica.grid(row=3, column=0, sticky="W", padx=428)
        self.musica.config(height=2, width=42)

        self.musica2 = Button(self, text="Blocca audio o\nInstrumental Salmo", font=("Arial Black", 10),command=lambda : self.music3())
        self.musica2.grid(row=7, column=0, sticky="W", padx=822)
        self.musica2.config(height=2, width=21)

        self.c = Canvas(self, height=160, width=200,bg="#239B56")
        self.stick = self.c.create_line(10,29,184,125 , width=10,fill="blue")
        self.tip_1 = self.c.create_line(44, 100, 12,29, width=10,fill="blue")
        self.tip_2 = self.c.create_line(90, 30, 9, 31, width=10,fill="blue")
        self.c.place(x = 820, y =135)


        self.ima = Label(self, image=self.immagine())
        self.ima.grid(row=9, column=0, sticky="W", padx=387)

        #self.ima2 = Label(self, image=self.immagine2())
        #self.ima2.grid(row=4, column=0, sticky="W", padx=500, pady=225)

        self.lbl = ImageLabel(self)
        self.lbl.grid(row=9,column=0,sticky="W",padx=740)
        self.path3 = r"C:\Users\39347\Desktop\Appl\venv\Foto_database\Nature_gif.gif"
        self.lbl.load(self.path3)

        self.Button_donate = Button(self, text="Donation", font=("Comic Sans MS",10), command=lambda: self.donate(), bg="#239B56")
        self.Button_donate .grid(row=2, column=0, sticky="N")
        self.Button_donate .place(x=1025,y=342)
        self.Button_donate .config(height=2, width=15)

        self.conn.close()





    def write_file(self,data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)

    def immagine(self):
        self.path = io.BytesIO(self.res[0][0])
        self.img = (Image.open(self.path))
        self.img = self.img.resize((300, 300), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        return self.img


    def music3(self):
        pygame.init()
        if (pygame.mixer.music.get_busy()) == False:
            pygame.mixer.music.load(io.BytesIO(self.res[3][0]))
            pygame.mixer.music.play(0, 0.0)
        else:
            self.toggleMusic()

    def toggleMusic(self):
        if self.IsPaused:
            pygame.mixer.music.unpause()
            self.IsPaused = False
        else:
            pygame.mixer.music.pause()
            self.IsPaused = True

    def donate(self):
        if self.IsEmpty:
            lbltxt_4 = Text(self,relief=SUNKEN,font=("Caladea",11,'underline'),bg="#F4D03F")
            lbltxt_4.insert(END,"Bitcoin address:\n3KnZ8SV2QvGvKJERdwxUwyTpUKt3GZXzFm")
            lbltxt_4.place(x=865, y=400,width=290,height=40)
            lbltxt_4.config(state=DISABLED)
            self.IsEmpty = False
        else:
            self.a = Canvas(self, height=37, width=287)
            self.a.place(x=865,y=400)
            self.IsEmpty = True


