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
        
    

