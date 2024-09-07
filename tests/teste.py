from utils.sortari import *
from domain.nota import Nota
from domain.student import *
from domain.materie import *


class Teste:
    def __init__(self, service_student, service_materie, service_nota, repo_student, repo_materie, repo_nota):
        self.__service_student = service_student
        self.__service_discipline = service_materie
        self.__service_nota = service_nota
        self.__repo_student = repo_student
        self.__repo_discipline = repo_materie
        self.__repo_nota = repo_nota

    def __test_create_student(self):
        id_student = 1
        name = "Bogdan Macovei"
        self.__student = Student(id_student, name)
        assert self.__student.get_id_student() == id_student
        assert self.__student.get_nume() == name

    def __test_create_materie(self):
        id_materie = 1
        nume = "FP"
        profesor = "Gelu Mihai"
        self.__materie = Materie(id_materie, nume, profesor)
        assert self.__materie.get_id_materie() == id_materie
        assert self.__materie.get_nume() == nume
        assert self.__materie.get_profesor() == profesor

    def __clear_lists(self):
        self.__repo_student.clear_list(self)
        self.__repo_discipline.clear_list(self)
        self.__repo_nota.clear_list(self)

    def __test_add_student(self):
        self.__clear_lists()
        id_student = 1
        name = "Bogdan Macovei"
        student = Student(id_student, name)
        self.__repo_student.adauga_student(student)
        student_found = self.__repo_student.cauta_student(id_student)

        assert id_student == student_found.get_id_student()
        assert name == student_found.get_nume()

    def __test_delete_student(self):
        self.__clear_lists()
        id_student = 4
        name = "Bogdan Macovei"
        student = Student(id_student, name)
        self.__repo_student.adauga_student(student)
        self.__repo_student.sterge_student(id_student)

        assert len(self.__repo_student.get_all_studenti()) == 0

    def __test_update_student(self):
        self.__clear_lists()
        id_student = 1
        name = "Bogdan Macovei"
        new_name = "Gelu Enache"
        student = Student(id_student, name)
        new_student = Student(id_student, new_name)

        self.__repo_student.adauga_student(student)
        self.__repo_student.modifica_student(new_student)
        new_student = self.__repo_student.cauta_student(id_student)

        assert new_student.get_id_student() == id_student
        assert new_student.get_nume() == new_name

    def __test_create_nota(self):
        id_nota = 1
        nota = 10
        self.__nota = Nota(id_nota, nota, self.__student.get_id_student(), self.__materie.get_id_materie())

        assert self.__nota.get_id_nota() == id_nota
        assert self.__nota.get_nota() == nota
        assert self.__nota.get_id_student() == self.__student.get_id_student()
        assert self.__nota.get_id_materie() == self.__materie.get_id_materie()

    def __test_add_nota(self):
        id_nota = 1
        nota = 10
        id_student = self.__student.get_id_student()
        id_materie = self.__materie.get_id_materie()
        self.__nota = Nota(id_nota, nota, id_student, id_materie)

        self.__repo_nota.adauga_nota(self.__nota)
        nota_gasita = self.__repo_nota.cauta_nota(id_nota)

        assert id_nota == nota_gasita.get_id_nota()
        assert nota == nota_gasita.get_nota()
        assert id_student == nota_gasita.get_id_student()
        assert id_materie == nota_gasita.get_id_materie()

    def __test_delete_nota(self):
        id_nota = 1
        nota = 10
        id_student = self.__student.get_id_student()
        id_materie = self.__materie.get_id_materie()
        self.__nota = Nota(id_nota, nota, id_student, id_materie)

        self.__repo_nota.adauga_nota(self.__nota)
        self.__repo_nota.sterge_nota(id_nota)

        assert len(self.__repo_nota.get_all_note()) == 0

    def __test_update_nota(self):
        id_nota = 1
        nota = 10
        id_student = self.__student.get_id_student()
        id_materie = self.__materie.get_id_materie()
        nota_noua = 9
        self.__nota = Nota(id_nota, nota, id_student, id_materie)
        self.__repo_nota.adauga_nota(self.__nota)

        nota_modificata = Nota(id_nota, nota_noua, id_student, id_materie)
        self.__repo_nota.modifica_nota(nota_modificata)

        assert nota_noua == nota_modificata.get_nota()

    """ def __test_delete_all_note_from_student(self):
        temp_list = {}
        id_nota = 1
        nota = 10
        nota = Note(self.__student, self.__materie, id_nota, nota)
        temp_list[1] = nota

        for id_nota in temp_list:
            if temp_list[id_nota].get_student() == self.__student:
                temp_list.pop(id_nota)
                break
        self.__repo_nota.add_nota(self,nota)
        list = self.__repo_nota.delete_all_note_from_student(self,self.__student)

        assert list == temp_list

        list.clear()

    def __test_delete_all_note_from_discipline(self):
        temp_list = {}
        id_nota = 1
        nota = 10
        nota = Note(self.__student, self.__materie, id_nota, nota)
        temp_list[1] = nota

        for id_nota in temp_list:
            if temp_list[id_nota].get_discipline() == self.__materie:
                temp_list.pop(id_nota)
                break
        self.__repo_nota.add_nota(self,nota)
        list = self.__repo_nota.delete_all_note_from_discipline(self, self.__materie)

        assert list == temp_list

        list.clear()


    def __test_add_discipline(self):
        temp_list = {}
        self.__clear_lists()
        id_discipline = 1
        name = "Informatica"
        profesor = "Mihai Popescu"
        discipline = Discipline(id_discipline, name, profesor)
        temp_list[1] = discipline

        id_discipline2 = 2
        name2 = "geografie"
        profesor2 = "George Ionut"
        discipline2 = Discipline(id_discipline2, name2, profesor2)
        temp_list[2] = discipline2

        self.__repo_discipline.add_discipline(discipline)
        discipline_found = self.__repo_discipline.search_discipline(id_discipline)

        assert id_discipline == discipline.get_id_disciplina()
        assert name == discipline_found.get_nume()
        assert profesor == discipline_found.get_profesor()


    def __test_delete_discipline(self):
        temp_list = {}
        self.__clear_lists()
        id_discipline = 1
        name = "Informatica"
        profesor = "Mihai Popescu"
        discipline = Discipline(id_discipline, name, profesor)
        temp_list[1] = discipline

        id_discipline2 = 2
        name2 = "geografie"
        profesor2 = "George Ionut"
        discipline2 = Discipline(id_discipline2, name2, profesor2)
        temp_list[2] = discipline2

        for x in temp_list.keys():
            if id_discipline == temp_list[x].get_id_disciplina():
                temp_list.pop(x)
                break

        self.__repo_discipline.add_discipline(discipline)
        self.__repo_discipline.delete_discipline(id_discipline)

        assert len(self.__repo_discipline.get_all_disciplines()) == 0



    def __test_update_discipline(self):
        temp_list = {}
        id_discipline = 1
        name = "Informatica"
        new_name = "geografie"
        profesor = "Mihai Popescu"
        new_profesor = "George Ionut"
        discipline = Discipline(id_discipline, name, profesor)
        new_discipline = Discipline(id_discipline, new_name, new_profesor)
        temp_list[1] = discipline

        for x in temp_list.keys():
            if id_discipline == temp_list[x].get_id_disciplina():
                temp_list[x].set_nume_disciplina(new_name)
                temp_list[x].set_nume_disciplina(new_profesor)
        self.__repo_discipline.add_discipline(discipline)
        self.__repo_discipline.update_discipline(new_discipline)

        assert new_discipline.get_id_disciplina() == id_discipline
        assert new_discipline.get_nume() == new_name
        assert new_discipline.get_profesor() == new_profesor

        self.__clear_lists()

    """

    def cmp_test(self, x, y):
        if x[0] == y[0]:
            if x[1] > y[1]:
                return 1
            return 0
        elif x[0] > y[0]:
            return 1
        return 0

    def __test_bubble_sort(self):
        arr = [[1, 2], [6, 1], [2, 1], [3, 1], [1, 1], [4, 1]]
        arr = bubble_sort(arr, key=lambda arr: arr, cmp=lambda a, b: self.cmp_test(a, b))
        assert arr == [[1, 1], [1, 2], [2, 1], [3, 1], [4, 1], [6, 1]]

    def __test_shell_sort(self):
        arr = [[1, 2], [6, 1], [2, 1], [3, 1], [1, 1], [4, 1]]
        arr = shell_sort(arr, key=lambda arr: arr, cmp=lambda a, b: self.cmp_test(a, b))
        assert arr == [[1, 1], [1, 2], [2, 1], [3, 1], [4, 1], [6, 1]]

    def run_all_tests(self):
        self.__test_bubble_sort()
        self.__test_shell_sort()
        self.__test_create_student()
        self.__test_add_student()
        self.__test_delete_student()
        self.__test_update_student()
        self.__test_create_nota()
        self.__test_add_nota()
        self.__test_delete_nota()
        self.__test_update_nota()

