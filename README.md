----------------------------------------------------------------------
Esta é uma versão modificada do ZSI. Tais modificações foram iniciadas
em 02/10/2008 e foram feitas por Ruhan Bidart <ruhanbidart@gmail.com>

update: 01/10/2011 Rafael Quintela
Alterado parte do código que causava erro ao trocar o nome de algumas tags.

----------------------------------------------------------------------

The Zolera SOAP Infrastructure
==============================

ZSI, the Zolera SOAP Infrastructure, is a pure-Python module that
provides an implementation of SOAP messaging, as described in SOAP 1.1
Specification (see http://www.w3.org/TR/soap).  It can also be used to
build applications using SOAP Messages with Attachments (see
http://www.w3.org/TR/SOAP-attachments).  ZSI is intended to make it
easier to write web services in Python.

In particular, ZSI parses and generates SOAP messages, and converts
between native Python datatypes and SOAP syntax. Simple dispatch and
invocation methods are supported.  There are no known bugs.  It's only
known limitation is that it cannot handle multi-dimensional arrays.

ZSI is built on top of DOM.  It requires Python 2.3 or later, and PyXML
0.8.3 or later.  It is open source.  We hope you find it useful.

The ZSI.twisted package will only be built if you're using Python >= 2.4,
and in order to use it you'll need twisted >= 2.0 and twistedWeb >= 0.5.0


The documentation (in PDF and HTML) is accurate.  We should probably
restructure the document as a HOWTO.  You probably can't usefully edit
the docs without having the Python2.0 sources and some other utilities
(TeX, pdfLaTeX, latex2html) on a Unix or Cygwin installation.  If you
want to format or revise the docs, see "Documentation Tools" in the
file RELEASE.

    /rich $alz
    rsalz@datapower.com

Things To Do
------------

Any volunteers?

- Use isinstance() for types.

- Update to SOAPv1.2.
