from abc import ABC, abstractmethod


class AIPlatform(ABC):
    @abstractmethod
    def chat(self, prompt: str) -> str:
        """Sends a prompt to the AI platform and returns the response."""
        pass
