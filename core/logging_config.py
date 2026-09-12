import logging
from pathlib import Path

from rich.logging import RichHandler

#switch case com os niveis
def setup_logging(console_level=logging.DEBUG, log_file=None
) -> logging.Logger:
    match console_level:
        case "DEBUG":
            console_level = logging.DEBUG
        case "INFO":
            console_level = logging.INFO
        case "ERROR":
            console_level = logging.ERROR
        case "WARNING":
            console_level = logging.WARNING

    logger = logging.getLogger("merge_sort")
    logger.setLevel(console_level)
    logger.handlers.clear()
    logger.propagate = False

    console_handler = RichHandler(
        level=console_level,
        rich_tracebacks=True,
        show_time=True,
    )

    console_handler.setFormatter(
        logging.Formatter("%(message)s")
    )

    logger.addHandler(console_handler)

    if log_file:
        path = Path(log_file)
        path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = logging.FileHandler(
            path,
            encoding="utf-8",
        )

        file_handler.setLevel(logging.DEBUG)

        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)-8s | "
                "%(name)s | %(filename)s:%(lineno)d | %(message)s"
            )
        )

        logger.addHandler(file_handler)

    return logger