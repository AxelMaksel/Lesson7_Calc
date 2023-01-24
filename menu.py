import menu_comp as mc
import menu_rac as rc

def menu():
    while True:
        num_typ=input("С какими числами работаем?\n"
                      "1 - Комплексные\n"
                      "2 - Рациональные\n"
                      "3 - выход\n")

        match num_typ:
            case "1":
                mc.menu_comp()
            case "2":
                rc.menu_rac()
            case "3":
                break
            case _:
                print("Erro!!")

menu ()