import argparse

from ._core import LOGGING_LEVELS, LOGGING_WARN


def add_logging_level(parser: argparse.ArgumentParser, short_opt: str = "-l", long_opt: str = "--logging_level"):
    """
    Adds an option for the logging level to the parser.

    :param parser: the parser to append.
    :type parser: argparse.ArgumentParser
    :param short_opt: the short option flag to use (eg -l)
    :type short_opt: str
    :param long_opt: the long option flag to use (eg --logging_level)
    :type long_opt: str
    """
    parser.add_argument(short_opt, long_opt, choices=LOGGING_LEVELS, default=LOGGING_WARN,
                        help="The logging level to use.")


def add_logger_name(parser: argparse.ArgumentParser, short_opt: str = "-N", long_opt: str = "--logger_name"):
    """
    Adds an option for the logger name to the parser.

    :param parser: the parser to append.
    :type parser: argparse.ArgumentParser
    :param short_opt: the short option flag to use (eg -N)
    :type short_opt: str
    :param long_opt: the long option flag to use (eg --logger_name)
    :type long_opt: str
    """
    parser.add_argument(short_opt, long_opt, type=str, default=None,
                        help="The custom name to use for the logger", required=False)
