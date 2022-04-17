from fastapi import Request


async def request_debug(request: Request):
    print(f"{request.method}: {request.url}")
    print("headers:")
    for k, v in request.headers.items():
        print(f"\t{k}: {v}")
    print("cookies:")
    print(request.cookies)
    return request
