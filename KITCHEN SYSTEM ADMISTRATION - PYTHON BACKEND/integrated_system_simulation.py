#Student Name 2024-2026: Pooja Ravikumar
#Asu ID :1234370880
# Date : 11/03/2024
# Define the SystemArchitecture class
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

# Define the Bus class
class Bus:
    def __init__(self, name):
        self.name = name

    def transfer_data(self, source, destination, data):
        print(f"Transferring '{data}' from {source} to {destination} via {self.name}")

# Define the ChannelSubsystem class
class ChannelSubsystem:
    def __init__(self, name):
        self.name = name

    def handle_io(self, source, destination, data):
        print(f"{self.name} handling I/O from {source} to {destination}: {data}")

# Define the IntegratedSystem class
class IntegratedSystem:
    def __init__(self):
        self.system = SystemArchitecture()
        self.cpu_bus = Bus("CPU Bus")
        self.memory_bus = Bus("Memory Bus")
        self.channel = ChannelSubsystem("Channel 1")

    def simulate_operations(self):
        self.system.show_layout()
        self.cpu_bus.transfer_data("CPU", "Memory Slot 1", "Instruction 2")
        self.memory_bus.transfer_data("Memory Slot 1", "Display", "Output Data")
        self.channel.handle_io("Disk Storage", "Memory Slot 2", "Program Data")

# Run the integrated system simulation
integrated_system = IntegratedSystem()
integrated_system.simulate_operations()
