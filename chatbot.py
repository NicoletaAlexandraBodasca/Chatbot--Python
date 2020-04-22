class Entitate:
    def __init__(self,intrebare,raspuns):
        self.__intrebare=intrebare
        self.__raspuns=raspuns

    def getIntrebare(self):
        return self.__intrebare

    def getRaspuns(self):
        return self.__raspuns

    def setIntrebare(self,i):
        self.__intrebare=i
    def setRaspuns(self,r):
        self.__raspuns=r

    def __eq__(self,other):
        return self.__raspuns==other
    def __ne__(self, other):
        return not self.__eq__(other)
    def __gt__(self, other):
        return self.__raspuns>other
    def __lt__(self, other):
        return self.__raspuns<other
