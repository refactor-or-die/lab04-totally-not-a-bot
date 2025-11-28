"""
Symulator botow internetowych (w celach edukacyjnych!).
Implementacja wzorca Bridge.
"""

#factory method  + petle do generowania adapterow
from typing import Dict
import random
from abc import ABC, abstractmethod

# Implementacja (JAK formatuje)
class Platform(ABC):
    @abstractmethod
    def format_message(self, message: str) -> str:
        pass

# Abstrakcja (CO generuje)
class Bot(ABC):
    def __init__(self, platform: Platform):
        self.platform = platform
    
    @abstractmethod
    def generate_content(self, topic: str) -> str:
        pass
    
    def generate_post(self, topic: str) -> Dict:
        content = self.generate_content(topic)
        message = self.platform.format_message(content)

        if hasattr(self.platform, "format_post"):
            message = self.platform.format_post(message)

        return {
            "bot_type": self.__class__.__name__,
            "platform": self.platform.__class__.__name__,
            "topic": topic,
            "content": message
        }

# Platformy
class Twitter(Platform):
    def format_message(self, message: str) -> str:
        formatted = message + " #triggered"
        if len(formatted) > 280:
            formatted = message[:277-len(" #triggered")] + "... #triggered"
        return formatted

    def format_post(self, text: str) -> str:
        if "conspiracy" in text.lower() or "government" in text.lower():
            text = "🧵 " + text
        if "ALERT" in text or "insider" in text:
            text = "⚠️ " + text
        return text

class TikTok(Platform):
    def format_message(self, message: str) -> str:
        return f"bestie... {message}\nits giving delulu 😭 no cap fr fr"

    def format_post(self, text: str) -> str:
        if "ALERT" in text or "insider" in text:
            text = "storytime... " + text
        return text

class Facebook(Platform):
    def format_message(self, message: str) -> str:
        return f"{message}... PROSZE SIE OBUDZIC LUDZIE!!! Udostepnij zanim USUNĄ!!! 😠😠😠"

    def format_post(self, text: str) -> str:
        if "🚀" in text or "dm me" in text.lower():
            text = text + " (mój kuzynka też potwierdziła)"
        if "ALERT" in text:
            text = "PILNE! " + text
        return text

class LinkedIn(Platform):
    def format_message(self, message: str) -> str:
        return (f"Unpopular opinion: {message}\n\n"
                "I know this might be controversial, but someone had to say it.\n\n"
                "🚀🚀🚀 Agree? ♻️ Repost to spread awareness\n"
                "#ThoughtLeadership #Disruption #Controversial")

    def format_post(self, text: str) -> str:
        if "dm me" in text.lower() or "🚀" in text:
            text = "ANNOUNCEMENT: " + text
        return text


class Troll(Bot):
    def generate_content(self, topic: str) -> str:
        texts = [
            f"Serio wierzysz w {topic}? SERIO!",
            f"Nie masz pojecia o {topic}, ratio incoming.",
            f"{topic}? przekret jakich malo.",
        ]
        return random.choice(texts)

class Spammer(Bot):
    def generate_content(self, topic: str) -> str:
        texts = [
            f"NOWY {topic.upper()} COIN! Zarobilem 1000x GUARANTEED 🚀",
            f"Chcesz zarobic na {topic}? LINK IN BIO!!",
            f"{topic} to MOON 🚀🚀🚀 DM ME!",
        ]
        return random.choice(texts)

class Conspiracist(Bot):
    def generate_content(self, topic: str) -> str:
        texts = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}? Oni ukrywaja prawde!",
            f"{topic}? coincidence? I THINK NOT 🧵",
            f"Wake up! {topic} to ich plan! 👁️",
        ]
        return random.choice(texts)

class FakeNews(Bot):
    def generate_content(self, topic: str) -> str:
        texts = [
            f"BREAKING: {topic} potwierdzony przez naukowcow ⚠️",
            f"SZOK! {topic} jest bardziej niebezpieczne niz myslelismy!",
            f"ALERT! {topic} confirmed przez insidera!",
        ]
        return random.choice(texts)


def create_bot_adapter(bot_class, platform_class):
    class BotAdapter:
        def __init__(self):
            self._bot = bot_class(platform_class())
            self.bot_type = bot_class.__name__
            self.platform = platform_class.__name__

        def generate_post(self, topic: str):
            return self._bot.generate_post(topic)

    return BotAdapter

BOT_TYPES = {
    "Troll": Troll,
    "Spammer": Spammer,
    "Conspiracist": Conspiracist,
    "FakeNews": FakeNews
}

PLATFORMS = {
    "Twitter": Twitter,
    "Facebook": Facebook,
    "LinkedIn": LinkedIn,
    "TikTok": TikTok
}

for bot_name, bot_class in BOT_TYPES.items():
    for platform_name, platform_class in PLATFORMS.items():
        class_name = f"{bot_name}{platform_name}Bot"   # <--
        globals()[class_name] = create_bot_adapter(bot_class, platform_class)

def get_bot(bot_type: str, platform: str):
    class_name = f"{bot_type}{platform}Bot"
    if class_name not in globals():
        raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform}'")
    return globals()[class_name]()


if __name__ == "__main__":
    print("=" * 60)
    print("SYMULATOR BOTOW INTERNETOWYCH")
    print("(w celach edukacyjnych!)")
    print("=" * 60)
    
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