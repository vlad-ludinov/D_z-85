class OX:

    def __init__(self) -> None:
        self.ox_field = [[" ", " ", " "], 
                         [" ", " ", " "], 
                         [" ", " ", " "]]
    
    def do_turn(self, number: int, symbol: str):
        self.ox_field[(number-1)//3][(number-1)%3] = symbol

    def get_ox_cell(self, number: int) -> str:
        return self.ox_field[(number-1)//3][(number-1)%3]

    def __str__(self) -> str:
        ox_string = f" {self.get_ox_cell(1)} | {self.get_ox_cell(2)} | {self.get_ox_cell(3)}\n"
        for i in range(2):
            ox_string += " --------- \n"
            ox_string += f" {self.get_ox_cell(i*3+4)} | {self.get_ox_cell(i*3+5)} | {self.get_ox_cell(i*3+6)}\n"
        return ox_string