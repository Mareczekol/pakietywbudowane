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
        values = change.split(',')
        # jezeli poda wartosc jest inna niz 3 informuje o tym uzytkownika
        if len(values) != 3:
            print(f"Nieprawidłowa zmiana: {change}. Oczekiwane 3 wartości "
                  f"oddzielone przecinkami.")
            continue
        x, y, value = values
        # sprawdzam czy x i y to liczby. jesli nie informuje uzytkownika
        if not x.isdigit():
            print(f"Nieprawidłowa zmiana {change}. Pierwszy argument musi być "
                  f"liczbą.")
            continue
        x = int(x)
        if not y.isdigit():
            print(f"Nieprawidłowa zmiana {change}. Drugi argument musi byc "
                  f"liczbą.")
            continue
        y = int(y)

        # jesli podamy x,y spoza zakresu doda go w to miejsce
        if y >= len(data) or x >= len(data[y]):
            # print(f"Nieprawidłowa zmiana: {change}. Zbyt wiele argumentów.")
            while y >= len(data):
                data.append([])
            while x >= len(data[y]):
                data[y].append('')
            data[y][x] = value
        else:
            data[y][x] = value

    for value in new_values:
        if len(value) < 3:
            continue
        x, y, value = value[0], value[1], value[2]
        if not x.isdigit():
            # print(f"Nieprawidłowa zmiana {change}. Pierwszy argument musi
            # być liczbą.")
            continue
        x = int(x)
        if not y.isdigit():
            # print(f"Nieprawidłowa zmiana {change}. Drugi argument musi być"
            # liczbą.")
            continue
        y = int(y)
        if y >= len(data):
            while y >= len(data):
                data.append([])
        if x >= len(data[y]):
            while x >= len(data[y]):
                data[y].append('')
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


# tworzenie pliku in.csv jezeli go nie ma-domyslnie są wartosci podane w
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
