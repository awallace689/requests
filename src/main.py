import json as j
from lib.my_requests import ResponseWrapper, get_json


URL = 'https://api.github.com/repos/awallace689/requests/events'


def debug_response(resp: ResponseWrapper):
    def formatted_print(to_print, label: str) -> None:
        print(
            f'################ BEGIN {label}',
            to_print,
            f'################ END {label}',
            sep='\n')

    formatted_print(j.dumps(resp.source, indent=2), 'source')
    formatted_print(j.dumps(resp.models, indent=2), 'models')
    print(f'[source==models: {j.dumps(resp.models == resp.source)}]')


def _main() -> None:
    resp = ResponseWrapper(get_json(URL))


if __name__ == "__main__":
    _main()
