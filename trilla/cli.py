# -*- coding: utf-8 -*-

import click
from config import Config, NotConfiguredError, ConfigurationError
from trilla import Trilla

pass_config = click.make_pass_decorator(Config)

@click.group()
@click.option('--profile','-p', help="profile name")
@click.pass_context
def main(ctx, profile):
    """Console script for trilla"""
    ctx.obj = Config(profile)

@main.group()
@pass_config
def search(config):
    """Search entities"""
    pass

@search.command()
@click.option('--url', default="bugzilla.redhat.com", help="bugillz url")
@click.option('--include', '-i', multiple=True,
              type=click.Choice(['product', 'component', 'version',
                                  'assigned_to', 'qa_contact', 'status',
                                    'depends_on', 'keywords', 'severity',
                                      'priority', 'summary']))
@click.argument('output', type=click.File('wb'), default="-")
@pass_config
def bugs(config, url, include, output):
    """Track bugzillla bugs"""
    config.update_bzilla(url)
    trilla = Trilla(config)
    include = list(include)
    bugs = trilla.get_bugs(url, config, include)
    output.write(bugs)

@search.command()
@click.option('--trello-board', '-b', help="the target trello board")
@click.option('--trello-list', '-l', help="the target list")
@click.option('--api-token', help="trello's API token")
@click.option('--api-secret', help="trello's API secret")
@click.option('--oauth-token', help="trello's OAuth token")
@click.option('--oauth-token-secret', help="trello's oauth token secret")
@click.argument('output', type=click.File('wb'), default="-")
@pass_config
def cards(config, trello_board, trello_list, api_token, api_secret, oauth_token,
    oauth_token_secret, output):
    """Track trello cards"""
    # Set the trello parameter overrides
    config.update_trello(api_token, api_secret, oauth_token, oauth_token_secret)
    trilla = Trilla(config)
    cards = trilla.list_cards(trello_board, trello_list)
    if len(cards) == 0:
        output.write("No cards found.\n")
        return
    for card in cards:
        output.write("%s -- %s\n" % (card.name, card.description))

@search.command()
@pass_config
def prs(config):
    """Track github PRs"""
    output.write("Implement me!!!")

@search.command()
@pass_config
def issues(config):
    """Track github issues"""
    output.write("Implement me!!!")

@main.group()
@pass_config
@click.argument('input', type=click.File('rb'))
def track(config):
    """Track entities"""
    pass

@main.command()
@click.option('--all-bugs', help="sync all tracked bugzilla bugs")
@click.option('--all-prs', help="sync all tracked github PRs")
@click.option('--all-issues', help="sync all tracked github issues")
@click.option('--all', help="sync all tracked bugs, github issues and PRs")
@pass_config
def sync(config, all_bugs, all_prs, all_issues, all):
    """Sync tracked entities"""
    click.echo('Implement Sync command')

@main.command()
@pass_config
def untrack(config):
    """Untrack specific entities"""
    click.echo('Implement untrack')

if __name__ == "__main__":
    main()

