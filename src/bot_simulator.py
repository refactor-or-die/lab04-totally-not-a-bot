
from typing import Dict
import random
from abc import ABC, abstractmethod

class Bot(ABC):
    @property
    @abstractmethod
    def bot_type(self):
        pass

    @property
    @abstractmethod
    def platform(self):
        pass

    @abstractmethod
    def generate_post(self):
        pass

class Platform(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def format_message(self, topic: str, content: str) -> str:
        pass


class ConspiracistBot(Bot):
    def __init__(self, platform: Platform):
        self._platform = platform

    @property
    def bot_type(self) -> str:
        return "Conspiracist"

    @property
    def platform(self) -> Platform:
        return self._platform

    def generate_post(self, topic: str) -> dict:
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}",
        ]
        content = random.choice(conspiracies)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform.get_name(),
            "topic": topic,
            "content": self.platform.format_message(topic, content),
        }

class TrollBot(Bot):
    """Troll na Twitterze - krotki, agresywny"""

    def __init__(self, platform: Platform):
        self._platform = platform

    @property
    def platform(self) -> Platform:
        return self._platform

    @property
    def bot_type(self) -> str:
        return "Troll"

    def generate_post(self, topic: str) -> dict:
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms",
        ]
        content = random.choice(provocations)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform.get_name(),
            "topic": topic,
            "content": self.platform.format_message(topic, content),
        }


class SpammerBot(Bot):
    def __init__(self, platform: Platform):
        self._platform = platform

    @property
    def bot_type(self) -> str:
        return "Spammer"

    @property
    def platform(self) -> Platform:
        return self._platform

    def generate_post(self, topic: str) -> dict:
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!",
        ]
        content = random.choice(spam_templates)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform.get_name(),
            "topic": topic,
            "content": self.platform.format_message(topic, content),
        }


class FakeNewsBot(Bot):
    def __init__(self, platform: Platform):
        self._platform = platform

    @property
    def bot_type(self) -> str:
        return "FakeNews"

    @property
    def platform(self) -> Platform:
        return self._platform

    def generate_post(self, topic: str) -> dict:
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}",
        ]
        content = random.choice(fake_news)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform.get_name(),
            "topic": topic,
            "content": self.platform.format_message(topic, content),
        }

class TwitterPlatform(Platform):
    def get_name(self) -> str:
        return "Twitter"

    def format_message(self, topic: str, content: str) -> str:
        formatted = f"{content} ratio + L + niemasz racji"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        formatted += " #triggered"
        return formatted


class FacebookPlatform(Platform):
    def get_name(self) -> str:
        return "Facebook"

    def format_message(self, topic: str, content: str) -> str:
        formatted = f"{content}... PROSZE SIE OBUDZIC LUDZIE!!! "
        formatted += "Udostepnij zanim USUNĄ!!! "
        formatted += "😠😠😠"
        return formatted


class LinkedInPlatform(Platform):
    def get_name(self) -> str:
        return "LinkedIn"

    def format_message(self, topic: str, content: str) -> str:
        formatted = f"Unpopular opinion: {content}\n\n"
        formatted += (
            "I know this might be controversial, but someone had to say it.\n\n"
        )
        formatted += "Agree? ♻️ Repost to spread awareness\n"
        formatted += "#ThoughtLeadership #Disruption #Controversial"

        return formatted


class TikTokPlatform(Platform):
    def get_name(self) -> str:
        return "TikTok"

    def format_message(self, topic: str, content: str) -> str:
        formatted = f"pov: ktos mowi ze {topic} ma sens 💀💀💀\n"
        formatted += f"bestie... {content}\n"
        formatted += "its giving delulu 😭 no cap fr fr"

        return formatted

def get_bot(bot_type: str, platform: str) -> Bot:
    bot = create_bot_adapter(bot_types[bot_type], platforms[platform])()
    return bot


def create_bot_adapter(bot_class, platform_class):
    """Factory Method - generuje klase adaptera"""

    class BotAdapter:
        def __init__(self):
            self._bot = bot_class(platform_class())
            self.bot_type = self._bot.bot_type
            self.platform = self._bot.platform.get_name()

        def generate_post(self, topic):
            return self._bot.generate_post(topic)

    return BotAdapter

bot_types = {
    "Troll": TrollBot,
    "Spammer": SpammerBot,
    "Conspiracist": ConspiracistBot,
    "FakeNews": FakeNewsBot
}

platforms = {
    "Twitter": TwitterPlatform,
    "Facebook": FacebookPlatform,
    "LinkedIn": LinkedInPlatform,
    "TikTok": TikTokPlatform,
}

# Magia!
for bot_name, bot_class in bot_types.items():
    for platform_name, platform_class in platforms.items():
        class_name = f"{bot_name}{platform_name}Bot"
        globals()[class_name] = create_bot_adapter(bot_class, platform_class)


if __name__ == "__main__":
    print("=" * 60)
    print("SYMULATOR BOTOW INTERNETOWYCH")
    print("(w celach edukacyjnych!)")
    print("=" * 60)

    random.seed(42)

    bot_types_list = ["Troll", "Spammer", "Conspiracist", "FakeNews"]
    platforms_list = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
    topics = ["AI", "szczepionki", "5G", "kryptowaluty"]

    for bot_type in bot_types_list:
        print(f"\n{'='*60}")
        print(f"TYP BOTA: {bot_type}")
        print("=" * 60)

        for platform in platforms_list:
            bot = get_bot(bot_type, platform)
            topic = random.choice(topics)
            result = bot.generate_post(topic)

            print(f"\n[{platform}] Temat: {topic}")
            print("-" * 40)
            print(result["content"])