from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        data = toml.loads(content)
        print(data)

        name = data["project"]["name"]
        description = data["project"]["description"]
        dependencies = [
           dependency.split(">=")[0]for dependency in data["project"]["dependencies"]
        ]
        dev_dependencies = [
            dependency.split(">=")[0] for dependency in data["dependency-groups"]["dev"]
        ]

        license = data["project"]["license"]

        authors = [ 
            author["name"] for author in data["project"]["authors"]
        ]



        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, license, authors)
