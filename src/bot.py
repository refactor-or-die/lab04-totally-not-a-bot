from abc import ABC, abstractmethod
import random
from typing import Dict
from platform import Platform

# Abstrakcja (CO generuje)
class Bot(ABC):
    def __init__(self, platform: Platform):
        self.platform = platform  # <-- TO JEST MOST!
    
    @abstractmethod
    def generate_content(self, topic: str) -> str:
        pass
    
    def generate_post(self, topic: str) -> Dict:
        content = self.generate_content(topic)
        formatted = self.platform.format_message(topic, content)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform.platform_type,
            "topic": topic,
            "content": formatted
        }
        

class Troll(Bot):
    bot_type = "Troll"
    def generate_content(self, topic: str) -> str:
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        return random.choice(provocations)

class Spammer(Bot):
    bot_type = "Spammer"
    def generate_content(self, topic: str) -> str:
        

class Conspiracist(Bot):
    bot_type = "Conspiracist"
    def generate_content(self, topic: str) -> str:

class FakeNews(Bot):
    bot_type = "FakeNews"
    def generate_content(self, topic: str) -> str:

