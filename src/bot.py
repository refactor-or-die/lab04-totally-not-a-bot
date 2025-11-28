from abc import ABC, abstractmethod
import random
from typing import Dict
from social_platform import SocialPlatform

# Abstrakcja (CO generuje)
class Bot(ABC):
    def __init__(self, platformObj: SocialPlatform):
        self.platformObj = platformObj  # <-- TO JEST MOST!
        self.platform = self.platformObj.platform_type
    
    @abstractmethod
    def generate_content(self, topic: str) -> str:
        pass
    
    def generate_post(self, topic: str) -> Dict:
        content = self.generate_content(topic)
        formatted = self.platformObj.format_message(topic, content)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
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
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        return random.choice(spam_templates)

class Conspiracist(Bot):
    bot_type = "Conspiracist"
    def generate_content(self, topic: str) -> str:
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?  Czy to jest prawda?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu. Czy to jest prawda?",
            f"Oni nie chca zebys wiedzial prawde o {topic}. Czy to jest prawda?"
        ]
        return random.choice(conspiracies)
    
class FakeNews(Bot):
    bot_type = "FakeNews"
    def generate_content(self, topic: str) -> str:
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        return random.choice(fake_news)
