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
    if ip_response[0][0] == "!done":
      ipExists = False
      ip_id = ""
    else:
      if self.ip_address == ip_response[0][1]["address"]:
        ipExists = True
        ip_id = ip_response[0][1][".id"]
      else:
        ipExists = False
        ip_id = ""
    return ipExists, ip_id

  def ip_address_remove(self, ip_id):
    ip_id = ip_id
    self.api.talk([
        b'/ip/address/remove',
        b'=.id=' + ip_id])

  def ip_address_add(self, interface_name, comment):
    interface = interface_name
    comment = comment

    self.api.talk([
        b'/ip/address/add',
        b'=address=' + self.ip_address,
        b'=interface=' + interface,
        b'=comment=' + comment])
