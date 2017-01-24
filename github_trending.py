import requests
import json
from datetime import datetime, timedelta


def get_last_week_day():
    return(datetime.today().date() - timedelta(days=7))


def get_trending_repositories(top_size, date):
    api_link = "https://api.github.com/search/repositories"
    get_params = {'q': 'created:>={0}'.format(date), 'sort': 'stars'}
    r = requests.get(api_link, params=get_params)
    json_from_request = json.loads(r.text)
    return json_from_request['items'][:top_size]


def get_repository_info(repository):
    return repository['html_url'], \
        repository['full_name'], repository['open_issues_count']


def print_trending_repositories(repositories):
    for repository in repositories:
        repository_info = get_repository_info(repository)
        print('{} {} open issues: {}'.format(repository_info[0],
                                             repository_info[1],
                                             repository_info[2]))

                                             
if __name__ == '__main__':
    last_week_date = get_last_week_day()
    trending_repositories = get_trending_repositories(20, last_week_date)
    print_trending_repositories(trending_repositories)
