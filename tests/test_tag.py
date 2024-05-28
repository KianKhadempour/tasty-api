import tasty_api.tag


def test_full_tag():
    data = {
        "display_name": "Brazilian",
        "id": 64446,
        "name": "brazilian",
        "parent_tag_name": "central_south_american",
        "root_tag_type": "cuisine",
        "type": "central_south_american",
    }
    assert tasty_api.tag.Tag(**data) == tasty_api.tag.Tag(
        display_name="Brazilian",
        id=64446,
        name="brazilian",
        parent_tag_name="central_south_american",
        root_tag_type="cuisine",
        type="central_south_american",
    )


def test_partial_tag():
    data = {
        "display_name": "North American",
        "id": 64444,
        "name": "north_american",
        "root_tag_type": "cuisine",
        "type": "cuisine",
    }
    assert tasty_api.tag.Tag(**data) == tasty_api.tag.Tag(
        display_name="North American",
        id=64444,
        name="north_american",
        root_tag_type="cuisine",
        type="cuisine",
    )
