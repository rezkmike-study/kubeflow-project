#!/bin/bash

# Message passed as an argument
MESSAGE=$1

# Slack webhook URL
WEBHOOK_URL="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# Send notification to Slack
curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"${MESSAGE}\"}" $WEBHOOK_URL
