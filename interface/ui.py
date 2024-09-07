class UI:
    def __init__(self, service_student, service_discipline, service_nota):
        self.__service_student = service_student
        self.__service_discipline = service_discipline
        self.__service_nota = service_nota
        self.__comands = {
            "add_student": self.__ui_add_student,
            "delete_student": self.__ui_delete_student,
            "update_student": self.__ui_update_student,
            "search_student": self.__ui_search_student,
            "generate_student": self.__ui_generate_student,
            "print_students": self.__ui_print_all_students,
            "add_discipline": self.__ui_add_discipline,
            "delete_discipline": self.__ui_delete_discipline,
            "update_discipline": self.__ui_update_discipline,
            "search_discipline": self.__ui_search_discipline,
            "generate_discipline": self.__ui_generate_discipline,
            "print_discipline": self.__ui_print_all_disciplines,
            "add_nota": self.__ui_add_nota,
            "delete_nota": self.__ui_delete_nota,
            "update_nota": self.__ui_update_nota,
            "print_note": self.__ui_print_all_note,
            "print_note_by_nota": self.__ui_print_all_note_by_nota_in_order,
            "print_note_by_name": self.__ui_print_all_note_by_name_in_order,
            "print_first_students": self.__ui_print_first_students,
        }

    def __ui_add_student(self, params):

        if len(params) < 2:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_student = int(params[0])
            nume = params[1]
        except:
            raise Exception("Valoare numerica ID invalida!\n")
        self.__service_student.service_adauga_student(id_student, nume)
        print(f"{nume} a fost adaugat!\n")

    def __ui_delete_student(self, params):
        if len(params) != 1:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_student = int(params[0])
        except:
            raise Exception("Valoare numerica ID invalida!\n")
        self.__service_nota.service_sterge_toate_notele_dupa_student(id_student)
        self.__service_student.service_sterge_student(id_student)
        print(f"Studentul cu id:{id_student} a fost sters!\n")

    def __ui_update_student(self, params):
        if len(params) < 2:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_student = int(params[0])
            new_name = params[1]
        except:
            raise Exception("Valoare numerica invalida!\n")
        self.__service_student.service_modifica_student(id_student, new_name)
        print(f"Studentul cu id:{id_student} a fost modificat!\n")

    def __ui_search_student(self, params):
        if len(params) != 1:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_student = int(params[0])
        except:
            raise Exception("Valoare numerica ID invalida!\n")
        student = self.__service_student.service_cauta_student(id_student)
        print(student, "\n")

    def __ui_print_all_students(self, params):
        students = self.__service_student.service_get_all_studenti()
        if not len(students):
            raise Exception("Lista de studenti invalida\n")
        for student in students:
            print(student)

    def __ui_generate_student(self, params):
        if len(params) != 1:
            raise Exception("Nr parametrii invalid!\n")
        try:
            nr = int(params[0])
        except:
            raise Exception("Valoare numerica NR invalida!\n")
        self.__service_student.service_genereaza_student(nr)

    def __ui_add_discipline(self, params):
        if len(params) < 3:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_disciplina = int(params[0])
            nume_disciplina = params[1]
            profesor = params[2]
        except:
            raise Exception("Valoare numerica ID invalida!\n")
        self.__service_discipline.service_adauga_materie(id_disciplina, nume_disciplina, profesor)
        print(f"Disciplina {nume_disciplina} a fost adaugata!\n")

    def __ui_delete_discipline(self, params):
        if len(params) != 1:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_disciplina = int(params[0])
        except:
            raise Exception("Valoare numerica ID invalida!\n")
        self.__service_nota.service_sterge_toate_notele_dupa_materie(id_disciplina)
        self.__service_discipline.service_sterge_materie(id_disciplina)
        print(f"Disciplina cu id:{id_disciplina} a fost stearsa!\n")

    def __ui_update_discipline(self, params):
        if len(params) < 3:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_discipline = int(params[0])
            new_discipline_name = params[1]
            new_profesor = params[2]
        except:
            raise Exception("Valoare numerica invalida!\n")
        self.__service_discipline.service_modifica_materie(id_discipline, new_discipline_name, new_profesor)
        print(f"Disciplina cu id:{id_discipline} a fost modificata!\n")

    def __ui_search_discipline(self, params):
        if len(params) != 1:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_disciplina = int(params[0])
        except:
            raise Exception("Valoare numerica ID invalida!\n")
        discipline = self.__service_discipline.service_cauta_materie(id_disciplina)
        print(discipline, "\n")

    def __ui_generate_discipline(self, params):
        if len(params) != 1:
            raise Exception("Nr parametrii invalid!\n")
        try:
            nr = int(params[0])
        except:
            raise Exception("Valoare numerica NR invalida!\n")
        self.__service_discipline.service_genereaza_materie(nr)

    def __ui_print_all_disciplines(self, params):
        disciplines = self.__service_discipline.service_get_all_materii()
        if not len(disciplines):
            raise Exception("Lista de studenti invalida\n")
        for discipline in disciplines:
            print(discipline)

    def __ui_add_nota(self, params):
        if len(params) != 4:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_nota = int(params[0])
            nota = int(params[1])
            id_student = int(params[2])
            id_disciplina = int(params[3])
        except:
            raise Exception("Valoare numerica invalida!\n")
        self.__service_nota.service_adauga_nota(id_nota, nota, id_student, id_disciplina)

    def __ui_delete_nota(self, params):
        if len(params) != 1:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_nota = int(params[0])
        except:
            raise Exception("Valoare numerica ID invalida!\n")
        self.__service_nota.service_sterge_nota(id_nota)
        print(f"Nota cu id:{id_nota} a fost stearsa!\n")

    def __ui_update_nota(self, params):
        if len(params) != 2:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_nota = int(params[0])
            new_nota = int(params[1])
        except:
            raise Exception("Valoare numerica invalida!\n")
        self.__service_nota.service_modifica_nota(id_nota, new_nota)
        print(f"Nota cu id:{id_nota} a fost modificata!\n")

    def __ui_print_all_note(self, params):
        note = self.__service_nota.service_get_all_note()
        if not len(note):
            raise Exception("Lista de note invalida\n")
        for nota in note:
            print(nota)

    def __ui_print_all_note_by_nota_in_order(self, params):
        if len(params) != 1:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_discipline = int(params[0])
        except:
            raise Exception("Valoare numerica invalida!\n")
        note = self.__service_nota.service_get_all_note_in_ordine_dupa_nota(id_discipline)
        for nota in note:
            print(nota)

    def __ui_print_all_note_by_name_in_order(self, params):
        if len(params) != 1:
            raise Exception("Nr parametrii invalid!\n")
        try:
            id_discipline = int(params[0])
        except:
            raise Exception("Valoare numerica invalida!\n")
        note = self.__service_nota.service_get_all_note_in_ordine_dupa_nume(id_discipline)
        for nota in note:
            print(nota)

    def __ui_print_first_students(self, params):
        medii = self.__service_nota.service_get_primii_studenti()
        for medie in medii:
            print(f"studentul {medie.get_nume_student()} cu media {medie.get_nota()} \n")

    def run(self):
        while True:
            try:
                cmd = input(">>>")
                cmd = cmd.strip()
                if cmd == "exit":
                    return
                parts = cmd.split(",")
                cmd_name = parts[0]
                params = parts[1:]
                if cmd_name in self.__comands:
                    self.__comands[cmd_name](params)
                else:
                    print("comanda invalida!")
            except KeyboardInterrupt:
                print("Ati oprit programul!")
                break
            except Exception as ex:
                print(f"Erori:{ex}")
#add_nota,1,9,1,1 add_nota,2,9,81,1 add_nota,3,8,84,1 add_nota,4,10,16,1 add_nota,5,9,16,4
'''print_note_by_nota: self.__ui_print_all_note_by_nota_in_order,
    print_note_by_name: self.__ui_print_all_note_by_name_in_order,
    print_first_students'''