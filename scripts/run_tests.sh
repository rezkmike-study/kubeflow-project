#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run tests using a testing framework like pytest
# This can also include linting, type checks, etc.
pytest tests/ --junitxml=test_report.xml

# Deactivate virtual environment
deactivate
