from controller.OX_controller import OX_controller

class OX_view:


    def __init__(self, ) -> None:
        print("Выберите кто будет ходить первым (x = 1, o = 2)")
        flag = True
        while flag:
            temp = input("Введите число: ")
            if (str(temp).isdigit()):
                if (int(temp)==1):
                    turn = True
                    flag = False
                elif (int(temp)==2):
                    turn = False
                    flag = False
                else:
                    print("Введено неверное число")
            else:
                print("Введено не число")
        self.ox_controller = OX_controller(turn)

    def start(self):
        while(not self.ox_controller.check_end()):
            print("Вот все доступные ходы:")
            print()
            print(self.ox_controller)
            if (self.ox_controller.get_turn()):
                temp = str(input("Игрок X сделайте ход (введите число): "))
            else:
                temp = str(input("Игрок O сделайте ход (введите число): "))
            if (temp.isdigit()):
                if (self.ox_controller.do_turn(int(temp))):
                    print("Ход сделан")
                else:
                    print("Введите число из доступных ходов")
            else:
                print("Введите ЧИСЛО из доступных ходов")
            print("Вот игровое поле:")
            print()
            print(self.ox_controller.ox)
        if (self.ox_controller.draw):
            print("Ничья! Победила дружба")
        elif (self.ox_controller.get_turn()):
            print("Игрок O победил!")
        else:
            print("Игрок X победил!")