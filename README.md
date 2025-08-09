# GenAI-with-OpenAI
This Repo is for housing the Gen AI Application that uses Open AI in the backend

# Commands to use

# Command to install pipenv
pip install pipenv

# Command to install packages in pipfile
python -m pipenv install -d

# Login to pipenv shell
python -m pipenv shell

# Prerequisite
Add the file "OpenAIKey" along with GenAi_Chat.py and include the OpenAI Key in it. This key would be read in the application to call OpenAI API. For security reason, this key is not included in Git.

# Trigger the Job
python .\GenAi_Chat.py run

Upon running the above Python code a public URL would be generated, copy it onto a Browser and start playing with it.