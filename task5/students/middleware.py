import datetime
import time


def log_middleware(get_response):

    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        execution_time = time.time() - start_time

        with open('log_info.txt', 'a') as log:
            log.write(f'{datetime.datetime.now()}, request.path: {request.path}, request.method: {request.method}, execution_time: {execution_time} \n')

        return response

    return middleware
