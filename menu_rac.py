from logg import logging
import calc as cl
import excepts as ex

def menu_rac():
    logging.info('Selected racional menu')
    while True:
        print("Меню рациональных чисел.")
        num_type = input("Что будем делать\n"
                        "1 - сложение\n"
                        "2 - вычитание\n"
                        "3 - умножение\n"
                        "4 - деление с остатком '/'\n"
                        "5 - деление без остатка '//'\n"
                        "6 - остаток от деления '%'\n"
                        "7 - возведение в степень '^'\n"
                        "8 - вычисление корня квадратного 'SQRT'\n"
                        "0 - выход в главное меню\n"
                        )

        match num_type:
            case "1":
                print("\nВыполняется сложение")
                a, b = cl.input_2_num()
                cl.print_result(f"{a} + {b} = ", cl.sum(a, b))
            case "2":
                print("\nВыполняется вычитание")
                a, b = cl.input_2_num()
                cl.print_result(f"{a} - {b} = ", cl.sub(a, b))
            case "3":
                print("\nВыполняется умножение")
                a, b = cl.input_2_num()
                cl.print_result(f"{a} * {b} = ", round(cl.mul(a, b),5))
            case "4":
                print("\nВыполняется деление")
                a, b = cl.input_2_num()
                while not ex.check_zero(a,b):
                    print ("На ноль делить нельзя!")
                    a, b = cl.input_2_num()
                cl.print_result(f"{a} / {b} = ", round(cl.div_1(a, b),5))
            case "5":
                print("\nВыполняется деление без остатка")
                a, b = cl.input_2_num()
                while not ex.check_zero(a,b):
                    print ("На ноль делить нельзя!")
                    a, b = cl.input_2_num()
                cl.print_result(f"{a} // {b} = ", cl.div_2(a, b))
            case "6":
                print("\nВычисляется остаток от деления")
                a, b = cl.input_2_num()
                while not ex.check_zero(a,b):
                    print ("На ноль делить нельзя!")
                    a, b = cl.input_2_num()
                cl.print_result(f"{a} % {b} = ", cl.div_3(a, b))
            case "7":
                print("\nВычисляется возведение в степень")
                a, b = cl.input_2_num()
                cl.print_result(f"{a} ^ {b} = ", round(cl.pow(a, b),5))
            case "8":
                print("\nВычисляется извлечение квадратного корня")
                a = cl.input_1_num()
                while not ex.check_posit(a):
                    print ("Из отрицательного числа квадратный корень не извлекается!")
                    a = cl.input_1_num()
                cl.print_result(f"SQRT {a} = ", round(cl.sqrt(a),5))
            case "0":
                break
            case _:
                print("Вы выбрали неверное значение: уточните выбор или нажмите 0 для возврата в главное меню")