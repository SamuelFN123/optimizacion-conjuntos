class Station_Manager:

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
        self._create_stations()

    def _create_stations(self):
        self.stations = [Station(name, states) for name, states in self.sets.items()]
        # Orednarlos de más estados a menos
        self.stations.sort(reverse=True)
    
    def reset_stations(self):
        self._create_stations()


    def __getitem__(self, name):
        index = [i for i, station in enumerate(self.stations) if station.name == name]
        if index:
            station = self._pop_station(index[0])
            return station
        else:
            raise IndexError(f"There's no station with name: '{name}'")
    
    def pop_best_station(self, covered_states):
        pass

    def pop_first_station(self):
        station = self._pop_station(0)
        return station

    def _pop_station(self, index):
        station = self.stations.pop(index)
        return station

    def get_all_states(self):
        all_states = set()
        for station in self.stations:
            all_states.update(station.states)
        return(all_states)
    
    def __len__(self):
        return len(self.stations)

class Station:
    def __init__(self, name:str, states:set[str]):
        self.name = name
        self.states = states
    
    def __repr__(self):
        return f"{self.name}: {self.states}"
    
    def __lt__(self, other):
        return len(self.states) < len(other.states)


if __name__ == "__main__":
    manager = Station_Manager()
    all_states = manager.get_all_states()
    states_covered = set()
    stations = []
    while states_covered != all_states:
        station = manager.pop_first_station()
        if not station.states.issubset(states_covered):
            states_covered.update(station.states)
            stations.append(station.name)
    states_covered = list(states_covered)
    states_covered.sort()
    all_states  = list(all_states)
    all_states.sort()
    print(f"States to cover: {", ".join(all_states)}\nStations needed: {", ".join(stations)}\nStates covered:  {", ".join(states_covered)}")
    