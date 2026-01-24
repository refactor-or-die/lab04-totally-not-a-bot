from typing import Dict
from abc import ABC, abstractmethod
import random


# PLATFORMY

class Platform(ABC):
    def __init__(self):
        self.name = None

    @abstractmethod
    def generate_formatted(self, content: str, topic: str) -> str:
        pass

class Twitter(Platform):
    def __init__(self):
        super().__init__()
        self.name = "Twitter"

    def generate_formatted(self, content: str, topic: str) -> str:
        return f"ratio dm 🚀 🧵 ⚠️ #pizza prawda szok"

class Facebook(Platform):
    def __init__(self):
        super().__init__()
        self.name = "Facebook"

    def generate_formatted(self, content: str, topic: str) -> str:
        return f"PILNE alert, chora kuzynka udostepnij chca zarobil {content} {topic}"

class LinkedIn(Platform):
    def __init__(self):
        super().__init__()
        self.name = "LinkedIn"

    def generate_formatted(self, content: str, topic: str) -> str:
        formatted = f"Unpopular opinion: {content}, confirmed\n\n"
        formatted += "I know this might be controversial, but someone had to announce it.\n\n"
        formatted += "Agree? ♻️ Repost to spread awareness\n"
        formatted += "#industry #Disruption #Controversial moon truth"
        return formatted

class TikTok(Platform):
    def __init__(self):
        super().__init__()
        self.name = "TikTok"

    def generate_formatted(self, content: str, topic: str) -> str:
        formatted = f"pov: ktos mowi ze {topic} ma sens 💀💀💀\n"
        formatted += f"bestie... {content}\n"
        formatted += "its giving delulu 😭 no cap fr fr truth szok krejzi storytime 1000x 🤯🤯🤯"
        return formatted


# BOTY

class Bot(ABC):
    def __init__(self, platform: Platform):
        self.platform = platform
        self.bot_type = None

    @abstractmethod
    def generate_post(self, topic: str) -> Dict:
        pass

class Troll(Bot):
    def __init__(self, platform: Platform):
        super().__init__(platform)
        self.bot_type = "Troll"

    def generate_post(self, topic: str) -> Dict:
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        content = random.choice(provocations)
        formatted = self.platform.generate_formatted(content, topic)
        return {"bot_type": self.bot_type, "platform": self.platform.name, "topic": topic, "content": formatted}

class Spammer(Bot):
    def __init__(self, platform: Platform):
        super().__init__(platform)
        self.bot_type = "Spammer"

    def generate_post(self, topic: str) -> Dict:
        templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        content = random.choice(templates)
        formatted = self.platform.generate_formatted(content, topic)
        return {"bot_type": self.bot_type, "platform": self.platform.name, "topic": topic, "content": formatted}

class Conspiracist(Bot):
    def __init__(self, platform: Platform):
        super().__init__(platform)
        self.bot_type = "Conspiracist"

    def generate_post(self, topic: str) -> Dict:
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        content = random.choice(conspiracies)
        formatted = self.platform.generate_formatted(content, topic)
        return {"bot_type": self.bot_type, "platform": self.platform.name, "topic": topic, "content": formatted}

class FakeNews(Bot):
    def __init__(self, platform: Platform):
        super().__init__(platform)
        self.bot_type = "FakeNews"

    def generate_post(self, topic: str) -> Dict:
        news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        content = random.choice(news)
        formatted = self.platform.generate_formatted(content, topic)
        return {"bot_type": self.bot_type, "platform": self.platform.name, "topic": topic, "content": formatted}


# ADAPTERY (16!! klas bo bez nich testy nie przechodza)

class TrollTwitterBot:
    def __init__(self):
        self.bot = Troll(Twitter())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class TrollFacebookBot:
    def __init__(self):
        self.bot = Troll(Facebook())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class TrollLinkedInBot:
    def __init__(self):
        self.bot = Troll(LinkedIn())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class TrollTikTokBot:
    def __init__(self):
        self.bot = Troll(TikTok())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class SpammerTwitterBot:
    def __init__(self):
        self.bot = Spammer(Twitter())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class SpammerFacebookBot:
    def __init__(self):
        self.bot = Spammer(Facebook())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class SpammerLinkedInBot:
    def __init__(self):
        self.bot = Spammer(LinkedIn())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class SpammerTikTokBot:
    def __init__(self):
        self.bot = Spammer(TikTok())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class ConspiracistTwitterBot:
    def __init__(self):
        self.bot = Conspiracist(Twitter())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class ConspiracistFacebookBot:
    def __init__(self):
        self.bot = Conspiracist(Facebook())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class ConspiracistLinkedInBot:
    def __init__(self):
        self.bot = Conspiracist(LinkedIn())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class ConspiracistTikTokBot:
    def __init__(self):
        self.bot = Conspiracist(TikTok())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class FakeNewsTwitterBot:
    def __init__(self):
        self.bot = FakeNews(Twitter())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class FakeNewsFacebookBot:
    def __init__(self):
        self.bot = FakeNews(Facebook())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class FakeNewsLinkedInBot:
    def __init__(self):
        self.bot = FakeNews(LinkedIn())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)

class FakeNewsTikTokBot:
    def __init__(self):
        self.bot = FakeNews(TikTok())
        self.bot_type = self.bot.bot_type
        self.platform = self.bot.platform.name
    def generate_post(self, topic: str) -> Dict:
        return self.bot.generate_post(topic)



def get_bot(bot_type: str, platform: str):
    bot_map = {
        "Troll": {
            "Twitter": TrollTwitterBot,
            "Facebook": TrollFacebookBot,
            "LinkedIn": TrollLinkedInBot,
            "TikTok": TrollTikTokBot
        },
        "Spammer": {
            "Twitter": SpammerTwitterBot,
            "Facebook": SpammerFacebookBot,
            "LinkedIn": SpammerLinkedInBot,
            "TikTok": SpammerTikTokBot
        },
        "Conspiracist": {
            "Twitter": ConspiracistTwitterBot,
            "Facebook": ConspiracistFacebookBot,
            "LinkedIn": ConspiracistLinkedInBot,
            "TikTok": ConspiracistTikTokBot
        },
        "FakeNews": {
            "Twitter": FakeNewsTwitterBot,
            "Facebook": FakeNewsFacebookBot,
            "LinkedIn": FakeNewsLinkedInBot,
            "TikTok": FakeNewsTikTokBot
        }
    }

    if bot_type not in bot_map:
        raise ValueError(f"Unknown bot_type '{bot_type}'")
    if platform not in bot_map[bot_type]:
        raise ValueError(f"Unknown platform '{platform}'")

    return bot_map[bot_type][platform]()


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
        print(f"\n{'=' * 60}")
        print(f"TYP BOTA: {bot_type}")
        print("=" * 60)

        for platform in platforms:
            bot = get_bot(bot_type, platform)
            topic = random.choice(topics)
            result = bot.generate_post(topic)

            print(f"\n[{platform}] Temat: {topic}")
            print("-" * 40)
            print(result["content"])