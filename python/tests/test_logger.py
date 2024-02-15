from snippets.logger import logger


def test_logger():
  logger.info("This is a DEBUG statement")
  logger.debug("This is an INFO statement")
  logger.warn("This is a WARN statement")
  logger.error("This is an ERROR statement")