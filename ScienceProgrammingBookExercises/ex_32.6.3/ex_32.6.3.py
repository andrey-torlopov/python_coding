# Приложение недописано, т.к. непонятна методика рассчета ESI коэффициента

filename = './data.txt'

planets = dict()
earth_params = {'radius': (1, 0.57), 'solidity': (1, 1.07), 'v_esc': (1, 0.7), 'temp': (288, 5.58)}
with open(filename, mode='rt', encoding="utf-8") as file:
    lines = file.readlines()
    names = lines[0].split()
    units = list(map(lambda x: x.replace('(','').replace(')',''), lines[1].split()))

    # print(names)
    # print(units)

    for i in range(3, len(lines)):
        line = lines[i].split()
        planets[line[0]] = line[1:]

    print(planets)