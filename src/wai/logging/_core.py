import logging
import os
from typing import List, Any


LOGGING_DEBUG = "DEBUG"
LOGGING_INFO = "INFO"
LOGGING_WARN = "WARN"
LOGGING_WARNING = "WARNING"
LOGGING_ERROR = "ERROR"
LOGGING_CRITICAL = "CRITICAL"
LOGGING_FATAL = "FATAL"
LOGGING_LEVELS = [
    LOGGING_DEBUG,
    LOGGING_INFO,
    LOGGING_WARNING,
    LOGGING_ERROR,
    LOGGING_CRITICAL,
    LOGGING_FATAL,
]


SIMPLE_LOG_FORMAT = "%(levelname)s:%(name)s:%(message)s"

TIMESTAMP_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"


def str_to_logging_level(level: str) -> int:
    """
    Turns a logging level string into the corresponding integer constant.

    :param level: the level to convert
    :type level: str
    :return: the int level
    :rtype: int
    """
    level = level.upper()
    if level == LOGGING_WARN:
        level = LOGGING_WARNING
    if level not in LOGGING_LEVELS:
        raise Exception("Invalid logging level (%s): %s" % ("|".join(LOGGING_LEVELS), level))
    if level == LOGGING_CRITICAL:
        return logging.CRITICAL
    elif level == LOGGING_ERROR:
        return logging.ERROR
    elif level == LOGGING_WARNING:
        return logging.WARNING
    elif level == LOGGING_INFO:
        return logging.INFO
    elif level == LOGGING_DEBUG:
        return logging.DEBUG
    else:
        raise Exception("Unhandled logging level: %s" % level)


def logging_level_to_str(level: int) -> str:
    """
    Turns the logging level value into the corresponding string representation.

    :param level:
    :return:
    """
    if level == logging.DEBUG:
        return LOGGING_DEBUG
    elif level == logging.INFO:
        return LOGGING_INFO
    elif level == logging.WARNING:
        return LOGGING_WARNING
    elif level == logging.ERROR:
        return LOGGING_ERROR
    elif level == logging.CRITICAL:
        return LOGGING_CRITICAL
    elif level == logging.FATAL:
        return LOGGING_FATAL
    else:
        raise Exception("Unhandled logging level: %d" % level)


def init_logging(default_level: str = LOGGING_WARNING, env_var: str = None, stream: Any = None, handlers: List[Any] = None,
                 filename: str = None, filename_env_var: str = None,
                 log_format: str = SIMPLE_LOG_FORMAT, log_format_env_var: str = None):
    """
    Initializes the logging.

    :param default_level: the default level to use
    :type default_level: str
    :param env_var: the environment variable to check for a level (overrides the default level), ignored if None
    :type env_var: str
    :param stream: the stream to use, uses stderr if None (default: None); cannot be used together with 'filename'
    :param handlers: the explicit handlers to use
    :type handlers: list
    :param filename: the filename to log to, ignored if None (default: None); cannot be used together with 'stream'
    :type filename: str
    :param filename_env_var: the environment variable to specify the filename to redirect the logging output to, overrides 'filename' parameter, ignored if None
    :type filename_env_var: str
    :param log_format: the format string for the logging output
    :type log_format: str
    :param log_format_env_var: the environment variable that contains the logging format, overriding 'log_format' parameter, ignored if None
    :type log_format_env_var: str
    """
    level = str_to_logging_level(default_level)
    if env_var is not None:
        if os.getenv(env_var) is not None:
            level = str_to_logging_level(os.getenv(env_var))
    if filename_env_var is not None:
        if os.getenv(filename_env_var) is not None:
            filename = os.getenv(filename_env_var)
    if handlers is None:
        handlers = []
        if filename is not None:
            handlers.append(logging.FileHandler(filename))
        handlers.append(logging.StreamHandler(stream=stream))
    else:
        if stream is not None:
            raise Exception("Cannot specify 'handlers' and 'stream' together!")
        if filename is not None:
            raise Exception("Cannot specify 'handlers' and 'filename' together!")
    if log_format_env_var is not None:
        if os.getenv(log_format_env_var) is not None:
            log_format = os.getenv(log_format_env_var)
    logging.basicConfig(level=level, handlers=handlers, format=log_format)


def set_logging_level(logger: logging.Logger, level: str):
    """
    Sets the logging level of the logger.

    :param logger: the logger to update
    :type logger: logging.Logger
    :param level: the level string, see LOGGING_LEVELS
    :type level: str
    """
    logger.setLevel(str_to_logging_level(level))


def log(level: int = logging.INFO, msg: str = None, log_file: str = None, logger: logging.Logger = None):
    """
    Outputs the message to the log file and the logger instance.

    :param level: the level to use for logging
    :type level: int
    :param msg: the message to output
    :type msg: str
    :param log_file: the log file to append
    :type log_file: str
    :param logger: the logger instance
    :type logger: logging.Logger
    """
    if msg is None:
        return
    if logger is not None:
        if not logger.isEnabledFor(level):
            return

    if logger is not None:
        if level == logging.INFO:
            logger.info(msg)
        elif level == logging.DEBUG:
            logger.debug(msg)
        elif level == logging.WARNING:
            logger.warning(msg)
        elif level == logging.ERROR:
            logger.error(msg)
        elif level == logging.CRITICAL:
            logger.critical(msg)
        elif level == logging.FATAL:
            logger.fatal(msg)

    if log_file is not None:
        level_str = logging_level_to_str(level)
        try:
            with open(log_file, "a") as fp:
                fp.write(level_str + ":" + msg + "\n")
        except:
            msg = "Failed to write to log file: %s" % log_file
            if logger is None:
                print(msg)
            else:
                logger.error(msg)
