### OPERATIONS
* The tool can be used to perform following operations:
 * search and filter bugzillas, github issues, pull requests to be tracked, and mark them tracked, create trello cards if none exist.
 * sync all tracked bugs with the cards
 * untrack specific entities

### NOTES
* the tool itself should not use its own database, and should rely on bugzilla keywords / github labels / trello labels to fetch the current state.
* The application will use a config file for ease of use:
 * [Example config file](https://github.com/vritant/trilla/blob/master/docs/example_config.md)

### USAGE
* usage: `trilla MODULE-NAME [MODULE-OPTIONS] [-p PROFILE-NAME]`
* examples:
 * track usages:
   * trilla track bugs --priority=HIGH --severity=HIGH --keywords=Triaged,EasyFix --states=NEW,ASSIGNED
    * trilla track issues --all
    * trilla track pr --labels=None --state=OPEN
 * sync usages:
   * trilla sync -p my_project_profile
  * untrack usages:
    * trilla untrack --bug=123123 --delete-card
