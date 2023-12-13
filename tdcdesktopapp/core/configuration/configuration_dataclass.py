from dataclasses import dataclass


@dataclass
class ConfigurationDataclass:
    api_host: str  # used by http implementations
    auth0_configuration_filepath: str  # used by http implementations
    no_auth: bool  # removes authentication (use for local development only)
    persistence_name: str  # defines if using http or ram implementations
    show_css_editor: bool
