# Basic Fitness Training Focus Specifier App
## Video Demo:  <URL HERE>
### Description: A prompt based selection questionnaire that quickly generates a training split entry point, ie focus in to the target muscles using questions.

This functionality is for those too busy to consider their training needs and who need a nudge in the right direction.

Use this application to synthesis the most likely to be most productive route for getting on with your fitness focus rather than being halted in a guagmire of self doubting questions.

## Introduction

This is a basic CLI prompt app.
To run this, you need to install dependencies listed in the [requirement.txt](/project/requirements.txt)

### Install

Use the command :```sudo pip install -r requirements.txt```

### Running application

Use the command :```python project.py```

### Useage limits

The project in question is not a commercial output, it is a certification project, so it has design limits.

The main limitation when confronted with using this app is the requirement to input numbers present in each guiding prompt.

Failure to doing so will raise ValueError, and stop the application mid-step and will require, following instructions to arrive at one of the many endpoint specializiations.

## Details & Testing

If curious about the unit testing, ensure that [test_project.py](/project/test_project.py) is present with [project.py](/project/project.py)

### Running tests with pytest

If all is well and the local folder has requiste files, run the tests with commands below:

```pytest test_project.py```

For additional test, you can also use ```mypy project.py``` which was used in conjunction with type hints.
