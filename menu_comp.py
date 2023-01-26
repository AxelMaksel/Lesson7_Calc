from logg import logging
import calc as cl
import excepts as ex

def menu_comp():
    logging.info('Selected complex menu')
    while True:
        print("Меню комплексных чисел.")
        num_type = input("Что будем делать\n"
                        "1 - сложение\n"
                        "2 - вычитание\n"
                        "3 - умножение\n"
                        "4 - деление\n"
                        "5 - возведение в степень '**'\n"
                        "6 - вычисление корня квадратного 'SQRT'\n"
                        "0 - выход в главное меню\n"
                        )

        match num_type:
            case "1":
                print("\n Сложение комплексных чисел")
                a, b = cl.input_complex()
                cl.print_result(f"{a} + {b} = ", cl.sum(a, b))
            case "2":
                print("\n Вычитание комплексных чисел")
                a, b = cl.input_complex()
                cl.print_result(f"{a} - {b} = ", cl.sub(a, b))
            case "3":
                print("\n Умножение комплексных чисел")
                a, b = cl.input_complex()
                cl.print_result(f"{a} * {b} = ", cl.mul(a, b))
            case "4":
                print("\n Деление комплексных чисел")
                a, b = cl.input_complex()
                cl.print_result(f"{a} / {b} = ", cl.div_1(a, b))
            case "5":
                print("\n Возведение в степень комплексных чисел")
                a = cl.input_1_complex()
                b = cl.input_1_num()
                cl.print_result(f"{a} ** {b}=", cl.pow(a,b))
            case "6":
                print("\n Вычисление квадратного корня комплексного числа")
                a = cl.input_1_complex()
                cl.print_result(f"SQRT {a}=", cl.sqrt_complex(a))
            case "0":
                break
            case _:
                print("Вы выбрали неверное значение: уточните выбор или нажмите 0 для возврата в главное меню")