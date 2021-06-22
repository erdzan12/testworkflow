las2peerClass = ""
with open("gradle.properties") as myfile:
    for line in myfile:
        name, var = line.partition("=")[::2]
        if(name == "service.class"):
            print(name, var)
            las2peerClass = var
