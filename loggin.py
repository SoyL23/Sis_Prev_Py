import logging

class Logger:
    def __init__(self):
        self.logger = logging.getLogger("VECTORES")
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)
        self.logger.setLevel(logging.DEBUG)
        
        self.logger.propagate = True
        self.formater = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"
        )
        
        self.logs_info = logging.FileHandler("./app/logs/logs_info.txt")
        self.logs_info.setLevel(logging.INFO)
        self.logs_info.addFilter(lambda record: record.levelno == logging.INFO)
        self.logs_info.setFormatter(self.formater)
        
        self.logs_error = logging.FileHandler("./app/logs/logs_errors.txt")
        self.logs_error.setLevel(logging.ERROR)
        self.logs_error.addFilter(lambda record: record.levelno == logging.ERROR)
        self.logs_error.setFormatter(self.formater)
        
        self.logs_warnings = logging.FileHandler("./app/logs/logs_warnings.txt")
        self.logs_warnings.setLevel(logging.WARNING)
        self.logs_warnings.addFilter(lambda record: record.levelno == logging.WARNING)
        self.logs_warnings.setFormatter(self.formater)
        
        self.console_handler.setFormatter(self.formater)
        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.logs_info)
        self.logger.addHandler(self.logs_error)
        self.logger.addHandler(self.logs_warnings)


LOGGER = Logger().logger


