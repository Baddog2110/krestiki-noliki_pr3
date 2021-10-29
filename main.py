from Class1 import base
board = list(range(1, 10))
def main(board):
    obj = base(board)
    counter = 0
    win = False
    while not win:
        obj.draw_board()
        if counter % 2 == 0:
            obj.take_input("X")
        else:
            obj.take_input("O")
        counter += 1
        if counter > 4:
            tmp = obj.check_win()
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    obj.draw_board()

main(board)