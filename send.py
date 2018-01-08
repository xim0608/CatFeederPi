import requests
import pickle
import settings

if __name__ == '__main__':
    cert = {}
    with open('token.pickle', mode='rb') as f:
        cert = pickle.load(f)
    print(cert)
    headers = {'ACCESS_TOKEN_UUID': str(cert['uuid'])}
    r = requests.get("{}/send".format(settings.FEEDER_URL), headers=headers)
    print(r)
