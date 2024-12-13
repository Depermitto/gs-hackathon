import yaml

with open("example.yaml", "r") as f:
    spec = yaml.safe_load(f)
    paths = spec.get("paths", {})
    for path, methods in paths.items():
        for method, details in methods.items():
            print(f"\nAnalyzing {method.upper()} {path}")

            # Check for authentication
            security = details.get("security", spec.get("security", []))
            if not security:
                print("- Warning: No security defined for this endpoint.")

            # Check for input validation
            request_body = details.get("requestBody")
            if request_body:
                content = request_body.get("content", {})
                if not any(
                    "schema" in content_type for content_type in content.values()
                ):
                    print("- Warning: No schema defined for request body.")
            else:
                print("- Info: No request body defined.")

            # Check HTTP method usage
            if method.lower() in ["get", "delete"]:
                print(
                    "- Info: Ensure sensitive operations aren't exposed via GET or DELETE."
                )
