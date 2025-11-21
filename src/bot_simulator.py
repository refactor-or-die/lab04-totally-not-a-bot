from abc import ABC, abstractmethod
from typing import Dict
import random


class Platform(ABC):

    @abstractmethod
    def format_message(self, content: str, bot_type: str) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


class TwitterPlatform(Platform):

    def get_name(self) -> str:
        return "Twitter"

    def format_message(self, content: str, bot_type: str) -> str:
        if bot_type == "Troll":
            formatted = f"{content} ratio + L + niemasz racji"
            if len(formatted) > 280:
                formatted = formatted[:277] + "..."
            formatted += " #triggered"
        elif bot_type == "Spammer":
            formatted = f"🚀🚀🚀 {content} Link in bio! #crypto #moon #lambo"
            if len(formatted) > 280:
                formatted = formatted[:277] + "..."
        elif bot_type == "Conspiracist":
            formatted = f"🧵 WATEK: {content} Coincidence? I think NOT! #WakeUp #Truth"
            if len(formatted) > 280:
                formatted = formatted[:277] + "..."
        elif bot_type == "FakeNews":
            formatted = f"⚠️ {content} RETWEET zanim zcenzuruja! #Breaking #News"
            if len(formatted) > 280:
                formatted = formatted[:277] + "..."
        return formatted


class FacebookPlatform(Platform):

    def get_name(self) -> str:
        return "Facebook"

    def format_message(self, content: str, bot_type: str) -> str:
        if bot_type == "Troll":
            formatted = f"{content}... PROSZE SIE OBUDZIC LUDZIE!!! "
            formatted += "Udostepnij zanim USUNĄ!!! "
            formatted += "😠😠😠"
        elif bot_type == "Spammer":
            formatted = f"Moja kuzynka zarobila 5000zl dzieki czegos!!! "
            formatted += f"{content} "
            formatted += "NapiszINFO w komentarzu!!! 💰💰💰"
        elif bot_type == "Conspiracist":
            formatted = f"UDOSTEPNIJ ZANIM USUNA!!!\n\n"
            formatted += f"{content}\n\n"
            formatted += "Mainstream media UKRYWA to przed Toba!!! "
            formatted += "Zrobie researcha!!! 👁️👁️👁️"
        elif bot_type == "FakeNews":
            formatted = f"🔴 PILNE 🔴\n\n"
            formatted += f"{content}\n\n"
            formatted += "Media MILCZA! Udostepnij swoim znajomym!!! "
            formatted += "Twoja rodzina MUSI to zobaczyc!!! ⚠️⚠️⚠️"
        return formatted


class LinkedInPlatform(Platform):

    def get_name(self) -> str:
        return "LinkedIn"

    def format_message(self, content: str, bot_type: str) -> str:
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


class TikTokPlatform(Platform):

    def get_name(self) -> str:
        return "TikTok"

    def format_message(self, content: str, bot_type: str) -> str:
        if bot_type == "Troll":
            formatted = f"pov: ktos mowi ze (temat) ma sens 💀💀💀\n"
            formatted += f"bestie... {content}\n"
            formatted += "its giving delulu 😭 no cap fr fr"
        elif bot_type == "Spammer":
            formatted = f"ok but why is nobody talking about (temat)?? 🤑\n"
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


class Bot(ABC):

    def __init__(self, platform_obj: Platform):
        self._platform_obj = platform_obj
        self.bot_type = self._get_bot_type()
        self.platform = platform_obj.get_name()

    @abstractmethod
    def _get_bot_type(self) -> str:
        pass

    @abstractmethod
    def generate_content(self, topic: str) -> str:
        pass

    def generate_post(self, topic: str) -> Dict:
        content = self.generate_content(topic)
        formatted = self._platform_obj.format_message(content, self.bot_type)

        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class TrollBot(Bot):

    def _get_bot_type(self) -> str:
        return "Troll"

    def generate_content(self, topic: str) -> str:
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        return random.choice(provocations)


class SpammerBot(Bot):

    def _get_bot_type(self) -> str:
        return "Spammer"

    def generate_content(self, topic: str) -> str:
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        return random.choice(spam_templates)


class ConspiracistBot(Bot):

    def _get_bot_type(self) -> str:
        return "Conspiracist"

    def generate_content(self, topic: str) -> str:
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        return random.choice(conspiracies)


class FakeNewsBot(Bot):

    def _get_bot_type(self) -> str:
        return "FakeNews"

    def generate_content(self, topic: str) -> str:
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        return random.choice(fake_news)


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


def get_bot(bot_type: str, platform: str):
    platforms = {
        "Twitter": TwitterPlatform(),
        "Facebook": FacebookPlatform(),
        "LinkedIn": LinkedInPlatform(),
        "TikTok": TikTokPlatform()
    }

    bots = {
        "Troll": TrollBot,
        "Spammer": SpammerBot,
        "Conspiracist": ConspiracistBot,
        "FakeNews": FakeNewsBot
    }

    if platform not in platforms:
        raise ValueError(f"Unknown platform '{platform}'")
    if bot_type not in bots:
        raise ValueError(f"Unknown bot_type '{bot_type}'")

    platform_obj = platforms[platform]
    bot_class = bots[bot_type]
    return bot_class(platform_obj)


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
