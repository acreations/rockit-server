from rockit.core.holders import Holder

class ErrorHolder(Holder):
    """
    Error holder
    """
    def __init__(self):
        super(ErrorHolder, self).__init__()

    def add_error(self, id, message):
        """
        Add error
        """
        self.append({ id: message })

    def get_errors(self):
        """
        Get all errors
        """
        if self.get_content():
            return self.get_content()['items']
        return [];

    def has_errors(self):
        """
        Check if any errors exist in this holder
        """
        return len(self.get_errors()) > 0