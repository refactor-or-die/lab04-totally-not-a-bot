"""
Symulator botow internetowych (w celach edukacyjnych!).
UWAGA: Ten kod ma EKSPLOZJE KLAS! Uzyj wzorca Bridge.

Mamy 4 typy botow i 4 platformy = 16 klas.
Dodanie nowej platformy wymaga 4 nowych klas!
Dodanie nowego bota wymaga 4 nowych klas!

To nie jest skalowalne rozwiazanie...
"""
from typing import Dict
from abc import ABC, abstractmethod
import random

class PlatformStyle(ABC):
    @abstractmethod
    def format_troll(self, content: str) -> str:
        pass
    @abstractmethod
    def format_spammer(self, content: str) -> str:
        pass
    @abstractmethod
    def format_conspiracist(self, content: str) -> str:
        pass
    @abstractmethod
    def format_fakenews(self, content: str) -> str:
        pass
    
class PlatformImplementation(ABC):
    def __init__(self, style: PlatformStyle):
        self.style = style
    
    def format_content(self, content: str, topic: str, bot_type: str) -> str:
        formatters = {
            "Troll": self.style.format_troll,
            "Spammer": self.style.format_spammer,
            "Conspiracist": self.style.format_conspiracist,
            "FakeNews": self.style.format_fakenews
        }
        return formatters[bot_type](content, topic)
        
    @abstractmethod
    def get_platform_name(self) -> str:
        pass
    
class TwitterImplementation(PlatformImplementation):
    def __init__(self):
        super().__init__(TwitterStyle())
    
    def get_platform_name(self):
        return "Twitter"
    
class FacebookImplementation(PlatformImplementation):
    def __init__(self):
        super().__init__(FacebookStyle())
    
    def get_platform_name(self):
        return "Facebook"
    
class LinkedInImplementation(PlatformImplementation):
    def __init__(self):
        super().__init__(LinkedInStyle())
    
    def get_platform_name(self):
        return "LinkedIn"  
    
class TikTokImplementation(PlatformImplementation):
    def __init__(self):
        super().__init__(TikTokStyle())
    
    def get_platform_name(self):
        return "TikTok"
    
class SocialMediaBot(ABC):
    def __init__(self, platform: PlatformImplementation):
        self.platform = platform
    @abstractmethod
    def generate_content(self, topic:str) -> str:
        pass
    def generate_post(self, topic:str) -> Dict:
        content = self.generate_content(topic)
        formatted_content = self.platform.format_content(content, topic, self.bot_type)
        return {
            "bot_type": self.bot_type,
            "platform": self.platform.get_platform_name(),
            "topic": topic,
            "content": formatted_content
        }

class TrollBot(SocialMediaBot):
    def __init__(self, platform: PlatformImplementation):
        super().__init__(platform)
        self.bot_type = "Troll"
        
    def generate_content(self, topic):
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        return random.choice(provocations)
           
class SpammerBot(SocialMediaBot):
    def __init__(self, platform: PlatformImplementation):
        super().__init__(platform)
        self.bot_type = "Spammer"
        
    def generate_content(self, topic):
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        return random.choice(spam_templates)    
   
class ConspiracistBot(SocialMediaBot):
    def __init__(self, platform: PlatformImplementation):
        super().__init__(platform)
        self.bot_type = "Conspiracist"
        
    def generate_content(self, topic):
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        return random.choice(conspiracies)    
   
class FakeNewsBot(SocialMediaBot):
    def __init__(self, platform: PlatformImplementation):
        super().__init__(platform)
        self.bot_type = "FakeNews"
        
    def generate_content(self, topic):
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        return random.choice(fake_news)  
    
class TwitterStyle(PlatformStyle):
    
    def format_troll(self, content: str, topic) -> str:
        formatted = f"{content} ratio + L + niemasz racji"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        formatted += " #triggered"
        return formatted
    
    def format_spammer(self, content: str, topic) -> str:
        formatted = f"🚀🚀🚀 {content} Link in bio! #crypto #moon #lambo"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        return formatted
    
    def format_conspiracist(self, content: str, topic) -> str:
        formatted = f"🧵 WATEK: {content} Coincidence? I think NOT! #WakeUp #Truth"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        return formatted
    
    def format_fakenews(self, content: str, topic) -> str:
        formatted = f"⚠️ {content} RETWEET zanim zcenzuruja! #Breaking #News"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        return formatted
    
