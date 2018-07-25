import pytest
from qa_automation.pages import categories
from qa_automation.qa_settings import DEVICES
from qa_automation.tools.steps_helper import is_page_loaded
from qa_automation.tools.test_data.test_data import (
    PARTNERS, CATEGORIES_NO_CLICK)


@pytest.mark.case_id(59978)
@pytest.mark.parametrize('partners', PARTNERS)
@pytest.mark.parametrize('setup', (DEVICES), indirect=['setup'])
def test_ppc_banner_phone_btn_for_all_categories(setup, partners):
    c = categories.Categories(setup)
    for category in partners['CATEGORIES']:
        url = (partners['URL'] + category['URL'])
        c.get_page(url)
        is_page_loaded(setup.driver, c)
        if category['NAME'] in CATEGORIES_NO_CLICK:
            assert c.get_ppc_banner_phone_btn('InsuraMatch') \
                is not None, "Phone button not present please check"
            c.click_ppc_banner_phone_btn('InsuraMatch')
        else:
            assert c.get_ppc_banner_phone_btn(category['TOP_POS'][1]) \
                is not None, "Phone button not present please check"
            c.click_ppc_banner_phone_btn(category['TOP_POS'][1])
