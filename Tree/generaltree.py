class Gtree:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children

    def __str__(self,level=0):
        ret=" "* level + str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret

    def addchildren(self,child):
        self.children.append(child)
        return


Drink=Gtree("Drink",[])
Hot=Gtree("Hot",[])
Tea=Gtree("Tea",[])
MasalaTea=Gtree("Masala_Tea",[])
Cold=Gtree("Cold",[])
cola=Gtree("cola",[])
fanta=Gtree("fanta",[])
Drink.addchildren(Hot)
Hot.addchildren(Tea)
Tea.addchildren(MasalaTea)
Drink.addchildren(Cold)
Cold.addchildren(cola)
cola.addchildren(fanta)
print(Drink)


        
    



