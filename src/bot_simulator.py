"""
Symulator botow internetowych (w celach edukacyjnych!).
Refaktoryzacja przy uzyciu wzorca Bridge.

Zamiast 16 klas (4 boty x 4 platformy) mamy teraz znacznie mniej duplikacji.
Dodanie nowej platformy = 1 nowa klasa platformy!
Dodanie nowego bota = 1 nowa klasa bota!
"""
from abc import ABC, abstractmethod
from typing import Dict
import random


# ============================================================================
# IMPLEMENTOR - Platform (JAK formatuje wiadomosci)
# ============================================================================

class Platform(ABC):
    """Abstrakcyjna klasa platformy - definiuje JAK formatowac wiadomosci."""

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def format_troll(self, message: str) -> str:
        pass

    @abstractmethod
    def format_spammer(self, message: str) -> str:
        pass

    @abstractmethod
    def format_conspiracist(self, message: str) -> str:
        pass

    @abstractmethod
    def format_fakenews(self, message: str) -> str:
        pass


class TwitterPlatform(Platform):
    """Twitter - krotko, z hashtagami"""

    @property
    def name(self) -> str:
        return "Twitter"

    def format_troll(self, message: str) -> str:
        formatted = f"{message} ratio + L + niemasz racji"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        formatted += " #triggered"
        return formatted

    def format_spammer(self, message: str) -> str:
        formatted = f"🚀🚀🚀 {message} Link in bio! #crypto #moon #lambo"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        return formatted

    def format_conspiracist(self, message: str) -> str:
        formatted = f"🧵 WATEK: {message} Coincidence? I think NOT! #WakeUp #Truth"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        return formatted

    def format_fakenews(self, message: str) -> str:
        formatted = f"⚠️ {message} RETWEET zanim zcenzuruja! #Breaking #News"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        return formatted


class FacebookPlatform(Platform):
    """Facebook - boomerski styl, duzo emotek"""

    @property
    def name(self) -> str:
        return "Facebook"

    def format_troll(self, message: str) -> str:
        formatted = f"{message}... PROSZE SIE OBUDZIC LUDZIE!!! "
        formatted += "Udostepnij zanim USUNĄ!!! "
        formatted += "😠😠😠"
        return formatted

    def format_spammer(self, message: str) -> str:
        formatted = f"Moja kuzynka zarobila 5000zl dzieki temu!!! "
        formatted += f"{message} "
        formatted += "NapiszINFO w komentarzu!!! 💰💰💰"
        return formatted

    def format_conspiracist(self, message: str) -> str:
        formatted = f"UDOSTEPNIJ ZANIM USUNA!!!\n\n"
        formatted += f"{message}\n\n"
        formatted += "Mainstream media UKRYWA to przed Toba!!! "
        formatted += "Zrobie researcha!!! 👁️👁️👁️"
        return formatted

    def format_fakenews(self, message: str) -> str:
        formatted = f"🔴 PILNE 🔴\n\n"
        formatted += f"{message}\n\n"
        formatted += "Media MILCZA! Udostepnij swoim znajomym!!! "
        formatted += "Twoja rodzina MUSI to zobaczyc!!! ⚠️⚠️⚠️"
        return formatted


class LinkedInPlatform(Platform):
    """LinkedIn - menedzerski belkot"""

    @property
    def name(self) -> str:
        return "LinkedIn"

    def format_troll(self, message: str) -> str:
        formatted = f"Unpopular opinion: {message}\n\n"
        formatted += "I know this might be controversial, but someone had to say it.\n\n"
        formatted += "Agree? ♻️ Repost to spread awareness\n"
        formatted += "#ThoughtLeadership #Disruption #Controversial"
        return formatted

    def format_spammer(self, message: str) -> str:
        formatted = f"I'm excited to announce that {message}\n\n"
        formatted += "This is not financial advice, but my portfolio is up 10000%.\n\n"
        formatted += "DM me for exclusive insights.\n"
        formatted += "#Entrepreneurship #Hustle #Blessed"
        return formatted

    def format_conspiracist(self, message: str) -> str:
        formatted = f"After 15 years in the industry, I need to share something:\n\n"
        formatted += f"{message}\n\n"
        formatted += "The elites don't want you to know this.\n\n"
        formatted += "Comment 'TRUTH' if you're awake.\n"
        formatted += "#DeepState #FollowTheMoney #QuestionEverything"
        return formatted

    def format_fakenews(self, message: str) -> str:
        formatted = f"🚨 Industry Alert 🚨\n\n"
        formatted += f"{message}\n\n"
        formatted += "My sources in the industry have confirmed this.\n\n"
        formatted += "Share with your network before it's too late.\n"
        formatted += "#BreakingNews #IndustryInsider #MustRead"
        return formatted


