import json

import pytest

import tasty_api.data_models
import tasty_api.feed


@pytest.mark.xfail()
def test_get_feeds_list():
    with open("tests/data/get_feeds_list.json", encoding="UTF-8") as f:
        data = json.load(f)

    model = tasty_api.data_models.FeedModel(**data)

    assert isinstance(model.results, list)
    assert isinstance(model.results[0], tasty_api.feed.Feed)
