# install the venv package by running the following command
  
pip install virtualenv

# Create a virtual environment for your project by running the following command in the Replit terminal
  
python -m venv venv

#  Activate the virtual environment by running the appropriate command

venv\Scripts\activate

# Once the virtual environment is activated, install the necessary dependencies from the requirements.txt file by running the following command

pip install -r requirements.txt

#  With the virtual environment active and the dependencies installed, run the main.py file by entering the following command

streamlit run main.py
