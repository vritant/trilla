# -*- coding: utf-8 -*-

import click

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
@pass_config
def bugs(config):
    """Track bugzillla bugs"""
    click.echo("Profile %s" % config.profile)

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
