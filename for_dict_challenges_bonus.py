"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list({random.randint(1, 10000) for _ in range(random.randint(5, 20))})
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice([None, random.choice([m["id"] for m in messages]) if messages else []]),
            "seen_by": random.sample(users_ids, random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    
    #Задание 1:
    lst1 = [n['sent_by'] for n in messages]
    s = list(set(lst1))
    lst2 = [lst1.count(m) for m in s]
    d = {lst2[i]: s[i] for i in range(len(lst2))}
    x1 = d[max(lst2)]

    #Задание 2:
    lst1 = []
    for n in messages:
        if n['reply_for'] is not None:
            lst1.append(n['sent_by'])
    lst2 = [lst1.count(m) for m in lst1]
    d = {lst2[i]: lst1[i] for i in range(len(lst2))}
    x2 = d[max(lst2)]

    #Задание 3:
    lst1 = [{n['sent_by']: n['id']} for n in messages]
    lst2 = []
    lst3 = []
    for i in range(len(lst1)):
        lst4 = []
        for k in lst1:
            if k.get(messages[i]['sent_by']) is not None:
                if k.get(messages[i]['sent_by']) not in lst4:
                    lst4.append(k.get(messages[i]['sent_by']))
                else:
                    continue
            else:
                continue
        s = set(lst4)
        if {len(s): messages[i]['sent_by']} not in lst2 and len(s) not in lst3:
            lst2.append({len(s): messages[i]['sent_by']})
            lst3.append(len(s))
    for p in lst2:
        if max(lst3) in p:
            x3 = p[max(lst3)]
    
    #Задание 4:
    lst1 = [n['sent_at'].strftime('%H:%M') for n in messages]

    lst2 = []
    d = {}
    lst3 = [0, 6, 12, 18] 
    lst4 = [5, 11, 17, 23]
    lst5 = ['утром', 'днем', 'вечером', 'ночью']

    def func_dict(*args):
        a = 0
        for m in args[0]:
            if args[2] <= int(m[:2]) <= args[3]:
                a += 1
        args[1].append(a)
        b = args[5]
        b |= {a: args[4]}
        return args[1], b
    
    for i in range(len(lst3)):
        c = func_dict(lst1, lst2, lst3[i], lst4[i], lst5[i], d)
        lst2 = c[0]
        d = c[1]
    x4 = f'Больше всего сообщений {d[max(lst2)]}'

    #Задание 5:
    lst1 = [n['id'] for n in messages]
    lst2 = [len(n['text']) for n in messages]
    d = {lst2[i]: lst1[i] for i in range(len(lst1))}
    x5 = d[max(lst2)]

    return [x1, x2, x3, x4, x5]

if __name__ == "__main__":
    print(*generate_chat_history(), sep='\n')
