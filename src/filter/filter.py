
def filter_by_int(data, field, min, max):
    pass

def filter_by_bool(data, field, value):
    pass

def filter_by_str(data, field, equal, contain):
    pass

def filter_by_list(data, field, len_equal, contain):
    pass

def equals (data, format, field, *value):
    if format == "csv":
        try:
            index = list(data[0]).index(field)
            data=[d for d in data if str(d[index]) in value or d[index] == field]
            return data
        except ValueError:
            print(f"Field {field} not found")
            return data
    if format == 'json':
        if field in data[0].keys():
            if isinstance(data[0][field], list):
                data = [d for d in data if len(d[field]) in value]
            else:
                data = [d for d in data if d[field] in value]
            return data
        else:
            print(f"Field {field} not found")
            return data

def contains (data, format, field, *value):
    try:
        data = [d for d in data if any([v == datalist for v in value for datalist in d[field]])]
        return data
    except TypeError:
        print(f"Field {field} is not a string or iterable") 
        return data
    except KeyError:
        print(f"Field {field} not found")
        return data