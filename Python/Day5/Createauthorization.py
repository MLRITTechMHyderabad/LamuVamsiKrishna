import re
import json
import logging

# Set up logging (console output only)
logging.basicConfig(level=logging.INFO, format='%(asctime)s -%(levelname)s -%(message)s')

class LaunchAuthorizationSystem:
    """Handles nuclear launch authorization validation."""
    
    AUTH_PATTERN = r"^AUTH-[A-Z]{3}\d{3}-\d{4}-SECURE$"

    @staticmethod
    def validate_code(code):
        if(re.findall(LaunchAuthorizationSystem.AUTH_PATTERN,code)):
            logging.info("Authorization successfully verified")
            return True
        else:
            logging.error("Authorization is not verified")
            return False