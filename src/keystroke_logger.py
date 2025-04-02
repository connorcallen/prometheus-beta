import logging
import datetime
import os

class KeystrokeLogger:
    """
    A class to log keystrokes with customizable logging options.
    
    Attributes:
        log_file (str): Path to the log file
        logger (logging.Logger): Logger instance for recording keystrokes
    """
    
    def __init__(self, log_file='keystrokes.log'):
        """
        Initialize the KeystrokeLogger.
        
        Args:
            log_file (str, optional): Path to the log file. Defaults to 'keystrokes.log'.
        """
        # Ensure log directory exists
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # Configure logging
        self.log_file = log_file
        self.logger = logging.getLogger('KeystrokeLogger')
        self.logger.setLevel(logging.INFO)
        
        # Create file handler
        file_handler = logging.FileHandler(self.log_file, mode='a')
        file_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        # Add handler to logger
        self.logger.addHandler(file_handler)
    
    def log_keystroke(self, key):
        """
        Log a single keystroke.
        
        Args:
            key (str): The keystroke to log
        
        Raises:
            ValueError: If the input is not a single character
        """
        if not isinstance(key, str):
            raise ValueError("Keystroke must be a string")
        
        if len(key) != 1:
            raise ValueError("Only single characters can be logged")
        
        # Log the keystroke
        self.logger.info(f"Keystroke: {key}")
    
    def log_text(self, text):
        """
        Log multiple keystrokes from a text input.
        
        Args:
            text (str): The text to log
        
        Raises:
            ValueError: If the input is not a string
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        # Log each character in the text
        for char in text:
            self.log_keystroke(char)
    
    def clear_log(self):
        """
        Clear the existing log file.
        """
        with open(self.log_file, 'w'):
            pass  # Truncate the file