class FacebookStyle(PlatformStyle):
    
    def format_troll(self, content: str, topic) -> str:
        formatted = f"{content}... PROSZE SIE OBUDZIC LUDZIE!!! "
        formatted += "Udostepnij zanim USUNĄ!!! "
        formatted += "😠😠😠"
        return formatted
    
    def format_spammer(self, content: str, topic) -> str:
        formatted = f"Moja kuzynka zarobila 5000zl dzieki {topic}!!! "
        formatted += f"{content} "
        formatted += "NapiszINFO w komentarzu!!! 💰💰💰"
        return formatted
    
    def format_conspiracist(self, content: str, topic) -> str:
        formatted = f"UDOSTEPNIJ ZANIM USUNA!!!\n\n"
        formatted += f"{content}\n\n"
        formatted += "Mainstream media UKRYWA to przed Toba!!! "
        formatted += "Zrobie researcha!!! 👁️👁️👁️"
        return formatted
    
    def format_fakenews(self, content: str, topic) -> str:
        formatted = f"🔴 PILNE 🔴\n\n"
        formatted += f"{content}\n\n"
        formatted += "Media MILCZA! Udostepnij swoim znajomym!!! "
        formatted += "Twoja rodzina MUSI to zobaczyc!!! ⚠️⚠️⚠️"
        return formatted
    
class LinkedInStyle(PlatformStyle):
    
    def format_troll(self, content: str, topic) -> str:
        formatted = f"Unpopular opinion: {content}\n\n"
        formatted += "I know this might be controversial, but someone had to say it.\n\n"
        formatted += "Agree? ♻️ Repost to spread awareness\n"
        formatted += "#ThoughtLeadership #Disruption #Controversial"
        return formatted
    
    def format_spammer(self, content: str, topic) -> str:
        formatted = f"I'm excited to announce that {content}\n\n"
        formatted += "This is not financial advice, but my portfolio is up 10000%.\n\n"
        formatted += "DM me for exclusive insights.\n"
        formatted += "#Entrepreneurship #Hustle #Blessed"
        return formatted
    
    def format_conspiracist(self, content: str, topic) -> str:
        formatted = f"After 15 years in the industry, I need to share something:\n\n"
        formatted += f"{content}\n\n"
        formatted += "The elites don't want you to know this.\n\n"
        formatted += "Comment 'TRUTH' if you're awake.\n"
        formatted += "#DeepState #FollowTheMoney #QuestionEverything"
        return formatted
    
    def format_fakenews(self, content: str, topic) -> str:
        formatted = f"🚨 Industry Alert 🚨\n\n"
        formatted += f"{content}\n\n"
        formatted += "My sources in the industry have confirmed this.\n\n"
        formatted += "Share with your network before it's too late.\n"
        formatted += "#BreakingNews #IndustryInsider #MustRead"
        return formatted
    
class TikTokStyle(PlatformStyle):
    
    def format_troll(self, content: str, topic) -> str:
        formatted = f"pov: ktos mowi ze {topic} ma sens 💀💀💀\n"
        formatted += f"bestie... {content}\n"
        formatted += "its giving delulu 😭 no cap fr fr"
        return formatted
    
    def format_spammer(self, content: str, topic) -> str:
        formatted = f"ok but why is nobody talking about {topic}?? 🤑\n"
        formatted += f"{content}\n"
        formatted += "link in bio bestie trust me im just like you 💅"
        return formatted
        
    
    def format_conspiracist(self, content: str, topic) -> str:
        formatted = f"wait wait wait... 🤯\n"
        formatted += f"{content}\n"
        formatted += "why is this not on the news?? theyre deleting this video in 3...2... 👁️"
        return formatted
    
    def format_fakenews(self, content: str, topic) -> str:
        formatted = f"STORYTIME: so i just found out something crazy 😱\n"
        formatted += f"{content}\n"
        formatted += "share before they take this down!! part 2 if this blows up 👀"
        return formatted
    
def get_bot(bot_type: str, platform: str):
    class_name = f"{bot_type}{platform}Bot"

    if class_name not in globals():
        raise ValueError(f"Unknown combination: {bot_type} + {platform}")

    return globals()[class_name]() 


def create_bot_adapter(bot_class, platform_class):
    class BotAdapter:
        def __init__(self):
            self._bot = bot_class(platform_class())
            self.bot_type = self._bot.bot_type
            self.platform = self._bot.platform.get_platform_name()

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
    "Twitter": TwitterImplementation,
    "Facebook": FacebookImplementation,
    "LinkedIn": LinkedInImplementation,
    "TikTok": TikTokImplementation
}


for bot_name, bot_class in bot_types.items():
    for platform_name, platform_class in platforms.items():
        class_name = f"{bot_name}{platform_name}Bot"
        globals()[class_name] = create_bot_adapter(bot_class, platform_class)



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
