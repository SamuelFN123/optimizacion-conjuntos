class Estation_Manager:

    def __init__(self):
        sets = {
            "k-one": {"ID", "NV", "UT"},
            "k-two": {"WA", "ID", "MT"},
            "k-three": {"OR", "NV", "CA"},
            "k-four": {"NV", "UT"},
            "k-five": {"CA", "AZ"},
            "k-six": {"NM", "TX", "OK"},
            "k-seven": {"OK", "KS", "CO"},
            "k-eight": {"KS", "CO", "NE"},
            "k-nine": {"NE", "SD", "WY"},
            "k-ten": {"ND", "IA"},
            "k-eleven": {"MN", "MO", "AR"},
            "k-twelve": {"LA"},
            "k-thirteen": {"MO", "AR"},
        }
        self.estations = [Estation(name, countries) for name, countries in sets.items()]


    def __getitem__(self, name):
        for estation in self.estations:
            if estation.name == name:
                return estation

    def get_most_covered_estation(self):
        pass


    def sort(self):
        sets = [item for item in self.sets.values()]
        stop = len(sets)
        for i in range(stop):
            for j in range(stop-i-1):
                if len(sets[j]) < len(sets[j+1]):
                    sets[j], sets[j+1] = sets[j+1], sets[j]
        return sets



class Estation:
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries


if __name__ == "__main__":
    pass