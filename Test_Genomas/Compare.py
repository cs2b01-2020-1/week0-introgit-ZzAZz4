from os import walk


def files_in_dir(parent_path: str):
    paths = []
    for (_, _, filenames) in walk(parent_path):
        paths.extend(filenames)
        break
    return [parent_path + '\\' + path for path in paths]


def get_info(path: str):
    with open(path) as fp:
        lines = fp.readlines()
        name = lines[0][1:11]
        genome = [item[0:-1] for item in lines[1:]]
        genome = "".join(genome)
    return name, genome


def get_virus_data(file_paths: list):
    names, genomes = [get_info(path)[0] for path in file_paths], [get_info(path)[1] for path in file_paths]
    return names, genomes


def string_match(str1: str, str2: str):
    min_len = min(len(str1), len(str2))
    return round(100 / len(str1) * sum([str1[i] == str2[i] and str1[i] != ' ' for i in range(min_len)]), 2)


def print_table(table, names):
    table, names = [names] + table, ['g. 1 \ g.2'] + names
    table = [[names[i]] + table[i] for i in range(len(names))]

    for row in table:
        for item in row:
            item = str(item)
            print(item + ' ' * (10 - len(item)), end=' | ')
        print('\n' + '-' * (6 * 13 - 1))


def entry():
    my_path = "genomas"
    names, genomes = get_virus_data(files_in_dir(my_path))

    table = [[string_match(f_gen, s_gen) for s_gen in genomes] for f_gen in genomes]
    print_table(table, names)


if __name__ == '__main__':
    entry()
