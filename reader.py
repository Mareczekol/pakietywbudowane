import csv
import sys
import os


# odczytywanie isniejącego pliku in.csv
def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data


# modyfikacja pliku in.csv
def modify_csv_file(data, changes, new_values):
    for change in changes:
        x, y, value = change.split(',')
        x = int(x)
        y = int(y)
        if y >= len(data) or x >= len(data[y]):
            print(f"Invalid change: {change}") # cos spoza zakresu - np.
            # kolumna, której nie ma
            continue
        data[y][x] = value
# dodawanie wartosci spoza zakresu w odpowiednie miejsce
    for value in new_values:
        if len(value) < 3:
            print(f"Invalid value: {value}")
            continue
        x, y, value = value[0], value[1], value[2]
        x = int(x)
        y = int(y)
        if y >= len(data):
            data.extend([[] for _ in range(y - len(data) + 1)])
        if x >= len(data[y]):
            data[y].extend([''] * (x - len(data[y]) + 1))
        data[y][x] = value


# wyswietlanie pliku csv
def display_csv_file(data):
    for row in data:
        print(','.join(row))


# zapisywanie do pliku out.csv
def write_csv_file(data, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


# tworzenie pliku in.csv jezeli go nie ma - domyslnie są wartosci podane w
# terminalu
def create_input_file(input_file_path, values):
    if not os.path.exists(input_file_path):
        with open(input_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(values)
    else:
        print(f"Plik in.csv '{input_file_path}' isnieje. Nie tworzę nowego.")


if __name__ == '__main__':
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    changes = sys.argv[3:]

    new_values = [value.split(',') for value in sys.argv[4:]]

    create_input_file(input_file_path, new_values)

    data = read_csv_file(input_file_path)
    modify_csv_file(data, changes, new_values)
    display_csv_file(data)
    write_csv_file(data, output_file_path)
