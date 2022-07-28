def extract_string(line):
    '''
    Esctract string beween '' in line of a file

    :param line:              line of the file
    :return: string <string>: string to extract
    '''
    line.strip('\n')
    count = 0
    index = []
    string = ''
    for i in range(len(line)):
        if line[i] == "'":
            index.append(i)
    for i in range(index[0], index[1] + 1):
        string += line[i]
    return string.strip("'")


def fill(liste, out):
    for i in range(1, len(liste)):
        if "###" not in liste[i] or liste[i] != "\n":
            out[liste[i].split(' ')[0]] = out.split[' '][1]
    return out


def get_key(value, dict):
    '''
    Get the key of a dictionary

    :param      value:  value of the dictionary
    :param      dict:   dictionary
    :return:    key:    key of the corresponding value
    '''
    for key in dict:
        if dict[key] == value:
            return key


def construct_menus():
    '''
    Construct the menus from the file Setup/menus.txt

    :raturn:    dic <list>:   list of dictinaries of the menus
                links <list>: list of the link between the menus
    '''
    f = open('Setup/menus.txt', 'r')
    # Extract informations on the menus parameters
    dir = []
    tags = []
    lineIndex = []
    c = 0
    l = 0
    for line in f:
        if '###' in line:
            dir.append({})
            tags.append(line.split('###')[1].strip(' ').strip("'"))
            c += 1
            lineIndex.append(l)
        l += 1
    f.close()

    # Fill the list of dictionaries
    f = open('Setup/menus.txt', 'r')
    lines = list(f.readlines())
    dicto = {}
    n = 0
    for j in lineIndex:
        for i in range(len(lines)):
            lines[i].strip("\n")
            if lines[i] != "\n" and '###' not in lines[i]:
                key = int(lines[i].split(' ')[0])
                dicto[key] = extract_string(lines[i])
            if i == j and i != 0 or i == len(lines) - 1:
                dir[n] = dicto
                if i != len(lines) - 1:
                    n += 1
                dicto = {}
    f.close()

    # Create the links between the menus
    links = []
    for menu in dir:
        liste = list(menu.values())
        for item in liste:
            if any(item == tag for tag in tags):
                links.append((item, get_key(item, menu)))

    return (dir, links)
