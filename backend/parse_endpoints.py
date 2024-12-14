import yaml


def parse_yaml(path):
    path_params = []
    insecure = []
    params = []
    with open("example.yaml", "r") as f:
        spec = yaml.safe_load(f)
    paths = spec.get("paths", {})
    for path, methods in paths.items():
        for method, details in methods.items():
            if "{" in path:
                path_params.append({"method": method, "path": path})
            security = details.get("security", spec.get("security", []))
            if not security:
                insecure.append({"method": method, "path": path})
            request_body = details.get("requestBody")
            if request_body:
                content = request_body.get("content", {})
                for content_type in content.values():
                    schema = content_type.get("schema")
                    if schema:
                        params.append(
                            {"method": method, "path": path, "schema": schema}
                        )
    return path_params, insecure, params

if __name__ == "__main__":
    path, ins, par = parse_yaml("example_yaml")

    print(f"PATH:\n{path}\n")
    print(f"INSECURE:\n{ins}\n")
    print(f"PARAMS:\n{par}\n")
