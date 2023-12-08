from tdcdesktopapp.configuration.singleton import ConfigurationSingleton
from tdcdesktopapp.projects.model import Project


def get_all():
    return ConfigurationSingleton().expense_persistence.get_all()


def get_all_for_project(project: Project):
    return ConfigurationSingleton().expense_persistence.get_all_for_project(project)
