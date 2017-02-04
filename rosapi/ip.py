#!/usr/bin/env python


class IP():
  def __init__(self, api, ip_address):
    self.ip_address = ip_address
    self.api = api

  def checkip(self):
    ipExists = False
    ip_response = self.api.talk([
        b'/ip/address/print',
        b'?=address=' +
        self.ip_address])
    print(ip_response)
    if self.ip_address == ip_response[0][1]["address"]:
      ipExists = True
    return ipExists

  def ip_address_remove(arg):
    pass

    def ip_address_add(arg):
      pass
