class NoteStudent:
    def __init__(self, id_student, id_materie, nota):
        self.__id_student = id_student
        self.__id_materie = id_materie
        self.__nota = nota
        self.__nume_student = ""
        self.__nume_materie = ""

    def get_id_student(self):
        return self.__id_student

    def get_id_materie(self):
        return self.__id_materie

    def get_nota(self):
        return self.__nota

    def get_nume_student(self):
        return self.__nume_student

    def set_nume_student(self, nume_student):
        self.__nume_student = nume_student

    def get_nume_materie(self):
        return self.__nume_materie

    def set_nume_materie(self, nume_materie):
        self.__nume_materie = nume_materie

    def __str__(self):
        return f"Nota {self.__nota} la {self.__nume_materie} pentru {self.__nume_student}"
