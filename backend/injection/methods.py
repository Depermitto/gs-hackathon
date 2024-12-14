import requests
from typing import Callable


def str_to_request_function(method: str) -> Callable:
    match method.upper():
        case "GET":
            return requests.get
        case "POST":
            return requests.post
        case "DELETE":
            return requests.delete
        case "PATCH":
            return requests.patch
        case "PUT":
            return requests.put
        case "HEAD":
            return requests.head
        case "OPTIONS":
            return requests.options
        case _:
            raise ValueError("Incorrect method you dipshit")
