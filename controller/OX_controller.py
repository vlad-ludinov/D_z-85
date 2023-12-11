from model.OX import OX

class OX_controller:

    def __init__(self, turn: bool) -> None:
        self.ox = OX()
        self.choose_ox_field = [["1", "2", "3"], 
                                ["4", "5", "6"], 
                                ["7", "8", "9"]]
        self.choose_ox = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.turn = turn
        self.x = "x"
        self.o = "o"
        self.draw = False

    def check_end(self):
        if    (self.ox.get_ox_cell(1) == self.ox.get_ox_cell(2) == self.ox.get_ox_cell(3) != " "
            or self.ox.get_ox_cell(4) == self.ox.get_ox_cell(5) == self.ox.get_ox_cell(6) != " "
            or self.ox.get_ox_cell(7) == self.ox.get_ox_cell(8) == self.ox.get_ox_cell(9) != " "
            or self.ox.get_ox_cell(1) == self.ox.get_ox_cell(4) == self.ox.get_ox_cell(7) != " "
            or self.ox.get_ox_cell(2) == self.ox.get_ox_cell(5) == self.ox.get_ox_cell(8) != " "
            or self.ox.get_ox_cell(3) == self.ox.get_ox_cell(6) == self.ox.get_ox_cell(9) != " "
            or self.ox.get_ox_cell(1) == self.ox.get_ox_cell(5) == self.ox.get_ox_cell(9) != " "
            or self.ox.get_ox_cell(3) == self.ox.get_ox_cell(5) == self.ox.get_ox_cell(7) != " "):
            return True
        elif (not self.choose_ox):
            self.draw = True
            return True
        
    def do_turn(self, number: int) -> bool:
        if (number in self.choose_ox):
            if self.turn:
                self.ox.do_turn(number, self.x)
                self.turn = False
                self.choose_ox.remove(number)
            elif not self.turn:
                self.ox.do_turn(number, self.o)
                self.turn = True
                self.choose_ox.remove(number)
            self.choose_ox_field[(number-1)//3][(number-1)%3] = "#"
            return True
        else:
            return False

    def get_ox_cell(self, number: int) -> str:
        return self.choose_ox_field[(number-1)//3][(number-1)%3]

    def get_turn(self):
        return self.turn
    
    def __str__(self) -> str:
        ox_string = f" {self.get_ox_cell(1)} | {self.get_ox_cell(2)} | {self.get_ox_cell(3)}\n"
        for i in range(2):
            ox_string += " --------- \n"
            ox_string += f" {self.get_ox_cell(i*3+4)} | {self.get_ox_cell(i*3+5)} | {self.get_ox_cell(i*3+6)}\n"
        return ox_string
    
    
