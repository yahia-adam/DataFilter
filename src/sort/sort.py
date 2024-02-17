def convert(value):
    if isinstance(value, str):
        types = [int, float, str]
        for t in types:
            try:
                return t(value)
            except:
                pass
    else:
        return value

def clean(data):
    for i in range(len(data)):
        if isinstance(data[i], (str, float, str)):
            data[i]=convert(data[i])
        elif isinstance(data, list):
            map(clean, data[i])
    return data

#TO DO : check with itemgetter() for sort on multiple keys
def unique_sort(data,  data_type, field, reversed = False, ):
    if data_type == "csv":
        try:
            index = list(data[0]).index(field)
            #data = list(map(clean, data))
            result =  sorted(data[1:], key = lambda x: x[index], reverse=reversed)
            result.insert(0,data[0])
            return result
        except ValueError:
            print(f"Field {field} not found")
            return data
    elif data_type == "json":
        if field in data[0].keys():
            return sorted(data, key = lambda x : x.get(field), reverse=reversed)
        else:
            print(f"Field {field} not found")
            return data
    elif data_type == "yaml":
        key = list(data.items())[0][0]
        if field in data[key][0].keys():
            data[key] = sorted(data[key], key = lambda x : x.get(field), reverse=reversed)
            return data
        else:
            print(f"Field {field} not found")
            return data


def sort(data, data_type, reversed = False, *fields):
    for f in fields[::-1]:
        print(f)
        data = unique_sort(data, data_type, f, reversed=reversed)
        print(data)
    return data