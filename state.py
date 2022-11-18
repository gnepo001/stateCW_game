
class States:
    def __init__(self):
        self.states = []
        statedict = [{"name":"Texas","faction":0,"defense":0}]
        for index in range(0,len(statedict)):
                state = State(statedict[index]["name"],statedict[index]["faction"],statedict[index]["defense"])
                self.states.append(state)

    def get_states(self):
        return self.states


class State:
    def __init__(self,name,faction,defense=0):
        self.name = name
        self.faction = faction
        self.defense = defense
    
        
