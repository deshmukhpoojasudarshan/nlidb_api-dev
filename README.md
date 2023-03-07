# nlidb_api


#
# Environment Setup
#

Create a virtual environment using Conda :
conda create -n nlidb

Activate the virtual environment :
conda activate nlidb

Install the project dependencies :
pip install -r requirements.txt 


#
# Run Project
#


From the project root folder execute the below command.

uvicorn --reload --port 8000 app.main:app
