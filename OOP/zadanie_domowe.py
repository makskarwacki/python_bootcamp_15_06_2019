class Konwerter:

    @staticmethod
    def cel_to_farh(cel):
        fahr = cel * 9 / 5 + 32
        return fahr




assert Konwerter.cel_to_farh(0) == 32
