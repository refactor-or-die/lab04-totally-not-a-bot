from typing import Dict
import random
from abc import ABC, abstractmethod

class Platform(ABC):
    @abstractmethod
    def format_message(self, message: str) -> str:
        pass

class Bot(ABC):
    def __init__(self, platform: Platform):
        self.platform = platform
    
    @abstractmethod
    def generate_content(self, topic: str) -> str:
        pass
    
    def generate_post(self, topic: str) -> Dict:
        content = self.generate_content(topic)
        formatted = self.platform.format_message(content)
        return {
            "bot_type": self.__class__.__name__,
            "platform": self.platform.__class__.__name__,
            "topic": topic,
            "content": formatted
        }

class Twitter(Platform):
    def format_message(self, message: str) -> str:
        formatted = message + " #triggered"
        if len(formatted) > 280:
            formatted = message[:277-len(" #triggered")] + "... #triggered"
        return formatted

# ZMIANA: Tiktok -> TikTok (wielka litera T)
class TikTok(Platform):
    def format_message(self, message: str) -> str:
        return f"bestie... {message}\nits giving delulu 😭 no cap fr fr"

class Facebook(Platform):
    def format_message(self, message: str) -> str:
        return f"{message}... PROSZE SIE OBUDZIC LUDZIE!!! Udostepnij zanim USUNĄ!!! 😠😠😠"

class LinkedIn(Platform):
    def format_message(self, message: str) -> str:
        return (f"Unpopular opinion: {message}\n\n"
                "I know this might be controversial, but someone had to say it.\n\n"
                "🚀🚀🚀 Agree? ♻️ Repost to spread awareness\n"
                "#ThoughtLeadership #Disruption #Controversial")

class Troll(Bot):
    def generate_content(self, topic: str) -> str:
        return f"Serio wierzysz w {topic}? SERIO!"

class Spammer(Bot):
    def generate_content(self, topic: str) -> str:
        return f"NOWY {topic} COIN! Zarobiles na {topic}? JA TAK! 1000x gwarantowane!"

class Conspiracist(Bot):
    def generate_content(self, topic: str) -> str:
        return f"Czy zastanawiales sie KOMU zalezy na {topic}? Oni ukrywa prawde!"

class FakeNews(Bot):
    def generate_content(self, topic: str) -> str:
        return f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne PILNE!!"

def get_bot(bot_type: str, platform: str) -> Bot:
    if bot_type not in ["Troll", "Spammer", "Conspiracist", "FakeNews"]:
        raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform}'")
    if platform not in ["Twitter", "Facebook", "LinkedIn", "TikTok"]:
        raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform}'")
    
    platform_instance = {
        "Twitter": Twitter(),
        "Facebook": Facebook(),
        "LinkedIn": LinkedIn(),
        "TikTok": TikTok()  # ZMIANA: Tiktok -> TikTok
    }[platform]
    
    bot_instance = {
        "Troll": Troll(platform_instance),
        "Spammer": Spammer(platform_instance),
        "Conspiracist": Conspiracist(platform_instance),
        "FakeNews": FakeNews(platform_instance)
    }[bot_type]
    
    return bot_instance