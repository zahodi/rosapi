#!/usr/bin/env python
import RosAPI

class MikInterface():
  def __init__(self, interface):
    self.path = interface

  def checkinterface():
    interface = RosAPI.talk([b'/interface/print', b"=.proplist=name,.id,type"])
    ####################################################
    # To Do:
    # * Verify that interface is present
    # * Only respond with the specific interface details
    #####################################################
    return interface
