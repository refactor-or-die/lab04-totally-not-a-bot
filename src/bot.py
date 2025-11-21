from abc import ABC, abstractmethod
from random import random
from typing import Dict

class Platform(ABC):
    @abstractmethod
    def format_message(self, message: str) -> str:
        pass


class Bot(ABC):
    def __init__(self, platform: Platform):
        self.bot_type = self.__class__.__name__
        self.platform = platform

    @abstractmethod
    def generate_content(self, topic: str) -> str:
        pass

    def generate_post(self, topic: str) -> Dict:
        content = self.generate_content(topic)
        formatted = self.platform.format_message(content)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform.__class__.__name__,
            "topic": topic,
            "content": formatted
        }

class Troll(Bot):
    def generate_content(self, topic: str) -> str:
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        content = random.choice(provocations)
        return content
    
class Spammer(Bot):
    