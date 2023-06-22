class BackendDeveloper:
    def write_python(self):
        print("I am writing python code.")


class FrontendDeveloper:
    def write_javascript(self):
        print("I am writing javascript code.")


class Project:
    def __init__(
        self,
        backend_developer: BackendDeveloper,
        frontend_developer: FrontendDeveloper,
    ):
        self.backend_developer = backend_developer
        self.frontend_developer = frontend_developer

    def implement(self):
        self.backend_developer.write_python()
        self.frontend_developer.write_javascript()


project = Project(BackendDeveloper(), FrontendDeveloper())
project.implement()
