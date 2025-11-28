"""
Symulator botow internetowych (w celach edukacyjnych!).
UWAGA: Ten kod został zrefaktoryzowany przy użyciu wzorca Bridge.
Dodano Dynamic Class Generation dla kompatybilności wstecznej.
"""
from typing import Dict
import random
from abc import ABC, abstractmethod

class Platform(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def format_troll(self, content: str, topic: str) -> str:
        pass

    @abstractmethod
    def format_spammer(self, content: str, topic: str) -> str:
        pass

    @abstractmethod
    def format_conspiracist(self, content: str, topic: str) -> str:
        pass

    @abstractmethod
    def format_fakenews(self, content: str, topic: str) -> str:
        pass

class Twitter(Platform):
    name = "Twitter"

    def format_troll(self, content: str, topic: str) -> str:
        formatted = f"{content} ratio + L + niemasz racji"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        formatted += " #triggered"
        return formatted

    def format_spammer(self, content: str, topic: str) -> str:
        formatted = f"🚀🚀🚀 {content} Link in bio! #crypto #moon #lambo"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        return formatted

    def format_conspiracist(self, content: str, topic: str) -> str:
        formatted = f"🧵 WATEK: {content} Coincidence? I think NOT! #WakeUp #Truth"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        return formatted

    def format_fakenews(self, content: str, topic: str) -> str:
        formatted = f"⚠️ {content} RETWEET zanim zcenzuruja! #Breaking #News"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        return formatted

class Facebook(Platform):
    name = "Facebook"

    def format_troll(self, content: str, topic: str) -> str:
        formatted = f"{content}... PROSZE SIE OBUDZIC LUDZIE!!! "
        formatted += "Udostepnij zanim USUNĄ!!! "
        formatted += "😠😠😠"
        return formatted

    def format_spammer(self, content: str, topic: str) -> str:
        formatted = f"Moja kuzynka zarobila 5000zl dzieki {topic}!!! "
        formatted += f"{content} "
        formatted += "NapiszINFO w komentarzu!!! 💰💰💰"
        return formatted

    def format_conspiracist(self, content: str, topic: str) -> str:
        formatted = f"UDOSTEPNIJ ZANIM USUNA!!!\n\n"
        formatted += f"{content}\n\n"
        formatted += "Mainstream media UKRYWA to przed Toba!!! "
        formatted += "Zrobie researcha!!! 👁️👁️👁️"
        return formatted

    def format_fakenews(self, content: str, topic: str) -> str:
        formatted = f"🔴 PILNE 🔴\n\n"
        formatted += f"{content}\n\n"
        formatted += "Media MILCZA! Udostepnij swoim znajomym!!! "
        formatted += "Twoja rodzina MUSI to zobaczyc!!! ⚠️⚠️⚠️"
        return formatted

class LinkedIn(Platform):
    name = "LinkedIn"

    def format_troll(self, content: str, topic: str) -> str:
        formatted = f"Unpopular opinion: {content}\n\n"
        formatted += "I know this might be controversial, but someone had to say it.\n\n"
        formatted += "Agree? ♻️ Repost to spread awareness\n"
        formatted += "#ThoughtLeadership #Disruption #Controversial"
        return formatted

    def format_spammer(self, content: str, topic: str) -> str:
        formatted = f"I'm excited to announce that {content}\n\n"
        formatted += "This is not financial advice, but my portfolio is up 10000%.\n\n"
        formatted += "DM me for exclusive insights.\n"
        formatted += "#Entrepreneurship #Hustle #Blessed"
        return formatted

    def format_conspiracist(self, content: str, topic: str) -> str:
        formatted = f"After 15 years in the industry, I need to share something:\n\n"
        formatted += f"{content}\n\n"
        formatted += "The elites don't want you to know this.\n\n"
        formatted += "Comment 'TRUTH' if you're awake.\n"
        formatted += "#DeepState #FollowTheMoney #QuestionEverything"
        return formatted

    def format_fakenews(self, content: str, topic: str) -> str:
        formatted = f"🚨 Industry Alert 🚨\n\n"
        formatted += f"{content}\n\n"
        formatted += "My sources in the industry have confirmed this.\n\n"
        formatted += "Share with your network before it's too late.\n"
        formatted += "#BreakingNews #IndustryInsider #MustRead"
        return formatted

class TikTok(Platform):
    name = "TikTok"

    def format_troll(self, content: str, topic: str) -> str:
        formatted = f"pov: ktos mowi ze {topic} ma sens 💀💀💀\n"
        formatted += f"bestie... {content}\n"
        formatted += "its giving delulu 😭 no cap fr fr"
        return formatted

    def format_spammer(self, content: str, topic: str) -> str:
        formatted = f"ok but why is nobody talking about {topic}?? 🤑\n"
        formatted += f"{content}\n"
        formatted += "link in bio bestie trust me im just like you 💅"
        return formatted

    def format_conspiracist(self, content: str, topic: str) -> str:
        formatted = f"wait wait wait... 🤯\n"
        formatted += f"{content}\n"
        formatted += "why is this not on the news?? theyre deleting this video in 3...2... 👁️"
        return formatted

    def format_fakenews(self, content: str, topic: str) -> str:
        formatted = f"STORYTIME: so i just found out something crazy 😱\n"
        formatted += f"{content}\n"
        formatted += "share before they take this down!! part 2 if this blows up 👀"
        return formatted

class Bot(ABC):
    def __init__(self, platform: Platform):
        self._platform_impl = platform
        self.bot_type = "Generic"

    @property
    def platform(self) -> str:
        """Zwraca nazwę platformy (dla kompatybilności z testami)"""
        return self._platform_impl.name

    @abstractmethod
    def _generate_content(self, topic: str) -> str:
        """Metoda wewnętrzna generująca surową treść"""
        pass

    @abstractmethod
    def _format_content(self, raw_content: str, topic: str) -> str:
        """Metoda zlecająca formatowanie konkretnej platformie"""
        pass

    def generate_post(self, topic: str) -> Dict:
        """Główna metoda publiczna (Template Method)"""
        raw_content = self._generate_content(topic)
        formatted_content = self._format_content(raw_content, topic)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted_content
        }

