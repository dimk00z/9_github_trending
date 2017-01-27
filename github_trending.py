import requests
import json
from datetime import datetime, timedelta

GITHUB_API_LINK = "https://api.github.com/search/repositories"


def get_last_week_day():
    return(datetime.today().date() - timedelta(days=7))


def get_trending_repositories(first_date):
    get_params = {'q': 'created:>={0}'.format(first_date), 'sort': 'stars'}
    response_from_git = requests.get(GITHUB_API_LINK, params=get_params)
    json_from_response = json.loads(response_from_git.text)
    return json_from_response['items'][:20]


def print_trending_repositories(repositories):
    for repository in repositories:
        print('{} {} open issues: {}'.format(repository['html_url'],
                                             repository['full_name'],
                                             repository['open_issues_count']))


if __name__ == '__main__':
    last_week_date = get_last_week_day()
    trending_repositories = get_trending_repositories(last_week_date)
    print_trending_repositories(trending_repositories)
