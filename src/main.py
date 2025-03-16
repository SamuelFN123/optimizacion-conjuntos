class Estation_Manager:

    def __init__(self):
        self.sets = {
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
        self._create_estations()

    def _create_estations(self):
        self.estations = [Estation(name, states) for name, states in self.sets.items()]
        # Orednarlos de más estados a menos
        self.estations.sort(reverse=True)
    
    def reset_estations(self):
        self._create_estations()


    def __getitem__(self, name):
        index = [i for i, estation in enumerate(self.estations) if estation.name == name]
        if index:
            station = self.pop_estation(index[0])
            return station
        else:
            raise IndexError(f"There's no estation with name: '{name}'")

    def get_most_covered_estation(self):
        station = self.pop_estation(0)
        return station

    def pop_estation(self, index):
        station = self.estations.pop(index)
        self.estations.sort(reverse=True)
        return station

    def get_all_states(self):
        all_states = set()
        for station in self.estations:
            all_states.update(station.states)
        return(all_states)
    
    def __len__(self):
        return len(self.estations)

class Estation:
    def __init__(self, name, states):
        self.name = name
        self.states = states
    
    def __repr__(self):
        return f"{self.name}: {self.states}"
    
    def __lt__(self, other):
        return len(self.states) < len(other.states)


if __name__ == "__main__":
    pass