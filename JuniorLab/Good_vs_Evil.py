'''
В средиземье близится война. Грядет много битв сил света со тьмой.
Как с одной так и с другой стороны расы решают объединиться, чтобы общими усилиями одолеть врага.
Каждая раса обладает своими силами, которые оцениваются баллами.
На стороне добра будут сражаться:
Хоббиты: 1, Люди: 2, Эльфы: 3, Гномы: 3, Орлы: 4, Волшебники: 10
На темной стороне сражаются:
Орки: 1, Люди: 2, Варги: 2, Гоблины: 2, Урук-хаи: 3, Тролли: 5, Волшебники: 10
Ваша задача определить, кто же победит в битве.

Функция принимает два аргумента, которые являются строками.
В каждой строке через пробел перечислено количество существ,
которые будут сражаться за расу (порядок такой же, как в перечисленных выше списках).

Функция должна возвращать "Battle Result: Good triumphs over Evil" если побеждают хорошие,
"Battle Result: Evil eradicates all trace of Good" если побеждает зло
и "Battle Result: No victor on this battle field" если ничья.
'''

good = "707 423 584 293 572 62"
evil = "135 864 981 626 15 152 121"

def goodvsevil(good, evil):
    good_score = [1,2,3,3,4,10]
    evil_score = [1,2,2,2,3,5,10]
    good = [int(x) * y for x,y in zip(good.split(' '),good_score)]
    evil = [int(x) * y for x,y in zip(evil.split(' '),evil_score)]
    answer = sum(good) - sum(evil)
    if answer > 0:
        return "Battle Result: Good triumphs over Evil"
    elif answer < 0:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

print(goodvsevil(good,evil))
