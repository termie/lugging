import json
import logging

import zmq


class ZmqHandler(logging.Handler):
  def __init__(self, address):
    logging.Handler.__init__(self)
    self.address = address
    self._sock = None

  @property
  def socket(self):
    if not self._sock:
      zctx = zmq.Context()
      self._sock = zctx.socket(zmq.DEALER)
      self._sock.connect(self.address)
    return self._sock


  def emit(self, record):
    message = {'message': record.getMessage(),
               #'asctime': record.asctime,
               'name': record.name,
               'msg': record.msg,
               'args': record.args,
               'levelname': record.levelname,
               'levelno': record.levelno,
               'pathname': record.pathname,
               'filename': record.filename,
               'module': record.module,
               'lineno': record.lineno,
               'funcname': record.funcName,
               'created': record.created,
               'msecs': record.msecs,
               'relative_created': record.relativeCreated,
               'thread': record.thread,
               'thread_name': record.threadName,
               'process_name': record.processName,
               'process': record.process,
               'exc_info': record.exc_info}

    self.socket.send_multipart(['add', json.dumps(message)])
