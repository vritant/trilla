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
      rule1:
          from: BUG_ASSIGNED
          to: CARD_BOARD_LIST
    -
      rule 2:
          from: "BUG_ASSIGNED, BUG_NEW"
          to: CARD_BOARD_LIST
    -
      rule3:
          from: CARD_BOARD_LIST
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
