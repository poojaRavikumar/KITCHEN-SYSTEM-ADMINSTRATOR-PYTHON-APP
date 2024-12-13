
#Student Name 2024-2026: Pooja Ravikumar
#Asu ID :1234370880
# Date : 11/03/2024
class Bus:
    def __init__(self, name):
        self.name = name

    def transfer_data(self, source, destination, data):
        print(f"Transferring {data} from {source} to {destination} via {self.name}")

# Create bus instances
cpu_bus = Bus("CPU Bus")
memory_bus = Bus("Memory Bus")

# Simulate data transfers
cpu_bus.transfer_data("CPU", "Memory Slot 1", "Instruction 1")
memory_bus.transfer_data("Memory Slot 1", "Display", "Data 1")
