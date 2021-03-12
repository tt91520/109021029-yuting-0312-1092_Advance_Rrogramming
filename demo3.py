class ArmyChess:
    
    def __init__(self,color,name,mobile,coordinate,order):
        self.ArmyChessColor=color
        self.ArmyChessName=name
        self.ArmyChessMobile=mobile
        self.ArmyChessCoordinate=coordinate
        self.ArmyChessOrder=order

    def showInfo(self):
        print(self.ArmyChessColor,"\t",self.ArmyChessName,"\t",self.ArmyChessMobile,"\t",self.ArmyChessCoordinate,"\t",self.ArmyChessOrder)


a=ArmyChess("將","黑","1","五","後")
b=ArmyChess("帥","紅","1","五","先")
c=ArmyChess("士","黑","1","六","先")
a.showInfo()
b.showInfo()
c.showInfo()