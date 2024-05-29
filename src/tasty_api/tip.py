from __future__ import annotations

import datetime
import typing

import pydantic


class TipPhoto(pydantic.BaseModel):
    height: int
    url: str
    width: int


class Tip(pydantic.BaseModel):
    author_avatar_url: str
    author_name: str
    author_rating: int
    author_user_id: int
    author_username: str
    author_is_verified: int
    is_flagged: bool
    recipe_id: int
    status_id: int
    comment_id: int
    comment_count: int
    tip_body: str
    tip_id: int
    tip_photo: typing.Optional[TipPhoto]
    created_at: typing.Optional[datetime.datetime]
    updated_at: datetime.datetime
    upvotes_total: int
