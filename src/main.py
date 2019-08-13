import json as j
from sys import argv
from lib.myrequests.getlib import ResponseWrapper, get_json
from asyncio import run
from timeit import default_timer as timer


DEFAULT_URL = 'https://api.github.com/repos/awallace689/requests/events'


def print_info(resp: ResponseWrapper) -> None:
    def formatted_print(to_print, label: str) -> None:
        print(
            f'################ BEGIN {label}',
            to_print,
            f'################ END {label}',
            sep='\n')

    formatted_print(j.dumps(resp.source, indent=2), 'source')
    formatted_print(j.dumps(resp.models, indent=2), 'models')
    print(f'[source==models: {j.dumps(resp.models == resp.source)}]\n'
          f'[# models: {len(resp.models)}]')


async def _main(url: str) -> None:
    resp = ResponseWrapper(await get_json(url), debug=True)
    print_info(resp)


if __name__ == "__main__":
    URL = argv[1] if len(argv) > 1 else DEFAULT_URL
    start = timer()
    run(_main(URL))
    end = timer()
    print(end - start)
