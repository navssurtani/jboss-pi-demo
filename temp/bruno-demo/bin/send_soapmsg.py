#!usr/bin/env/python
import httplib
import urllib
import xml.dom.minidom

#-------SETTINGS-------
HOST = 'localhost:8080'
URL = '/jboss-as-helloworld-mdb/JMSService'
httplib.HTTPConnection.debuglevel = 0
#----------------------

def _SOAP_post(SOAPAction,xml):
    """Handles making the SOAP request"""
    h = httplib.HTTPConnection(HOST)
    headers={
	'Host':HOST,
	'Content-Type':'text/xml; charset=utf-8',
	'Content-Length':len(xml),
	'SOAPAction':'"%s"' % SOAPAction,
	}
    h.request ('POST', URL, body=xml,headers=headers)
    r = h.getresponse()
    d = r.read()
    if r.status!=200:
	raise ValueError('Error connecting: %s, %s' % (r.status, r.reason))
    return d

def _notify(textMessage):
     in_xml="""\
	<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:jms="http://org.jboss.ws/samples/jmstransport">
   <soapenv:Header/>
   <soapenv:Body>
      <jms:notifyEndpoint>
         <arg0>%s</arg0>
      </jms:notifyEndpoint>
   </soapenv:Body>
</soapenv:Envelope>""" %(textMessage)
     result_xml=_SOAP_post("",in_xml)
     return result_xml


if __name__=='__main__':
    token=_notify('This message is sent from python client')
    print token
