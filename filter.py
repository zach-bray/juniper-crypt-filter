#!/usr/bin/python
# -*- coding: utf-8 -*-

from juniperSNMPv3crypt import crypt9, snmpv3_hash

class FilterModule(object):
    def filters(self):
        return {
            'juniper_usm_crypt9': self.juniper_usm_crypt9
        }

    def juniper_usm_crypt9(self, passphrase, ipaddr, alg="sha1"):
    	engineid = snmpv3_hash.gen_engineid(ipaddr)
    	hashed = snmpv3_hash.derive_msg(passphrase, engineid, alg)
    	return crypt9.encrypt(hashed, seed=1337)
