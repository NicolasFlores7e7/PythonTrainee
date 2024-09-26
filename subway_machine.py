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
            ticket_value = int(input("Introduce el número de la opción deseada: "))
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
            zone_value = int(input("Introduce la zona deseada: "))
            if zone_value in range(1, 7):
                valid_zone = True
            else:
                print("Error: Por favor, introduce una opción válida.")
        except ValueError:
            print("Error: Por favor, introduce una opción válida.")
    return zone_value


def ticket_completion(ticket_value, zone_value):
    ticket_dictionary = {"Sencillo": 2.40, "Casual": 11.35, "Usual": 40.00, "Familiar": 10.00, "Jóven": 80.00}
    ticket_selection_list = ["Sencillo", "Casual", "Usual", "Familiar", "Jóven"]
    zone = ["1 zona", "2 zonas", "3 zonas", "4 zonas", "5 zonas", "6 zonas"]
    zone_increment = 1.25
    base_price = ticket_dictionary[ticket_selection_list[ticket_value-1]]
    if zone_value == 1:
        final_price = base_price
    elif zone_value > 1:
        final_price = base_price
        for i in range(1, zone_value):
            final_price *= zone_increment
        final_price = round(final_price, 2)
    print(f"El precio de su billete {ticket_selection_list[ticket_value-1]} con {zone[zone_value-1]} es de {final_price}€.")
    return final_price

def payment(price_to_pay):
    valid_coins = [0.05, 0.10, 0.20, 0.50, 1, 2]
    valid_bills = [5, 10, 20, 50]
    try:
        while price_to_pay > 0:
            amount = float(input("Introduce una moneda/billete: "))
            if amount in valid_coins:
                price_to_pay -= amount
                amount = round(amount, 2)
                print("Importe restante: ", price_to_pay)
            elif amount in valid_bills:
                price_to_pay -= amount
                amount = round(amount, 2)
                print("Importe restante: ", price_to_pay)
            else:
                print("Error: Por favor, introduzca una moneda/billete real.")
    except ValueError:
        print("Error: Por favor, introduzca una moneda/billete real.")

while True:
    MAX_TICKETS = 3
    tickets = 0
    more_tickets = True
    total_price = 0.0
    while more_tickets and tickets < MAX_TICKETS:
        ticket_value = ticket_selection()
        zone_value = zone_selection()
        price_to_pay = ticket_completion(ticket_value, zone_value)
        total_price += price_to_pay
        valid_input = False
        while not valid_input:
            try:
                more_tickets_input = input("¿Desea adquirir más billetes? (s/n): ")
                if more_tickets_input == "s":
                    tickets += 1
                    valid_input = True
                elif more_tickets_input == "n":
                    more_tickets = False
                    valid_input = True
                else:
                    print("Error: Por favor, introduce una opción válida.")
            except ValueError:
                print("Error: Por favor, introduzca una opción válida.")
    if not more_tickets or tickets == MAX_TICKETS:
        print(f"El precio total de los billetes adquiridos es de {total_price}€.")
        payment(total_price)