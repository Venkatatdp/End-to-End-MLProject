import os
import logging
from pathlib import Path

class Logger:
    """Overall, this Logger class provides a structured way to log messages to 
    both the console and a file, with varying levels of severity. 
    This is particularly useful for monitoring and debugging applications."""

    def __init__(self,logfile):
        # creating a Logger Object
        self.logger = logging.getLogger(__name__)
        # Setting the logging level
        self.logger.setLevel(logging.INFO)
        # Creating Streamhandler to send the logging ouput to console or Terminal
        streamhandler = logging.StreamHandler()
        """Creating Filehandler to write logging messages to the 
        logfile which is one of the input params"""
        filehandler = logging.FileHandler(logfile)
        # Create a format for log messages
        """It includes the timestamp (asctime), the module name (name),
         the severity level of the message (levelname)
         and the actual log message (message)."""
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # Adding the format to streamhandler
        streamhandler.setFormatter(formatter)
        #Adding the format to filehandler
        filehandler.setFormatter(formatter)
        # Adding the handlers to logger object so that it starts writing to console and logfile
        self.logger.addHandler(streamhandler)
        self.logger.addHandler(filehandler)

    def log(self,msg,level='info') -> None:
        '''This method is used for saving various levels of logging'''
        if level == 'info':
            self.logger.info(msg)
        elif level == 'error':
            self.logger.error(msg,exc_info=True)
        elif level == 'warning':
            self.logger.warning(msg)




class CreateProjectStructure:
    """This class is used to create the project folder structure Dynamically"""
    def __init__(self,logger):
        self.logger = logger

    def create_folders(self,project_name):
        """ This function creates list of all the files and folders required for the project"""
        list_of_files = [
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/utils/common.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/entity/config_entity.py",
        f"src/{project_name}/constants/__init__.py",
        "config/config.yaml",
        "params.yaml",
        "schema.yaml",
        "main.py",
        "app.py",
        "requirements.txt",
        "setup.py",
        "research/trials.ipynb",
        "templates/index.html"]
        for file_path in list_of_files:
            filepath = Path(file_path)
            self.logger.log(f"path of {file_path} : {filepath}","info")
            filedir,filename = os.path.split(filepath)
            if filedir != '':
                os.makedirs(filedir,exist_ok=True)
                self.logger.log(f"Creating directory; {filedir} for the file: {filename}","info")
            if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
                with open(filepath,'w'):
                    self.logger.log(f"Creating empty file: {filepath}","info")
            else:
                self.logger.log(f"{filename} is already exists")

if __name__ == "__main__":
    logger = Logger(f"{os.path.join(os.getcwd(),'Tracker.log')}")
    project_structure = CreateProjectStructure(logger)
    project_structure.create_folders('mlProject')