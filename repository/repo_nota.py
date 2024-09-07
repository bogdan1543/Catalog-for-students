from domain.nota import Nota
from domain.note_student import NoteStudent
from domain.medie import Medie
class RepoNota:
    def __init__(self):
        self._note = {}

    def __len__(self):
        return len(self._note)

    def clear_list(self):
        self._note = {}

    def adauga_nota(self, nota):
        id_nota = nota.get_id_nota()
        if id_nota in self._note:
            raise Exception("Exista deja o nota cu acelasi id!\n")
        self._note[id_nota] = nota
        return self._note

    def sterge_nota(self, id_nota):
        if id_nota not in self._note:
            raise Exception("Nu exista un student cu acest id")
        del self._note[id_nota]
        return self._note

    def sterge_toate_notele_dupa_student_mem(self, id_student, id_nota):
        '''
        Caz favorabil O(1)
        Caz nefavorabil O(n)
        Complexitate O(n)
        :param id_student:
        :param id_nota:
        :return: lista note
        '''
        if self._note[id_nota].get_id_student() == id_student:
            self._note.pop(id_nota)
            return self._note
        return self.sterge_toate_notele_dupa_student_mem(id_student, id_nota + 1)


    def sterge_toate_notele_dupa_materie_mem(self, id_materie, id_nota):
        '''
        Caz favorabil O(1)
        Caz nefavorabil O(n)
        Complexitate O(n)
        :param id_materie:
        :param id_nota:
        :return: lista note
        '''
        if self._note[id_nota].get_id_materie() == id_materie:
            self._note.pop(id_nota)
            return self._note
        return self.sterge_toate_notele_dupa_materie_mem(id_materie, id_nota + 1)


    def modifica_nota(self, id_nota, nota_noua):
        if id_nota not in self._note:
            raise Exception("Nu exista o nota cu acest id")
        self._note[id_nota].set_nota(nota_noua)
        return self._note

    def cauta_nota(self, id_nota):
        if id_nota not in self._note:
            raise Exception("Nu exista o nota cu acest id")
        return self._note[id_nota]

    def get_primii_studenti(self):
        note = []
        for id_nota in self._note:
            nota = NoteStudent(self._note[id_nota].get_id_student(), self._note[id_nota].get_id_materie(), float(self._note[id_nota].get_nota()))
            note.append(nota)
        medii = []
        for x in note:
            s = 0
            nr = 0
            id_student = x.get_id_student()
            for nota in note:
                if nota.get_id_student() == id_student:
                    s = s + nota.get_nota()
                    nr += 1
            media = float(s / nr)
            medii.append(Medie(media, x.get_id_student()))
        return medii


class FileRepoNota(RepoNota):
    def __init__(self, file_path_note):
        self.__file_path_note = file_path_note
        RepoNota.__init__(self)

    def __citeste_fisier(self):
        with open(self.__file_path_note, "r") as f:
            self._note.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                parti = line.split(";")
                id_nota = int(parti[0])
                nota = int(parti[1])
                id_student = int(parti[2])
                id_materie = int(parti[3])
                nota = Nota(id_nota, nota, id_student, id_materie)
                self._note[id_nota] = nota

    def __scrie_in_fisier(self):
        with open(self.__file_path_note, "w") as f:
            note = RepoNota.get_all_note(self)
            for nota in note:
                input = str(nota.get_id_nota()) + " ; " + str(nota.get_nota()) + str(nota.get_id_student()) + " ; " + str(nota.get_id_materie()) + "\n"
                f.write(input)

    def adauga_nota(self, nota):
        self.__citeste_fisier()
        RepoNota.adauga_nota(self, nota)
        self.__scrie_in_fisier()

    def sterge_nota(self, id_nota):
        self.__citeste_fisier()
        return RepoNota.sterge_nota(self, id_nota)

    def sterge_toate_notele_dupa_student(self, id_student, id_nota):
        self.__citeste_fisier()
        RepoNota.sterge_toate_notele_dupa_student_mem(self, id_student, id_nota)
        self.__scrie_in_fisier()

    def sterge_toate_notele_dupa_materie(self, id_materie, id_nota):
        self.__citeste_fisier()
        RepoNota.sterge_toate_notele_dupa_materie_mem(self, id_materie, id_nota)
        self.__scrie_in_fisier()

    def modifica_nota(self, id_nota, nota_noua):
        self.__citeste_fisier()
        RepoNota.modifica_nota(self, id_nota, nota_noua)
        self.__scrie_in_fisier()

    def get_primii_studenti(self):
        self.__citeste_fisier()
        return RepoNota.get_primii_studenti(self)

    def get_all_note(self):
        """
        Functie de getall note
        :param materie:
        :return:
        """
        f = open(self.__file_path_note, "r")

        note = []
        parts = []
        line = f.readline().strip()
        while line != "":
            parts = line.split(";")
            nota = NoteStudent(int(parts[2]), int(parts[3]), float(parts[1]))
            note.append(nota)
            line = f.readline().strip()
        f.close()
        return note

    def get_all_note_dupa_materie(self, materie):
        """
        Functie de getall note dupa materie
        :param materie:
        :return: Notele studentilor de la o materie
        """
        f = open(self.__file_path_note, "r")

        note = []
        parts = []
        line = f.readline().strip()
        while line != "":
            parts = line.split(";")
            if int(parts[3]) == materie:
                nota = NoteStudent(int(parts[2]), int(parts[3]), float(parts[1]))
                note.append(nota)
            line = f.readline().strip()
        f.close()
        return note
