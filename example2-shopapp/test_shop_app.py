import pytest
from shop_app import Shop

@pytest.fixture
def basket():
    return Shop()

def test_add_item(basket):
    basket.add("keyboard")
    assert basket.size() == 1

def test_item_added_correctly(basket):
    basket.add("keyboard")
    assert "keyboard" in basket.get_items()