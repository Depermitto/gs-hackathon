import injection

if __name__ == "__main__":
    base, routes = injection.parse_yaml("example.yaml")
    print(f"BASE URL: {base}\n")
    with open("injections.txt", "r") as f:
        injs = f.read().splitlines()

    # parsing parameters
    print("\nSCHEMA PARSING")
    for route in routes:
        if not route.get("schema"):
            continue
        print(f"\nRoute: {route['method']} {route['path']}")
        for inj in injs:
            payload = injection.prepare_payload(route["schema"], inj)
            print(f"\t{payload}")

    # parsing path parameters
    print("\nPARAMETER PARSING")
    for route in routes:
        if not route["path_param"]:
            continue
        print(f"\n{route['path']}")
        for inj in injs:
            print(f"\t{route['path'].split('{')[0]}{inj}")

    # parsing insecure
    print("\nINSECURITY PARSING\n")
    for route in routes:
        if not route["secure"]:
            print(f"WARNING: Route {route['method']} {route['path']} is insecure")
