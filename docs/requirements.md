Note: intent is to split this into appropriate documents later.
## Requirements
### Phase 1 - bugzilla and trello integration
* search bugs using search criteria and mark them as tracked.
* sync tracked bugs with trello cards.
 * create trello card from tracked bugs if it does not exist
 * move it to the appropriate queue based on a bz state and trello queue mapping
 * make sure the assignee is a member of the trello card ( if the user exists in trello )

### Phase 2 - trello and github integration - this is a little vague right now, we can work on this later.
* sync tracked trello cards with github pull requests / issues
 * create trello cards from github issues / PRs if it does not exist ( let a user skip some if he wants to )
 * move it to the appropriate queue based on a PR state - trello queue - bz state mapping.
 * make sure the issue reporter, author of the PR and assignee of the PR is a member of the trello card ( if the user exists in trello )

