import argparse

from tdcdesktopapp.core.configuration.abstract_loader import AbstractConfigurationLoader


class ArgparseConfigurationLoader(AbstractConfigurationLoader):
    def load(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--auth0-configuration', '-a')
        parser.add_argument('--api-host', '-s')
        parser.add_argument('--persistence', '-p', required=True)
        parser.add_argument('--show-css-editor', '-c', action='store_true')
        args = parser.parse_args()

        self.api_host = args.api_host
        self.auth0_configuration = args.auth0_configuration
        self.persistence_name = args.persistence
        self.show_css_editor = args.show_css_editor
