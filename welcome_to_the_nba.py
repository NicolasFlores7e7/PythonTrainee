import csv
data = csv.reader(open('/home/nicolas.flores.7e7/Escriptori/DADES/dades/dades/Nico/Python/Ejercicios basicos/PytongTrainee/files/basket_players.csv', 'r'))

def print_data(data):
    for i, row in enumerate(data):
        print(row, "fila número", i)

def transform(data):
    data_transformed = []
    
    for row in data[1:]: 
        row_dict = dict(zip( row))
        data_transformed.append(row_dict)
    
    return data_transformed


transformed_data = transform(data)
print(transformed_data)
