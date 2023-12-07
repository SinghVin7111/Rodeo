# Project Setup Instructions

## Installation

1. **Install the `virtualenv` package:**

    Use the following command to install the `virtualenv` package:

    ```bash
    pip install virtualenv
    ```

2. **Create a Virtual Environment:**

    In your project directory, create a virtual environment by running:

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**

    Activate the virtual environment using the following command:

    On Windows:
    ```bash
    venv\Scripts\activate
    ```

    On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```

4. **Install Dependencies:**

    With the virtual environment active, install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

- **Start the Application:**

    Run your `main.py` file using Streamlit:

    ```bash
    streamlit run main.py
    ```

Remember to activate your virtual environment each time you work on the project.
