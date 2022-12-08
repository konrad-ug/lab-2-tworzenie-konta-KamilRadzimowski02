
class RejestrKont:

    list = []

    @classmethod
    def add(cls, other):
        print(other.pesel)
        exists = cls.find(other.pesel)
        if exists is not None:
            return False
        else:
            cls.list.append(other)
            return True

    @classmethod
    def count(cls):
        return len(cls.list)

    @classmethod
    def find(cls, pesel):
        result = None
        for konto in cls.list:
            print("find")
            print(konto.pesel)
            if konto.pesel == pesel:
                result = konto
        print(result)
        return result

    @classmethod
    def delete(cls, pesel):
        result = []
        for konto in cls.list:
            if konto.pesel != pesel:
                result.append(konto)
        cls.list = result