"""
Приведение исходных данных в формате:
    [('device', price, 'Client', 'number'),
    ('device', price, 'Client_1', 'number_1'),...]
 к формату:
    {('Client', number'): [('device', 'price'), ('device', 'price'), ...],
    ('Client_1', number_1'): [('device', 'price'), ('device', 'price'), ...],
    }
"""

def get_optimize_format_data(technic):
    optimize_data = {}
    for client in technic:
        key = (client[2], client[3])
        if key in optimize_data:
            optimize_data[key].append((client[0], client[1]))
        else:
            optimize_data[key] = [(client[0], client[1])]
    return optimize_data


"""
Сборка данных для вывода на печать в заданном формате
"""

def devices_list_to_str(devices_list):
    result_list = ''
    for device in devices_list:
        result_list += device[0] + ' - ' + str(device[1]) + '; '
    return result_list[:-2]

def get_printed_data(data):
    data = get_optimize_format_data(data)
    printed_data = ''
    for key in data:
        client = key[0] + ' ' + str(key[1]) + ': '
        devices = devices_list_to_str(data[key])
        printed_data += client + devices + '\n'
    return printed_data[:-1]

