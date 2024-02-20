def read_input():
    n = int(input())
    strings = [input() for i in range(n)]
    return strings, n



def palindrom(nInputs:int,stringsList:list[str]):
    answer = []
    for word_i in range(int(nInputs)):
        for word_j in range(int(nInputs)):
            if word_i != word_j:
                if (stringsList[word_i]+stringsList[word_j]) == (stringsList[word_i]+stringsList[word_j])[::-1]:
                    answer.append(f'{word_i+1} {word_j+1}')
    return answer



def main():
    stringsList, nInputs = read_input()
    print(" \n".join(palindrom(nInputs,stringsList)))

if __name__ == '__main__':
    main()


###Решение для Яндекс Контеста
n = int(input())
strings = [input() for i in range(n)]


answer = []
for word_i in range(int(n)):
    for word_j in range(int(n)):
        if word_i != word_j:
            if (strings[word_i]+strings[word_j]) == (strings[word_i]+strings[word_j])[::-1]:
                answer.append(f'{word_i+1} {word_j+1}')
            
print(" \n".join(answer))




