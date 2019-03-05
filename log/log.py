import hashlib
from setting import setting
from logging import config, getLogger

config.dictConfig(setting.LOGGING)
logger = getLogger(__name__)


logger.info("test")
