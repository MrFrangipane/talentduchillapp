import argparse

from tdcdesktopapp.core.configuration.abstract_loader import AbstractConfigurationLoader, ConfigurationDataclass


class ArgparseConfigurationLoader(AbstractConfigurationLoader):
    def load(self) -> ConfigurationDataclass:
        parser = argparse.ArgumentParser()
        parser.add_argument('--auth0-configuration', '-a')
        parser.add_argument('--api-host', '-s')
        parser.add_argument('--no-auth', '-n', action='store_true')
        parser.add_argument('--persistence', '-p', required=True)
        parser.add_argument('--show-css-editor', '-c', action='store_true')
        args = parser.parse_args()

        return ConfigurationDataclass(
            api_host=args.api_host,
            no_auth=args.no_auth,
            auth0_configuration=args.auth0_configuration,
            persistence_name=args.persistence,
            show_css_editor=args.show_css_editor
        )
