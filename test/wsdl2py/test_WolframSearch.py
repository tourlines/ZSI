#!/usr/bin/env python
# -*- coding: utf-8 -*

############################################################################
# Joshua R. Boverhof, LBNL
# See LBNLCopyright for copyright notice!
###########################################################################
import sys, unittest
from ServiceTest import main, ServiceTestCase, ServiceTestSuite, TestException
from ZSI.schema import ElementDeclaration, GED
from ZSI import ParsedSoap

"""

WSDL: 

"""
# General targets
def dispatch():
    """Run all dispatch tests"""
    suite = ServiceTestSuite()
    suite.addTest(unittest.makeSuite(TestCase, 'test_dispatch'))
    return suite

def local():
    """Run all local tests"""
    suite = ServiceTestSuite()
    suite.addTest(unittest.makeSuite(TestCase, 'test_local'))
    return suite

def net():
    """Run all network tests"""
    suite = ServiceTestSuite()
    suite.addTest(unittest.makeSuite(TestCase, 'test_net'))
    return suite
    
def all():
    """Run all tests"""
    suite = ServiceTestSuite()
    suite.addTest(unittest.makeSuite(TestCase, 'test_'))
    return suite


class TestCase(ServiceTestCase):
    """Test case for WolframSearch
    """
    name = "test_WolframSearch"
    client_file_name = "WolframSearchService_services"
    types_file_name  = "WolframSearchService_services_types"
    server_file_name = "WolframSearchService_services_server"

    def __init__(self, methodName):
        ServiceTestCase.__init__(self, methodName)
        self.wsdl2py_args.append('-b')

    def test_local_import(self):
        wsreq = self.client_module.WolframSearchRequest() 

    def test_net_search(self):
        loc = self.client_module.WolframSearchServiceLocator()
        port = loc.getWolframSearchmyPortType(**self.getPortKWArgs())

        msg = self.client_module.WolframSearchRequest() 

        opts = msg.new_Options() 
        msg.Options = opts 
        opts.Query = 'Newton'
        opts.set_element_Limit(10) 

        rsp = port.WolframSearch(msg)
        self.failUnless(rsp.Result.SearchTime > 0, 'expecting a search time >0')

    def test_dispatch_search(self):
        loc = self.client_module.WolframSearchServiceLocator()
        port = loc.getWolframSearchmyPortType(**self.getPortKWArgs())

        msg = self.client_module.WolframSearchRequest() 

        opts = msg.new_Options() 
        msg.Options = opts 
        opts.Query = 'Newton'
        opts.set_element_Limit(10) 

        rsp = port.WolframSearch(msg)
        self.failUnless(rsp.Result.SearchTime > 0, 'expecting a search time >0')



if __name__ == '__main__':
    main()