class TikTokPlatform(Platform):
    """TikTok - GenZ slang"""

    @property
    def name(self) -> str:
        return "TikTok"

    def format_troll(self, message: str) -> str:
        formatted = f"pov: ktos mowi ze to ma sens 💀💀💀\n"
        formatted += f"bestie... {message}\n"
        formatted += "its giving delulu 😭 no cap fr fr"
        return formatted

    def format_spammer(self, message: str) -> str:
        formatted = f"ok but why is nobody talking about this?? 🤑\n"
        formatted += f"{message}\n"
        formatted += "link in bio bestie trust me im just like you 💅"
        return formatted

    def format_conspiracist(self, message: str) -> str:
        formatted = f"wait wait wait... 🤯\n"
        formatted += f"{message}\n"
        formatted += "why is this not on the news?? theyre deleting this video in 3...2... 👁️"
        return formatted

    def format_fakenews(self, message: str) -> str:
        formatted = f"STORYTIME: so i just found out something crazy 😱\n"
        formatted += f"{message}\n"
        formatted += "share before they take this down!! part 2 if this blows up 👀"
        return formatted


# ============================================================================
# ABSTRACTION - Bot (CO generuje)
# ============================================================================

class Bot(ABC):
    """Abstrakcyjna klasa bota - definiuje CO generowac."""

    def __init__(self, platform: Platform):
        self._platform = platform  # <-- TO JEST MOST!

    @property
    @abstractmethod
    def bot_type(self) -> str:
        pass

    @property
    def platform(self) -> str:
        return self._platform.name

    @abstractmethod
    def generate_content(self, topic: str) -> str:
        """Generuje tresc wiadomosci (bez formatowania platformy)."""
        pass

    @abstractmethod
    def format_with_platform(self, content: str) -> str:
        """Formatuje tresc przy uzyciu platformy."""
        pass

    def generate_post(self, topic: str) -> Dict:
        """Generuje pelny post - laczy tresc z formatowaniem platformy."""
        content = self.generate_content(topic)
        formatted = self.format_with_platform(content)

        return {
            "bot_type": self.bot_type,
            "platform": self._platform.name,
            "topic": topic,
            "content": formatted
        }


class TrollBot(Bot):
    """Troll - prowokuje klocnie"""

    @property
    def bot_type(self) -> str:
        return "Troll"

    def generate_content(self, topic: str) -> str:
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        return random.choice(provocations)

    def format_with_platform(self, content: str) -> str:
        return self._platform.format_troll(content)


class SpammerBot(Bot):
    """Spammer - promuje krypto i okazje"""

    @property
    def bot_type(self) -> str:
        return "Spammer"

    def generate_content(self, topic: str) -> str:
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        return random.choice(spam_templates)

    def format_with_platform(self, content: str) -> str:
        return self._platform.format_spammer(content)


class ConspiracistBot(Bot):
    """Conspiracist - wszedzie widzi spiski"""

    @property
    def bot_type(self) -> str:
        return "Conspiracist"

    def generate_content(self, topic: str) -> str:
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        return random.choice(conspiracies)

    def format_with_platform(self, content: str) -> str:
        return self._platform.format_conspiracist(content)


