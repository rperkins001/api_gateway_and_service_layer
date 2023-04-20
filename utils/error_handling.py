class CustomError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code

def handle_error(error):
    print(f"Error: {error}")
    # Perform additional error handling, such as logging or sending alerts
