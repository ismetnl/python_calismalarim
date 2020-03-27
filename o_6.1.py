from time import sleep
from threading import Thread

#Eşzamanlı fonksiyon çalıştırma (thread yardımıyla)

def arttır(ne, bekleme):
    for i in range(ne,101):
        print(i)
        dosya = open("tablo.txt", "a")
        dosya.write("{}\n".format(i))
        sleep(bekleme)

def azalt(ne,bekleme):

    for i in range (ne,0,-1):
        print("\n"*50)
        print(i)
        dosya = open("tablo.txt", "a")
        dosya.write("{}    ".format(i))
        dosya.close()
        sleep(bekleme)


if __name__ == '__main__':
    dum = Thread(target = azalt, args = (100,1))
    tis = Thread(target = arttır, args = (1,1.001))


    dosya = open("tablo.txt","w")
    dosya.write("TAB1   TAB2\n")
    dosya.close()

    dum.start()
    tis.start()

