class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        while self.finish_time and self.finish_time[0] <= request.arrival_time:
            self.finish_time.pop(0)

        if len(self.finish_time) == self.size:
            return Response(True, -1)

        if not self.finish_time:
            start_time = request.arrival_time
        else:
            start_time = self.finish_time[-1]

        self.finish_time.append(start_time + request.process_time)
        return Response(False, start_time)

def process_packages():
    size, count = map(int, input().split())
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().split())
        requests.append(Request(arrival_time, process_time))

    buffer = Buffer(size)
    responses = []
    for request in requests:
        response = buffer.process(request)
        responses.append(response)

    for response in responses:
        if response.dropped:
            print(-1)
        else:
            print(response.start_time)

if __name__ == '__main__':
    process_packages()
