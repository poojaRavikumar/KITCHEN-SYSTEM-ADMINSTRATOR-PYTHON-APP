
#Student Name 2024-2026: Pooja Ravikumar
#Asu ID :1234370880
# Date : 11/03/2024

class SystemArchitecture:
    def __init__(self):
        self.cpu = "CPU"
        self.memory = ["Memory Slot 1", "Memory Slot 2"]
        self.io_devices = ["Keyboard", "Display", "Disk Storage"]
    
    def show_layout(self):
        print("System Architecture (Kitchen Layout):")
        print(f"CPU: {self.cpu}")
        print(f"Memory: {self.memory}")
        print(f"I/O Devices: {self.io_devices}")

# Create a system architecture instance
system = SystemArchitecture()
system.show_layout()
