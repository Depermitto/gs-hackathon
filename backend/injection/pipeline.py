import requests
from parse_endpoints import parse_yaml
from prepare_payloads import prepare_payload


def pipeline(yaml_path, injections_path, auth):
    base_path, routes = parse_yaml(yaml_path)
    print(f"Base URL determined as: {base_path}\n")
    with open(injections_path, "r") as f:
        injs = f.read().splitlines()
    result = []
    for route in routes:
        print(route)
    for route in routes:
        if route.get("schema"):
            print(f"\nRoute: {route['method']} {route['path']}")
            for inj in injs:
                payload = prepare_payload(route["schema"], inj)
                print(req(base_path + route["path"], route["method"], payload, auth))
        if route["path_param"]:
            print(f"\nRoute: {route['method']} {route['path']}")
            for inj in injs:
                payload = prepare_payload(route["schema"], inj)
                print(
                    req(
                        base_path + route["path"].split("{")[0] + inj,
                        route["method"],
                        payload,
                        auth,
                    )
                )


def req(url, method, body, auth):
    func = None
    success = False
    try:
        match method:
            case "GET":
                func = requests.get
            case "POST":
                func = requests.post
            case "PUT":
                func = requests.put
            case "DELETE":
                func = requests.delete
            case "PATCH":
                func = requests.patch
        response = func(
            url, params=body, json=body, headers={"Authorization": f"Bearer {auth}"}
        )
        if response.status_code == 200:
            success = True
    except:
        pass
    return success


if __name__ == "__main__":
    pipeline(
        "example.yaml",
        "injections.txt",
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQxNDUzNjAsImlhdCI6MTczNDE0NTMwMCwic3ViIjoibmFtZTEifQ.o7HFDDT4et3J30dsjt2LfIi1bSuVfNgsIiAls8wzeH0",
    )
