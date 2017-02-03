#!/usr/bin/env python


class Interface():
  def __init__(self, api, interface):
    self.interface_name = interface
    self.api = api

  def checkinterface(self):
    intExists = False
    interface = self.api.talk([
        b'/interface/print',
        b"?=name=" +
        self.interface_name])
    if self.interface_name == interface[0][1]['default-name']:
      intExists = True
    return intExists
