# -*- coding: utf-8 -*-

import click
import trilla

class Config(object):
    def __init__(self):
        self.profile = "default"

pass_config = click.make_pass_decorator(Config, ensure = True)

@click.group()
@click.option('--profile','-p', default = "default", help="profile name")
@pass_config
def main(config, profile):
    """Console script for trilla"""
    config.profile = profile
    pass

@main.group()
def track():
    """Track entities"""

@track.command()
@click.option('--url', default="bugzilla.redhat.com", help="bugillz url")
@click.argument('output', type=click.File('wb'))
@pass_config
def bugs(config, url, output):
    """Track bugzillla bugs"""
    bugs = trilla.get_bugs(url, config)
    for bug in bugs:
        output.write(str(bug.id) + "\n")

@track.command()
@pass_config
def prs(config):
    """Track github PRs"""

@track.command()
@pass_config
def issues(config):
    """Track github issues"""

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
