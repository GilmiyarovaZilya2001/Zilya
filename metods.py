alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class Alien:
    def __init__(self, name: str, value: int, fullness: int):
        self.name = name
        self.value = value
        self.fullness = fullness

    def __eq__(self, other):
        return self.value * self.fullness == other.value * other.fullness

    def __add__(self, other):
        temp1 = -1
        temp2 = -1
        __name = ""
        for i in range(len(alpabet)):
            if self.name[0].lower() == alpabet[i]:
                temp1 = i
            if other.name[0].lower() == alpabet[i]:
                temp2 = i
            if temp1 >= 0 and temp2 >= 0:
                break
        if temp1 <= temp2:
            __name = self.name + "-" + other.name
        else:
            __name = other.name + "-" + self.name
        return Alien(__name, (self.value + other.value) // 2, min(self.fullness, other.fullness))

    def __iadd__(self, other):
        return Alien(self.name, self.value + other, self.fullness)

    def __isub__(self, other):
        return Alien(self.name, self.value - other, self.fullness)

    def __mul__(self, other):
        temp = []
        for i in range(other):
            temp.append(str(Alien(self.name + "-" + str(i + 1), self.value, self.fullness)))
        return temp

    def fill_up(self, number: int):
        if number >= 0:
            return self.fullness + number
        else:
            if self.fullness - number >= 0:
                return self.fullness - number
            else:
                return self.fullness == 0

    def __str__(self):
        return f"Wheel Alien {self.name} with {self.value} valume and filled up {self.fullness}."



al = Alien("Man", 200, 148)
al1 = Alien("Spider", 800, 201)
print(al <= al1, al != al1, al > al1)
print(al, al1, sep="\n")
print()
al.fill_up(-203)
res = al1 * 3
print(al, al1, res,sep="\n")
