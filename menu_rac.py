from logg import logging
import calc as cl


def menu_rac():
    logging.info('Selected racional menu')
    while True:
        print("Меню рациональных чисел.")
        num_typ = input("Что будем делать\n"
                        "1 - сложение\n"
                        "2 - вычитание\n"
                        "3 - умножение\n"
                        "4 - деление с остатком '/'\n"
                        "5 - деление без остатка '//'\n"
                        "6 - остаток от деления '%'\n"
                        "7 - возведение в степень '**'\n"
                        )

        match num_typ:
            case "1":
                pass
            case "2":
                menu_rac()
            case "3":
                break
            case "4":
                a, b = cl.input_2_num()
                print(f"{a}/{b}={cl.div01(a,b)}")
            case "5":
                menu_rac()
            case "6":
                break
            case "7":
                pass
            case _:
                print("Erro!!")
