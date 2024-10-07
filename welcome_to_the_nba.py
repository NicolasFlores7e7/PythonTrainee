import csv
import numpy as np
import matplotlib.pyplot as plt

data = csv.reader(open('/home/nicolas.flores.7e7/Escriptori/DADES/dades/dades/Nico/Python/Ejercicios basicos/PytongTrainee/files/basket_players.csv', 'r'), delimiter=';')

def print_data_raw_data(data):
    for i, row in enumerate(data):
        print("fila número", i,row)

def transform_data(data):
    data = list(data)  # Convertir el objeto reader a una lista
    data_transformed = []
    
    for i, row in enumerate(data[1:], start=1): 
        row_dict = {i: row}
        data_transformed.append(row_dict)
    
    return np.array(data_transformed)



def translate_data(transformed_data):
    INCH_TO_CM = 2.54
    POUND_TO_KG = 0.4
    translated_data = transformed_data.copy()  # Crear una copia de los datos transformados
    for player in translated_data:
        for key, value in player.items():
            if value[2] == "Point Guard":
                value[2] = "Base"
            elif value[2] == "Shooting Guard":
                value[2] = "Escolta"
            elif value[2] == "Small Forward":
                value[2] = "Alero"
            elif value[2] == "Power Forward":
                value[2] = "Ala-pivot"
            elif value[2] == "Center":
                value[2] = "Pivot"
            value[3] = round(float(value[3])* INCH_TO_CM, 2)
            value[4] = round(float(value[4])* POUND_TO_KG,2)
            value[5] = int(round(float(value[5]),0))
            
    return translated_data

def export_data(translated_data, output_file):
    file = open(output_file, 'w')
    writer = csv.writer(file, delimiter='^')

    headers = ["Nom", "Equip", "Posició", "Alçada", "Pes", "Edat"]
    writer.writerow(headers)

    for player in translated_data:
        for key, value in player.items():
            writer.writerow(value)
    file.close()

def max_weight_and_min_height(translated_data):
    max_weight = -1
    min_height = float('inf')
    player_max_weight = None
    player_min_height = None

    for player in translated_data:
        for key, value in player.items():
            weight = float(value[4])  # Peso en kg
            height = float(value[3])  # Altura en cm

            if weight > max_weight:
                max_weight = weight
                player_max_weight = value[0]  # Nombre del jugador

            if height < min_height:
                min_height = height
                player_min_height = value[0]  # Nombre del jugador

    print("El jugador más pesado es", player_max_weight, "con", max_weight, "kgs")
    print("El jugador más bajo es", player_min_height, "con", min_height, "cms")


def plot_height_distribution(translated_data):
    heights = [float(player[list(player.keys())[0]][3]) for player in translated_data]
    plt.figure(figsize=(10, 6))
    plt.hist(heights, bins=15, color='blue', edgecolor='black')
    plt.title('Distribució d Alçades dels Jugadors')
    plt.xlabel('Alçada (cm)')
    plt.ylabel('Número de Jugadors')
    plt.show()


transformed_data = transform_data(data)
translated_data = translate_data(transformed_data)
"""export_data(translated_data, '/home/nicolas.flores.7e7/Escriptori/DADES/dades/dades/Nico/Python/Ejercicios basicos/PytongTrainee/files/jugadors_basket.csv')
"""

max_weight_and_min_height(translated_data)
plot_height_distribution(translated_data)