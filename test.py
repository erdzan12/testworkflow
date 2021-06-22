import requests
import sys

multipart_form_data = {
    'jarfile': ('i5.las2peer.services.las2peerakg-1.0.5.jar', open('export/jars/i5.las2peer.services.las2peerakg-1.0.0.jar', 'rb')),
    'supplement': '{"class":"' + sys.argv[2] + '","name":"'+sys.argv[3]+'","description":"","vcsUrl":"","frontendUrl":"/akg"}'

}

cookies = {'sessionid': sys.argv[1]}

print(multipart_form_data)
response = requests.post('https://cae-dev.tech4comp.dbis.rwth-aachen.de/las2peer/services/upload',
                         files=multipart_form_data, cookies=cookies)

print(response.content)
