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
                        "8 - вычисление корня квадратного 'SQRT'\n"
                        "0 - выход в главное меню\n"
                        )

        match num_typ:
            case "1":
                a, b = cl.input_2_num()
                cl.print_result(f"{a} + {b} = ", cl.sum(a, b))
            case "2":
                a, b = cl.input_2_num()
                cl.print_result(f"{a} - {b} = ", cl.sub(a, b))
            case "3":
                a, b = cl.input_2_num()
                cl.print_result(f"{a} * {b} = ", cl.mul(a, b))
            case "4":
                a, b = cl.input_2_num()
                cl.print_result(f"{a} / {b} = ", cl.div_1(a, b))
            case "5":
                a, b = cl.input_2_num()
                cl.print_result(f"{a} // {b} = ", cl.div_2(a, b))
            case "6":
                a, b = cl.input_2_num()
                cl.print_result(f"{a} % {b} = ", cl.div_3(a, b))
            case "7":
                a, b = cl.input_2_num()
                cl.print_result(f"{a} ** {b} = ", cl.pow(a, b))
            case "8":
                a = cl.input_1_num()
                cl.print_result(f"SQRT {a} = ", cl.sqrt(a))
            case "0":
                break
            case _:
                print("Erro!!")
