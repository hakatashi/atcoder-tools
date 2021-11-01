import logging
import io

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")

stdout_handler = logging.StreamHandler()
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)

logger_io = io.StringIO()
string_handler = logging.StreamHandler(logger_io)
string_handler.setFormatter(formatter)
logger.addHandler(string_handler)
