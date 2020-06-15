# Simple server for return "Got: " + client msg

from socket import *
import asyncio
from pprint import pprint


async def echo_server(address, loop):
    con = socket(AF_INET, SOCK_STREAM)  # Set TCP
    con.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # Set reusable socket address
    con.bind(address)  # Bind socket to (ip, port)
    con.listen(5)  # Set maximum connections of connected clients
    con.setblocking(False)  # True is equivalent to settimeout(None); False is equivalent to settimeout(0.0).

    print('Server started..')

    while True:
        client, addr = await loop.sock_accept(con)  # Accept connection from a single client
        print("Connection from", addr)  # Show client ip address
        task = loop.create_task(echo_handler(client))  # Asynchronous clients connections


async def echo_handler(client):
    while True:  # Create generator for yielding
        if not loop.is_closed():  # Check for opened event loop
            data = await loop.sock_recv(client, 4096)  # None blocking socket receiving task
            pprint(data)
            await asyncio.sleep(2)  # Set extra load for example
            if not data:
                break  # Exit if no client data send after successful connection
            await loop.sock_sendall(client, b"Server answer: " + data)  # Send answer to client. Not blocking task
    print("Connection closed")
    client.close()  # Client connection closing


if __name__ == "__main__":
    loop = asyncio.get_event_loop()  # Create event loop to handle clients
    loop.run_until_complete(echo_server(('', 9000), loop))  # Run server
