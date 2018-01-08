import websocket
import json
import pickle
import time
import settings

def on_message(ws, message):
    msg = json.loads(message)
    print(msg)

    time.sleep(2)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    ws.send(json.dumps({'command': 'subscribe', 'identifier': json.dumps({'channel': 'FeedChannel'})}))
    print("### opened ###")


if __name__ == "__main__":
    cert = {}
    with open('token.pickle', mode='rb') as f:
        cert = pickle.load(f)
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("{}?uuid={}".format(settings.FEEDER_WS_URL, str(cert['uuid'])),
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
