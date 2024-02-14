"""
Example printout:

[2024-02-14 13:24:13,188] [snippets] {test_logger.py:5} [INFO] This is a DEBUG statement
[2024-02-14 13:24:13,188] [snippets] {test_logger.py:6} [DEBUG] This is an INFO statement
[2024-02-14 13:24:13,188] [snippets] {test_logger.py:7} [WARNING] This is a WARN statement
[2024-02-14 13:24:13,188] [snippets] {test_logger.py:8} [ERROR] This is an ERROR statement
"""

import logging

_PREFIX = 'snippets'

logger = logging.getLogger(_PREFIX)
logger.setLevel(logging.DEBUG)
logger.propagate = False
if not logger.hasHandlers():
  ch = logging.StreamHandler()
  formatter = logging.Formatter(fmt='[%(asctime)s] [%(name)s] {%(filename)s:%(lineno)d} [%(levelname)s] %(message)s')
  ch.setFormatter(formatter)
  logger.addHandler(ch)