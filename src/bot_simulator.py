"""
Symulator botow internetowych (w celach edukacyjnych!).
UWAGA: Ten kod ma EKSPLOZJE KLAS! Uzyj wzorca Bridge.
"""
from abc import ABC, abstractmethod
from typing import Dict
import random


class Platform(ABC):
    @abstractmethod
    def format_troll(self, content: str, topic: str) -> str: pass
    @abstractmethod
    def format_spammer(self, content: str, topic: str) -> str: pass
    @abstractmethod
    def format_conspiracist(self, content: str, topic: str) -> str: pass
    @abstractmethod
    def format_fakenews(self, content: str, topic: str) -> str: pass
    @abstractmethod
    def get_name(self) -> str: pass

class Twitter(Platform):
    def get_name(self) -> str: return "Twitter"
    def _limit(self, t): return t[:277] + "..." if len(t) > 280 else t

    def format_troll(self, content, topic): return self._limit(f"{content} ratio + L + niemasz racji #triggered")
    def format_spammer(self, content, topic): return self._limit(f"🚀🚀🚀 {content} Link in bio! #crypto #moon #lambo")
    def format_conspiracist(self, content, topic): return self._limit(f"🧵 WATEK: {content} Coincidence? I think NOT! #WakeUp #Truth")
    def format_fakenews(self, content, topic): return self._limit(f"⚠️ {content} RETWEET zanim zcenzuruja! #Breaking #News")

class Facebook(Platform):
    def get_name(self) -> str: return "Facebook"
    def format_troll(self, content, topic): return f"{content}... PROSZE SIE OBUDZIC LUDZIE!!! Udostepnij zanim USUNĄ!!! 😠😠😠"
    def format_spammer(self, content, topic): return f"Moja kuzynka zarobila 5000zl dzieki {topic}!!! {content} NapiszINFO w komentarzu!!! 💰💰💰"
    def format_conspiracist(self, content, topic): return f"UDOSTEPNIJ ZANIM USUNA!!!\n\n{content}\n\nMainstream media UKRYWA to przed Toba!!! Zrobie researcha!!! 👁️👁️👁️"
    def format_fakenews(self, content, topic): return f"🔴 PILNE 🔴\n\n{content}\n\nMedia MILCZA! Udostepnij swoim znajomym!!! Twoja rodzina MUSI to zobaczyc!!! ⚠️⚠️⚠️"

class LinkedIn(Platform):
    def get_name(self) -> str: return "LinkedIn"
    def format_troll(self, content, topic): return f"Unpopular opinion: {content}\n\nI know this might be controversial, but someone had to say it.\n\nAgree? ♻️ Repost to spread awareness\n#ThoughtLeadership #Disruption #Controversial"
    def format_spammer(self, content, topic): return f"I'm excited to announce that {content}\n\nThis is not financial advice, but my portfolio is up 10000%.\n\nDM me for exclusive insights.\n#Entrepreneurship #Hustle #Blessed"
    def format_conspiracist(self, content, topic): return f"After 15 years in the industry, I need to share something:\n\n{content}\n\nThe elites don't want you to know this.\n\nComment 'TRUTH' if you're awake.\n#DeepState #FollowTheMoney #QuestionEverything"
    def format_fakenews(self, content, topic): return f"🚨 Industry Alert 🚨\n\n{content}\n\nMy sources in the industry have confirmed this.\n\nShare with your network before it's too late.\n#BreakingNews #IndustryInsider #MustRead"

class TikTok(Platform):
    def get_name(self) -> str: return "TikTok"
    def format_troll(self, content, topic): return f"pov: ktos mowi ze {topic} ma sens 💀💀💀\nbestie... {content}\nits giving delulu 😭 no cap fr fr"
    def format_spammer(self, content, topic): return f"ok but why is nobody talking about {topic}?? 🤑\n{content}\nlink in bio bestie trust me im just like you 💅"
    def format_conspiracist(self, content, topic): return f"wait wait wait... 🤯\n{content}\nwhy is this not on the news?? theyre deleting this video in 3...2... 👁️"
    def format_fakenews(self, content, topic): return f"STORYTIME: so i just found out something crazy 😱\n{content}\nshare before they take this down!! part 2 if this blows up 👀"

class Bot(ABC):
    def __init__(self, platform_impl: Platform):
        self._platform_impl = platform_impl
        self.bot_type = "Generic"
    @property
    def platform(self) -> str:
        return self._platform_impl.get_name()

    @abstractmethod
    def generate_post(self, topic: str) -> Dict:
        pass

