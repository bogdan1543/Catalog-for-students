from random import choice, random, randint
from domain.student import Student

class RepoStudent:
    def __init__(self):
        self._studenti = {}

    def __len__(self):
        return len(self._studenti)

    def clear_list(self):
        self._studenti = {}

    def adauga_student(self, student):
        id_student = student.get_id_student()
        if id_student in self._studenti:
            raise Exception("Exista deja un student cu acelasi id!\n")

        self._studenti[id_student] = student
        return self._studenti

    def sterge_student(self, id_student):
        if id_student not in self._studenti:
            raise Exception("Nu exista un student cu acest id")
        del self._studenti[id_student]
        return self._studenti

    def modifica_student(self, student):
        if student.get_id_student() not in self._studenti:
            raise Exception("Nu exista un student cu acest id")
        self._studenti[student.get_id_student()] = student
        return self._studenti

    def cauta_student(self, id_student):
        if id_student not in self._studenti:
            raise Exception("Nu exista un student cu acest id")
        return self._studenti[id_student]

    def genereaza_student_mem(self, nr):
        '''
        Caz favorabil O(1)
        Caz nefavorabil O(nr)
        Complexitate O(n)
        Genereaza studenti recursiv
        :param nr: numarul de generari
        :return: lista de studenti generati
        '''
        if nr == 0:
            return self._studenti
        name = ["Bogdan Macovei", "George Enescu", "Lucian Blaga", "Mihai Eminescu"]
        random_name = choice(name)
        random_id = randint(1, 100)
        if random_id not in self._studenti:
            student = Student(random_id, random_name)
            self._studenti[random_id] = student

        return self.genereaza_student_mem(nr-1)

    def get_all_studenti(self):
        return [self._studenti[x] for x in self._studenti.keys()]

class FileRepoStudent(RepoStudent):
    def __init__(self, file_path_student):
        self.__file_path_student = file_path_student
        RepoStudent.__init__(self)

    def __len__(self):
        return RepoStudent.__len__(self)

    def __citeste_fisier(self):
        with open(self.__file_path_student, "r") as f:
            self._studenti.clear()
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                parti = line.split(";")
                id_student = int(parti[0])
                nume = parti[1]
                student = Student(id_student, nume)
                self._studenti[id_student] = student

    def __scrie_in_fisier(self):
        with open(self.__file_path_student, "w") as f:
            studenti = RepoStudent.get_all_studenti(self)
            for student in studenti:
                input = str(student.get_id_student()) + ";" + str(student.get_nume())
                f.write(input + "\n")

    def adauga_student(self, studentt):
        self.__citeste_fisier()
        RepoStudent.adauga_student(self, studentt)
        self.__scrie_in_fisier()

    def cauta_student(self, id_student):
        self.__citeste_fisier()
        return RepoStudent.cauta_student(self, id_student)

    def sterge_student(self, id_student):
        self.__citeste_fisier()
        RepoStudent.sterge_student(self, id_student)
        self.__scrie_in_fisier()

    def modifica_student(self, student):
        self.__citeste_fisier()
        RepoStudent.modifica_student(self, student)
        self.__scrie_in_fisier()

    def genereaza_student(self, nr):
        self.__citeste_fisier()
        RepoStudent.genereaza_student_mem(self, nr)
        self.__scrie_in_fisier()

    def get_all_studenti(self):
        self.__citeste_fisier()
        return RepoStudent.get_all_studenti(self)