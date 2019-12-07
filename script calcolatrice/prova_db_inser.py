
import sqlite3



conn = sqlite3.connect('C:/Users/39347/Desktop/Appl/data/Dati_calcolatrice.db')
c = conn.cursor()


def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

empPicture = convertToBinaryData(r"C:\Users\39347\Desktop\Appl\venv\Foto_database\Welcome.wav")
c.execute("insert into File_inseriti values (?,?)", (5, sqlite3.Binary(empPicture)))
conn.commit()
conn.close()
