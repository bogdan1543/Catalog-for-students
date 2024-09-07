class ValidStudent:
    def valid_student(self, student):
        erori = ""
        if student.get_id_student() <= 0:
            erori += "id invalid\n"
        if len(student.get_nume().split()) < 2:
            erori += "nume incomplet\n"
        for word in student.get_nume().split():
            if not word.isalpha():
                erori += "nume invalid\n"
        if len(erori):
            raise Exception(erori)

    def valid_id_student(self, id_student):
        if id_student <= 0:
            raise Exception("id invalid\n")

    def valid_nume(self, nume):
        if len(nume.split()) < 2:
            raise Exception("nume incomplet\n")
        else:
            for word in nume.split():
                if not word.isalpha():
                    raise Exception("nume invalid\n")