import json
from typing import Optional, Any


def json_of(filepath: str) -> Optional[Any]:
    try:
        with open(filepath) as json_file:
            return json.load(json_file)
    except Exception as err:
        return None
