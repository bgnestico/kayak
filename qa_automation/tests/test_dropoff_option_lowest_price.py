import pytest
from qa_automation.pages import cars
from qa_automation.qa_settings import DEVICES
from qa_automation.tools.steps_helper import is_page_loaded
from qa_automation.tools.test_data.test_data import (
    PICKUP_LOCATION, DROPOFF_LOCATION, PICKUP_DATE, DROPOFF_DATE)


@pytest.mark.parametrize('setup', DEVICES, indirect=['setup'])
def test_dropoff_option_lowest_price(setup, partners):
    c = cars.Cars(setup)
    c.get_page()
    is_page_loaded(setup.driver, c)
    c.click_dropoff_menu()
    c.click_same_dropoff()
    c.click_pickup_location_display()
    c.enter_pickup_location(PICKUP_LOCATION)
    c.click_dateRange_display()
    c.enter_dateRange(PICKUP_DATE, DROPOFF_DATE)
    c.click_search_btn()
    same_dropoff_price = c.get_first_price_value()
    c.click_dropoff_menu()
    c.click_different_dropoff()
    c.click_pickup_location_display()
    c.enter_pickup_location(PICKUP_LOCATION)
    c.click_dropoff_location_display()
    c.enter_dropoff_location(DROPOFF_LOCATION)
    c.click_dateRange_display()
    c.enter_dateRange(PICKUP_DATE, DROPOFF_DATE)
    c.click_search_btn()
    different_dropoff_price = c.get_first_price_value()
    try:
        assert (same_dropoff_price < different_dropoff_price), \
                            "price comparison not as expected"
    except AssertionError:
        print(same_dropoff_price)
        print(different_dropoff_price)
        print('Date range:' + PICKUP_DATE + '-' + DROPOFF_DATE)
        print('Source Airport:' + PICKUP_LOCATION)
        print('Destination Airport:' + DROPOFF_LOCATION)
