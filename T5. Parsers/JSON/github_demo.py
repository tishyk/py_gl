from github import Github
from pprint import pprint
import getpass

guser = 'tishyk'
gpass = getpass.getpass("password:")

GITHUB = Github(guser, gpass)
REPOS = [_ for _ in GITHUB.get_user('tishyk').get_repos()]

pprint('Total public repos: {}'.format(GITHUB.get_user().public_repos))
pprint('Total private repos: {}'.format(GITHUB.get_user().total_private_repos))
pprint(REPOS)

