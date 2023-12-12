import logging

from tdcdesktopapp.core.abstract_persistence_configuration import AbstractPersistenceConfiguration


_logger = logging.getLogger(__name__)


class RamPersistenceConfiguration(AbstractPersistenceConfiguration):

    def is_available(self) -> bool:
        return True
