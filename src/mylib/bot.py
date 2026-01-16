from abc import ABC, abstractmethod
import random
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
    def __init__(self, platform):
        super().__init__(platform)

    def generate_content(self, topic: str) -> str:
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        return random.choice(provocations)
    
class Spammer(Bot):
    def __init__(self, platform):
        super().__init__(platform)
    
    def generate_content(self, topic: str) -> str:
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        content = random.choice(spam_templates)
        return content
     
class Conspiracist(Bot):
    def __init__(self, platform):
        super().__init__(platform)

    def generate_content(self, topic: str) -> Dict:
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        content = random.choice(conspiracies)
        return content

class FakeNews(Bot):
    def __init__(self, platform):
        super().__init__(platform)

    def generate_content(self, topic: str) -> Dict:
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        content = random.choice(fake_news)
        return content

class TikTok(Platform):
    def format_message(self, message: str) -> str:
        # TikTok formatowanie
        formatted = f"STORYTIME: so i just found out something crazy 😱\n"
        formatted += f"{message}\n"
        formatted += "share before they take this down!! part 2 if this blows up 👀"
        return formatted

class Twitter(Platform):
    def format_message(self, message: str) -> str:
        # Twitter formatowanie
        formatted = f"⚠️ {message} RETWEET zanim zcenzuruja! #Breaking #News"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        return formatted
    
class Facebook(Platform):
    def format_message(self, message: str) -> str:
        # Twitter formatowanie
        # Facebook formatowanie
        formatted = f"🔴 PILNE 🔴\n\n"
        formatted += f"{message}\n\n"
        formatted += "Media MILCZA! Udostepnij swoim znajomym!!! "
        formatted += "Twoja rodzina MUSI to zobaczyc!!! ⚠️⚠️⚠️"
        return formatted
    
class LinkedIn(Platform):
    def format_message(self, message: str) -> str:
        # LinkedIn formatowanie
        formatted = f"🚨 Industry Alert 🚨\n\n"
        formatted += f"{message}\n\n"
        formatted += "My sources in the industry have confirmed this.\n\n"
        formatted += "Share with your network before it's too late.\n"
        formatted += "#BreakingNews #IndustryInsider #MustRead"
        return formatted