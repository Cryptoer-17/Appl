from tkinter import  *
from PIL import ImageTk, Image
import pygame
import  boolean
import operator
import  numpy as np
import sqlite3
import math
import cmath






def addition(n1_input,n2_input,testo):
    try:
        testo.delete('1.0', END)
        conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
        c = conn.cursor()
        if n1_input.get() and n2_input.get():
            testo.delete('1.0', END)
            n1 = n1_input.get()
            n2 = n2_input.get()
            if(n1 != "e" and n2!="NON QUI"):
                sum = float(n1) + float(n2)
                """operator.add(n1,n2) inserire funzioni utilizzando operator"""
                testo.insert(END,"La somma fra "+n1+" e "+n2+" è %.2f" % sum)
                c.execute("DELETE from Valori_ris where Riga==1")
                c.execute("insert into Valori_ris values (?,?)", (1,"%.2f" % sum,))
                conn.commit()
            else:testo.insert(END, "Rimuovere la lettere 'e' o 'NON QUI' dalla\n"
                                   "casella di testo, per svolgere l'operazione")
        else:testo.insert(END, "Insesrisci i due numeri per fare l'addizione")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:inserisci due numeri nelle caselle di\n"
                          "testo per svolgere l'operazione")
    finally:conn.close()

def subtraction(n1_input,n2_input,testo):
    try:
        testo.delete('1.0', END)
        conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
        c = conn.cursor()
        if n1_input.get() and n2_input.get():
            testo.delete('1.0', END)
            n1 = n1_input.get()
            n2 = n2_input.get()
            if (n1 != "e"):
             sub = float(n1) - float(n2)
             testo.insert(END,"La sottrazione fra "+n1+" e "+n2+" è %.2f" % sub)
             c.execute("DELETE from Valori_ris where Riga==1")
             c.execute("insert into Valori_ris values (?,?)", (1, "%.2f" % sub,))
             conn.commit()
            else:testo.insert(END, "Rimuovere la lettere 'e' o 'NON QUI' dalla\n"
                                   "casella di testo, per svolgere l'operazione")
        else:testo.insert(END, "Insesrisci i due numeri per fare la sottrazione")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:inserisci due numeri nelle caselle di\n"
                          "testo per svolgere l'operazione")
    finally:conn.close()

def multiplication(n1_input,n2_input,testo):
    try:
        testo.delete('1.0', END)
        conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
        c = conn.cursor()
        if n1_input.get() and n2_input.get():
            testo.delete('1.0', END)
            n1 = n1_input.get()
            n2 = n2_input.get()
            if (n1 != "e"):
                mul = float(n1) * float(n2)
                testo.insert(END,"La moltiplicazione fra "+n1+" e "+n2+" è %.2f" % mul)
                c.execute("DELETE from Valori_ris where Riga==1")
                c.execute("insert into Valori_ris values (?,?)", (1, "%.2f" % mul,))
                conn.commit()
            else:testo.insert(END, "Rimuovere la lettere 'e' o 'NON QUI' dalla\n"
                                   "casella di testo, per svolgere l'operazione")
        else:testo.insert(END, "Insesrisci i due numeri per fare la\nmoltiplicazione")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:inserisci due numeri nelle caselle di\n"
                          "testo per svolgere l'operazione")
    finally:conn.close()

def division(n1_input,n2_input,testo):
    try:
        testo.delete('1.0', END)
        conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
        c = conn.cursor()
        if n1_input.get() and n2_input.get():
            testo.delete('1.0', END)
            n1 = n1_input.get()
            n2 = n2_input.get()
            if (n1 != "e"):
                div = float(n1) / float(n2)
                testo.insert(END,"La divisione fra "+n1+" e "+n2+ " è %.2f" % div)
                c.execute("DELETE from Valori_ris where Riga==1")
                c.execute("insert into Valori_ris values (?,?)", (1, "%.2f" % div,))
                conn.commit()
            else:testo.insert(END, "Rimuovere la lettere 'e' o 'NON QUI' dalla\n"
                                   "casella di testo, per svolgere l'operazione")
        else:testo.insert(END, "Insesrisci i due numeri per fare la divisione")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:inserisci due numeri nelle caselle di\n"
                          "testo per svolgere l'operazione")
    except ZeroDivisionError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:Impossibile eseguire questa operazione")
    finally:conn.close()

