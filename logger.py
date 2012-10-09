import json
import logging

import zmq

class ZmqHandler(logging.Handler):
  def __init__(self, address):
    logging.Handler.__init__(self)
    self.address = address

  @property
  def socket(self):
    if not self._sock:
      zctx = zmq.Context()
      self._sock = zctx.socket(zmq.DEALER)
      self._sock.connect()
    return self._sock


  def emit(self, record):
    self.socket.send_multipart(['add', json.dumps(record)])
