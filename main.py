import websockets
import asyncio

PORT = 1234
print("[>] Websocket Server listening on ws://localhost:" + str(PORT))

connected = set()

async def main(websocket, path):
    print("[^] A client just connected")
    connected.add(websocket)

    try:
        async for message in websocket:
            print("[^] Received message from client: " + message)
            for conn in connected:
                if conn != websocket:
                    await conn.send("[?] Someone said: " + message)
    except websockets.exceptions.ConnectionClosed as e:
        print("[!] A client just disconnected")
    finally:
        connected.remove(websocket)

start_server = websockets.serve(main, "localhost", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()