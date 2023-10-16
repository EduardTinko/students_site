import time
from .models import Log


def simple_middleware(get_response):
    print("get_response", get_response)

    def middleware(request):
        start_time = time.time()
        path = request.path
        method = request.method
        response = get_response(request)
        execution_time = time.time() - start_time

        with open("log.txt", "a") as file:
            file.write(
                f"PATH: {path} METHOD: {method} EXECUTION_TIME: {execution_time} \n"
            )
        Log.objects.create(
            log_path=path, log_method=method, execution_time=execution_time
        )
        return response

    return middleware
