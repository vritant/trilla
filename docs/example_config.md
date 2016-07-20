```yaml
---
-
  profiles:
    -
      name: default
      bugzilla:
        tracker-keyword: tracker
        url: bugzilla.work.com
      rules:
        - "rule 1"
        - "rule 2"
      trello:
        api_key: aaa
        api_secret: aab
        oauth_token: aac
        oauth_token_secret: aad
    -
      name: override
      bugzilla:
        tracker-keyword: tracker
        url: bugzilla.home.com
      rules:
        - "rule 3"
        - "rule 2"
-
  rules:
    -
      from: BUG_ASSIGNED
      name: "rule 1"
      to: CARD_BOARD_LIST
    -
      from: "BUG_ASSIGNED, BUG_NEW"
      name: "rule 2"
      to: CARD_BOARD_LIST
    -
      from: CARD_BOARD_LIST
      name: "rule 3"
      to: ISSUE_LABEL_NAME
-
  users:
    -
      bugzilla: mynick@bugzilla.com
      github: mynick@github.com
      nick: "my nick"
      trello: mynick@mydomain.com
    -
      bugzilla: mynick@bugzilla.com
      github: mynick@github.com
      nick: "my nick 2"
      trello: mynick@mydomain.com
---
```
