#!/usr/bin/python
# -*- coding: utf-8 -*-

from junipercrypt import junipercrypt

class FilterModule(object):
    def filters(self):
        return {
            'juniper_encrypt': self.juniper_encrypt
        }

    def juniper_encrypt(self, hash):
        return junipercrypt.encrypt(hash)