class TrollBot(Bot):
    def __init__(self, platform_impl):
        super().__init__(platform_impl)
        self.bot_type = "Troll"

    def generate_post(self, topic: str) -> Dict:
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        raw_content = random.choice(provocations)
        final_content = self._platform_impl.format_troll(raw_content, topic)
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": final_content
        }

class SpammerBot(Bot):
    def __init__(self, platform_impl):
        super().__init__(platform_impl)
        self.bot_type = "Spammer"

    def generate_post(self, topic: str) -> Dict:
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        raw_content = random.choice(spam_templates)
        final_content = self._platform_impl.format_spammer(raw_content, topic)
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": final_content
        }

class ConspiracistBot(Bot):
    def __init__(self, platform_impl):
        super().__init__(platform_impl)
        self.bot_type = "Conspiracist"
    def generate_post(self, topic: str) -> Dict:
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        raw_content = random.choice(conspiracies)
        final_content = self._platform_impl.format_conspiracist(raw_content, topic)
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": final_content
        }

class FakeNewsBot(Bot):
    def __init__(self, platform_impl):
        super().__init__(platform_impl)
        self.bot_type = "FakeNews"
    def generate_post(self, topic: str) -> Dict:
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        raw_content = random.choice(fake_news)
        final_content = self._platform_impl.format_fakenews(raw_content, topic)
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": final_content
        }

def create_bot_adapter(bot_class, platform_class):
    """Factory Method - generuje klase adaptera"""
    class BotAdapter:
        def __init__(self):
            self._bot = bot_class(platform_class())
            self.bot_type = self._bot.bot_type
            self.platform = self._bot.platform
        
        def generate_post(self, topic):
            return self._bot.generate_post(topic)
    
    return BotAdapter  # zwraca klase adaptera
bot_types = {
    "Troll": TrollBot,
    "Spammer": SpammerBot,
    "Conspiracist": ConspiracistBot,
    "FakeNews": FakeNewsBot
}

platforms = {
    "Twitter": Twitter,
    "Facebook": Facebook,
    "LinkedIn": LinkedIn,
    "TikTok": TikTok
}

for bot_name, bot_class in bot_types.items():
    for platform_name, platform_class in platforms.items():
        class_name = f"{bot_name}{platform_name}Bot"
        globals()[class_name] = create_bot_adapter(bot_class, platform_class)


def get_bot(bot_type: str, platform_name: str):
    if bot_type == "Troll":
        if platform_name == "Twitter": return TrollTwitterBot()
        elif platform_name == "Facebook": return TrollFacebookBot()
        elif platform_name == "LinkedIn": return TrollLinkedInBot()
        elif platform_name == "TikTok": return TrollTikTokBot()
    elif bot_type == "Spammer":
        if platform_name == "Twitter": return SpammerTwitterBot()
        elif platform_name == "Facebook": return SpammerFacebookBot()
        elif platform_name == "LinkedIn": return SpammerLinkedInBot()
        elif platform_name == "TikTok": return SpammerTikTokBot()
    elif bot_type == "Conspiracist":
        if platform_name == "Twitter": return ConspiracistTwitterBot()
        elif platform_name == "Facebook": return ConspiracistFacebookBot()
        elif platform_name == "LinkedIn": return ConspiracistLinkedInBot()
        elif platform_name == "TikTok": return ConspiracistTikTokBot()
    elif bot_type == "FakeNews":
        if platform_name == "Twitter": return FakeNewsTwitterBot()
        elif platform_name == "Facebook": return FakeNewsFacebookBot()
        elif platform_name == "LinkedIn": return FakeNewsLinkedInBot()
        elif platform_name == "TikTok": return FakeNewsTikTokBot()
    
    raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform_name}'")


if __name__ == "__main__":
    print("=" * 60)
    print("SYMULATOR BOTOW INTERNETOWYCH (BRIDGE PATTERN)")
    print("=" * 60)
    random.seed(42)
    
    bot_types = ["Troll", "Spammer", "Conspiracist", "FakeNews"]
    platform_names = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
    
    for b_type in bot_types:
        print(f"\n--- {b_type} ---")
        for p_name in platform_names:
            bot = get_bot(b_type, p_name)
            res = bot.generate_post("AI")
            print(f"[{res['platform']}] {res['content'][:50]}...")