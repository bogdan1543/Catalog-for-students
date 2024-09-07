from repository.repo_student import RepoStudent, FileRepoStudent
from repository.repo_materie import RepoMaterie, FileRepoMaterie
from repository.repo_nota import RepoNota, FileRepoNota
from business.service_student import ServiceStudent
from business.service_nota import ServiceNota
from business.service_materie import ServiceMaterie
from validation.valid_student import ValidStudent
from validation.valid_nota import ValidNota
from validation.valid_materie import ValidMaterie
from interface.ui import UI
from tests.teste import Teste

if __name__ == '__main__':
    repo_student = FileRepoStudent("repository/studenti.txt")
    valid_student = ValidStudent()
    repo_materie = FileRepoMaterie("repository/materii.txt")
    valid_materie = ValidMaterie()
    repo_nota = FileRepoNota("repository/note.txt")
    valid_nota = ValidNota()
    service_student = ServiceStudent(repo_student, valid_student)
    service_materie = ServiceMaterie(repo_materie, valid_materie)
    service_nota = ServiceNota(repo_nota, valid_nota, repo_student, repo_materie)

    test_repo_student = RepoStudent
    test_repo_materie = RepoMaterie
    test_repo_nota = RepoNota
    test_service_student = ServiceStudent(test_repo_student, valid_student)
    test_service_materie = ServiceMaterie(test_repo_materie, valid_materie)
    test_service_nota = ServiceNota(test_repo_nota, valid_nota, test_repo_student, test_repo_materie)

    console = UI(service_student, service_materie, service_nota)

    tests = Teste(test_service_student, test_service_materie, test_service_nota, test_repo_student, test_repo_materie, test_repo_nota)
    #tests.run_all_tests()
    console.run()
