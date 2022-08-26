from domain.Song import Song


class SongRepository:

    def __init__(self):
        self.__entity_list = []
        piesa1 = Song("Mote", "Sonic Youth", "Post-Punk", 7)
        piesa2 = Song("Andromeda", "Weyes Blood", "Art Pop", 3)
        piesa3 = Song("Calabria", "Vale", "Drill", 3)
        piesa4 = Song("Kody Blu 31", "JID", "Rap", 3)
        piesa5 = Song("at thirst sight by Assia", "MIKE", "Abstract Rap", 3)
        piesa6 = Song("Raydar", "JID", "Rap", 3)
        piesa7 = Song("CHIP SHOP", "kkbutterfly27", "TikTok", 1)
        piesa8 = Song("Momentary Bliss", "Gorillaz", "Pop Rap", 4)
        piesa9 = Song("Give Me Everything", "Pittbul", "Mainstream Pop", 4)
        self.add_entity(piesa1)
        self.add_entity(piesa2)
        self.add_entity(piesa3)
        self.add_entity(piesa4)
        self.add_entity(piesa5)
        self.add_entity(piesa6)
        self.add_entity(piesa7)
        self.add_entity(piesa8)

    def get_entity_list(self):
        return self.__entity_list

    def add_entity(self, entity):
        self.get_entity_list().append(entity)
