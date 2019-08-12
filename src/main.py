import requests
import json as j


# get request counter / lifespan
class run:
    call_count = 0


class GitHub_Response:
    def __init__(self, json):
        self.source = json
        self._model = json

    @property
    def model(json: dict):
        return self._model

    @model.setter
    def model(json):


def get(url: str) -> requests.models.Request:
    if r.call_count < 10:
        requests.get(url)


def get_json(url: str) -> dict:
    resp = requests.get(url)
    return resp.json()


def pretty_str(resp: dict) -> dict:
    """Dict -> String, indent=2"""
    return j.dumps(resp, indent=2)


def get_and_print(url: str) -> None:
    """Pretty print 'get' response from url."""
    r = pretty_str(get_json(url))
    print(r)
    return r


def _main() -> None:
    r = get_and_print(
        'https://api.github.com/repos/awallace689/requests/events')


if __name__ == "__main__":
    _main()


class C(object):


def __init__(self):
    self._x = None


@property
def x(self):
    """I'm the 'x' property."""
    return self._x


@x.setter
def x(self, value):
    self._x = value


@x.deleter
def x(self):
    del self._x
