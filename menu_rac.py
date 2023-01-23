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
                a, b = cl.input_2_num()
                print(f"\n{a}+{b}={cl.sum(a,b)}\n")
            case "2":
                a, b = cl.input_2_num()
                print(f"\n{a}-{b}={cl.sub(a,b)}\n")
            case "3":
                a, b = cl.input_2_num()
                print(f"\n{a}*{b}={cl.mul(a,b)}\n")
            case "4":
                a, b = cl.input_2_num()
                print(f"\n{a}/{b}={cl.div01(a,b)}\n")
            case "5":
                menu_rac()
            case "6":
                break
            case "7":
                pass
            case _:
                print("Erro!!")
