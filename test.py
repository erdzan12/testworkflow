import requests
multipart_form_data = {
    'jarfile': ('i5.las2peer.services.las2peerakg-1.0.5.jar', open('i5.las2peer.services.las2peerakg-1.0.5.jar', 'rb')),
    'supplement': '{"class":"akgService","name":"akgService","description":"","vcsUrl":"","frontendUrl":"/akg"}'
}
cookies = {'sessionid': 'c35m8r7hut3h3kgc4vs4v4paseirpercrij560h20id774ob645m'}

response = requests.post('https://cae-dev.tech4comp.dbis.rwth-aachen.de/ba-erdzan/las2peer/services/upload', files=multipart_form_data, cookies=cookies)

print(response.content)