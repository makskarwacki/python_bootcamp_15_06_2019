def columns(file, headers=[], missing=None):
    result = dict()
    value = []
    if not headers:
        first_line = file.readline()
        first_line = first_line.strip()
        keys = first_line.split(",")
    else:
        keys = headers
    for key in keys:
        value.append([])
    for line in file:
        line = line.strip()
        elements = line.split(",")
        while len(elements) < len(keys):
            elements.append(missing)
        for n in elements:
            index = elements.index(n)
            value[index].append(n)
    for key in keys:
        result[key] = value[keys.index(key)]

    return result


print(columns(open("p.txt")))
print(columns(open("p.txt"), headers=["header1", "header2"]))
print()
print(columns(open("p_missing.txt"), missing="0"))
print(columns(open("p_missing.txt")))
