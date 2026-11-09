
# CMSC 426 - Jenkins CI Project

## Overview

This project demonstrates Continuous Integration (CI)
using GitHub, Jenkins, and automated Python testing.

## Technologies

- Python 3
- Python unittest
- Git and GitHub
- Jenkins

## Application Features

- Addition
- Subtraction
- Multiplication

## Run the Application

```bash
python app.py
```

## Run Automated Tests

```bash
python -m unittest discover -s tests -v
```

## CI Workflow

1. A developer pushes changes to GitHub.
2. Jenkins detects a configured build trigger.
3. Jenkins retrieves the latest source code.
4. Jenkins runs automated unit tests.
5. Jenkins reports build success or failure.

## Course

CMSC 426 - In-Class Activity #3

## Webhook Verification
This commit tests automatic Jenkins builds.
