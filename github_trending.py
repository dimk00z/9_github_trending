import requests
import json
from datetime import datetime, timedelta


def get_first_day(number_of_days_ago=7):
    return(datetime.today().date() - timedelta(number_of_days_ago))


def get_trending_repositories(first_date,
                              count_repositories_for_request=20):
    github_api_link = "https://api.github.com/search/repositories?"
    get_params = {'q': 'created:>={0}'.format(first_date),
                  'sort': 'stars',
                  'per_page': count_repositories_for_request}
    response_from_github = requests.get(github_api_link, params=get_params)
    return json.loads(response_from_github.text)['items']


def print_trending_repositories(repositories):
    for repository in repositories:
        print('{} {} open issues: {}'.format(repository['html_url'],
                                             repository['full_name'],
                                             repository['open_issues_count']))


if __name__ == '__main__':
    trending_repositories = get_trending_repositories(get_first_day())
    print_trending_repositories(trending_repositories)
