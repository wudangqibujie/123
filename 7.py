import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Start reading database')
# read database here
a="as"
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.info('Updating records ..%s.'%a)
# update records here
print(records)

logger.info('Finish updating records')