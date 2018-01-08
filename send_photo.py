import requests
import pickle
import settings

if __name__ == '__main__':
    cert = {}
    with open('token.pickle', mode='rb') as f:
        cert = pickle.load(f)
    print(cert)
    headers = {'ACCESS_TOKEN_UUID': str(cert['uuid'])}
    files = {'media': open('IMG_4486.PNG', 'rb')}
    r = requests.post("{}/send".format(settings.FEEDER_URL), headers=headers, files=files)
    print(r)
