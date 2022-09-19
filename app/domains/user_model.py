from typing import Union, List, Set

from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
