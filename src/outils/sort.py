def convert(value):
    types = [int, float, str]
    for t in types:
        try:
            return t(value)
        except:
            pass

def clean(data):
    for i in range(len(data)):
        if isinstance(data[i], str):
            data[i]=convert(data[i])
        else:
            map(clean, data[i])
    return data


def sort(data, field, data_type, reversed = False):
    if data_type == "csv":
        try:
            index = list(data[0]).index(field)
            data = list(map(clean, data))
            return sorted(data[1:], key = lambda x: x[index], reverse=reversed)
        except ValueError:
            print(f"Field {field} not found")
