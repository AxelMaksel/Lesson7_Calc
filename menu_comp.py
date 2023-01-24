from logg import logging
import calc as cl


def menu_comp():
    logging.info('Selected complex menu')
    while True:
        print("Меню комплексных чисел.")
        num_typ = input("Что будем делать\n"
                        "1 - сложение\n"
                        "2 - вычитание\n"
                        "3 - умножение\n"
                        "4 - деление\n"
                        "5 - возведение в степень '**'\n"
                        "6 - вычисление корня квадратного 'SQRT'\n"
                        "0 - выход в главное меню\n"
                        )

        match num_typ:
            case "1":
                a, b = cl.input_2_complex()
                cl.print_result(f"{a} + {b} = ", cl.sum_compl(a, b))
            case "2":
                a, b = cl.input_2_complex()
                cl.print_result(f"{a} - {b} = ", cl.sub_compl(a, b))
            case "3":
                a, b = cl.input_2_complex()
                cl.print_result(f"{a} * {b} = ", cl.mul_compl(a, b))
            case "4":
                a, b = cl.input_2_complex()
                cl.print_result(f"{a} / {b} = ", cl.div_compl(a, b))
            case "5":
                a = cl.input_1_complex()
                b = cl.input_1_num()
                cl.print_result(f"{a} ** {b}=", cl.pow_compl(a,b))
            case "6":
                a = cl.input_1_complex()
                cl.print_result(f"SQRT {a}=", cl.sqrt_compl(a))
            case "0":
                break
            case _:
                print("Erro!!")
