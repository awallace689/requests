import requests
import json as j


URL = 'https://api.github.com/repos/awallace689/requests/events'


# get request counter / lifespan
class run:
    call_count = 0
    call_limit = 10


class GitHub_Response:
    """'requests' response wrapper for api.github.com/repos/<user>/<repo>/events"""

    def __init__(self, json):
        self.source = json
        self._model = j.dumps(json[0], indent=2)

    @property
    def model(self) -> dict:
        return self._model


def get(url: str) -> requests.models.Request:
    """Restrict # of calls to run.call_limit"""
    if run.call_count < run.call_limit:
        print(run.call_count)
        run.call_count += 1
        return requests.get(url)
    else:
        raise RuntimeError(
            f'ERROR: Call limit {str(run.call_count)} exceeded.')


def get_json(url: str) -> dict:
    """Get Request as dict (json)"""
    resp = get(url)
    return resp.json()


def _main() -> None:
    resp = GitHub_Response(get_json(URL))
    print(resp.model)


if __name__ == "__main__":
    _main()
