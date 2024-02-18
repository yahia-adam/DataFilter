def calculate_int_stats(data):
    return {
        "min": min(data),
        "max": max(data),
        "avg": sum(data) / len(data) if data else None
    }

def calculate_str_stats(data):
    lengths = [len(item) for item in data]
    return {
        "len-min": min(lengths),
        "len-max": max(lengths),
        "total-len": sum(lengths)
    }

def calculate_list_stats(data):
    return {
        "mean": sum(len(item) for item in data) / len(data) if data else None,
        "min": min(len(item) for item in data) if data else None,
        "max": max(len(item) for item in data) if data else None
    }

def calculate_bool_stats(data):
    true_count = sum(1 for item in data if item)
    false_count = sum(1 for item in data if not item)
    return {
        "true": true_count,
        "false": false_count
    }

def calculate_stats(datas, column_name, column_type):
    column_data = [item[column_name] for item in datas]

    if column_type == int:
        return calculate_int_stats(column_data)
    elif column_type == str:
        return calculate_str_stats(column_data)
    elif column_type == list:
        return calculate_list_stats(column_data)
    elif column_type == bool:
        return calculate_bool_stats(column_data)
    else:
        return None
