def menu_comp():
    while True:
        num_typ=input("С какими числами работаем?\n"
                      "1 - Комплексные\n"
                      "2 - Рациональные\n"
                      "3 - выход\n")

        match num_typ:
            case "1":
                pass
            case "2":
                print()
            case "3":
                break
            case _:
                print("Erro!!")

