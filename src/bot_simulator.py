"""
Symulator botow internetowych (w celach edukacyjnych!).
UWAGA: Ten kod ma EKSPLOZJE KLAS! Uzyj wzorca Bridge.

Mamy 4 typy botow i 4 platformy = 16 klas.
Dodanie nowej platformy wymaga 4 nowych klas!
Dodanie nowego bota wymaga 4 nowych klas!

To nie jest skalowalne rozwiazanie...
"""

from abc import ABC, abstractmethod
from typing import Dict
import functools
import random


class Platform(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def format_message(self, topic: str, content: str) -> str:
        pass


class Bot(ABC):
    @property
    @abstractmethod
    def bot_type(self) -> str:
        pass

    @property
    @abstractmethod
    def platform(self) -> str:
        pass

    @abstractmethod
    def generate_post(self, topic: str) -> dict:
        pass


class TrollBot(Bot):
    """Troll na Twitterze - krotki, agresywny"""

    def __init__(self, platform: Platform):
        self._platform = platform

    @property
    def platform(self) -> str:
        return self._platform.get_name()

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
            "platform": self.platform,
            "topic": topic,
            "content": self._platform.format_message(topic, content),
        }


class SpammerBot(Bot):
    def __init__(self, platform: Platform):
        self._platform = platform

    @property
    def bot_type(self) -> str:
        return "Spammer"

    @property
    def platform(self) -> str:
        return self._platform.get_name()

    def generate_post(self, topic: str) -> dict:
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!",
        ]
        content = random.choice(spam_templates)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": self._platform.format_message(topic, content),
        }


class ConspiracistBot(Bot):
    def __init__(self, platform: Platform):
        self._platform = platform

    @property
    def bot_type(self) -> str:
        return "Conspiracist"

    @property
    def platform(self) -> str:
        return self._platform.get_name()

    def generate_post(self, topic: str) -> dict:
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}? Coincidence?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}",
        ]
        content = random.choice(conspiracies)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": self._platform.format_message(topic, content),
        }


class FakeNewsBot(Bot):
    def __init__(self, platform: Platform):
        self._platform = platform

    @property
    def bot_type(self) -> str:
        return "FakeNews"

    @property
    def platform(self) -> str:
        return self._platform.get_name()

    def generate_post(self, topic: str) -> dict:
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}",
        ]
        content = random.choice(fake_news)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": self._platform.format_message(topic, content),
        }


class TwitterPlatform(Platform):
    def get_name(self) -> str:
        return "Twitter"

    def format_message(self, topic: str, content: str) -> str:
        formatted = f"🚀🧵⚠️ {content} ratio + L + niemasz racji"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        formatted += " #triggered"
        return formatted


class FacebookPlatform(Platform):
    def get_name(self) -> str:
        return "Facebook"

    def format_message(self, topic: str, content: str) -> str:
        # Facebook formatuje inaczej
        formatted = f"🔴 INFO {content}... PROSZE SIE OBUDZIC LUDZIE!!! "
        formatted += "Udostepnij zanim USUNĄ!!! "
        formatted += "😠😠😠"
        return formatted


class LinkedInPlatform(Platform):
    def get_name(self) -> str:
        return "LinkedIn"

    def format_message(self, topic: str, content: str) -> str:
        # LinkedIn formatuje "profesjonalnie"
        formatted = f"Unpopular excited opinion: {content}\n\n"
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
        # TikTok formatuje w stylu GenZ
        formatted = f"👁️ pov: ktos mowi ze {topic} ma sens 💀💀💀\n"
        formatted += f"storytime bestie... {content}\n"
        formatted += "its giving delulu 😭 no cap fr fr"

        return formatted


@functools.cache
def create_bot_adapter(bot_class, platform_class):
    """Factory Method - generuje klase adaptera"""

    class BotAdapter(Bot):
        def __init__(self):
            self._bot = bot_class(platform_class())

        @property
        def bot_type(self) -> str:
            return self._bot.bot_type

        @property
        def platform(self) -> str:
            return self._bot.platform

        def generate_post(self, topic):
            return self._bot.generate_post(topic)

    return BotAdapter


bot_types = {
    "Troll": TrollBot,
    "Spammer": SpammerBot,
    "Conspiracist": ConspiracistBot,
    "FakeNews": FakeNewsBot,
}

platforms = {
    "Twitter": TwitterPlatform,
    "Facebook": FacebookPlatform,
    "LinkedIn": LinkedInPlatform,
    "TikTok": TikTokPlatform,
}


def get_bot(bot_type: str, platform: str) -> Bot:
    """
    Zwraca odpowiedniego bota dla danego typu i platformy.

    SPÓJRZ NA TE IFY! 16 kombinacji! A co jak dodamy Mastodon i Reddit?
    """

    try:
        bot = bot_types[bot_type]
    except KeyError:
        raise ValueError(f"Invalid bot type: '{bot_type}'")

    try:
        plat = platforms[platform]
    except KeyError:
        raise ValueError(f"Invalid platform: '{platform}'")

    BotAdapter = create_bot_adapter(bot, plat)

    return BotAdapter()


# Magia!
for bot_name, bot_class in bot_types.items():
    for platform_name, platform_class in platforms.items():
        class_name = f"{bot_name}{platform_name}Bot"
        print(class_name)
        globals()[class_name] = create_bot_adapter(bot_class, platform_class)


# Przykladowe uzycie
def main():
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


if __name__ == "__main__":
    main()
