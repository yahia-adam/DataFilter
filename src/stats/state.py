def calculate_int_stats(data):
    return {
        "min": min(data),
        "max": max(data),
        "avg": sum(data) / len(data) if data else None
    }

def calculate_float_stats(data):
    data = [number for number in data if isinstance(number, float)]

    avg = round(sum(data) / len(data), 2)

    return {
        "min": min(data),
        "max": max(data),
        "avg": avg
    }

def calculate_str_stats(data):
    lengths = [len(item) for item in data]
    return {
        "len-min": min(lengths),
        "len-max": max(lengths),
        "total-len": sum(lengths)
    }

def calculate_list_stats(data):
    # flatten the list of lists into a single list
    data = [item for sublist in data for item in sublist]

    # convert the list to a set to get unique values
    unique_values_set = set(data)

    min_val = min(unique_values_set)
    max_val = max(unique_values_set)
    avg_val = round(sum(unique_values_set) / len(unique_values_set), 2)

    return {
        "min": min_val,
        "max": max_val,
        "avg": avg_val
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
    elif column_type == float:
        return calculate_float_stats(column_data)
    else:
        return None
