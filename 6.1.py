with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    list_logs = []
    for line in f:
        list_log = line.split(' ')
        list_logs.append((list_log[0], list_log[5].strip('"'), list_log[6]))
    print(list_logs)
