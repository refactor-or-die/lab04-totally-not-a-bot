"""
Symulator botow internetowych (w celach edukacyjnych!).
UWAGA: Ten kod ma EKSPLOZJE KLAS! Uzyj wzorca Bridge.

Mamy 4 typy botow i 4 platformy = 16 klas.
Dodanie nowej platformy wymaga 4 nowych klas!
Dodanie nowego bota wymaga 4 nowych klas!

To nie jest skalowalne rozwiazanie...
"""
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
        # Facebook formatuje inaczej
        formatted = f"{content}... PROSZE SIE OBUDZIC LUDZIE!!! "
        formatted += "Udostepnij zanim USUNĄ!!! "
        formatted += "😠😠😠"
        return formatted


class LinkedInPlatform(Platform):
    def get_name(self) -> str:
        return "LinkedIn"

    def format_message(self, topic: str, content: str) -> str:
        # LinkedIn formatuje "profesjonalnie"
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
        # TikTok formatuje w stylu GenZ
        formatted = f"pov: ktos mowi ze {topic} ma sens 💀💀💀\n"
        formatted += f"bestie... {content}\n"
        formatted += "its giving delulu 😭 no cap fr fr"

        return formatted

def get_bot(bot_type: str, platform: str) -> Bot:

    if platform == "Twitter":
        plat = TwitterPlatform()
    elif platform == "Facebook":
        plat = FacebookPlatform()
    elif platform == "LinkedIn":
        plat = LinkedInPlatform()
    elif platform == "TikTok":
        plat = TikTokPlatform()
    else:
        raise ValueError(f"Unknown platform '{platform}'")

    if bot_type == "Troll":
        return TrollBot(plat)
    elif bot_type == "Spammer":
        return SpammerBot(plat)
    elif bot_type == "Conspiracist":
        return ConspiracistBot(plat)
    elif bot_type == "FakeNews":
        return FakeNewsBot(plat)
    else:
        raise ValueError(f"Unknown bot_type '{bot_type}'")



class TrollTwitterBot(TrollBot):
    def __init__(self):
        super().__init__(TwitterPlatform())
    @property
    def platform(self):
        return "Twitter"
class TrollFacebookBot(TrollBot):
    def __init__(self):
        super().__init__(FacebookPlatform())
    @property
    def platform(self):
        return "Facebook"
class TrollLinkedInBot(TrollBot):
    def __init__(self):
        super().__init__(LinkedInPlatform())
    @property
    def platform(self):
        return "LinkedIn"
class TrollTikTokBot(TrollBot):
    def __init__(self):
        super().__init__(TikTokPlatform())
    @property
    def platform(self):
        return "TikTok"


class SpammerTwitterBot(SpammerBot):
    def __init__(self):
        super().__init__(TwitterPlatform())
    @property
    def platform(self):
        return "Twitter"
class SpammerFacebookBot(SpammerBot):
    def __init__(self):
        super().__init__(FacebookPlatform())
    @property
    def platform(self):
        return "Facebook"
class SpammerLinkedInBot(SpammerBot):
    def __init__(self):
        super().__init__(LinkedInPlatform())
    @property
    def platform(self):
        return "LinkedIn"
class SpammerTikTokBot(SpammerBot):
    def __init__(self):
        super().__init__(TikTokPlatform())
    @property
    def platform(self):
        return "TikTok"


class ConspiracistTwitterBot(ConspiracistBot):
    def __init__(self):
        super().__init__(TwitterPlatform())
    @property
    def platform(self):
        return "Twitter"
class ConspiracistFacebookBot(ConspiracistBot):
    def __init__(self):
        super().__init__(FacebookPlatform())
    @property
    def platform(self):
        return "Facebook"
class ConspiracistLinkedInBot(ConspiracistBot):
    def __init__(self):
        super().__init__(LinkedInPlatform())
    @property
    def platform(self):
        return "LinkedIn"
class ConspiracistTikTokBot(ConspiracistBot):
    def __init__(self):
        super().__init__(TikTokPlatform())
    @property
    def platform(self):
        return "TikTok"


class FakeNewsTwitterBot(FakeNewsBot):
    def __init__(self):
        super().__init__(TwitterPlatform())
    @property
    def platform(self):
        return "Twitter"
class FakeNewsFacebookBot(FakeNewsBot):
    def __init__(self):
        super().__init__(FacebookPlatform())
    @property
    def platform(self):
        return "Facebook"
class FakeNewsLinkedInBot(FakeNewsBot):
    def __init__(self):
        super().__init__(LinkedInPlatform())
    @property
    def platform(self):
        return "LinkedIn"
class FakeNewsTikTokBot(FakeNewsBot):
    def __init__(self):
        super().__init__(TikTokPlatform())
    @property
    def platform(self):
        return "TikTok"


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
