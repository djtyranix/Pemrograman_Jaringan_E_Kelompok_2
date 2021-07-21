class ReverseProxy:
    def __init__(self):
        self.server_default=('localhost',8886)
        self.server_list = {}
        self.server_list['/images']=('localhost', 8887)
        self.server_list['/pdf']=('localhost', 8888)

    def proses(self, data):
        forward_response = {}
        data=data.decode()
        for server_name in self.server_list:
            if (server_name in data):
                forward_response['server']=self.server_list[server_name]
                break
        if (len(forward_response) == 0):
            forward_response['server']=self.server_default

        forward_response['request'] = data
        return forward_response

