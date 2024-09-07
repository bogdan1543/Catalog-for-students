from domain.student import Student


class ServiceStudent:
    def __init__(self, repo_student, valid_student):
        """
        Intializare service student
        :param repo_student:
        :param valid_student:
        """
        self.__repo = repo_student
        self.__valid = valid_student

    def service_adauga_student(self, id_student, nume):
        """
        Functie de adaugare student
        :param id_student:
        :param nume:
        :return: Studentul adaugat
        """
        student = Student(id_student, nume)
        self.__valid.valid_student(student)
        return self.__repo.adauga_student(student)

    def service_sterge_student(self, id_student):
        """
        Functie de sterge student
        :param id_student:
        :return: Studentul sters
        """
        self.__valid.valid_id_student(id_student)
        return self.__repo.sterge_student(id_student)

    def service_modifica_student(self, id_student, nume_nou):
        """
        Functie de modifica student
        :param id_student:
        :param nume_nou:
        :return: Studentul modificat
        """
        self.__valid.valid_id_student(id_student)
        self.__valid.valid_nume(nume_nou)
        student = Student(id_student, nume_nou)
        return self.__repo.modifica_student(student)

    def service_cauta_student(self, id_student):
        """
        Functie de cauta student
        :param id_student:
        :return: Studentul cautat
        """
        self.__valid.valid_id_student(id_student)
        return self.__repo.cauta_student(id_student)

    def service_genereaza_student(self, nr):
        """
        Functie de generare studenti
        :param nr: Numarul de generari
        :return:
        """
        return self.__repo.genereaza_student(nr)

    def service_get_all_studenti(self):
        """
        Functie de getall studenti
        :return: Toti studentii
        """
        return self.__repo.get_all_studenti()
