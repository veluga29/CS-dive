from abc import ABCMeta


class Developer(metaclass=ABCMeta):
    def develop(self):
        pass


class BackendDeveloper(Developer):
    def develop(self):
        self.write_python()

    def write_python(self):
        print("I am writing python code.")


class FrontendDeveloper(Developer):
    def develop(self):
        self.write_javascript()

    def write_javascript(self):
        print("I am writing javascript code.")


class AndroidDeveloper(Developer):
    def develop(self):
        self.write_kotlin()

    def write_kotlin(self):
        print("I am writing kotlin code.")


class Project:
    def __init__(self, developers: list[Developer]):
        self.developers = developers

    def implement(self):
        for developer in self.developers:
            developer.develop()


dev = [BackendDeveloper(), FrontendDeveloper(), AndroidDeveloper()]
project = Project(dev)
project.implement()
