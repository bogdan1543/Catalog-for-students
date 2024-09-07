class ValidMaterie:
    def valid_materie(self, materie):
        erori = ""
        if materie.get_id_materie() <= 0:
            erori += "id invalid\n"
        for word in materie.get_nume().split():
            if not word.isalpha():
                erori += "materie invalida\n"
        if len(materie.get_profesor().split()) < 2:
            erori += "nume profesor incomplet\n"
        for word in materie.get_profesor().split():
            if not word.isalpha():
                erori += "nume profesor invalid\n"

        if len(erori):
            raise Exception(erori)

    def valid_id_materie(self, id_materie):
        if id_materie <= 0:
            raise Exception("id invalid\n")

    def valid_nume(self, nume):
        for word in nume.split():
            if not word.isalpha():
                raise Exception("disciplina invalida\n")

    def valid_profesor(self, professor):
        if len(professor.split()) < 2:
            raise Exception("nume profesor incomplet\n")
        for word in professor.split():
            if not word.isalpha():
                raise Exception("nume profesor invalid\n")