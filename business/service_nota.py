from domain.nota import Nota
from utils.sortari import *


class ServiceNota:
    def __init__(self, repo_nota, valid_nota, repo_student, repo_materie):
        """
        Initializam service nota
        :param repo_nota:
        :param valid_nota:
        :param repo_student:
        :param repo_materie:
        """
        self.__repo_nota = repo_nota
        self.__valid = valid_nota
        self.__repo_student = repo_student
        self.__repo_materie = repo_materie

    def service_adauga_nota(self, id_nota, nota, id_student, id_materie):
        """
        Functie adaugare nota
        :param id_nota:
        :param nota:
        :param id_student:
        :param id_materie:
        :return: Nota adaugata
        """
        nota_student = Nota(id_nota, nota, id_student, id_materie)
        self.__valid.valid_nota_student(nota_student)
        return self.__repo_nota.adauga_nota(nota_student)

    def service_sterge_nota(self, id_nota):
        """
        Functie stergere nota
        :param id_nota:
        :return: Nota stearsa
        """
        self.__valid.valid_id_nota(id_nota)
        return self.__repo_nota.sterge_nota(id_nota)

    def service_sterge_toate_notele_dupa_student(self, id_student):
        """
        Functie stergere toate notele unui student
        :param id_student:
        :return:
        """
        return self.__repo_nota.sterge_toate_notele_dupa_student(id_student, 1)

    def service_sterge_toate_notele_dupa_materie(self, id_materie):
        """
        Functie stergere toate notele de la o materie
        :param id_materie:
        :return:
        """
        return self.__repo_nota.sterge_toate_notele_dupa_materie(id_materie, 1)

    def service_modifica_nota(self, id_nota, nota_noua):
        """
        Functie de modificare nota
        :param id_nota:
        :param nota_noua:
        :return: Nota modificata
        """
        self.__valid.valid_id_nota(id_nota)
        self.__valid.valid_nota(nota_noua)
        return self.__repo_nota.modifica_nota(id_nota, nota_noua)

    def service_get_all_note(self):
        """
        Functie de getall note
        :return: Toate notele
        """
        note = self.__repo_nota.get_all_note()
        for nota in note:
            student = self.__repo_student.cauta_student(nota.get_id_student())
            materie = self.__repo_materie.cauta_materie(nota.get_id_materie())
            nota.set_nume_student(student.get_nume())
            nota.set_nume_materie(materie.get_nume())
        return note

    def cmp_note(self, x, y):
        """
        Functie de comparare note dupa nota
        :param x: nota 1
        :param y: nota 2
        :return: 1 sau 0
        """
        if x.get_nota() == y.get_nota():
            if x.get_nume_student() < y.get_nume_student():
                return 1
            return 0
        elif x.get_nota() > y.get_nota():
            return 1
        return 0

    def cmp_nume(self, x, y):
        """
        Functie de comparare note dupa nume
        :param x: nota 1
        :param y: nota 2
        :return: 1 sau 0
        """
        if x.get_nume_student() == y.get_nume_student():
            if x.get_nota() < y.get_nota():
                return 1
            return 0
        elif x.get_nume_student() > y.get_nume_student():
            return 1
        return 0

    def service_get_all_note_in_ordine_dupa_nota(self, id_materie):
        """
        Functie de sortare a tuturor notelor de la o materie dupa nota
        :param id_materie:
        :return: note sortate
        """
        note = self.__repo_nota.get_all_note_dupa_materie(id_materie)
        materie = self.__repo_materie.cauta_materie(id_materie)
        for nota in note:
            student = self.__repo_student.cauta_student(nota.get_id_student())
            nota.set_nume_student(student.get_nume())
            nota.set_nume_materie(materie.get_nume())

        note_sorted = bubble_sort(note, key=lambda nota: nota, cmp=lambda x, y: self.cmp_note(x, y), reverse=True)
        return note_sorted

    def service_get_all_note_in_ordine_dupa_nume(self, id_materie):
        """
        Functie de sortare a tuturor notelor de la o materie dupa nume
        :param id_materie:
        :return: note sortate
        """
        note = self.__repo_nota.get_all_note_dupa_materie(id_materie)
        materie = self.__repo_materie.cauta_materie(id_materie)
        for nota in note:
            student = self.__repo_student.cauta_student(nota.get_id_student())
            nota.set_nume_student(student.get_nume())
            nota.set_nume_materie(materie.get_nume())

        note_sorted = bubble_sort(note, key=lambda nota: nota, cmp=lambda x, y: self.cmp_nume(x, y))

        return note_sorted

    def service_get_primii_studenti(self):
        """
        Functie de sortare a primilor 20% din studenti dupa media generala
        :return: Studenti sortati
        """
        medii = self.__repo_nota.get_primii_studenti()
        for medie in medii:
            student = self.__repo_student.cauta_student(medie.get_id_student())
            medie.set_nume_student(student.get_nume())
        medii_sorted = shell_sort(medii, key=lambda media: media, cmp=lambda x, y: self.cmp_note(x, y), reverse=True)
        index = int(0.2 * len(medii_sorted))

        primele_medii = medii_sorted[:index]
        return primele_medii
