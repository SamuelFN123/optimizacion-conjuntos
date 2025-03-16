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
        self.estations = [Estation(name, states) for name, states in sets.items()]
        # Orednarlos de más estados a menos
        self.estations.sort(reverse=True)


    def __getitem__(self, name):
        for estation in self.estations:
            if estation.name == name:
                return estation
        raise IndexError(f"There's no estation with name: '{name}'")

    def get_most_covered_estation(self):
        pass


class Estation:
    def __init__(self, name, states):
        self.name = name
        self.states = states
    
    def __repr__(self):
        return f"{self.name}: {self.states}"
    
    def __lt__(self, other):
        return len(self.states) < len(other.countries)


if __name__ == "__main__":
    pass