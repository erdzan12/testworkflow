import requests
import sys
las2peerClass = ""
las2peerName = ""
las2peerVersion = ""
with open("gradle.properties") as myfile:
    for line in myfile:
        name, var = line.partition("=")[::2]
        if(name == "service.class"):
            print(name, var)
            las2peerClass = var
            las2peerClass = las2peerClass.replace('\n', '')
        if(name == "service.name"):
            print(name, var)
            las2peerName = var
            las2peerName = las2peerName.replace('\n', '')
        if(name == "service.version"):
            print(name, var)
            las2peerVersion = var
            las2peerVersion = las2peerVersion.replace('\n', '')

multipart_form_data = {
    'jarfile': (las2peerName + '-'+las2peerVersion+'.jar', open('export/jars/'+las2peerName+'-'+las2peerVersion+'.jar', 'rb')),
    'supplement': '{"class":"' + las2peerClass + '","name":"'+las2peerClass+'","description":"","vcsUrl":"","frontendUrl":"/akg"}'

}

cookies = {'sessionid': sys.argv[1]}

print(multipart_form_data)
response = requests.post('https://cae-dev.tech4comp.dbis.rwth-aachen.de/las2peer/services/upload',
                         files=multipart_form_data, cookies=cookies)

print(response.content)
