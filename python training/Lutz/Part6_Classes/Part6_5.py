# # 1
# a = {1, 2, 3}
# b = {4, 3, 8}
#
# print(a & b)
# print(a | b)
#
# # 2
# c = set("hello world")
# print("c:", c)
# # print(c[3], c[1:3]) - sets don't support indexing
#
# # 3
# for item in c:
#     print(item)
#
# # 4
# # print(c & 'hello') - unsupported operand
# # print(c | 'hello') - unsupported operand


class Set:
    def __init__(self, value = []):  # Конструктор
        self.data = []  # Управляет списком
        self.concat(value)

    def intersect(self, other):  # other – любая последовательность
        res = []  # self – подразумеваемый объект
        for x in self.data:
            if x in other:  # Выбрать общие элементы
                res.append(x)
        return Set(res)  # Вернуть новый экземпляр Set

    def union(self, other):  # other – любая последовательность
        res = self.data[:]  # Копировать список
        for x in other:  # Добавить элементы из other
            if not x in res:
                res.append(x)
        return Set(res)


class TestSet(Set):
    def __init__(self, data={}):
        self.data = data

    def __and__(self, other):
        return self.data & other

    def __or__(self, other):
        return self.data | other

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        for item in self.data:
            yield item

    def intersect(self, *other):
        res = []
        for x in self:
            for y in other:
                if x not in y:
                    break
            else:
                res.append(x)
        return res


if __name__ == "__main__":
    a = TestSet({1, 2, 3})
    print(a & {2, 5, 6})
    print(a | {2, 5, 6})
    # print(a[2])
    for i in a:
        print(i)

    print(a.intersect([1,2,3], [2,3,4], [1,2,3]))
