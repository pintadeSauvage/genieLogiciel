class InfosEscales(object):

    def __init__(self, heureDepart, heureArrivee):
        self.heureDepart=heureDepart
        self.heureArrivee=heureArrivee 
        self.duree=heureDepart-heureArrivee

    def _get_duree(self):
        return self.duree


    pass




