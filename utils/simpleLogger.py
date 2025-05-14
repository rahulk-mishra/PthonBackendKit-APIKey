from abc import ABC, abstractmethod
from typing import Any
import logging
from logging.handlers import RotatingFileHandler

class Logger(ABC):
    @abstractmethod
    def info(self, message: Any = None) -> 'Logger' | Any:
        pass

    @abstractmethod
    def error(self, message: Any = None) -> 'Logger' | Any:
        pass


class SimpleLogger(Logger):
    def __init__(self, is_logger_disabled, logger: Logger = None):
        if logger is not None:
            self.logger = logger
        else:
            self.logger = logging.getLogger("Merchant")
            self.logger.setLevel(logging.INFO)

            if not self.logger.handlers:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.INFO)

                file_handler = RotatingFileHandler('file.log', maxBytes=2 * 1024 * 1024, backupCount=5)
                file_handler.setLevel(logging.INFO)

                formatter = logging.Formatter('Merchant : %(asctime)s - %(levelname)s - %(message)s')
                console_handler.setFormatter(formatter)
                file_handler.setFormatter(formatter)

                self.logger.addHandler(console_handler)
                self.logger.addHandler(file_handler)
        self.disable_logger = is_logger_disabled

    def info(self, message: any = None) -> Logger | None:
        if not self.disable_logger and self.logger:
            self.logger.info(message)
        return self.logger

    def error(self, message: any = None) -> Logger | None:
        if not self.disable_logger and self.logger:
            self.logger.error(message)
        return self.logger

