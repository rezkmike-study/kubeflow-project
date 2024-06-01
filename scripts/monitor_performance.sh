#!/bin/bash

# Define the URL of your application
URL="http://your-application-url.com"

# Filename to store the performance log
LOGFILE="performance_log.txt"

# Function to get HTTP response time
function check_response_time() {
    # Using curl to fetch the HTTP header and extracting time details
    RESPONSE=$(curl -o /dev/null -s -w "Connect: %{time_connect}s\nTTFB: %{time_starttransfer}s\nTotal time: %{time_total}s\nHTTP Code: %{http_code}\n" $URL)

    # Log the response time and status to a logfile
    echo "$(date): $RESPONSE" >> $LOGFILE
}

# Function to summarize the performance
function summarize_performance() {
    echo "Performance Summary:"
    awk '/Total time:/ {print $3}' $LOGFILE | awk '{sum+=$1; count+=1} END {print "Average Response Time: ", sum/count, "s"}'
}

# Main execution block
echo "Starting performance monitoring for $URL"
check_response_time
summarize_performance
echo "Performance monitoring completed."
