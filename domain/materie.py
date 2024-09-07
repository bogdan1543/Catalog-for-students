class Materie:
    def __init__(self, id_materie, nume, profesor):
        self.__id_materie = id_materie
        self.__nume = nume
        self.__profesor = profesor

    def get_id_materie(self):
        return self.__id_materie

    def get_nume(self):
        return self.__nume

    def set_nume(self, nume):
        self.__nume = nume

    def get_profesor(self):
        return self.__profesor

    def set_profesor(self, profesor):
        self.__profesor = profesor

    def __eq__(self, other):
        return self.__id_materie == other.__id_materie

    def __str__(self):
        return f"[{self.__id_materie}]: {self.__nume} - prof. {self.__profesor}"