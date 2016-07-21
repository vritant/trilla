### ENTITIES
* Trilla can be used to sync the following entities
 * Bugzilla bugs ( phase 1 )
 * Trello cards ( phase 1 )
 * Github issues ( phase 2 )
 * Github pull requests ( phase 2 )

### OPERATIONS
* The tool can be used to perform following operations on the above entities:
 * **search** entities to be tracked, and output the search result in YAML format
 * **track** entities by accepting a list of entities in a YAML file and adding it to the database
 * **sync** specific / all tracked bugs based on rules defined in configurated profiles
 * **untrack** specific entities specified directly or based on profile rules
 * **configure** trilla if not already configured, via interactive questions. If already configured, open an editable file with current configuration.

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
