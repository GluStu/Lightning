import websocket
import json
import threading
import time

output_file = "incoming_data.bin"

def on_open(ws):
    print("Connected")
    init_message = {"a": 111}
    ws.send(json.dumps(init_message))
    print("init message Sent")

    def close_socket():
        time.sleep(15)
        ws.close()
        print("Closed")

    threading.Thread(target=close_socket).start()

def on_message(ws, message):
    with open("incoming_data.bin", "a") as f:
        f.write(message + "\n")
# def on_message(ws, message):
#     with open(output_file, "ab") as f:
#         f.write(message.encode('utf-8'))
#         f.write(b'\n')

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, code, reason):
    print(f"Closed: {code}, {reason}")

headers = {
    "Origin": "https://www.blitzortung.org",
    "User-Agent": "Mozilla/5.0"
}

ws = websocket.WebSocketApp(
    "wss://ws2.blitzortung.org/",
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

ws.run_forever()