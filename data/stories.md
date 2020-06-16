## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## hello_world
* hello_world
  - action_hello_world_response

## search_resturant
* search_resturant
  - action_search_resturant


## corona_state
* corona_state
  - action_corona_tracker

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
