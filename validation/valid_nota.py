class ValidNota:
    def valid_nota_student(self, nota_student):
        erori = ""
        if nota_student.get_id_nota() <= 0:
            erori += "id invalid\n"
        if nota_student.get_nota() < 1 or nota_student.get_nota() > 10:
            erori += "nota invalida\n"
        if len(erori):
            raise Exception(erori)

    def valid_nota(self, nota):
        if nota < 1 or nota > 10:
            raise Exception("nota invalida\n")

    def valid_id_nota(self, id_nota):
        if id_nota <= 0:
            raise Exception("id invalid\n")