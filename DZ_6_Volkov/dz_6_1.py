with open('nginx_logs.txt', 'r', encoding='utf-8') as data:
    request_list = []
    for line in data:
        remote_addr = line[:line.find(' ')]
        request_type = line[line.find('"') + 1:line.find(' /')]
        requested_resource = line[line.find('/d'):line.find(' HTTP')]
        tuple_rquest = (remote_addr, request_type, requested_resource)
        request_list.append(tuple_rquest)

print(request_list)