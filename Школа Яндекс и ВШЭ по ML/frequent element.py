# Частый элемент
n = int(input())
a = list(map(int, input().split()))

number_count = {}

for number in a:
    if number in number_count:
        number_count[number] += 1
    else:
        number_count[number] = 1

max_count = max(number_count.values())
max_numbers = [number for number, count in number_count.items() if count == max_count]
max_number = max_numbers[0]
print(max_number)