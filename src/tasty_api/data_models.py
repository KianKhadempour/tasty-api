import typing

import pydantic

import tasty_api.feed
import tasty_api.recipe
import tasty_api.tip


class RecipeListModel(pydantic.BaseModel):
    count: int
    results: typing.List[tasty_api.recipe.Recipe]


class TipModel(pydantic.BaseModel):
    count: int
    results: typing.List[tasty_api.tip.Tip]


class FeedModel(pydantic.BaseModel):
    results: typing.List[tasty_api.feed.Feed]
