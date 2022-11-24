
class RejestrKont:

    list = []

    @classmethod
    def add(cls, other):
        cls.list.append(other)

    @classmethod
    def count(cls):
        return len(cls.list)

    @classmethod
    def find(cls, pesel):
        result = None
        for konto in cls.list:
            print(konto.pesel)
            if konto.pesel == pesel:
                result = konto
        return result
