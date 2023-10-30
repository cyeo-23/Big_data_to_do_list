"""This module contains the logger class and its configurations."""

import logging
import os


class LoggerConfigurations:
    """Configuration for the logger."""

    @staticmethod
    def get_logger(name=__name__):
        """Return a logger instance for the given name."""
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        project_root = os.path.dirname(os.path.dirname(
            os.path.abspath(__file__)))
        log_path = os.path.join(project_root, 'logs', 'debug.log')
        log_path_error = os.path.join(project_root, 'logs', 'error.log')
        print("project root", project_root)

        # Common formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Debug handler
        debug_file_handler = logging.FileHandler(log_path)
        debug_file_handler.setLevel(logging.DEBUG)
        debug_file_handler.setFormatter(formatter)
        logger.addHandler(debug_file_handler)

        # Error handler
        error_file_handler = logging.FileHandler(log_path_error)
        error_file_handler.setLevel(logging.ERROR)
        error_file_handler.setFormatter(formatter)
        logger.addHandler(error_file_handler)

        # Console handler for errors
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger


class Logger:
    """Class to log different levels of logs."""

    def __init__(self, name=__name__):
        """Initialize the logger with a specific name."""
        self.logger = LoggerConfigurations.get_logger(name)

    def log_error(self, msg):
        """Log an error message."""
        self.logger.error(msg)

    def log_debug(self, msg):
        """Log a debug message."""
        self.logger.debug(msg)

    def log_critical(self, msg):
        """Log a critical message."""
        self.logger.critical(msg)

# Test our logger
# if __name__ == "__main__":
#    log = Logger()
#    log.log_error("this is a test for error message")
#    log.log_debug("this is a test for debug message")
#    log.log_critical("this is a test for critical message")
