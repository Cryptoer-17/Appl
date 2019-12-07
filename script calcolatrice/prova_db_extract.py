
import sqlite3
import io



conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
c = conn.cursor()



def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)




c.execute("select immagini from File_inseriti")
res = c.fetchall()
write_file(res[0][0],r"C:\Users\39347\Desktop\Persone\Andrea\Foto,video e audio\foto personali\DSC_1985.jpg")
conn.commit()
conn.close()
