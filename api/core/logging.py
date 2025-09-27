import sys

from loguru import logger

_configured = False


def configure_logging() -> None:
	global _configured
	if _configured:
		return
	logger.remove()
	logger.add(sys.stdout, level="INFO", backtrace=False, diagnose=False)
	_configured = True
