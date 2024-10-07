import csv
import numpy as np
import matplotlib.pyplot as plt

data = list(csv.reader(open('PytongTrainee/files/basket_players.csv', 'r'), delimiter=';'))

def print_data_raw_data(data):
    for i, row in enumerate(data):
        print("fila número", i,row)

def transform_data(data):
    data_transformed = []
    for i, row in enumerate(data[1:], start=1): 
        row_dict = {i: row}
        data_transformed.append(row_dict)
    
    return np.array(data_transformed)



def translate_data(transformed_data):
    INCH_TO_CM = 2.54
    POUND_TO_KG = 0.4
    translated_data = transformed_data.copy()  
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
            weight = float(value[4])  
            height = float(value[3])  

            if weight > max_weight:
                max_weight = weight
                player_max_weight = value[0]  

            if height < min_height:
                min_height = height
                player_min_height = value[0]  

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


def plot_avg_weight_height_per_team(translated_data):
    team_data = {}
    for player in translated_data:
        for key, value in player.items():
            team = value[1]
            height = float(value[3])
            weight = float(value[4])
            if team not in team_data:
                team_data[team] = {'height': [], 'weight': []}
            team_data[team]['height'].append(height)
            team_data[team]['weight'].append(weight)
    
    teams = list(team_data.keys())
    avg_heights = [np.mean(team_data[team]['height']) for team in teams]
    avg_weights = [np.mean(team_data[team]['weight']) for team in teams]

    x = np.arange(len(teams))
    width = 0.35

    fig, ax1 = plt.subplots(figsize=(12, 8))

    ax1.bar(x - width/2, avg_heights, width, label='Alçada Promig (cm)', color='blue')
    ax1.set_xlabel('Equips')
    ax1.set_ylabel('Alçada Promig (cm)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_xticks(x)
    ax1.set_xticklabels(teams, rotation=45, ha='right')

    ax2 = ax1.twinx()
    ax2.bar(x + width/2, avg_weights, width, label='Pes Promig (kg)', color='red')
    ax2.set_ylabel('Pes Promig (kg)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    fig.tight_layout()
    plt.title('Alçada y Pes Promig per Equip')
    plt.show()

def plot_position_distribution(translated_data):
    position_counts = {'Base': 0, 'Escolta': 0, 'Alero': 0, 'Ala-pivot': 0, 'Pivot': 0}
    for player in translated_data:
        for key, value in player.items():
            position = value[2]
            position_counts[position] += 1

    labels = list(position_counts.keys())
    sizes = list(position_counts.values())
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen']

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Jugadores por Posición')
    plt.axis('equal')
    plt.show()

def plot_age_distribution(translated_data):
    ages = [int(player[list(player.keys())[0]][5]) for player in translated_data]
    plt.figure(figsize=(10, 6))
    plt.hist(ages, bins=range(min(ages), max(ages) + 1), color='purple', edgecolor='black')
    plt.title('Distribució d Edats dels Jugadors')
    plt.xlabel('Edat')
    plt.ylabel('Número de Jugadors')
    plt.show()
transformed_data = transform_data(data)
translated_data = translate_data(transformed_data)
print_data_raw_data(data)
print("//////////////////////")
print(translated_data)
print("//////////////////////")
export_data(translated_data, 'PytongTrainee/files/jugadors_basket.csv')
max_weight_and_min_height(translated_data)
print("//////////////////////")
plot_height_distribution(translated_data)
plot_avg_weight_height_per_team(translated_data)
plot_position_distribution(translated_data)
plot_age_distribution(translated_data)
