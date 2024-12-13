#Student Name 2024-2026: Pooja Ravikumar
#Asu ID :1234370880
# Date : 11/03/2024
class ChannelSubsystem:
    def __init__(self, name):
        self.name = name

    def handle_io(self, source, destination, data):
        print(f"{self.name} handling I/O from {source} to {destination}: {data}")

# Simulate channel subsystem operations
channel = ChannelSubsystem("Channel 1")
channel.handle_io("Disk Storage", "Memory Slot 2", "File Data")
