from abc import ABC, abstractmethod
class Computer:
    def __init__(self):
        self.processor = None
        self.memory = None
        self.hard_drive = None
        self.operating_system = None

    def __str__(self):
        return f"Computer with {self.processor}, {self.memory}, {self.hard_drive}, {self.operating_system}"

class ComputerBuilder(ABC):
    @abstractmethod
    def build_processor(self):
        pass

    @abstractmethod
    def build_memory(self):
        pass

    @abstractmethod
    def build_hard_drive(self):
        pass

    @abstractmethod
    def build_operating_system(self):
        pass

    @abstractmethod
    def get_computer(self):
        pass

class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_processor(self):
        self.computer.processor = "High-end gaming processor"

    def build_memory(self):
        self.computer.memory = "32GB RAM"

    def build_hard_drive(self):
        self.computer.hard_drive = "1TB SSD"

    def build_operating_system(self):
        self.computer.operating_system = "Windows 10"

    def get_computer(self):
        return self.computer

class OfficeComputerBuilder(ComputerBuilder):
    
    def __init__(self):
        self.computer = Computer()

    def build_processor(self):
        self.computer.processor = "Mid level low power consumption processor"

    def build_memory(self):
        self.computer.memory = "8GB RAM"

    def build_hard_drive(self):
        self.computer.hard_drive = "256GB SSD"

    def build_operating_system(self):
        self.computer.operating_system = "Windows XP"

    def get_computer(self):
        return self.computer
     
class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_computer(self):
        self.builder.build_processor()
        self.builder.build_memory()
        self.builder.build_hard_drive()
        self.builder.build_operating_system()

    def get_computer(self):
        return self.builder.get_computer()
    
def choice_computer(builder):
    validate_result = False
    try:
        result = input("Input the type of computer you would like to build: [g] for gaming computer, [o] for office computer: ")
        computer_builder = builder[result]()
        validate_result = True
    except KeyError:
        print("Only gaming computer and office computer are available")
        validate_result = False
        return (validate_result,None)
    return (validate_result,computer_builder)


def main():
    computer_dict = dict(g = GamingComputerBuilder, o = OfficeComputerBuilder)
    computer_type = False
    while not computer_type:
        computer_type, builder = choice_computer(computer_dict)
        
    computer_builder = builder
    director = ComputerDirector(computer_builder)
    director.build_computer()
    computer = director.get_computer()
    print(computer)   
    
if __name__ == "__main__":
    main()