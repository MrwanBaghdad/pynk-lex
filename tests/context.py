import logging
logging.basicConfig(level=logging.DEBUG,format='%(levelname)s:%(name)s:%(filename)s %(message)s')
logger = logging.getLogger(__name__)
import sys, os

logger.info('Start importing context')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import src
logger.info('Finished import context')
