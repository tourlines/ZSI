#!/usr/bin/env python
############################################################################
# Joshua R. Boverhof, LBNL
# See LBNLCopyright for copyright notice!
###########################################################################
import sys, time
from ZSI.ServiceContainer import AsServer
from WolframSearchService_services_server import WolframSearchService

"""
WolframSearch Service
"""


class Service(WolframSearchService):

    def soap_WolframSearch(self, ps):
        rsp = WolframSearchService.soap_WolframSearch(self, ps)
        msg = self.request

        t1 = time.time()
        opts = msg.Options

        rsp.Result = result = rsp.new_Result()
        if opts.Query == 'Newton':
            result.TotalMatches = 1
            result.Matches = match = result.new_Matches()
            item = match.new_Item()
            item.Title = "Fig Newtons"
            item.Score = 10
            item.URL = 'http://www.nabiscoworld.com/newtons/'
            match.Item = [item]

        result.SearchTime = time.time() - t1

        return rsp


if __name__ == "__main__" :
    port = int(sys.argv[1])
    AsServer(port, (Service('test'),))
