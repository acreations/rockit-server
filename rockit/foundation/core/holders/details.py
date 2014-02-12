from rockit.foundation.core.holders.holder import Holder

class DetailsHolder(Holder):

    def add_details(self, title, value):
        self.append({
            'title': title,
            'value': value
            })
