from __future__ import annotations

import typing

import pydantic

if typing.TYPE_CHECKING:
    import tasty_api.recipe


class RecipeListModel(pydantic.BaseModel):
    count: int
    results: typing.List[tasty_api.recipe.Recipe]
