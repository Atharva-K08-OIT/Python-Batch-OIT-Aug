class Earphones:
    def __init__(self, Company, Price, Color, BL):
        self.company = Company
        self.price = Price
        self.color = Color
        self.battery_life = BL
        self.__a = 5

    def PrintInvoice(self):
        print("Company :", self.company)
        print("Colour :", self.color)
        print("Battery Life :", self.battery_life)
        print("Price :", self.price)

    def PairDevice(self, name):
        print("Pairing device...")
        print("Device paired successfully with", name)

    @property
    def getA(self):
        return self.__a
    

    @getA.setter
    def setA(self,new_value):
        self.__a = new_value


ap1 = Earphones("Apple", 25000, "White", 3)
ap1.PrintInvoice()
ap1.PairDevice("Oppa F21 sPro")
ap2 = Earphones("Boat", 15000, "Black", 4)
ap1.PrintInvoice()
ap3 = Earphones("Boat", 15000, "Black", 4)
ap1.PrintInvoice()
ap4 = Earphones("Boat", 15000, "Black", 4)
ap1.PrintInvoice()


# print("Company :", ap2.company)
# print("Price :", ap2.price)
# print("Colour :", ap2.color)
# print("Battery Life :", ap2.battery_life)

# print("Company :", ap3.company)
# print("Price :", ap3.price)
# print("Colour :", ap3.color)
# print("Battery Life :", ap3.battery_life)

# print("Company :", ap4.company)
# print("Price :", ap4.price)
# print("Colour :", ap4.color)
# print("Battery Life :", ap4.battery_life)
