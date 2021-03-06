#!/usr/bin/env python
############################################################################
# Joshua R. Boverhof, LBNL
# See LBNLCopyright for copyright notice!
###########################################################################
import sys
from ZSI.ServiceContainer import AsServer
from EchoWSAddr200403Server_services_server import EchoWSAddr200403Server as EchoServer
from ZSI.schema import GTD

"""
EchoServer example service

WSDL:  ../../samples/Echo/Echo.wsdl

"""

EndpointReferenceType = GTD('http://schemas.xmlsoap.org/ws/2004/03/addressing','EndpointReferenceType')


class WSAService(EchoServer):
    def wsa_Echo(self, ps, addr):
        response = EchoServer.wsa_Echo(self, ps, addr)
        response.EchoResult = self.request.EchoIn

        if isinstance(response.EchoResult, EndpointReferenceType):
            addr1 = response.EchoResult
            for a in addr.Any:
                if a not in addr1.ReferenceProperties.Any:
                    raise RuntimeError, 'EPRs dont match'

        return response


if __name__ == "__main__" :
    port = int(sys.argv[1])
    AsServer(port, (WSAService('test'),))
