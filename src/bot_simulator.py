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
# Adaptery do testów
# ============================================================================

class TrollTwitterBot:   
    def __init__(self):
        self.bot = Troll(Twitter())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)       
class TrollFacebookBot:
    def __init__(self):
        self.bot = Troll(Facebook())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name

    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)
        
class TrollLinkedInBot:
    def __init__(self):
        self.bot = Troll(LinkedIn())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class TrollTikTokBot:
    def __init__(self):
        self.bot = Troll(TikTok())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class SpammerTwitterBot:    
    def __init__(self):
        self.bot = Spammer(Twitter())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)



class SpammerFacebookBot:    
    def __init__(self):
        self.bot = Spammer(Facebook())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)



class SpammerLinkedInBot:    
    def __init__(self):
        self.bot = Spammer(LinkedIn())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)



class SpammerTikTokBot:   
    def __init__(self):
        self.bot = Spammer(TikTok())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)


class ConspiracistTwitterBot:   
    def __init__(self):
        self.bot = Conspiracist(Twitter())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)


class ConspiracistFacebookBot:    
    def __init__(self):
        self.bot = Conspiracist(Facebook())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)


class ConspiracistLinkedInBot:   
    def __init__(self):
        self.bot = Conspiracist(LinkedIn())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)


class ConspiracistTikTokBot:    
    def __init__(self):
        self.bot = Conspiracist(TikTok())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class FakeNewsTwitterBot:    
    def __init__(self):
        self.bot = FakeNews(Twitter())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)


class FakeNewsFacebookBot:    
    def __init__(self):
        self.bot = FakeNews(Facebook())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class FakeNewsLinkedInBot:   
    def __init__(self):
        self.bot = FakeNews(LinkedIn())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)


class FakeNewsTikTokBot:
    def __init__(self):
        self.bot = FakeNews(TikTok())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform_type.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)


# ============================================================================
# FUNKCJA POMOCNICZA
# ============================================================================

def get_bot(bot_type: str, platform: str):
    """
    Zwraca odpowiedniego bota dla danego typu i platformy.
    
    SPÓJRZ NA TE IFY! 16 kombinacji! A co jak dodamy Mastodon i Reddit?
    """
    if bot_type == "Troll":
        if platform == "Twitter":
            return TrollTwitterBot()
        elif platform == "Facebook":
            return TrollFacebookBot()
        elif platform == "LinkedIn":
            return TrollLinkedInBot()
        elif platform == "TikTok":
            return TrollTikTokBot()
    elif bot_type == "Spammer":
        if platform == "Twitter":
            return SpammerTwitterBot()
        elif platform == "Facebook":
            return SpammerFacebookBot()
        elif platform == "LinkedIn":
            return SpammerLinkedInBot()
        elif platform == "TikTok":
            return SpammerTikTokBot()
    elif bot_type == "Conspiracist":
        if platform == "Twitter":
            return ConspiracistTwitterBot()
        elif platform == "Facebook":
            return ConspiracistFacebookBot()
        elif platform == "LinkedIn":
            return ConspiracistLinkedInBot()
        elif platform == "TikTok":
            return ConspiracistTikTokBot()
    elif bot_type == "FakeNews":
        if platform == "Twitter":
            return FakeNewsTwitterBot()
        elif platform == "Facebook":
            return FakeNewsFacebookBot()
        elif platform == "LinkedIn":
            return FakeNewsLinkedInBot()
        elif platform == "TikTok":
            return FakeNewsTikTokBot()
    
    raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform}'")


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
