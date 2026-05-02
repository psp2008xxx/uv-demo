# python
"""
Module providing a simple logger factory that ensures consistent log formatting
including datetime. Use `ApiLogger.get_logger(name, level, logfile, enable_stream)`
to obtain a configured logger instance.

Example:
    from utils.logger import ApiLogger
    logger = ApiLogger.get_logger(__name__, logfile='app.log', enable_stream=False)
    logger.info('Started')
"""

import logging
import os
from typing import Optional


class ApiLogger:
    """
    ApiLogger configures and returns Python logger instances with a consistent
    format that includes datetime.

    The default format is:
        %(asctime)s - %(levelname)s - %(name)s - %(message)s

    Date format defaults to: %Y-%m-%d %H:%M:%S

    Handlers are managed idempotently: calling `get_logger` multiple times will
    not add duplicate handlers. You can enable or disable the stream (console)
    handler via the `enable_stream` parameter.
    """

    DEFAULT_FORMAT: str = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    DEFAULT_DATEFMT: str = "%Y-%m-%d %H:%M:%S"

    @staticmethod
    def _has_stream_handler(logger: logging.Logger) -> bool:
        return any(isinstance(h, logging.StreamHandler) for h in logger.handlers)

    @staticmethod
    def _remove_stream_handlers(logger: logging.Logger) -> None:
        for h in list(logger.handlers):
            if isinstance(h, logging.StreamHandler):
                logger.removeHandler(h)
                try:
                    h.close()
                except Exception:
                    pass

    @staticmethod
    def _has_file_handler_for(logger: logging.Logger, filepath: str) -> bool:
        abspath = os.path.abspath(filepath)
        for h in logger.handlers:
            if isinstance(h, logging.FileHandler):
                # FileHandler exposes baseFilename
                try:
                    if os.path.abspath(getattr(h, "baseFilename", "")) == abspath:
                        return True
                except Exception:
                    continue
        return False

    @staticmethod
    def get_logger(name: Optional[str] = None,
                   level: int = logging.INFO,
                   logfile: Optional[str] = None,
                   enable_stream: bool = True) -> logging.Logger:
        """
        Return a configured logger.

        Parameters:
            name: Optional logger name (use __name__ from caller).
            level: Logging level (default: logging.INFO).
            logfile: Optional file path to also write logs to a file.
            enable_stream: If True, ensure a stream (console) handler is attached.
                           If False, remove any existing stream handlers.

        Returns:
            logging.Logger: Configured logger instance.
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)

        formatter = logging.Formatter(ApiLogger.DEFAULT_FORMAT, datefmt=ApiLogger.DEFAULT_DATEFMT)

        # Manage stream handler according to enable_stream flag
        if enable_stream:
            if not ApiLogger._has_stream_handler(logger):
                stream_handler = logging.StreamHandler()
                stream_handler.setLevel(level)
                stream_handler.setFormatter(formatter)
                logger.addHandler(stream_handler)
        else:
            # remove any existing stream handlers
            if ApiLogger._has_stream_handler(logger):
                ApiLogger._remove_stream_handlers(logger)

        # Optional file handler: add if logfile provided and not already added
        if logfile:
            try:
                if not ApiLogger._has_file_handler_for(logger, logfile):
                    file_handler = logging.FileHandler(logfile, encoding="utf-8")
                    file_handler.setLevel(level)
                    file_handler.setFormatter(formatter)
                    logger.addHandler(file_handler)
            except Exception:
                # If file handler cannot be created, do not raise to avoid breaking caller;
                # caller can handle absence of file logging.
                pass

        # Do not propagate to root logger to avoid duplicate output
        logger.propagate = False

        return logger
