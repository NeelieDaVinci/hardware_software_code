def menu_display():
    menu_dict = {
        '1': 'decimal_to_binary',
        '2': 'binary_to_decimal',
        'X': 'exit_program'
    }
    return menu_dict

def execute_display(menu_dict):
    print("Menu:")
    for key, value in menu_dict.items():
        print(f"{key}: {value}")

    selection = input("Enter your choice: ")
    return selection, menu_dict.get(selection)

def main():
    sel, sel_choice = execute_display(menu_display())
    print(f"You selected {sel} and wanted to convert {sel_choice}")

if __name__ == "__main__":
    main()
