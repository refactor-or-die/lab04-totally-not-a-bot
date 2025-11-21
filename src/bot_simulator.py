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


class PlatformImplementation(ABC):

    @abstractmethod
    def format_content(self, content: str, bot_type: str) -> str:
        pass

    @abstractmethod
    def get_platform_name(self) -> str:
        pass


class TwitterImplementation(PlatformImplementation):

    def format_content(self, content: str, bot_type: str) -> str:
        if bot_type == "Troll":
            formatted = f"{content} ratio + L + niemasz racji"
            if len(formatted) > 280:
                formatted = formatted[:277] + "..."
            formatted += " #triggered"
        elif bot_type == "Spammer":
            formatted = f"🚀🚀🚀 {content} Link in bio! #crypto #moon #lambo"
        elif bot_type == "Conspiracist":
            formatted = f"🧵 WATEK: {content} Coincidence? I think NOT! #WakeUp #Truth"
        elif bot_type == "FakeNews":
            formatted = f"⚠️ {content} RETWEET zanim zcenzuruja! #Breaking #News"

        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        return formatted

    def get_platform_name(self) -> str:
        return "Twitter"


class FacebookImplementation(PlatformImplementation):

    def format_content(self, content: str, bot_type: str) -> str:
        if bot_type == "Troll":
            formatted = f"{content}... PROSZE SIE OBUDZIC LUDZIE!!! "
            formatted += "Udostepnij zanim USUNĄ!!! "
            formatted += "😠😠😠"
        elif bot_type == "Spammer":
            formatted = f"Moja kuzynka zarobila 5000zl dzieki {content}!!! "
            formatted += f"{content} "
            formatted += "NapiszINFO w komentarzu!!! 💰💰💰"
        elif bot_type == "Conspiracist":
            formatted = f"UDOSTEPNIJ ZANIM USUNA!!!\n\n{content}\n\n"
            formatted += "Mainstream media UKRYWA to przed Toba!!! "
            formatted += "Zrobie researcha!!! 👁️👁️👁️"
        elif bot_type == "FakeNews":
            formatted = f"🔴 PILNE 🔴\n\n{content}\n\n"
            formatted += "Media MILCZA! Udostepnij swoim znajomym!!! "
            formatted += "Twoja rodzina MUSI to zobaczyc!!! ⚠️⚠️⚠️"
        return formatted

    def get_platform_name(self) -> str:
        return "Facebook"


class LinkedInImplementation(PlatformImplementation):

    def format_content(self, content: str, bot_type: str) -> str:
        if bot_type == "Troll":
            formatted = f"Unpopular opinion: {content}\n\n"
            formatted += "I know this might be controversial, but someone had to say it.\n\n"
            formatted += "Agree? ♻️ Repost to spread awareness\n"
            formatted += "#ThoughtLeadership #Disruption #Controversial"
        elif bot_type == "Spammer":
            formatted = f"I'm excited to announce that {content}\n\n"
            formatted += "This is not financial advice, but my portfolio is up 10000%.\n\n"
            formatted += "DM me for exclusive insights.\n"
            formatted += "#Entrepreneurship #Hustle #Blessed"
        elif bot_type == "Conspiracist":
            formatted = f"After 15 years in the industry, I need to share something:\n\n"
            formatted += f"{content}\n\n"
            formatted += "The elites don't want you to know this.\n\n"
            formatted += "Comment 'TRUTH' if you're awake.\n"
            formatted += "#DeepState #FollowTheMoney #QuestionEverything"
        elif bot_type == "FakeNews":
            formatted = f"🚨 Industry Alert 🚨\n\n"
            formatted += f"{content}\n\n"
            formatted += "My sources in the industry have confirmed this.\n\n"
            formatted += "Share with your network before it's too late.\n"
            formatted += "#BreakingNews #IndustryInsider #MustRead"
        return formatted

    def get_platform_name(self) -> str:
        return "LinkedIn"


class TikTokImplementation(PlatformImplementation):

    def format_content(self, content: str, bot_type: str) -> str:
        if bot_type == "Troll":
            formatted = f"pov: ktos mowi ze {content} ma sens 💀💀💀\n"
            formatted += f"bestie... {content}\n"
            formatted += "its giving delulu 😭 no cap fr fr"
        elif bot_type == "Spammer":
            formatted = f"ok but why is nobody talking about {content}?? 🤑\n"
            formatted += f"{content}\n"
            formatted += "link in bio bestie trust me im just like you 💅"
        elif bot_type == "Conspiracist":
            formatted = f"wait wait wait... 🤯\n"
            formatted += f"{content}\n"
            formatted += "why is this not on the news?? theyre deleting this video in 3...2... 👁️"
        elif bot_type == "FakeNews":
            formatted = f"STORYTIME: so i just found out something crazy 😱\n"
            formatted += f"{content}\n"
            formatted += "share before they take this down!! part 2 if this blows up 👀"
        return formatted

    def get_platform_name(self) -> str:
        return "TikTok"


