### RULES CONFIGURATION
* Users can define a list of rules in the config file.
* A profile can be configured to apply a subset of rules defined using the rule names.
* format of a rule is :
```
      name: rule name
      from: ENTITY_STATE(, ENTITY_STATE)
      to: ENTITY_STATE
```
* where an **entity_state** definition could be one of:
  * BUG_*bugId*
  * CARD_*boardName*_*listName*
  * ISSUE_*label*
  * PR_*label*
* for all tracked etities, if the state of the entity matches one of the states in the 'from' state, trilla ensures there is a corresponding entity in the 'to' state.
