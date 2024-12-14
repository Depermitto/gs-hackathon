import requests
from .parse_endpoints import parse_yaml
from .prepare_payloads import prepare_payload

from typing import Any

def pipeline(yaml_path: str, injections_path: str, auth: dict[str,str] | None = None) -> list[dict[str,str|bool]]:
    """
    Check API for possible SQL injections

    # Args:
        yaml_path (`str`): path to the OpenAPI .yaml file
        injections_path(`str`): path to the file containing commands that will be possibly injected
        auth (`dict[str,str] | None`): API authorization method (None if not required)
    
    # Returns:
        result (`list[dict[str,str|bool]]`): A dictionary with the following fields:
            route (`str`): method + path to endpoint
            requires_auth (`str`): whether the endpoint requires user authorization
            body_injection (`bool`): whether injection through request body was successful
            path_injection (`bool`): whether injection through path was successful
    """
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
                "requires_auth": route["secure"],
                "body_injection": body_status,
                "path_injection": path_status,
            }
        )
    return result


def req(url: str, method: str, body: dict[str, Any], auth: dict[str,str] | None = None, is_body: bool = True) -> bool:
    """
    Perform a request to the API endpoint
    
    # Args:
        url (`str`): URL to the API endpoint
        method (`str`): HTTP request method
        body (`dict[str,Any]`): json body of the request
        auth (`dict[str,str] | None`): API authorization method (None if not required)
        is_body (`bool`): stating whether checking for body injection or path injection
    
    # Returns:
        success (`bool`): whether the injection was successful
    """
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
        if auth:
            response = func(url, params=body, json=body, headers=auth)
        else:
            response = func(url, params=body, json=body)

        if response.status_code == 200:
            success = True
    except Exception as e:
        print(e)
    return success


if __name__ == "__main__":
    # HAS TO BE SET MANUALLY IN ORDER TO WORK PROPERLY
    # THIS IS A DIRTY EXAMPLE FOR https://github.com/erev0s/VAmPI
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
