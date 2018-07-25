import requests
import qa_automation.qa_settings as qaset


def post(method, payload):
    base = qaset.TEST_RAIL_URL
    headers = {'Content-Type': 'application/json'}
    url = base + '/' + method
    return requests.post(
                        url,
                        auth=(qaset.TEST_RAIL_USER, qaset.TEST_RAIL_KEY),
                        headers=headers, json=payload)


def get(method, param):
    base = qaset.TEST_RAIL_URL
    headers = {'Content-Type': 'application/json'}
    url = base + '/' + method + '/' + param
    return requests.get(
                       url,
                       auth=(qaset.TEST_RAIL_USER, qaset.TEST_RAIL_KEY),
                       headers=headers)


def get_results_for_case(run_id, case_id):
    method = 'get_results_for_case'
    param = str(run_id) + '/' + str(case_id)
    response = get(method, param)
    return response.json()


def add_result_for_case(run_id, case_id, passed, comment):
    method = 'add_result_for_case/' + str(run_id) + '/' + str(case_id)

    if(passed):
        result = 1  # passed
    else:
        result = 5  # failed

    payload = {
        "status_id": result,
        "comment": comment
    }

    return post(method, payload)


def get_section_ids(name):
    method = 'get_sections'
    response = get(method, str(qaset.TEST_RAIL_PROJECT))
    json = response.json()
    sections = []
    for s in json:
        if(s['name'] == name):
            my_section = s['id']
            sections.append(s['id'])
    for child in json:
        if(child['parent_id'] == my_section):
            sections.append(child['id'])
    return sections


def get_case_ids(sections):
    method = 'get_cases'
    case_ids = []
    for s in sections:
        response = get(
            method,
            str(qaset.TEST_RAIL_PROJECT) + '&section_id=' + str(s))
        for c in response.json():
            case_ids.append(c['id'])
    return case_ids


def create_plan(name, runs):
    method = 'add_plan/' + str(qaset.TEST_RAIL_PROJECT)
    entries = []
    for run_name, case_ids in runs.items():
        entry = {
            "suite_id": qaset.TEST_RAIL_SUITE_ID,
            "include_all": False,
            "name": run_name,
            "case_ids": case_ids
        }

        entries.append(entry)

    payload = {
        "name": name,
        "include_all": False,
        "suite_id": qaset.TEST_RAIL_SUITE_ID,
        "entries": entries
    }
    method = 'add_plan/' + str(qaset.TEST_RAIL_PROJECT)
    return post(method, payload).json()


def get_plan_id(plan_name):
    method = 'get_plans'
    params = str(qaset.TEST_RAIL_PROJECT) + '&is_completed=0'
    response = get(method, params).json()

    for r in response:
        if r['name'] == plan_name:
            return r['id']


def create_run_by_section(name, section_name):
    sections = get_section_ids(section_name)
    case_ids = get_case_ids(sections)
    return create_run(name, case_ids)


def get_run_id(plan_id, run_name):
    method = 'get_plan'
    response = get(method, str(plan_id)).json()
    entries = response['entries']
    for e in entries:
        if(run_name in e['runs'][0]['name']):
            return e['runs'][0]['id']


def create_run(name, case_ids):
    method = 'add_run/' + str(qaset.TEST_RAIL_PROJECT)
    payload = {
        "include_all": False,
        "name": name,
        "case_ids": case_ids
    }

    return post(method, payload).json()


def close_run(run_id):
    method = 'close_run/' + str(run_id)
    return post(method, {})
