""" class Logger: 
        - log_error: log an error
        - log_debug: log a debug
        - log_critical: log a critical
    class LoggerConfigurations:
        - get_logger: return a logger instance for the given name 
"""

import logging


class LoggerConfigurations:
    """Configuration for the logger"""

    @staticmethod
    def get_logger(name=__name__):
        """Return a logger instance for the given name"""
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # Common formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Debug handler
        debug_file_handler = logging.FileHandler('logs/debug.log')
        debug_file_handler.setLevel(logging.DEBUG)
        debug_file_handler.setFormatter(formatter)
        logger.addHandler(debug_file_handler)

        # Error handler
        error_file_handler = logging.FileHandler('logs/error.log')
        error_file_handler.setLevel(logging.ERROR) #Error is handling error and critical
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
        self.logger = LoggerConfigurations.get_logger(name)

    def log_error(self, msg):
        self.logger.error(msg)

    def log_debug(self, msg):
        self.logger.debug(msg)

    def log_critical(self, msg):
        self.logger.critical(msg)


#if __name__ == "__main__":
#    for testing purpose
#    log = Logger()
#    log.log_error("this is a test for error message")
#    log.log_debug("this is a test for debug message")
#    log.log_critical("this is a test for critical message")
