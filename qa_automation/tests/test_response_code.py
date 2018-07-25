import pytest
from qa_automation.tools import steps_helper
from qa_automation.tools.test_data.test_data import PARTNERS


@pytest.mark.parametrize('partners', PARTNERS)
def test_status_code(partners):
    for category in partners['CATEGORIES']:
        url = (partners['URL'] + category['URL'])
        steps_helper.check_status_code(url, 200)
