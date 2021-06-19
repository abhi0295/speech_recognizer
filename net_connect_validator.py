from urllib import request

def checkConnectivity(host = "https://www.google.com"):
    try:
        request.urlopen(host)
        return True
    except:
        return False
