from typing import List
from copy import deepcopy
from typing import Dict, List
from requests import get as _get, models


class _run:
  """Request count, limit"""
  call_count = 0
  call_limit = 10


class ResponseWrapper:
  """'requests' response wrapper for api.github.com/repos/<user>/<repo>/events"""

  def __init__(self, json):
    self._source: List[dict] = json
    self._models: List[dict] = self._get_models()
    
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
  

def get(url: str) -> models.Request:
  """Restrict # of calls to _run.call_limit"""
  if _run.call_count < _run.call_limit:
    _run.call_count += 1
    return _get(url)
  else:
    raise RuntimeError(
        f'ERROR: Call limit ({str(_run.call_count)}) exceeded.')


def get_json(url: str) -> dict:
  """Get Request as dict (json)"""
  resp = get(url)
  return resp.json()
