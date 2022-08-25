from domain.Song import Song


class SongRepository:

    def __init__(self):
        self.__entity_list = []
        piesa1 = Song("Mote", "Sonic Youth", "Post-Punk", 7)
        piesa2 = Song("Andromeda", "Weyes Blood", "Art Pop", 3)
        piesa3 = Song("Calabria", "Vale", "Drill", 3)
        self.add_entity(piesa1)
        self.add_entity(piesa2)
        self.add_entity(piesa3)

    def get_entity_list(self):
        return self.__entity_list

    def add_entity(self, entity):
        self.get_entity_list().append(entity)