class FakeNewsBot(Bot):
    """FakeNews - szerzy dezinformacje"""

    @property
    def bot_type(self) -> str:
        return "FakeNews"

    def generate_content(self, topic: str) -> str:
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        return random.choice(fake_news)

    def format_with_platform(self, content: str) -> str:
        return self._platform.format_fakenews(content)


# ============================================================================
# BACKWARD COMPATIBLE CLASSES (dla testow)
# Dzieki Bridge te klasy sa teraz tylko aliasami!
# ============================================================================

class TrollTwitterBot(TrollBot):
    def __init__(self):
        super().__init__(TwitterPlatform())


class TrollFacebookBot(TrollBot):
    def __init__(self):
        super().__init__(FacebookPlatform())


class TrollLinkedInBot(TrollBot):
    def __init__(self):
        super().__init__(LinkedInPlatform())


class TrollTikTokBot(TrollBot):
    def __init__(self):
        super().__init__(TikTokPlatform())


class SpammerTwitterBot(SpammerBot):
    def __init__(self):
        super().__init__(TwitterPlatform())


class SpammerFacebookBot(SpammerBot):
    def __init__(self):
        super().__init__(FacebookPlatform())


class SpammerLinkedInBot(SpammerBot):
    def __init__(self):
        super().__init__(LinkedInPlatform())


class SpammerTikTokBot(SpammerBot):
    def __init__(self):
        super().__init__(TikTokPlatform())


class ConspiracistTwitterBot(ConspiracistBot):
    def __init__(self):
        super().__init__(TwitterPlatform())


class ConspiracistFacebookBot(ConspiracistBot):
    def __init__(self):
        super().__init__(FacebookPlatform())


class ConspiracistLinkedInBot(ConspiracistBot):
    def __init__(self):
        super().__init__(LinkedInPlatform())


class ConspiracistTikTokBot(ConspiracistBot):
    def __init__(self):
        super().__init__(TikTokPlatform())


class FakeNewsTwitterBot(FakeNewsBot):
    def __init__(self):
        super().__init__(TwitterPlatform())


class FakeNewsFacebookBot(FakeNewsBot):
    def __init__(self):
        super().__init__(FacebookPlatform())


class FakeNewsLinkedInBot(FakeNewsBot):
    def __init__(self):
        super().__init__(LinkedInPlatform())


class FakeNewsTikTokBot(FakeNewsBot):
    def __init__(self):
        super().__init__(TikTokPlatform())


# ============================================================================
# FUNKCJA POMOCNICZA
# ============================================================================

def get_bot(bot_type: str, platform: str):
    """
    Zwraca odpowiedniego bota dla danego typu i platformy.
    Teraz uzywamy wzorca Bridge - tworzymy bota z odpowiednia platforma.
    """
    platform_map = {
        "Twitter": TwitterPlatform(),
        "Facebook": FacebookPlatform(),
        "LinkedIn": LinkedInPlatform(),
        "TikTok": TikTokPlatform(),
    }

    # Mapowanie do klas kompatybilnych wstecz (dla isinstance w testach)
    bot_class_map = {
        "Troll": {
            "Twitter": TrollTwitterBot,
            "Facebook": TrollFacebookBot,
            "LinkedIn": TrollLinkedInBot,
            "TikTok": TrollTikTokBot,
        },
        "Spammer": {
            "Twitter": SpammerTwitterBot,
            "Facebook": SpammerFacebookBot,
            "LinkedIn": SpammerLinkedInBot,
            "TikTok": SpammerTikTokBot,
        },
        "Conspiracist": {
            "Twitter": ConspiracistTwitterBot,
            "Facebook": ConspiracistFacebookBot,
            "LinkedIn": ConspiracistLinkedInBot,
            "TikTok": ConspiracistTikTokBot,
        },
        "FakeNews": {
            "Twitter": FakeNewsTwitterBot,
            "Facebook": FakeNewsFacebookBot,
            "LinkedIn": FakeNewsLinkedInBot,
            "TikTok": FakeNewsTikTokBot,
        },
    }

    if bot_type not in bot_class_map:
        raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform}'")

    if platform not in platform_map:
        raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform}'")

    return bot_class_map[bot_type][platform]()


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