def power(n1_input,n2_input,testo):

    try:
        testo.delete('1.0', END)
        conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
        c = conn.cursor()
        if n1_input.get() and n2_input.get():
            testo.delete('1.0', END)
            n1 = n1_input.get()
            n2 = n2_input.get()
            if len(n1) <5 and len(n2) <5:
                if (n1 != "e"):
                    pow = float(n1) ** float(n2)
                    testo.insert(END, "%.2f" % pow)
                    c.execute("DELETE from Valori_ris where Riga==1")
                    c.execute("insert into Valori_ris values (?,?)", (1, "%.2f" % pow,))
                    conn.commit()
                else:testo.insert(END, "Rimuovere la lettere 'e' o 'NON QUI' dalla\n"
                                       "casella di testo, per svolgere l'operazione")
            else:testo.insert(END, "Insesrisci dei numeri più picoli.")
        else:testo.insert(END, "Insesrisci il numero da elevare a sinistra,\nla sua potenza a destra")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:inserisci due numeri nelle caselle di\n"
                          "testo per svolgere l'operazione")
    except ZeroDivisionError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:Impossibile eseguire questa operazione")
    except OverflowError:
        testo.delete('1.0',END)
        testo.insert(END, "Errore:inserisci numeri più piccoli")
    finally:conn.close()

def exponential(n1_input,n2_input,testo):
    testo.delete('1.0', END)
    n1_input.delete(0,END)
    n1_input.insert(ANCHOR,"e")
    try:
        conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
        c = conn.cursor()
        if n2_input.get() :
            testo.delete('1.0', END)
            n2 = n2_input.get()
            if(n2!="NON QUI"):
             exp =2.7 ** float(n2)
             testo.insert(END, "Il risultato di e con esponente "+str(n2)+" è %.2f" % exp)
             c.execute("DELETE from Valori_ris where Riga==1")
             c.execute("insert into Valori_ris values (?,?)", (1, "%.2f" % exp,))
             conn.commit()
            else:testo.insert(END, "Rimuovere 'NON QUI' dalla prima casella di\n"
                                       "testo, per svolgere l'operazione")
        else:testo.insert(END, "Insesrisci a destra il numero da usare come\npotenza di e")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:Inserisci nella casella di destra il\n"
                          "numero da usare come potenza di e")
    except OverflowError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:inserisci un numero minore di 715")
    finally:conn.close()

def equals(n1_input,n2_input,testo):
            testo.delete('1.0', END)
            if n1_input.get() and n2_input.get():
             testo.delete('1.0', END)
             n1 = n1_input.get()
             n2 = n2_input.get()
             algebra = boolean.BooleanAlgebra()
             x, y= algebra.symbols(n1, n2)
             equals = (x == y)
             if(equals == True):
              testo.insert(END, "La stringa "+n1+" è uguale alla stringa "+n2)
             else:testo.insert(END, "La stringa "+n1+" non è uguale alla stringa "+n2)
            else: testo.insert(END, "insesrisci due stringhe per cotrollare se sono uguali")
            """ else : raise ValueError()"""


def concat(n1_input,n2_input,testo):
        testo.delete('1.0', END)
        if n1_input.get() and n2_input.get():
            testo.delete('1.0', END)
            n1 = n1_input.get()
            n2 = n2_input.get()
            concat = operator.add(n1,n2)
            testo.insert(END,"Concatenando la stringa "+n1+" e la stringa "+n2+" il risultato è "+str(concat))
        else: testo.insert(END, "Insesrisci due stringhe per poterle unire")

def lt(n1_input,n2_input,testo):
    try:
        testo.delete('1.0',END)
        if n1_input.get() and n2_input.get():
            testo.delete('1.0', END)
            if(n1_input.get()!="e"):
                n1 = float(n1_input.get())
                n2 = float(n2_input.get())
                let = operator.lt(n1,n2)
                if(let):
                 testo.insert(END,"Vero, il numero "+str(n1)+" è minore di "+str(n2))
                else: testo.insert(END,"Falso, il numero "+str(n1)+" non è minore di "+str(n2))
            else:testo.insert(END, "Rimuovere la lettere 'e' o 'NON QUI' dalla\n"
                                    "casella di testo, per svolgere l'operazione")
        else: testo.insert(END,"Insesrisci due numeri per controllare se il\nprimo è minore del secondo")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:inserisci due numeri nelle caselle di\n"
                          "testo per svolgere l'operazione")

