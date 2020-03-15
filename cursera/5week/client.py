import socket
import time

class ClientError(Exception):
    pass

class Client:
    def __init__(self,server,port,timeout=None):
        self.server = server
        self.port = port
        self.timeout = timeout
        try:
            self.conn = socket.create_connection((server, port), timeout)
        except socket.error as err:
            raise ClientError("error create connection", err)
        except socket.timeout as err:
            raise ClientError("error timeout", err)

    def __read(self):

        data = b""
        while not data.endswith(b"\n\n"):
            try:
                data += self.conn.recv(1024)
            except socket.error as err:
                raise ClientError("error recv data", err)
            except socket.timeout as err:
                raise ClientError("error timeout", err)

        decoded_data = data.decode()

        status, payload = decoded_data.split("\n", 1)
        payload = payload.strip()

        if status == "error":
            raise ClientError(payload)
        print(status)
        return payload

    def put(self,metric,value,timestamp=None):
            try:
                if timestamp == None:
                    timestamp = int(time.time())
                str = f'put {metric} {value} {timestamp}\n'
                self.conn.sendall(str.encode("utf8"))
                self.__read()
            except socket.error as err:
                raise ClientError("error send data", err)
    def get(self,key):
        try:
            str = f"get {key}\n"
            self.conn.sendall(str.encode())
        except socket.error as err:
            raise ClientError("error send data", err)
        except socket.timeout as err:
            raise ClientError("error timeout", err)

        rows = self.__read()
        data_dict = {}

        if not rows:
            return data_dict

        for row in rows.split("\n"):
            try:
                key, value, timestamp = row.split()
            except ValueError as err:
                raise ClientError("server wrong answer", err)

            if key not in data_dict:
                data_dict[key] = []
            data_dict[key].append((int(timestamp), float(value)))
            data_dict[key].sort()
        return data_dict

    def close(self):
        try:
            self.conn.close()
        except socket.error as err:
            raise ClientError("error close connection", err)

if __name__ == "__main__":
    client = Client("127.0.0.1", 8888, timeout=None)
    client.put("test", 0.5, timestamp=1)
    client.put("test", 2.0, timestamp=2)
    client.put("test", 0.5, timestamp=3)
    client.put("load", 3, timestamp=4)
    client.put("load", 4, timestamp=5)
    print(client.get("*"))
    client.close()