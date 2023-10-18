

def szamlalos_ciklus():
    i:int = 1
    while (i<=10):
        print(i,"Többet nem kések mert le maradok fontos infokrol")

        i+=1
def eloltesztelos_ciklus():
    szam: int = int(input("adjon meg egy szamot ami nagyobb 10nel"))
    while szam < 10:
        print("10nel nagyobb szamot!")
        szam: int = int(input("adjon meg egy szamot ami nagyobb 10nel"))

def feladatok():
    i: int = 1
    while (i <= 10):
        print(i,end=",")

        i += 1
def feladatok2():
    i: int = 20
    while (i <= 30):
        print(i)
        i += 1
def feladatok3():
    i: int = 15
    while (i <= 25):
        if i % 2 ==0:
            print(i)

        i += 1

def feladatok4():
    i:int =1
    while i <= 10:
        print("********")
        i+=1

def feladat5():
    i: int = 1
    while i <= 100:
        print(i)
        i += 1