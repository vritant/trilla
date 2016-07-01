# -*- coding: utf-8 -*-

import sys
import trilla
from okaara.cli import Cli, Section, Command
from config import Config, NotConfiguredError, ConfigurationError

class BaseCommand(Command):
    def __init__(self, name, description, action, prompt):
        Command.__init__(self, name, description, action)
        self.prompt = prompt
        self.create_option('--profile', "the target configuration profile", required=False,
            aliases=['-p'])


class ConfigurationCommand(BaseCommand):
    def __init__(self, prompt):
        BaseCommand.__init__(self, "config", "use to configure trilla", self.configure, prompt)

    def configure(self):
        self.prompt.write("Implement the configure command.")


class ConfigurationReadyCommand(BaseCommand):
    def __init__(self, name, description, action, prompt):
        BaseCommand.__init__(self, name, description, self._do_command, prompt)
        self.action = action

    def _do_command(self, **kwargs):
        try:
            config = Config(kwargs['profile'])
        except NotConfiguredError, e:
            self.prompt.write("trilla is not configured. Run 'trilla config' to configure it!")
            sys.exit(1)
        except ConfigurationError, e:
            self.prompt.write(e.message )
            sys.exit(1)
        self.action(config, **kwargs)

    
class TrillaCli(Cli):
    def __init__(self):
        Cli.__init__(self)
        self.add_section(TrackSection(self.prompt))
        
        sync_command = ConfigurationReadyCommand('sync', "sync tracked entities", self.sync,
            self.prompt)
        sync_command.create_flag('--all', "sync all tracked bugs, github issues and PRs",)
        sync_command.create_flag('--all-bugs', "sync all tracked bugs")
        sync_command.create_flag('--all-prs', "sync all tracked pull requests")
        sync_command.create_flag('--all-issues', "sync all tracked github issues")
        self.add_command(sync_command)
        
        untrack_command = ConfigurationReadyCommand('untrack', "untrack entities", self.untrack,
            self.prompt)
        self.add_command(untrack_command)
        
        self.add_command(ConfigurationCommand(self.prompt))

    def sync(self, config, **kwargs):
        self.prompt.write("Using profile: %s" % config.profile)
        self.prompt.write("Implement sync command %s" % kwargs['all'])
    
    def untrack(self, config, **kwargs):
        self.prompt.write("Implement untrack command.")


class TrackSection(Section):
    def __init__(self, prompt):
        Section.__init__(self, 'track', 'Track entities')
        self.prompt = prompt
        
        track_bugs_command = ConfigurationReadyCommand('bugs', "track bugs", self.bugs, self.prompt)
        track_bugs_command.create_option('--url', "the bugzilla url", default="bugzilla.redhat.com")
        self.add_command(track_bugs_command)
        
        track_prs_command = ConfigurationReadyCommand('prs', "track github pull requests",
            self.pull_requests, self.prompt)
        self.add_command(track_prs_command)
        
        track_issues_command = ConfigurationReadyCommand('issues', "track github issues",
            self.issues, self.prompt)
        self.add_command(track_issues_command)
        

    def bugs(self, config, **kwargs):
        """Track bugzillla bugs"""
        url = kwargs['url']
        bugs = trilla.get_bugs(url, config)
        for bug in bugs:
            self.prompt.write(str(bug.id) + "\n")

    def pull_requests(self, config, **kwargs):
        self.prompt.write("Implement track PRs")

    def issues(self, config, **kwargs):
        self.prompt.write("Implement track issues")
        

def run():
    sys.exit(TrillaCli().run(sys.argv[1:]))

if __name__ == "__main__":
    run()

