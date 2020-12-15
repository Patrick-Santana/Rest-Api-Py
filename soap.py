from zeep import Client  

client = Client('http://soapclient.com/xml/soapresponder.wsdl')
result = client.service.Method1(bsrtParam1='Olá tudo bem?', bsrtParam2= 'tudo e com vc?')

print (result)


