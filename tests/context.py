import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
import sys, os

logger.info('Start importing context')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import src
logger.info('Finished import context')
