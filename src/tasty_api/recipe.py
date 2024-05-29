import datetime
import typing

import pydantic
import pydantic_extra_types.country
import pydantic_extra_types.language_code

import tasty_api.tag


class Show(pydantic.BaseModel):
    id: int
    name: str


class Compilation(pydantic.BaseModel):
    approved_at: datetime.datetime
    aspect_ratio: typing.Optional[str]
    beauty_url: typing.Any
    buzz_id: typing.Any
    canonical_id: str
    country: pydantic_extra_types.country.CountryAlpha2
    created_at: datetime.datetime
    description: typing.Optional[str]
    draft_status: str
    facebook_posts: typing.List[typing.Any]
    id: int
    is_shoppable: bool
    keywords: typing.Any
    language: pydantic_extra_types.language_code.ISO639_3
    name: str
    promotion: str
    show: typing.List[Show]
    slug: str
    thumbnail_alt_text: str
    thumbnail_url: str
    video_id: int
    video_url: str


class Credit(pydantic.BaseModel):
    name: typing.Optional[str]
    type: str


class Instruction(pydantic.BaseModel):
    appliance: typing.Optional[str]
    display_text: str
    end_time: int
    id: int
    position: int
    start_time: int
    temperature: typing.Optional[int]


class Nutrition(pydantic.BaseModel):
    calories: int
    carbohydrates: int
    fat: int
    fiber: int
    protein: int
    sugar: int
    updated_at: datetime.datetime


class Price(pydantic.BaseModel):
    consumption_portion: int
    consumption_total: int
    portion: int
    total: int
    updated_at: datetime.datetime


class Rendition(pydantic.BaseModel):
    aspect: str
    bit_rate: typing.Optional[int]
    container: str
    content_type: str
    duration: int
    file_size: typing.Optional[int]
    height: int
    maximum_bit_rate: typing.Optional[int]
    minimum_bit_rate: typing.Optional[int]
    name: str
    poster_url: str
    url: str
    width: int


class Ingredient(pydantic.BaseModel):
    created_at: datetime.datetime
    display_plural: str
    display_singular: str
    id: int
    name: str
    updated_at: datetime.datetime


class Unit(pydantic.BaseModel):
    abbreviation: str
    display_plural: str
    display_singular: str
    name: str
    system: str


class Measurement(pydantic.BaseModel):
    id: int
    quantity: str
    unit: Unit


class Component(pydantic.BaseModel):
    extra_comment: str
    id: int
    ingredient: Ingredient
    measurements: typing.List[Measurement]
    position: int
    raw_text: str


class Section(pydantic.BaseModel):
    components: typing.List[Component]
    name: typing.Any
    position: int


class Topic(pydantic.BaseModel):
    name: str
    slug: str


class TotalTimeTier(pydantic.BaseModel):
    display_tier: str
    tier: str


class UserRatings(pydantic.BaseModel):
    count_negative: int
    count_positive: int
    score: float


class TipsSummary(pydantic.BaseModel):
    by_line: str
    content: str
    header: str


class MetadataRecipe(pydantic.BaseModel):
    approved_at: datetime.datetime
    aspect_ratio: typing.Optional[str]
    beauty_url: typing.Any
    brand: typing.Any
    brand_id: typing.Any
    buzz_id: typing.Any
    canonical_id: str
    compilations: typing.List[Compilation]
    cook_time_minutes: typing.Optional[int]
    country: pydantic_extra_types.country.CountryAlpha2
    created_at: datetime.datetime
    credits: typing.List[Credit]
    draft_status: str
    facebook_posts: typing.List[typing.Any]
    inspired_by_url: typing.Any
    is_app_only: bool
    is_one_top: bool
    is_shoppable: bool
    is_subscriber_content: bool
    keywords: typing.Optional[str]
    language: pydantic_extra_types.language_code.ISO639_3
    nutrition_visibility: str
    original_video_url: typing.Optional[str]
    prep_time_minutes: typing.Optional[int]
    promotion: str
    renditions: typing.List[Rendition]
    seo_path: str
    seo_title: typing.Optional[str]
    servings_noun_plural: str
    servings_noun_singular: str
    show: Show
    show_id: int
    slug: str
    tags: typing.List[tasty_api.tag.Tag]
    thumbnail_alt_text: str
    thumbnail_url: str
    tips_and_ratings_enabled: bool
    topics: typing.List[Topic]
    total_time_minutes: typing.Optional[int]
    total_time_tier: TotalTimeTier
    updated_at: datetime.datetime
    user_ratings: UserRatings
    video_ad_content: typing.Optional[str]
    video_id: typing.Optional[int]
    video_url: typing.Optional[str]
    tips_summary: typing.Optional[TipsSummary] = None


class Recipe(pydantic.BaseModel):
    description: str
    id: int
    instructions: typing.List[Instruction]
    name: str
    num_servings: int
    nutrition: Nutrition
    price: Price
    sections: typing.List[Section]
    yields: str
    metadata: MetadataRecipe

    @pydantic.model_validator(mode="before")
    @classmethod
    def nest_metadata(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        metadata_fields = set(MetadataRecipe.model_fields)
        metadata_data = {
            key: values.pop(key) for key in metadata_fields if key in values
        }
        values["metadata"] = metadata_data
        return values
