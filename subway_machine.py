TICKET_DICTIONARY = {"Sencillo": 2.40, "Casual": 11.35, "Usual": 40.00, "Familiar": 10.00, "Jóven": 80.00}
TICKET_SELECTION_LIST = ["Sencillo", "Casual", "Usual", "Familiar", "Jóven"]
ZONE = ["1 zona", "2 zonas", "3 zonas", "4 zonas", "5 zonas", "6 zonas"]

def secret_code(input_value):
    if input_value == "4321":
        print("Código secreto activado. La máquina se detendrá.")
        exit()

def ticket_selection():
    print("¿Qué billete desea adquirir?"
          "\n1. Billete sencillo"
          "\n2. Billete Casual"
          "\n3. Billete Usual"
          "\n4. Billete Familiar"
          "\n5. Billete Jóven")
    valid_ticket = False
    while not valid_ticket:
        try:
            ticket_value = input("Introduce el número de la opción deseada: ")
            secret_code(ticket_value)
            ticket_value = int(ticket_value)
            if ticket_value in range(1, 6):
                valid_ticket = True
            else:
                print("Error: Por favor, introduce una opción válida.")
        except ValueError:
            print("Error: Por favor, introduce una opción válida.")
    return ticket_value

def zone_selection():
    valid_zone = False
    print("¿Cúantas zonas desea?"
          "\n1. 1 zona"
          "\n2. 2 zonas"
          "\n3. 3 zonas"
          "\n4. 4 zonas"
          "\n5. 5 zonas"
          "\n6. 6 zonas")
    while not valid_zone:
        try:
            zone_value = input("Introduce la zona deseada: ")
            secret_code(zone_value)
            zone_value = int(zone_value)
            if zone_value in range(1, 7):
                valid_zone = True
            else:
                print("Error: Por favor, introduce una opción válida.")
        except ValueError:
            print("Error: Por favor, introduce una opción válida.")
    return zone_value

def ticket_completion(ticket_value, zone_value):
    zone_increment = 1.25
    base_price = TICKET_DICTIONARY[TICKET_SELECTION_LIST[ticket_value-1]]
    final_price = base_price
    for i in range(1, zone_value):
        final_price *= zone_increment
    print(f"El precio de su billete {TICKET_SELECTION_LIST[ticket_value-1]} con {ZONE[zone_value-1]} es de {final_price:.2f}€.")
    return final_price

def payment(price_to_pay):
    valid_coins = [0.05, 0.10, 0.20, 0.50, 1, 2]
    valid_bills = [5, 10, 20, 50]
    try:
        while price_to_pay > 0:
            amount = input("Introduce una moneda/billete: ")
            secret_code(amount)
            amount = float(amount)
            if amount in valid_coins or amount in valid_bills:
                price_to_pay -= amount
                price_to_pay = round(price_to_pay, 2)
                print("Importe restante: ", price_to_pay)
            else:
                print("Error: Por favor, introduzca una moneda/billete real.")
    except ValueError:
        print("Error: Por favor, introduzca una moneda/billete real.")

def print_ticket_list(ticket_list):
    print("//////////////////////////////////////////"
          "\nLista de billetes adquiridos:"
          "\n//////////////////////////////////////////")
    for ticket in ticket_list:
        print(f"Billete: {ticket[0]} | Zona: {ticket[1]} | Precio: {ticket[2]:.2f}€")
    print("Gracias por su compra.")

def subway_machine():
    MAX_TICKETS = 3
    tickets = 0
    more_tickets = True
    total_price = 0.0
    ticket_list = []
    while more_tickets:
        ticket_value = ticket_selection()
        zone_value = zone_selection()
        price_to_pay = ticket_completion(ticket_value, zone_value)
        total_price += price_to_pay
        ticket_list.append((TICKET_SELECTION_LIST[ticket_value-1], ZONE[zone_value-1], price_to_pay))
        tickets += 1
        if tickets >= MAX_TICKETS:
            print("Ha alcanzado el número máximo de billetes.")
            more_tickets = False
        else:
            valid_input = False
            while not valid_input:
                more_tickets_input = input("¿Desea adquirir más billetes? (s/n): ").lower()
                secret_code(more_tickets_input)
                if more_tickets_input == "s":
                    valid_input = True
                elif more_tickets_input == "n":
                    more_tickets = False
                    valid_input = True
                else:
                    print("Error: Por favor, introduce una opción válida.")
    print(f"El precio total de los billetes adquiridos es de {total_price:.2f}€.")
    payment(total_price)
    print_ticket_list(ticket_list)

subway_machine()