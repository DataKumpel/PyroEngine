import logging
import pyray as pr


def setup_logging() -> logging.Logger:
    pr.set_trace_log_level(pr.TraceLogLevel.LOG_ERROR)
    logger = logging.getLogger("PYRO_ENGINE")
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_fmt = logging.Formatter("[{levelname}] {name}: {message}", style="{")
    console_handler.setFormatter(console_fmt)
    logger.addHandler(console_handler)
    return logger
