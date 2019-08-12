import json as j
from sys import argv
from lib.my_requests import ResponseWrapper, get_json


DEFAULT_URL = 'https://api.github.com/repos/awallace689/requests/events'


def debug_response(resp: ResponseWrapper) -> None:
    def formatted_print(to_print, label: str) -> None:
        print(
            f'################ BEGIN {label}',
            to_print,
            f'################ END {label}',
            sep='\n')

    formatted_print(j.dumps(resp.source, indent=2), 'source')
    formatted_print(j.dumps(resp.models, indent=2), 'models')
    print(f'[source==models: {j.dumps(resp.models == resp.source)}]')


def _main(url: str) -> None:
    resp = ResponseWrapper(get_json(url))
    debug_response(resp)


if __name__ == "__main__":
    URL = argv[1] if argv[1] else DEFAULT_URL
    _main(URL)
