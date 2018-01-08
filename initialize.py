import uuid
import qrcode
import pickle
import settings

if __name__ == '__main__':
    _uuid = uuid.uuid1()
    img = qrcode.make("https://line.me/R/oaMessage/{}/?".format(settings.LINE_USER_ID) + str(_uuid))
    with open('token.pickle', mode='wb') as f:
        pickle.dump({'uuid': _uuid}, f)
    img.show()