class TrollBot(Bot):
    def __init__(self, platform: Platform):
        super().__init__(platform)
        self.bot_type = "Troll"

    def _generate_content(self, topic: str) -> str:
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        return random.choice(provocations)

    def _format_content(self, raw_content: str, topic: str) -> str:
        return self._platform_impl.format_troll(raw_content, topic)

class SpammerBot(Bot):
    def __init__(self, platform: Platform):
        super().__init__(platform)
        self.bot_type = "Spammer"

    def _generate_content(self, topic: str) -> str:
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        return random.choice(spam_templates)

    def _format_content(self, raw_content: str, topic: str) -> str:
        return self._platform_impl.format_spammer(raw_content, topic)

class ConspiracistBot(Bot):
    def __init__(self, platform: Platform):
        super().__init__(platform)
        self.bot_type = "Conspiracist"

    def _generate_content(self, topic: str) -> str:
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        return random.choice(conspiracies)

    def _format_content(self, raw_content: str, topic: str) -> str:
        return self._platform_impl.format_conspiracist(raw_content, topic)

class FakeNewsBot(Bot):
    def __init__(self, platform: Platform):
        super().__init__(platform)
        self.bot_type = "FakeNews"

    def _generate_content(self, topic: str) -> str:
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        return random.choice(fake_news)

    def _format_content(self, raw_content: str, topic: str) -> str:
        return self._platform_impl.format_fakenews(raw_content, topic)

def create_bot_adapter(bot_class, platform_class):

    class BotAdapter:
        def __init__(self):

            self._bot = bot_class(platform_class())

            self.bot_type = self._bot.bot_type
            self.platform = self._bot.platform

        def generate_post(self, topic):

            return self._bot.generate_post(topic)

    return BotAdapter

bot_types_map = {
    "Troll": TrollBot,
    "Spammer": SpammerBot,
    "Conspiracist": ConspiracistBot,
    "FakeNews": FakeNewsBot
}

platforms_map = {
    "Twitter": Twitter,
    "Facebook": Facebook,
    "LinkedIn": LinkedIn,
    "TikTok": TikTok
}

for bot_name, bot_class in bot_types_map.items():
    for platform_name, platform_class in platforms_map.items():
        class_name = f"{bot_name}{platform_name}Bot"
        adapter_class = create_bot_adapter(bot_class, platform_class)
        globals()[class_name] = adapter_class


def get_bot(bot_type: str, platform: str):

    expected_class_name = f"{bot_type}{platform}Bot"

    if expected_class_name in globals():
        bot_instance = globals()[expected_class_name]()
        return bot_instance
    else:
        raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform}'")

if __name__ == "__main__":
    print("=" * 60)
    print("SYMULATOR BOTOW INTERNETOWYCH")
    print("(Refaktoryzacja: BRIDGE PATTERN + DYNAMIC CLASSES)")
    print("=" * 60)

    random.seed(42)

    bot_types = ["Troll", "Spammer", "Conspiracist", "FakeNews"]
    platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
    topics = ["AI", "szczepionki", "5G", "kryptowaluty"]

    for bot_type in bot_types:
        print(f"\n{'=' * 60}")
        print(f"TYP BOTA: {bot_type}")
        print("=" * 60)

        for platform in platforms:
            # Teraz get_bot używa dynamicznie wygenerowanych klas
            bot = get_bot(bot_type, platform)

            topic = random.choice(topics)
            result = bot.generate_post(topic)

            print(f"\n[{platform}] Temat: {topic}")
            print("-" * 40)
            print(result["content"])