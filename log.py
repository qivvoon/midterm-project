import logging
from asyncio.log import logger

usual_log = logging.getLogger("usual_log")
unusual_log = logging.getLogger("unusual_log")

format = logging.Formatter("%(name)s__  %(message)s")

usual_handler = logging.FileHandler('usual_log_file', mode = "a", encoding = None, delay = False, errors = None) 
unusual_handler = logging.FileHandler('unusual_log_file', mode = "a", encoding = None, delay = False, errors = None)

usual_handler.setLevel(logging.ERROR)
unusual_handler.setLevel(logging.ERROR)

usual_handler.setFormatter(format)
unusual_handler.setFormatter(format)

usual_log.addHandler(usual_handler)
unusual_log.addHandler(unusual_handler)