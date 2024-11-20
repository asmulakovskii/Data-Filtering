def apply_filters(data, filters):
    for filter_cond in filters:
        column, condition = filter_cond.split('=')
        if '-' in condition:
            min_val, max_val = map(int, condition.split('-'))
            data = [row for row in data if min_val <= int(row[column]) <= max_val]
        else:
            data = [row for row in data if row[column] == condition]
    return data
