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
                print(ticket_value)
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
                print(zone_value)
            else:
                print("Error: Por favor, introduce una opción válida.")
        except ValueError:
            print("Error: Por favor, introduce una opción válida.")
    return zone_value

ticket_value = ticket_selection()
zone_value = zone_selection()

def ticket_completion(ticket_value, zone_value):
    ticket_dictionary = {"Sencillo": 2.40, "Casual": 11.35, "Usual": 40.00, "Familiar": 10.00, "Jóven": 80.00}
    ticket_selection_list = ["Sencillo", "Casual", "Usual", "Familiar", "Jóven"]
    zona = ["1 zona", "2 zonas", "3 zonas", "4 zonas", "5 zonas", "6 zonas"]
    zone_increment = (1.25)
    print (ticket_dictionary[ticket_selection_list[ticket_value-1]])
    if zone_value == 1:
        print(f"El precio de su billete {ticket_selection_list[ticket_value-1]} con {zona[zone_value-1]} es de {ticket_dictionary[ticket_selection_list[ticket_value-1]]}€.")
    elif zone_value > 1:
        print(f"El precio de su billete {ticket_selection_list[ticket_value-1]} con {zona[zone_value-1]} es de {ticket_dictionary[ticket_selection_list[ticket_value-1]]*(zone_increment * zone_value)}€.")
ticket_completion(ticket_value, zone_value)

