# inheritance:
#   - a class can inherit properties and methods from another class


class Computer:
    def __init__(self, ip, pro, op, price ,os):
        self.iuput_devices = ip
        self.processor = pro
        self.output_device = op
        self.price = price
        self.operating_system = os

    def display_details(self):
        print("Input Devices Connected:", " & ".join(self.iuput_devices))
        print("Processor:", self.processor)
        print("Output Devices Connected:", " & ".join(self.output_device))
        print("Price of Computer:", self.price)
        print("Operating System:", self.operating_system)

    


class Mobile(Computer):
    def __init__(self, ip, pro, op, price, os = None, ch_type = "U-type", mgpx ="50", networkIs5g = "No"):
        super().__init__(ip, pro, op, price, os)
        self.charging_type = ch_type
        self.camera_mgpx = mgpx
        self.network_5G = networkIs5g

    def show_details(self):
        self.display_details()
        print("Charging Type:", self.charging_type)
        print("Camera Megapixels:", self.camera_mgpx)
        print("Network 5G:", self.network_5G,"\n")


m1 = Mobile(["v-Keyboard", "touch-pad"], "Sanpdragon-680",
            ["Display", "Speakers"], 35000, "Android 14", "C type", 64, "Yes")

m1.show_details()


m2 = Mobile(["v-Keyboard", "touch-pad"], "Sanpdragon-680",
            ["Display", "Speakers"], 35000, "Android 14", "C type", 64)

m2.show_details()

m3 = Mobile(ip="M",op="Sp",ch_type="c-type",networkIs5g="yes",price=34567,pro="MediaTech",mgpx=50)

m3.show_details()



class Object:
    def __init__():
        pass