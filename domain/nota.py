class Nota:
    def __init__(self, id_nota, nota, student, materie):
        self.__id_student = student
        self.__id_materie = materie
        self.__id_nota = id_nota
        self.__nota = nota

    def get_id_nota(self):
        return self.__id_nota

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        self.__nota = nota

    def get_id_student(self):
        return self.__id_student

    def get_id_materie(self):
        return self.__id_materie

    def __str__(self):
        return f"Nota {self.__nota} la {self.__id_materie} pentru {self.__id_student}"