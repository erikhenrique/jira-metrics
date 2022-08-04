from abc import ABC, abstractmethod


class Exporter(ABC):

    def build_headers(self, issues):
        headers = set()
        for issue in issues:
            headers.update(issue.keys())
        return headers
    
    @abstractmethod
    def export(self, issues) -> None:
        pass
