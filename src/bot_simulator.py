"""
Symulator botow internetowych (w celach edukacyjnych!).
UWAGA: Ten kod ma EKSPLOZJE KLAS! Uzyj wzorca Bridge.

Mamy 4 typy botow i 4 platformy = 16 klas.
Dodanie nowej platformy wymaga 4 nowych klas!
Dodanie nowego bota wymaga 4 nowych klas!

To nie jest skalowalne rozwiazanie...
"""
from typing import Dict
from abc import ABC, abstractmethod
import random

# ============================================================================
# BOTY 
# ============================================================================

class Bot(ABC):
    abstractmethod
    def __init__(self, platform):
        pass
    abstractmethod
    def generate_post(self, topic: str) -> Dict:
        pass
        
    def generate_formatted(self, content: str) -> Dict:
        self.platform.generate_formatted(content)
    



class Troll(Bot):
    def __init__(self, platform):
        self.bot_type = "Troll"
        self.platform_type = platform

    def generate_post(self, topic: str) -> Dict:
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms",
            ]        
        content = random.choice(provocations)
        formatted = self.platform_type.generate_formatted(content, topic)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform_type.name,
            "topic": topic,
            "content": formatted
        }
        

class Spammer(Bot):
    def __init__(self, platform):
        self.bot_type = "Spammer"
        self.platform_type = platform

    def generate_post(self, topic: str) -> Dict:
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        content = random.choice(spam_templates)
        formatted = self.platform_type.generate_formatted(content, topic)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform_type.name,
            "topic": topic,
            "content": formatted
        }
    

class Conspiracist(Bot):
    def __init__(self, platform):
        self.bot_type = "Conspiracist"
        self.platform_type = platform

    def generate_post(self, topic: str) -> Dict:
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        content = random.choice(conspiracies)
        formatted = self.platform_type.generate_formatted(content, topic)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform_type.name,
            "topic": topic,
            "content": formatted
        }

class FakeNews(Bot):
    def __init__(self, platform):
        self.bot_type = "FakeNews"
        self.platform_type = platform

    def generate_post(self, topic: str) -> Dict:
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        content = random.choice(fake_news)
        formatted = self.platform_type.generate_formatted(content, topic)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform_type.name,
            "topic": topic,
            "content": formatted
        }

# ============================================================================
# PLATFORMY 
# ============================================================================

class Platform(ABC):
    abstractmethod
    def generate_formatted(self, content: str, topic: str) -> str:
        pass
        

class Twitter(Platform):
    def __init__(self):
        self.name = "Twitter"
    def generate_formatted(self, content: str, topic: str) -> str:
        formatted = f"ratio dm 🚀 🧵 ⚠️ #pizza prawda szok"
        return formatted


class Facebook(Platform):
    def __init__(self):
        self.name = "Facebook"
    def generate_formatted(self, content: str, topic: str) -> str:
        formatted = f"PILNE alert   ,chora kuzynka udostepnij chca zarobil {content} {topic}"
        return formatted


class LinkedIn(Platform):
    def __init__(self):
        self.name = "LinkedIn"
    def generate_formatted(self, content:str, topic:str) -> str:
        formatted = f"Unpopular opinion: {content}, confirmed\n\n"
        formatted += "I know this might be controversial, but someone had to announce it.\n\n"
        formatted += "Agree? ♻️ Repost to spread awareness\n"
        formatted += "#industry #Disruption #Controversial moon truth"
        return formatted
class TikTok(Platform):
    def __init__(self):
        self.name = "TikTok"
    def generate_formatted(self, content:str, topic:str) -> str:
        formatted = f"pov: ktos mowi ze {topic} ma sens 💀💀💀\n"
        formatted += f"bestie... {content}\n"
        formatted += "its giving delulu 😭 no cap fr fr truth szok krejzi storytime 1000x 🤯🤯🤯"
        return formatted


# ============================================================================
# Mega Adapter Removal Technique - certified magic
# ============================================================================

def create_bot_adapter(bot_class, platform_class):
    """Factory Method - generuje klase adaptera"""
    class BotAdapter:
        def __init__(self):
            self._bot = bot_class(platform_class())
            self.bot_type = self._bot.bot_type
            self.platform = self._bot.platform_type.name
        
        def generate_post(self, topic):
            return self._bot.generate_post(topic)
    
    return BotAdapter  # Zwraca KLASE !?!??!!??!?!?!?!?!?

bot_types = {
    "Troll": Troll,
    "Spammer": Spammer,
    "Conspiracist": Conspiracist,
    "FakeNews": FakeNews
}

platforms = {
    "Twitter": Twitter,
    "Facebook": Facebook,
    "LinkedIn": LinkedIn,
    "TikTok": TikTok
}

# Magia!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for bot_name, bot_class in bot_types.items():
    for platform_name, platform_class in platforms.items():
        class_name = f"{bot_name}{platform_name}Bot"
        globals()[class_name] = create_bot_adapter(bot_class, platform_class)

# ============================================================================
# FUNKCJA POMOCNICZA
# ============================================================================

def get_bot(bot_type: str, platform: str):
    class_name = f"{bot_type}{platform}Bot"

    if class_name not in globals():
        raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform}'")

    return globals()[class_name]()


# Przykladowe uzycie
if __name__ == "__main__":
    print("=" * 60)
    print("SYMULATOR BOTOW INTERNETOWYCH")
    print("(w celach edukacyjnych!)")
    print("=" * 60)
    
    # Ustawmy seed dla powtarzalnosci
    random.seed(42)
    
    bot_types = ["Troll", "Spammer", "Conspiracist", "FakeNews"]
    platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
    topics = ["AI", "szczepionki", "5G", "kryptowaluty"]
    
    for bot_type in bot_types:
        print(f"\n{'='*60}")
        print(f"TYP BOTA: {bot_type}")
        print("=" * 60)
        
        for platform in platforms:
            bot = get_bot(bot_type, platform)
            topic = random.choice(topics)
            result = bot.generate_post(topic)
            
            print(f"\n[{platform}] Temat: {topic}")
            print("-" * 40)
            print(result["content"])