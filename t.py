import sys
import time


import logging

import logger


def main(entries=50000):
  my_handler = logger.ZmqHandler('tcp://127.0.0.1:5000')

  LOG = logging.getLogger(__name__)
  LOG.setLevel(logging.DEBUG)
  LOG.addHandler(my_handler)

  start = time.time()
  for i in range(entries):
    LOG.warn('OH MY FRICKIN GAWD %s', i)
  end = time.time()
  #print (end - start) / 1000
  print 'Elapsed: %.4fs' % (end - start)
  print 'Entries/s: %.4f' % (entries / (end - start))


if __name__ == '__main__':
  main(int(sys.argv[1]))
