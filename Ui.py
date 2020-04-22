# from chatbot import Entitate
# def adaugare(x,y):
#     file=open("q&a","a")
#     file.write(x+str(y))
#     file.write("\n")
#     file.close()
# adaugare("Cate mere are Ana?",10)

#Descr:citeste o intrebare
#I:-
#O:intrebarea
def readData():
    q=input("Intrebarea este:")
    return q

#Descr:adauga in fisier intrebarea cu raspunsul corect
#I:intrebarea si raspunsul
#:O-

def adaugare(q,a):
    print("Raspunsul e corect")
    file=open("raspunsuri","a")
    file.write(q+" "+str(a))
    file.write("\n")
    file.close()
#Descr:cauta raspunsul corect intre limita inferioara si limita superioara
#I:limitele sirului unde trebuie cautat raspunsul
#O:raspunsul corect(x)
def CautareBinara(linf, lsup):
    if linf<=lsup:
        x=(linf+lsup)//2
        print(x)
        print("Daca raspunsul corect este x apasati 1")
        print("Daca raspunsul este mai mare apasati 2")
        print("Daca raspunsul este mai mic apasati 3")
        r=int(input("r="))
        if(r==1):
            return x
        else:
            if(r==2):
                return CautareBinara(x+1,lsup)
            elif (r==3):
                return CautareBinara(linf,x-1)

def main():
    x=readData()
    y=50
    print(y)
    print("Daca raspunsul este corect apasati tasta 1")
    print("Daca raspunsul este mai mare apasati tasta 2")
    print("Daca raspunsul este mai mic apasati tasta 3")
    r=int(input("r="))
    if(r==2):
        while(r==2):
            p=y
            y=y+50
            print(y)
            print("Daca raspunsul este corect apasati tasta 1")
            print("Daca raspunsul este mai mare apasati tasta 2")
            print("Daca raspunsul este mai mic apasati tasta 3")
            r=int(input("r="))
        raspuns=CautareBinara(p,y)
    elif (r==1):
        raspuns=y
    elif (r==3):
        raspuns=CautareBinara(0,y)
    adaugare(x,raspuns)

main()







