from abc import ABC, abstractmethod
from typing import Dict
import random

# =================================================================
# 1. IMPLEMENTACJA (Platformy - formatowanie)
# =================================================================

class Platform(ABC):
    @abstractmethod
    def format_message(self, bot_type: str, content: str, topic: str) -> str: pass
    @abstractmethod
    def get_name(self) -> str: pass

class Twitter(Platform):
    def get_name(self) -> str: return "Twitter"
    def _limit(self, t): return t[:277] + "..." if len(t) > 280 else t
    def format_message(self, bot_type: str, content: str, topic: str) -> str:
        formats = {
            "Troll": f"{content} ratio + L + niemasz racji #triggered",
            "Spammer": f"🚀🚀🚀 {content} Link in bio! #crypto #moon #lambo",
            "Conspiracist": f"🧵 WATEK: {content} Coincidence? I think NOT! #WakeUp #Truth",
            "FakeNews": f"⚠️ {content} RETWEET zanim zcenzuruja! #Breaking #News"
        }
        return self._limit(formats.get(bot_type, content))

class Facebook(Platform):
    def get_name(self) -> str: return "Facebook"
    def format_message(self, bot_type: str, content: str, topic: str) -> str:
        formats = {
            "Troll": f"{content}... PROSZE SIE OBUDZIC LUDZIE!!! Udostepnij zanim USUNĄ!!! 😠😠😠",
            "Spammer": f"Moja kuzynka zarobila 5000zl dzieki {topic}!!! {content} Napisz INFO w komentarzu!!! 💰💰💰",
            "Conspiracist": f"UDOSTEPNIJ ZANIM USUNA!!! prawda jest taka: {content} Mainstream media UKRYWA to przed Toba!!! Zrobie researcha!!! 👁️👁️👁️",
            "FakeNews": f"🔴 PILNE 🔴\n\n{content}\n\nMedia MILCZA! Udostepnij swoim znajomym!!! Twoja rodzina MUSI to zobaczyc!!! ⚠️⚠️⚠️"
        }
        return formats.get(bot_type, content)

class LinkedIn(Platform):
    def get_name(self) -> str: return "LinkedIn"
    def format_message(self, bot_type: str, content: str, topic: str) -> str:
        formats = {
            "Troll": f"Unpopular opinion: {content}\n\nI know this might be controversial, but someone had to say it.\n\nAgree? ♻️ Repost to spread awareness\n#ThoughtLeadership #Disruption #Controversial",
            "Spammer": f"I'm excited to announce that {content}\n\nThis is not financial advice, but my portfolio is up 10000%.\n\nDM me for exclusive insights.\n#Entrepreneurship #Hustle #Blessed",
            "Conspiracist": f"After 15 years in the industry, I need to share something:\n\n{content}\n\nThe elites don't want you to know this.\n\nComment 'TRUTH' if you're awake.\n#DeepState #FollowTheMoney #QuestionEverything",
            "FakeNews": f"🚨 Industry Alert 🚨\n\n{content}\n\nMy sources in the industry have confirmed this.\n\nShare with your network before it's too late.\n#BreakingNews #IndustryInsider #MustRead"
        }
        return formats.get(bot_type, content)

class TikTok(Platform):
    def get_name(self) -> str: return "TikTok"
    def format_message(self, bot_type: str, content: str, topic: str) -> str:
        formats = {
            "Troll": f"pov: ktos mowi ze {topic} ma sens 💀💀💀\nbestie... {content}\nits giving delulu 😭 no cap fr fr",
            "Spammer": f"ok but why is nobody talking about {topic}?? 🤑\n{content}\nlink in bio bestie trust me im just like you 💅",
            "Conspiracist": f"wait wait wait... 🤯\n{content}\nwhy is this not on the news?? theyre deleting this video in 3...2... 👁️",
            "FakeNews": f"STORYTIME: so i just found out something crazy 😱\n{content}\nshare before they take this down!! part 2 if this blows up 👀"
        }
        return formats.get(bot_type, content)

# =================================================================
# 2. ABSTRAKCJA (Boty - logika treści)
# =================================================================

class Bot(ABC):
    def __init__(self, platform: Platform):
        self._platform_impl = platform
        self.bot_type = "Generic"

    @property
    def platform(self) -> str:
        return self._platform_impl.get_name()

    @abstractmethod
    def get_raw_content(self, topic: str) -> str: pass

    def generate_post(self, topic: str) -> Dict:
        raw_content = self.get_raw_content(topic)
        final_content = self._platform_impl.format_message(self.bot_type, raw_content, topic)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": final_content
        }

class TrollBot(Bot):
    def __init__(self, platform): super().__init__(platform); self.bot_type = "Troll"
    def get_raw_content(self, topic):
        return random.choice([f"Serio wierzysz w {topic}?", f"{topic} to najwiekszy przekret w historii", f"Kazdy kto popiera {topic} nie ma pojecia o czyms"])

class SpammerBot(Bot):
    def __init__(self, platform): super().__init__(platform); self.bot_type = "Spammer"
    def get_raw_content(self, topic):
        return random.choice([f"NOWY {topic} COIN! 1000x gwarantowane!", f"Zarobiles na {topic}? JA TAK! Sprawdz jak", f"{topic} MOON SOON! Ostatnia szansa!"])

class ConspiracistBot(Bot):
    def __init__(self, platform): super().__init__(platform); self.bot_type = "Conspiracist"
    def get_raw_content(self, topic):
        return random.choice([f"Czy zastanawiales sie KOMU zalezy na {topic}?", f"{topic} to przykrywka dla PRAWDZIWEGO planu", f"Oni nie chca zebys wiedzial prawde o {topic}"])

class FakeNewsBot(Bot):
    def __init__(self, platform): super().__init__(platform); self.bot_type = "FakeNews"
    def get_raw_content(self, topic):
        return random.choice([f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne", f"PILNE: Rzad ukrywa prawde o {topic}", f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"])

# =================================================================
# 3. BRIDGE ADAPTER I FABRYKA (Zgodność z testami)
# =================================================================

_bot_map = {"Troll": TrollBot, "Spammer": SpammerBot, "Conspiracist": ConspiracistBot, "FakeNews": FakeNewsBot}
_plat_map = {"Twitter": Twitter, "Facebook": Facebook, "LinkedIn": LinkedIn, "TikTok": TikTok}

# Funkcja pomocnicza do tworzenia klas adapterów, aby uniknąć problemów z super()
def create_adapter_class(bot_cls, plat_cls):
    class Adapter(bot_cls):
        def __init__(self):
            super().__init__(plat_cls())
    return Adapter

for b_name, b_class in _bot_map.items():
    for p_name, p_class in _plat_map.items():
        name = f"{b_name}{p_name}Bot"
        globals()[name] = create_adapter_class(b_class, p_class)

def get_bot(bot_type: str, platform_name: str):
    """Factory Method zwracająca instancję odpowiedniego bota."""
    class_name = f"{bot_type}{platform_name}Bot"
    if class_name in globals():
        return globals()[class_name]()
    raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform_name}'")

class BotFactory:
    @staticmethod
    def create_bot(bot_type: str, platform: str):
        return get_bot(bot_type, platform)