def shift(n1_input,n2_input,testo):
    try:
        testo.delete('1.0', END)
        conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
        c = conn.cursor()
        if n1_input.get() and n2_input.get():
            testo.delete('1.0', END)
            if (n1_input.get() != "e"):
                if len(n1_input.get()) < 6 and len(n2_input.get()) < 6:
                    n1 = int(n1_input.get())
                    n2 = int(n2_input.get())
                    shift = operator.lshift(n1,n2)
                    testo.insert(END,"Il numero "+str(n1)+" shiftato di "+str(n2)+" bit è "+str(shift))
                    c.execute("DELETE from Valori_ris where Riga==1")
                    c.execute("insert into Valori_ris values (?,?)", (1, str(shift),))
                    conn.commit()
                else:testo.insert(END, "Insesrisci dei numeri più picoli.")
            else:testo.insert(END, "Rimuovere la lettere 'e' o 'NON QUI' dalla\n"
                                    "casella di testo, per svolgere l'operazione")
        else: testo.insert(END,"inserisci a sinistra il numero che vuoi\nshiftare e a destra di quanti bit")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:inserisci due numeri interi nelle\n"
                          "caselle di testo per svolgere l'operazione shift")
    finally:conn.close()

def length(n1_input,n2_input,testo):
        testo.delete('1.0', END)
        if n1_input.get() and n2_input.get():
            testo.delete('1.0', END)
            n1 = n1_input.get()
            n2 = n2_input.get()
            length_n1 = operator.length_hint(n1)
            length_n2 = operator.length_hint(n2)
            testo.insert(END,"Lunghezza stringa 1 : " + str(length_n1) + "\nLunghezza stringa 2 : "+str(length_n2))
        else: testo.insert(END,"Inserisci due stringhe per vedere la loro\nlunghezza")



def matmul(n1_input,n2_input,testo):
    try:
        testo.delete('1.0', END)
        if n1_input.get() and n2_input.get():
            testo.delete('1.0', END)
            if (n1_input.get() != "e"):
             n1 = n1_input.get()
             n2 = n2_input.get()
             A = np.matrix(n1)
             B = np.matrix(n2)
             matmul = A @ B
             testo.insert(END,"La moltiplicazione fra matrici è:\n"+str(matmul))
            else:testo.insert(END, "Rimuovere la lettere 'e' o 'NON QUI' dalla\n"
                                    "casella di testo, per svolgere l'operazione")
        else: testo.insert(END,"Inserisci le matrici in questo modo:"
                               "\nn1 n2; n3 n4")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:Il numero di colonne della prima matrice\n"
                          "deve essere almeno pari al numero di righe\n"
                          "della seconda matrice")
    except SyntaxError:
        testo.delete('1.0',END)
        testo.insert(END, "Errore:Inserisci le matrici in questo modo:"
                           "\nn1 n2; n3 n4")

def addmul(n1_input,n2_input,testo):
    try:
        testo.delete('1.0', END)
        if n1_input.get() and n2_input.get():
            testo.delete('1.0', END)
            if (n1_input.get() != "e"):
             n1 = n1_input.get()
             n2 = n2_input.get()
             A = np.matrix(n1)
             B = np.matrix(n2)
             addmul = np.add(A,B)
             testo.insert(END,"L'addizione fra matrici è:\n"+str(addmul))
            else:testo.insert(END, "Rimuovere la lettere 'e' o 'NON QUI' dalla\n"
                                    "casella di testo, per svolgere l'operazione")
        else: testo.insert(END,"Inserisci le matrici in questo modo:"
                               "\nn1 n2; n3 n4")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:le matrici devono essere di euguali\n"
                          "dimensioni")
    except SyntaxError:
        testo.delete('1.0',END)
        testo.insert(END, "Errore:Inserisci le matrici in questo modo:"
                           "\nn1 n2; n3 n4")

