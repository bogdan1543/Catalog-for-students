from random import random, choice, randint
from domain.materie import Materie
class RepoMaterie:
    def __init__(self):
        self._materii = {}

    def __len__(self):
        return len(self._materii)

    def clear_list(self):
        self._materii = {}

    def adauga_materie(self, materie):
        id_materie = materie.get_id_materie()
        if id_materie in self._materii:
            raise Exception("Exista deja o materie cu acelasi id!\n")
        self._materii[id_materie] = materie
        return self._materii

    def sterge_materie(self, id_materie):
        if id_materie not in self._materii:
            raise Exception("Nu exista o materie cu acelasi id!\n")
        del self._materii[id_materie]

    def modifica_materie(self, materie_noua):
        if materie_noua.get_id_materie() not in self._materii:
            raise Exception("Nu exista o materie cu acelasi id!")
        self._materii[materie_noua.get_id_materie()] = materie_noua

    def cauta_materie(self, id_materie):
        if id_materie not in self._materii:
            raise Exception("Nu exista o materie cu acest id")
        return self._materii[id_materie]

    def genereaza_materie(self, nr):
        while nr:
            name = ["Geografie", "Informatica", "Biologie", "Matematica", "Romana"]
            profesor = ["Bogdan Macovei", "George Enescu", "Lucian Blaga", "Mihai Eminescu"]
            random_nume = choice(name)
            random_profesor = choice(profesor)
            random_id = randint(1, 100)
            if random_id not in self._materii:
                materie = Materie(random_id, random_nume, random_profesor)
                self._materii[random_id] = materie
                nr -= 1
        return self._materii

    def get_all_materii(self):
        return [self._materii[x] for x in self._materii.keys()]

class FileRepoMaterie(RepoMaterie):
    def __init__(self, file_path_materie):
        self.__file_path_materie = file_path_materie
        RepoMaterie.__init__(self)

    def __len__(self):
        return RepoMaterie.__len__(self)

    def __citeste_fisier(self):
        with open(self.__file_path_materie, "r") as f:
            self._materii.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                parti = line.split(";")
                id_materie = int(parti[0])
                nume = parti[1]
                profesor = parti[2]
                materie = Materie(id_materie, nume, profesor)
                self._materii[id_materie] = materie

    def __scrie_in_fisier(self):
        with open(self.__file_path_materie, "w") as f:
            materii = RepoMaterie.get_all_materii(self)
            for materie in materii:
                input = str(materie.get_id_materie()) + " ; " + str(materie.get_nume()) + " ; " + str(
                    materie.get_profesor()) + "\n"
                f.write(input)

    def adauga_materie(self, materie):
        self.__citeste_fisier()
        RepoMaterie.adauga_materie(self, materie)
        self.__scrie_in_fisier()

    def cauta_materie(self, id_materie):
        self.__citeste_fisier()
        return RepoMaterie.cauta_materie(self, id_materie)

    def sterge_materie(self, id_materie):
        self.__citeste_fisier()
        RepoMaterie.sterge_materie(self, id_materie)
        self.__scrie_in_fisier()

    def modifica_materie(self, materie):
        self.__citeste_fisier()
        RepoMaterie.modifica_materie(self, materie)
        self.__scrie_in_fisier()

    def genereaza_materie(self, nr):
        self.__citeste_fisier()
        RepoMaterie.genereaza_materie(self, nr)
        self.__scrie_in_fisier()

    def get_all_materii(self):
        self.__citeste_fisier()
        return RepoMaterie.get_all_materii(self)


