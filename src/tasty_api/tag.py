from __future__ import annotations

import typing

import pydantic


class Tag(pydantic.BaseModel):
    display_name: str
    id: int
    name: str
    parent_tag_name: typing.Optional[str] = None
    root_tag_type: str
    type: str
