class SmartDevice:
    def __init__(self, device_name, brand):
        self.device_name = device_name
        self.brand = brand
        self.status = "Off"
    def turn_on(self):
        self.status = "On"
    def turn_off(self):
        self.status = "Off"
    def display_info(self):
        print(f"Device Name: {self.device_name}")
        print(f"Brand: {self.brand}")
        print(f"Status: {self.status}")

class SmartLight(SmartDevice):  
    def __init__(self, device_name, brand, brightness):
        super().__init__(device_name, brand)
        self.brightness = brightness

    def display_info(self):  
        print(f"Smart Light: {self.device_name}")
        print(f"Brand: {self.brand}")
        print(f"Brightness: {self.brightness}%")
        print(f"Status: {self.status}")

class SmartFan(SmartDevice):  # Inheritance
    def __init__(self, device_name, brand, speed):
        super().__init__(device_name, brand)
        self.speed = speed

    def display_info(self):  # Method Overriding
        print(f"Smart Fan: {self.device_name}")
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed}")
        print(f"Status: {self.status}")


# Objects
light1 = SmartLight("Living Room Light", "Philips", 80)
fan1 = SmartFan("Bedroom Fan", "Samsung", 3)

light1.turn_on()
fan1.turn_on()

print("Light Details")
light1.display_info()
print("\nFan Details")
fan1.display_info()