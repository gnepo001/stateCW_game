import pygame

class States:
    def __init__(self,group):
        self.states = []
        statedict = [
            {"state":"Alabama","pos":(1600,1050),"name":"Montgomery","faction":0,"defense":0},
            #{"state":"Alaska ","pos":(1100,1150),"name":"Juneau","faction":0,"defense":0},
            {"state":"Arizona","pos":(500,950),"name":"Phoenix","faction":0,"defense":0},
            {"state":"Arkansas","pos":(1320,910),"name":"Little Rock","faction":0,"defense":0},
            {"state":"California","pos":(94,536),"name":"Sacramento","faction":0,"defense":0},
            {"state":"Colorado","pos":(827,626),"name":"Denver","faction":0,"defense":0},
            {"state":"Connecticut","pos":(2068,404),"name":"Hartford","faction":0,"defense":0},
            {"state":"Delaware","pos":(1998,588),"name":"Dover","faction":0,"defense":0},
            {"state":"Florida","pos":(1682,1120),"name":"Tallahassee","faction":0,"defense":0},
            {"state":"Georgia","pos":(1670,939),"name":"Atlanta","faction":0,"defense":0},
            #{"state":"Hawaii ","pos":(1100,1150),"name":"Honolulu","faction":0,"defense":0},
            {"state":"Idaho","pos":(401,393),"name":"Boise","faction":0,"defense":0},
            {"state":"Illinois","pos":(1430,673),"name":"Springfield","faction":0,"defense":0},
            {"state":"Indiana","pos":(1565,643),"name":"Indianapolis","faction":0,"defense":0},
            {"state":"Iowa","pos":(1278,548),"name":"Des Moines","faction":0,"defense":0},
            {"state":"Kansas","pos":(1145,676),"name":"Topeka","faction":0,"defense":0},
            {"state":"Kentucky","pos":(1604,725),"name":"Frankfort","faction":0,"defense":0},
            {"state":"Louisiana","pos":(1394,1169),"name":"Baton Rouge","faction":0,"defense":0},
            {"state":"Maine","pos":(2128,218),"name":"Augusta","faction":0,"defense":0},
            {"state":"Maryland","pos":(1972,592),"name":"Annapolis","faction":0,"defense":0},
            {"state":"Massachusetts","pos":(2129,359),"name":"Boston","faction":0,"defense":0},
            {"state":"Michigan","pos":(1610,474),"name":"Lansing","faction":0,"defense":0},
            {"state":"Minnesota","pos":(1230,396),"name":"St. Paul","faction":0,"defense":0},
            {"state":"Mississippi","pos":(1420,1058),"name":"Jackson","faction":0,"defense":0},
            {"state":"Missouri","pos":(1306,697),"name":"Jefferson City","faction":0,"defense":0},
            {"state":"Montana","pos":(551,253),"name":"Helena","faction":0,"defense":0},
            {"state":"Nebraska","pos":(1101,602),"name":"Lincoln","faction":0,"defense":0},
            {"state":"Nevada","pos":(232,559),"name":"Carson City","faction":0,"defense":0},
            {"state":"New Hampshire","pos":(2079,304),"name":"Concord","faction":0,"defense":0},
            {"state":"New Jersey","pos":(2019,531),"name":"Trenton","faction":0,"defense":0},
            {"state":"New Mexico","pos":(757,859),"name":"Santa Fe","faction":0,"defense":0},
            {"state":"New York","pos":(1978,365),"name":"Albany","faction":0,"defense":0},
            {"state":"North Carolina","pos":(1930,778),"name":"Raleigh","faction":0,"defense":0},
            {"state":"North Dakota","pos":(1000,269),"name":"Bismarck","faction":0,"defense":0},
            {"state":"Ohio","pos":(1663,604),"name":"Columbus","faction":0,"defense":0},
            {"state":"Oklahoma ","pos":(1086,860),"name":"Oklahoma City","faction":0,"defense":0},
            {"state":"Oregon ","pos":(150,220),"name":"Salem","faction":0,"defense":0},
            {"state":"Pennsylvania ","pos":(1904,523),"name":"Harrisburg","faction":0,"defense":0},
            {"state":"Rhode Island","pos":(2109,391),"name":"Providence","faction":0,"defense":0},
            {"state":"South Carolina","pos":(1805,908),"name":"Columbia","faction":0,"defense":0},
            {"state":"South Dakota","pos":(1043,429),"name":"Pierre","faction":0,"defense":0},
            {"state":"Tennessee","pos":(1558,836),"name":"Nashville","faction":0,"defense":0},
            {"state":"Texas ","pos":(1069,1186),"name":"Austin","faction":0,"defense":0},
            {"state":"Utah ","pos":(495,547),"name":"Salt Lake City","faction":0,"defense":0},
            {"state":"Vermont ","pos":(2018,250),"name":"Montpelier","faction":0,"defense":0},
            {"state":"Virginia ","pos":(1961,701),"name":"Richmond","faction":0,"defense":0},
            {"state":"Washington ","pos":(208,115),"name":"Olympia","faction":0,"defense":0},
            {"state":"West Virginia","pos":(1748,679),"name":"Charleston","faction":0,"defense":0},
            {"state":"Wisconsin ","pos":(1440,451),"name":"Madison","faction":0,"defense":0},
            {"state":"Wyoming ","pos":(759,536),"name":"Cheyenne","faction":0,"defense":0},
        ]
        for index in range(0,len(statedict)):
                state = State(statedict[index]['pos'],statedict[index]['state'],group,statedict[index]["name"],statedict[index]["faction"],statedict[index]["defense"])
                self.states.append(state)

    def get_states(self):
        return self.states


class State(pygame.sprite.Sprite):
    def __init__(self,pos,state,group,name,capital,faction,defense=0):
        super().__init__(group)
        self.state = state
        self.name = name
        self.capital = capital
        self.faction = faction
        self.defense = defense
        self.pos = pos
        self.image = pygame.image.load("./assets/faction0.png")
        self.rect = self.image.get_rect(center= self.pos)



    
        