def submul(n1_input,n2_input,testo):

    try:

        testo.delete('1.0', END)
        if n1_input.get() and n2_input.get():
            testo.delete('1.0', END)
            if(n1_input.get() != "e"):
             n1 = n1_input.get()
             n2 = n2_input.get()
             A = np.matrix(n1)
             B = np.matrix(n2)
             submul = np.subtract(A,B)
             testo.insert(END,"La sottrazione fra matrici è:\n"+str(submul))
            else:testo.insert(END, "Rimuovere la lettere 'e' o 'NON QUI' dalla\n"
                                    "casella di testo, per svolgere l'operazione")
        else: testo.insert(END,"Inserisci le matrici in questo modo:"
                               "\nn1 n2; n3 n4")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:le matrici devono essere di euguali\n"
                          "dimensioni")
    except SyntaxError:
        testo.delete('1.0',END)
        testo.insert(END, "Errore:Inserisci le matrici in questo modo:"
                           "\nn1 n2; n3 n4")

def sommatoria(n1_input,n2_input,testo):
    testo.delete('1.0', END)
    n2_input.delete(0,END)
    n2_input.insert(ANCHOR,"NON QUI")
    try:
        conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
        c = conn.cursor()
        if n1_input.get() :
            testo.delete('1.0', END)
            if (n1_input.get() != "e"):
             n1 = int(n1_input.get())
             if(n1 >=0):
              if (n1<100000):
               somma = sommmatoria(n1)
               testo.insert(END,"La sommatoria di "+ str(n1) + " è "+str(somma))
               c.execute("DELETE from Valori_ris where Riga==1")
               c.execute("insert into Valori_ris values (?,?)", (1, str(somma),))
               conn.commit()
              else:testo.insert(END, "Insesrisci un numero più picolo.")
             else:testo.insert(END, "Insesrisci un numero maggiore o uguale a 0 su\n"
                                    "cui svolgere l'operazione.")
            else:testo.insert(END, "Rimuovere la lettere 'e' dalla prima casella\n"
                                    "di testo, per svolgere l'operazione")
        else:testo.insert(END, "Insesrisci solo a sinistra, il numero intero su\ncui svolgere la sommatoria")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:inserisci un numero intero, per eseguire\n"
                          "l'operazione")
    finally:conn.close()

def squareroot(n1_input,n2_input,testo):
    testo.delete('1.0', END)
    n2_input.delete(0,END)
    n2_input.insert(ANCHOR,"NON QUI")
    try:
        conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
        c = conn.cursor()
        if n1_input.get() :
            testo.delete('1.0', END)
            if (n1_input.get() != "e"):
             n1 = float(n1_input.get())
             if(len(str(n1))<16):
              sqrt = math.sqrt(n1)
              testo.insert(END,"La radice quadrata di "+ str(n1) + " è "+str(sqrt))
              c.execute("DELETE from Valori_ris where Riga==1")
              c.execute("insert into Valori_ris values (?,?)", (1, str(sqrt),))
              conn.commit()
             else:testo.insert(END, "Insesrisci un numero più picolo.")
            else:testo.insert(END, "Rimuovere la lettera 'e' nella prima casella\n"
                                   "di testo, per svolgere l'operazione")
        else:testo.insert(END, "Insesrisci solo a sinistra, il numero su cui\n"
                               "svolgere l'operazione.")
    except ValueError:
        testo.delete('1.0', END)
        testo.insert(END, "Errore:inserisci un numero maggiore o uguale a\n"
                          "0, per svolgere questa operazione.")
    finally:conn.close()


def ans(n1_input,n2_input,testo):
    try:
        testo.delete('1.0', END)
        conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
        c = conn.cursor()
        c.execute("select Valore from Valori_ris")
        risultato = c.fetchall()
        ris = str(risultato[0])
        ris = ris[2:-3]
        if (n1_input.get()!=ris):
         n1_input.delete(0,END)
         n1_input.insert(END,str(ris))
        else:
         n2_input.delete(0, END)
         n2_input.insert(END,str(ris))
    except IndexError:
        testo.delete('1.0', END)
        testo.insert(END, "Nessun valore memorizzato da utilizzare nelle\n"
                          "operazioni")
    finally:conn.close()
def exit():
    conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
    c = conn.cursor()
    c.execute("DELETE from Valori_ris where Riga==1")
    conn.commit()
    conn.close()
    sys.exit()



def music():
    pygame.init()
    pygame.mixer.music.load(r"C:\Users\39347\Desktop\Appl\venv\Foto_database\Welcome.wav")
    pygame.mixer.music.play(0,0.0)

def sommmatoria(n1):
        somma = 0
        for numero in range(1, n1 + 1):
            somma += numero
        return somma