import yaml

from typing import Tuple


def parse_yaml(path) -> Tuple[str, dict[str, str | bool]]:
    """
    Read information about API endpoints from the OpenAPI .yaml file

    # Args:
        path (`str`): path to the file

    # Returns:
        base_url (`str`): the entrypoint to the API service
        results (`dict[str,str | bool]`): dictionary containing information about endpoints containing the following fields:
            method (`str`): HTTP request method
            path (`str`): path to the API endpoint
            secure (`bool`): whether the API endpoint requires authorization
            path_param (`bool`): whether the API endpoint path contains a parameter
            schema (`dict[str,Any] | None`): request body schema (None if no body is specified)
    """
    try:
        with open(path) as f:
            spec = yaml.safe_load(f)
    except:
        spec = yaml.safe_load(path)
    base_url = spec["servers"][0]["url"]

    results = []
    paths = spec.get("paths", {})
    for path, methods in paths.items():
        for method, details in methods.items():
            path_param = True if "{" in path else False
            schema = None
            security = details.get("security", spec.get("security", []))
            request_body = details.get("requestBody")
            if request_body:
                content = request_body.get("content", {})
                for content_type in content.values():
                    schema = content_type.get("schema")
            results.append(
                {
                    "method": method.upper(),
                    "path": path,
                    "secure": True if security else False,
                    "path_param": path_param,
                    "schema": schema,
                }
            )
    return base_url, results


if __name__ == "__main__":
    base, res = parse_yaml("example.yaml")
    print(f"Base URL: {base}")
    for r in res:
        print(f"{r}\n")
