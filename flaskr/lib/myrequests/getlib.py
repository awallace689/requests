from typing import List
from copy import deepcopy
from typing import Dict, List, Any
from json import dumps
from requests import get as _get, models
from asyncio import run


class _run:
  """Request count, limit"""
  call_count = 0
  call_limit = 10


class ResponseWrapper:
  """'requests' library 'get' response wrapper"""

  def __init__(self, json, debug=False):
    self._source: List[dict] = json
    self._models: List[dict] = self._get_models()
    self.debug = debug
    
    if debug:
      self.print_info()

  def print_info(self) -> None:
    """Print response source and unique models"""
    def formatted_print(to_print: Any | str, label: str) -> None:
      print(
        f'################ BEGIN {label}',
        to_print,
        f'################ END {label}',
        sep='\n')

    formatted_print(dumps(self.source, indent=2), 'source')
    formatted_print(dumps(self.models, indent=2), 'models')
    print(
      f'[source==models: {dumps(self.models == self.source)}]\n'
      f'[# models: {len(self.models)}]')
    
  @property
  def models(self) -> str:
    return self._models

  @property
  def source(self) -> List[dict]:
    return deepcopy(self._source)
  
  def _get_models(self) -> List[dict]:
    """Returns list of unique JSON models"""
    models: List[dict] = []
    added: List[iter] = []
    for obj in self._source:
      if not obj.keys() in added:
        added.append(obj.keys())
        models.append(obj)
    return models
  

async def get(url: str) -> models.Request:
  """Restrict # of calls to _run.call_limit"""
  if _run.call_count < _run.call_limit:
    _run.call_count += 1
    return _get(url)
  else:
    raise RuntimeError(
      f'ERROR: Call limit ({str(_run.call_count)}) exceeded.')


async def get_json(url: str) -> dict:
  """Get Request as dict (json)"""
  resp = await get(url)
  return resp.json()
