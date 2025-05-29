from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
import os

class Logger:
    _instance = None
    _initialized = False

    @staticmethod
    def get_logger(name):
        if not Logger._instance:
            logs_dir = "logs"
            os.makedirs(logs_dir, exist_ok=True)
            log_file = os.path.join(logs_dir, "automation.log")
            
            # Add run separator only once per program execution
            if not Logger._initialized:
                with open(log_file, 'a') as f:
                    separator = f"\n{'='*80}\n"
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"{separator}New Test Run Started at {timestamp}{separator}\n")
                Logger._initialized = True
            
            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)
            
            if not logger.handlers:
                file_handler = RotatingFileHandler(
                    log_file,
                    maxBytes=5 * 1024 * 1024,  # 5MB
                    backupCount=5
                )
                file_handler.setLevel(logging.DEBUG)
                
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.INFO)
                
                formatter = logging.Formatter(
                    "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S"
                )
                
                file_handler.setFormatter(formatter)
                console_handler.setFormatter(formatter)
                
                logger.addHandler(file_handler)
                logger.addHandler(console_handler)
            
            Logger._instance = logger
            
        return Logger._instance