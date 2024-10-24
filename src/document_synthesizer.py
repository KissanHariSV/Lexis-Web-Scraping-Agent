class Document:
    def __init__(self, url, summary):
        self.url = url
        self.summary = summary

    def to_dict(self):
        return {
            "url": self.url,
            "summary": self.summary
        }
