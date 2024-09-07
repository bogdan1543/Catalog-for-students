from domain.materie import Materie


class ServiceMaterie:
    def __init__(self, repo_materie, valid_materie):
        """
        Initializam service materie
        :param repo_materie: repository materie
        :param valid_materie: validator materie
        """
        self.__repo = repo_materie
        self.__valid = valid_materie

    def service_adauga_materie(self, id_materie, nume, profesor):
        """
        Functie de adaugare materie
        :param id_materie:
        :param nume:
        :param profesor:
        :return: Materia adaugata
        """
        materie = Materie(id_materie, nume, profesor)
        self.__valid.valid_materie(materie)
        return self.__repo.adauga_materie(materie)

    def service_sterge_materie(self, id_materie):
        """
        Functie de stergere materie
        :param id_materie:
        :return: Materia stearsa
        """
        self.__valid.valid_id_materie(id_materie)
        return self.__repo.sterge_materie(id_materie)

    def service_modifica_materie(self, id_materie, nume_nou, profesor_nou):
        """
        Functie de modificare materie
        :param id_materie:
        :param nume_nou:
        :param profesor_nou:
        :return: Materia modificata
        """
        self.__valid.valid_id_materie(id_materie)
        if nume_nou:
            self.__valid.valid_nume(nume_nou)
        if profesor_nou:
            self.__valid.valid_profesor(profesor_nou)
        materie = Materie(id_materie, nume_nou, profesor_nou)
        return self.__repo.modifica_materie(materie)

    def service_cauta_materie(self, id_materie):
        """
        Functie de cautare materie
        :param id_materie:
        :return: Materia cautata
        """
        self.__valid.valid_id_materie(id_materie)
        return self.__repo.cauta_materie(id_materie)

    def service_genereaza_materie(self, nr_generari):
        """
        Functie de generare materii
        :param nr_generari:
        :return:
        """
        return self.__repo.genereaza_materie(nr_generari)

    def service_get_all_materii(self):
        """
        Functie de getter a tuturor materiilor
        :return: Toate materiile
        """
        return self.__repo.get_all_materii()
