class Medie:
    def __init__(self, nota, id_student):
        self.__nota = nota
        self.__id_student = id_student
        self.__nume_student = ""

    def get_nota(self):
        return self.__nota

    def get_id_student(self):
        return self.__id_student

    def get_nume_student(self):
        return self.__nume_student

    def set_nume_student(self, nume_student):
        self.__nume_student = nume_student