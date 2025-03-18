# This file contains the different endpoints your bot can use.

# Server where the models are pulled from.
# https://rasa.com/docs/rasa/model-storage#fetching-models-from-a-server
models:
  url: http://my-server.com/models/default/core/latest
  wait_time_between_pulls: 10  # [optional] (default: 100)

# Server which runs your custom actions.
# https://rasa.com/docs/rasa/custom-actions
action_endpoint:
  url: "http://localhost:5055/webhook"

# Tracker store which is used to store the conversations.
# By default, the conversations are stored in memory.
# https://rasa.com/docs/rasa/tracker-stores

# Uncomment and configure one of the following tracker stores:

# Redis Tracker Store
# tracker_store:
#   type: redis
#   url: "localhost"
#   port: 6379
#   db: 0
#   password: "<password used for authentication>"

# MongoDB Tracker Store
# tracker_store:
#   type: mongod
#   url: "mongodb://localhost:27017"
#   db: "rasa"
#   username: "<username used for authentication>"
#   password: "<password used for authentication>"
