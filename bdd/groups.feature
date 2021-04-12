Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When i add the group to the list
  Then the new group list is equal to the old list with the added one


  Examples:
  | name  | header  | footer  |
  | name1 | header1 | footer1 |
  | name2 | header2 | footer2 |


Scenario: Delete a group
  Given a non-empty group list
  Given a random group from the list
  When i delete a group from the group list
  Then The new list becomes less then old group list on one
