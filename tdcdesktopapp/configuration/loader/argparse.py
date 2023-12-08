import argparse

from tdcdesktopapp.configuration.loader.abstract import AbstractConfigurationLoader


class ArgparseConfigurationLoader(AbstractConfigurationLoader):
    def load(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--show-css-editor', '-c', action='store_true')
        parser.add_argument('--persistence', '-p', required=True)
        args = parser.parse_args()

        self.show_css_editor = args.show_css_editor
        self.persistence_name = args.persistence