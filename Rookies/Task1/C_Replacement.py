N = int(input(''))
numbers = list (map(int,input().split()))
result_list = []
for number in numbers :
    if number > 0 :
        result_list.append(1)

    if number < 0:
        result_list.append(2)

    if number == 0:
        result_list.append(0)

print (' '.join(map(str,result_list)))