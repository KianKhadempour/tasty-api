import typing

import pydantic

import tasty_api.recipe
import tasty_api.tag


class Complimation(pydantic.BaseModel):
    aspect_ratio: typing.Optional[str]
    country: str
    keywords: typing.Any
    facebook_posts: typing.List[typing.Any]
    show: tasty_api.recipe.Show
    created_at: int
    description: typing.Optional[str]
    draft_status: str
    language: str
    thumbnail_url: str
    thumbnail_alt_text: str
    video_url: typing.Optional[str]
    updated_at: int
    credits: typing.List[tasty_api.recipe.Credit]
    approved_at: int
    renditions: typing.List[tasty_api.recipe.Rendition]
    id: int
    beauty_url: typing.Any
    slug: str
    recipes: typing.List[tasty_api.recipe.Recipe]
    is_shoppable: bool
    show_id: int
    tags: typing.List[tasty_api.tag.Tag]
    name: str
    canonical_id: str
    buzz_id: typing.Any
    promotion: str
    video_id: int


RecipeOrComplimation = typing.Union[tasty_api.recipe.Recipe, Complimation]


class Feed(pydantic.BaseModel):
    type: str
    items: typing.List[RecipeOrComplimation]
    name: typing.Optional[str] = None
    category: typing.Optional[str] = None
    min_items: typing.Optional[int] = None

    @pydantic.model_validator(mode="before")
    @classmethod
    def convert_singular_item_to_items(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        if "item" in values:
            values["items"] = [values.pop("item")]

        return values
