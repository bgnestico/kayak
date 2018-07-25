"""
Leads helper function.
"""
import requests
from datetime import date, timedelta
from qa_automation.tools.steps_helper import REQUEST_TIMEOUT


"""
Leads
"""


def leads_get(url):
    from local_settings import LEADS_API
    url = LEADS_API['base_url'] + url
    token = "Token " + LEADS_API['token']
    auth = {
        'Authorization': token,
        'Accept': 'application/json'
    }
    return requests.get(
        url, headers=auth, timeout=REQUEST_TIMEOUT['DEFAULT']).json()


def get_latest_form_lead_by_brand_id(brand_id):
    return get_latest_form_lead(brand_id)


def get_latest_form_lead(brand_id):
    return get_latest_lead_by_type(brand_id, 'form')


def get_latest_lead_by_type(brand, lead_type):
    today = str(date.today())
    yesterday = str(date.today() - timedelta(1))

    response = leads_get(
        'brands/' + str(brand) + '?include_details=1&' +
        'datetime_from=' + yesterday + '&datetime_from=' + today)
    details = response.get('lead_details')

    if details is not None and len(details):
        newest = details[0]
        for lead in details:
            if lead.get('lead_type') != lead_type:
                continue
            for m in lead.get('data'):
                date_compare = m.get('lead_submitted')
                if date_compare and date_compare > newest['lead_submitted']:
                    for m in newest.get('data'):
                        if 'matching tool' in newest.get('page_type'):
                            newest = m
        assert newest is not None, 'No recent leads'
        return newest
