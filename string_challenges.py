# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
word = word.lower()
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
word = word.lower()
n = 0
for i in word:
    if i in 'аеёиоуэюя':
        n += 1
print(n)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(sentence.count(' ') + 1)


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in range(len(sentence)):
    if not i:
        print(sentence[i])
    elif sentence[i - 1] == ' ':
        print(sentence[i]) 


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
a = (len(sentence) - sentence.count(' ')) / (sentence.count(' ') + 1)
print(a)

