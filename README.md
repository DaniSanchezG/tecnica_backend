# Django Rest Framework Project


  1. **Download Python:**
     
      Open your web browser and visit the official Python website at Python.org.
      
      Click on the download button that corresponds to your operating system. Python is available for Windows, macOS, and Linux.
      
      Once the download is complete, run the downloaded installation file.

  2. **Install Python**:
     
      On Windows:
      Run the downloaded Python installation file.
      
      Make sure to check the option "Add Python x.x to PATH" during the installation process. This will add Python to the system PATH, allowing you to run Python commands from any location in the command prompt.
      
      Click "Install Now" to start the installation.
      
      Once the installation is complete, you can verify that Python has been installed correctly by opening a command prompt and running the following command:
      ```sh
      python --version
      ```
      
      This should display the version of Python you just installed.
      
      On macOS:
      Run the downloaded Python installation file.
      
      Follow the instructions in the installer to complete the installation. You may be prompted to enter the administrator password during the process.
      
      After the installation, you can verify that Python has been installed correctly by opening Terminal and running the following command:
      ```sh
      python3 --version
      ```
      
      This should display the version of Python you just installed.
      
      On Linux (Ubuntu/Debian):
      Open a terminal.
      
      Update the package index:

      ```sh
      sudo apt update
      ```
      
      Install Python by running the following command:

      ```sh
      sudo apt install python3
      ```
      
      After the installation, you can verify that Python has been installed correctly by running the following command:
     
      ```sh
      python3 --version
      ```
      
      This should display the version of Python you just installed.
  
  3. **Verify pip Installation**:
     
      Once you have installed Python, pip should be automatically installed along with it. You can verify if pip has been installed correctly by running the following command in the terminal:
      
      On Windows:
      
      ```sh
      py -m pip --version
      ```
      
      On macOS and Linux:
      
      ```sh
      pip3 --version
      ```
      
      This should display the version of pip that has been installed. If you see the version number, it means that pip has been installed successfully on your system.
      
      Now you have Python and pip installed on your system and you're ready to start developing!

  4. **Downloading the Project from GitHub:**
      Open your terminal or command line.
      Navigate to the directory where you want to clone the project.
      Run the following command to clone the repository from GitHub:

      ```sh
      git clone https://github.com/DaniSanchezG/tecnica_backend.git
      ```
      
      Once the cloning is complete, navigate to the newly created directory:
     
     ```sh 
      cd project-name
     ```
     
      Replace project-name with the name of the directory created when cloning the repository.

  5. **Setting up the Development Environment:**
      Create a virtual environment for the project. Run the following command to create a new virtual environment using venv:

     ```sh
      python -m venv env
     ```
     
      Activate the virtual environment. Depending on your operating system, you can use one of the following commands:
      
      On Windows:
     
     ```sh
      env\Scripts\activate
     ```
     
      On macOS and Linux:

     ```sh
      source env/bin/activate
     ```
     
      Install the project dependencies using pip and the requirements.txt file:

      ```sh
      pip install -r requirements.txt
      ```
      
  6. **Configuring the Database:**
        Configure the database in your development environment. Open the settings.py file in your project and update the database configuration as needed. For example, you can configure SQLite for local use or use another database management system such as PostgreSQL or MySQL.

  7. **Running Database Migrations:**
      Run the database migrations to create the necessary tables and apply any changes to the database schema:

      ```sh
      python manage.py migrate
      ```

  8 .**Running the Development Server:**
  
      Once the above steps are completed, you can run the Django development server to see your application in action:

      python manage.py runserver

        
      Open your web browser and navigate to the address http://localhost:8000 to view your application.
