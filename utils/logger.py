import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name: str) -> logging.Logger:
    """
    Docstring for get_logger
    
    :param name: Description
    :type name: str
    :return: Description
    :rtype: Logger
    企业级日志封装
    -控制台 + 文件
    -自动滚动
    """

    logger =logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger
    
    os.makedirs("logs", exist_ok=True)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        "logs/app.log",
        maxBytes= 5 * 1024 * 1024,
        backupCount= 3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger