import json

with open('candidates.json', encoding='UTF-8') as f:
    raw_json = f.read()

profile = json.loads(raw_json)  # получаем список словарей


def load_candidates_from_json():
    """Возвращает список всех кандидатов"""
    list_all_candidates = []
    for dict in profile:
        list_all_candidates.append(dict['name'])
    # return list_all_candidates
    return profile


def get_candidate(candidate_id):
    """Возвращает словарь кандидата по его id"""
    for dict in profile:
        if candidate_id == dict['id']:
            return dict


def get_candidates_by_name(candidate_name):
    """Возвращает список кандидатов по совпадению в имени"""
    list_count_name = []  # список совпадений
    for dict in profile:
        if candidate_name not in dict['name']:
            continue
        list_count_name.append(dict['name'])
    return list_count_name


def get_candidates_by_skill(skill_name):
    """Возвращает список кандидатов по навыку"""
    list_candidates_by_skill = []
    for dict in profile:
        if skill_name not in dict['skills']:
            continue
        list_candidates_by_skill.append(dict['name'])
    return list_candidates_by_skill