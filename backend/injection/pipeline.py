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
        body_status = False
        path_status = False
        if route.get("schema"):
            for inj in injs:
                payload = prepare_payload(route["schema"], inj)
                body_status = req(
                    base_path + route["path"], route["method"], payload, auth
                )
                if body_status:
                    break
        if route["path_param"]:
            for inj in injs:
                payload = prepare_payload(route["schema"], inj)
                path_status = req(
                    base_path + route["path"].split("{")[0] + inj,
                    route["method"],
                    payload,
                    auth,
                    False,
                )
                if path_status:
                    break
        result.append(
            {
                "route": f"{route['method']} {route['path']}",
                "secure": route["secure"],
                "body_injection": body_status,
                "path_injection": path_status,
            }
        )
    return result


def req(url, method, body, auth, is_body=True):
    func = None
    success = False
    try:
        match method:
            case "GET":
                func = requests.get
            case "POST":  # Rather impossible to differ
                return False
            case "PUT":
                if is_body:  # makes no sense when in body
                    return False
                func = requests.put
            case "DELETE":
                # WARNING - VERY DANGEROUS, COMMENTED FOR SAFETY
                # func = requests.delete
                return False
            case "PATCH":
                func = requests.patch
        response = func(url, params=body, json=body, headers=auth)
        if response.status_code == 200:
            success = True
    except Exception as e:
        print(e)
    return success


if __name__ == "__main__":
    # HAS TO BE SET MANUALLY IN ORDER TO WORK PROPERLY
    # THIS IS A DIRTY EXAMPLE FOR https://github.com/erev0s/VAmPI/tree/master
    res = requests.post(
        "http://127.0.0.1:5000/users/v1/login",
        json={"password": "pass1", "username": "name1"},
    )
    print(res._content)
    token = f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzQxNDc4NjMsImlhdCI6MTczNDE0NzgwMywic3ViIjoibmFtZTEifQ.SHQ-YrI2gW4H-RNgidc49YtvA7sYT5BavRcqnBTkpuw"
    auth = {"Authorization": token}

    result = pipeline("example.yaml", "injections.txt", auth)
    for res in result:
        print(res)
