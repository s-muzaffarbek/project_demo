from typing import Union, List, Set

from pydantic import BaseModel, HttpUrl
from pydantic.schema import datetime


class Image(BaseModel):
    url: HttpUrl
    name: str

class Blog(BaseModel):
    title: str
    content: str
    created: datetime
    image: Union[List[Image], None] = None
    tags: Set[str] = set()
    views: int
