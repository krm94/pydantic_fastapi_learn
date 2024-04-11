from datetime import datetime
from typing import Annotated, Dict, List, Literal, Tuple
from annotated_types import Gt
from pydantic import BaseModel

class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int,int]

m = Delivery(timestamp = '2020-01-02T03:04:05Z', dimensions = ['10','20'])

## Why use pydantic?
# - Powered by type hints - schema validation, serialization are controlled by type annotations.


class Fruit(BaseModel):
    name: str
    color: Literal['red', 'green', 'yellow']
    weight: Annotated[float, Gt(0)]
    bazam: Dict[str, List[Tuple[int, bool, float]]]

print(
    Fruit(
        name='Apple',
        color='red',
        weight=4,
        bazam={'foobar': [(1, True, 0.1)]},
    )
)