class BotImplementation(ABC):

    @abstractmethod
    def generate_content(self, topic: str) -> str:
        pass

    @abstractmethod
    def get_bot_type(self) -> str:
        pass


class TrollImplementation(BotImplementation):

    def generate_content(self, topic: str) -> str:
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        return random.choice(provocations)

    def get_bot_type(self) -> str:
        return "Troll"


class SpammerImplementation(BotImplementation):

    def generate_content(self, topic: str) -> str:
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        return random.choice(spam_templates)

    def get_bot_type(self) -> str:
        return "Spammer"


class ConspiracistImplementation(BotImplementation):

    def generate_content(self, topic: str) -> str:
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        return random.choice(conspiracies)

    def get_bot_type(self) -> str:
        return "Conspiracist"


class FakeNewsImplementation(BotImplementation):

    def generate_content(self, topic: str) -> str:
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        return random.choice(fake_news)

    def get_bot_type(self) -> str:
        return "FakeNews"


class TrollTwitterBot:

    def __init__(self):
        self.bot_type = "Troll"
        self.platform = "Twitter"
        self._bot_impl = TrollImplementation()
        self._platform_impl = TwitterImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class TrollFacebookBot:

    def __init__(self):
        self.bot_type = "Troll"
        self.platform = "Facebook"
        self._bot_impl = TrollImplementation()
        self._platform_impl = FacebookImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class TrollLinkedInBot:

    def __init__(self):
        self.bot_type = "Troll"
        self.platform = "LinkedIn"
        self._bot_impl = TrollImplementation()
        self._platform_impl = LinkedInImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class TrollTikTokBot:

    def __init__(self):
        self.bot_type = "Troll"
        self.platform = "TikTok"
        self._bot_impl = TrollImplementation()
        self._platform_impl = TikTokImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class SpammerTwitterBot:

    def __init__(self):
        self.bot_type = "Spammer"
        self.platform = "Twitter"
        self._bot_impl = SpammerImplementation()
        self._platform_impl = TwitterImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class SpammerFacebookBot:

    def __init__(self):
        self.bot_type = "Spammer"
        self.platform = "Facebook"
        self._bot_impl = SpammerImplementation()
        self._platform_impl = FacebookImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class SpammerLinkedInBot:

    def __init__(self):
        self.bot_type = "Spammer"
        self.platform = "LinkedIn"
        self._bot_impl = SpammerImplementation()
        self._platform_impl = LinkedInImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class SpammerTikTokBot:

    def __init__(self):
        self.bot_type = "Spammer"
        self.platform = "TikTok"
        self._bot_impl = SpammerImplementation()
        self._platform_impl = TikTokImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class ConspiracistTwitterBot:

    def __init__(self):
        self.bot_type = "Conspiracist"
        self.platform = "Twitter"
        self._bot_impl = ConspiracistImplementation()
        self._platform_impl = TwitterImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class ConspiracistFacebookBot:

    def __init__(self):
        self.bot_type = "Conspiracist"
        self.platform = "Facebook"
        self._bot_impl = ConspiracistImplementation()
        self._platform_impl = FacebookImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class ConspiracistLinkedInBot:

    def __init__(self):
        self.bot_type = "Conspiracist"
        self.platform = "LinkedIn"
        self._bot_impl = ConspiracistImplementation()
        self._platform_impl = LinkedInImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class ConspiracistTikTokBot:

    def __init__(self):
        self.bot_type = "Conspiracist"
        self.platform = "TikTok"
        self._bot_impl = ConspiracistImplementation()
        self._platform_impl = TikTokImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class FakeNewsTwitterBot:

    def __init__(self):
        self.bot_type = "FakeNews"
        self.platform = "Twitter"
        self._bot_impl = FakeNewsImplementation()
        self._platform_impl = TwitterImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class FakeNewsFacebookBot:

    def __init__(self):
        self.bot_type = "FakeNews"
        self.platform = "Facebook"
        self._bot_impl = FakeNewsImplementation()
        self._platform_impl = FacebookImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class FakeNewsLinkedInBot:

    def __init__(self):
        self.bot_type = "FakeNews"
        self.platform = "LinkedIn"
        self._bot_impl = FakeNewsImplementation()
        self._platform_impl = LinkedInImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class FakeNewsTikTokBot:

    def __init__(self):
        self.bot_type = "FakeNews"
        self.platform = "TikTok"
        self._bot_impl = FakeNewsImplementation()
        self._platform_impl = TikTokImplementation()

    def generate_post(self, topic: str) -> Dict:
        content = self._bot_impl.generate_content(topic)
        formatted = self._platform_impl.format_content(content, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


def get_bot(bot_type: str, platform: str):
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

