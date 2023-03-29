import pytest
from pytest_check import check

from swagger_client.models.api_tag import ApiTag


@pytest.mark.tags
def test_default_tags(json_defaults, tag_names):
    assert set(json_defaults["tags"]).issubset(tag_names), "Default tags check FAILED! (found : expected)"  # noqa: E501


@pytest.mark.tags
def test_default_tagcategories(json_defaults, tagcategories_names):
    assert set(json_defaults["tagcategories"]).issubset(tagcategories_names), "Default tag types check FAILED!"


@pytest.mark.tags
def test_create_tag(tagcategories_ids, create_api, get_api, delete_api):
    for tag_category_id in tagcategories_ids:
        tag_category = {"id": tag_category_id}
        api_tag = ApiTag(category=tag_category, name="Api Tag")
        new_tag = create_api.tags_post(api_tag.to_dict())
        new_tag_from_db = get_api.tags_id_get(new_tag.id)
        check.equal(new_tag_from_db, new_tag, "Checking the created tag")
        delete_api.tags_id_delete(str(new_tag.id))
