import yaml


def parse_yaml(path):
    results = []
    with open("example.yaml", "r") as f:
        spec = yaml.safe_load(f)
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
    return results


if __name__ == "__main__":
    res = parse_yaml("example_yaml")

    for r in res:
        print(f"{r}\n")
