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
import bot

# ============================================================================
# TROLL BOTY - prowokuja klocnie na roznych platformach
# ============================================================================

class TrollTwitterBot:
    """Troll na Twitterze - krotki, agresywny"""
    
    def __init__(self):
        self.bot_type = "Troll"
        self.platform = "Twitter"
    
    def generate_post(self, topic: str) -> Dict:
        # Troll generuje prowokacyjna tresc
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        content = random.choice(provocations)
        
        # Twitter formatuje na swoj sposob
        formatted = f"{content} ratio + L + niemasz racji"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        formatted += " #triggered"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class TrollFacebookBot:
    """Troll na Facebooku - boomerski styl"""
    
    def __init__(self):
        self.bot_type = "Troll"
        self.platform = "Facebook"
    
    def generate_post(self, topic: str) -> Dict:
        # Troll generuje prowokacyjna tresc (DUPLIKACJA!)
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        content = random.choice(provocations)
        
        # Facebook formatuje inaczej
        formatted = f"{content}... PROSZE SIE OBUDZIC LUDZIE!!! "
        formatted += "Udostepnij zanim USUNĄ!!! "
        formatted += "😠😠😠"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class TrollLinkedInBot:
    """Troll na LinkedIn - korporacyjna prowokacja"""
    
    def __init__(self):
        self.bot_type = "Troll"
        self.platform = "LinkedIn"
    
    def generate_post(self, topic: str) -> Dict:
        # Troll generuje prowokacyjna tresc (ZNOWU DUPLIKACJA!)
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        content = random.choice(provocations)
        
        # LinkedIn formatuje "profesjonalnie"
        formatted = f"Unpopular opinion: {content}\n\n"
        formatted += "I know this might be controversial, but someone had to say it.\n\n"
        formatted += "Agree? ♻️ Repost to spread awareness\n"
        formatted += "#ThoughtLeadership #Disruption #Controversial"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class TrollTikTokBot:
    """Troll na TikToku - GenZ styl"""
    
    def __init__(self):
        self.bot_type = "Troll"
        self.platform = "TikTok"
    
    def generate_post(self, topic: str) -> Dict:
        # Troll generuje prowokacyjna tresc (4 RAZ TO SAMO!)
        provocations = [
            f"Serio wierzysz w {topic}?",
            f"{topic} to najwiekszy przekret w historii",
            f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
        ]
        content = random.choice(provocations)
        
        # TikTok formatuje w stylu GenZ
        formatted = f"pov: ktos mowi ze {topic} ma sens 💀💀💀\n"
        formatted += f"bestie... {content}\n"
        formatted += "its giving delulu 😭 no cap fr fr"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


# ============================================================================
# SPAMMER BOTY - promuja podejrzane produkty/krypto
# ============================================================================

class SpammerTwitterBot:
    """Spammer na Twitterze"""
    
    def __init__(self):
        self.bot_type = "Spammer"
        self.platform = "Twitter"
    
    def generate_post(self, topic: str) -> Dict:
        # Spammer generuje spam
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        content = random.choice(spam_templates)
        
        # Twitter formatowanie
        formatted = f"🚀🚀🚀 {content} Link in bio! #crypto #moon #lambo"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class SpammerFacebookBot:
    """Spammer na Facebooku"""
    
    def __init__(self):
        self.bot_type = "Spammer"
        self.platform = "Facebook"
    
    def generate_post(self, topic: str) -> Dict:
        # Spammer generuje spam (DUPLIKACJA!)
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        content = random.choice(spam_templates)
        
        # Facebook formatowanie
        formatted = f"Moja kuzynka zarobila 5000zl dzieki {topic}!!! "
        formatted += f"{content} "
        formatted += "NapiszINFO w komentarzu!!! 💰💰💰"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class SpammerLinkedInBot:
    """Spammer na LinkedIn"""
    
    def __init__(self):
        self.bot_type = "Spammer"
        self.platform = "LinkedIn"
    
    def generate_post(self, topic: str) -> Dict:
        # Spammer generuje spam (ZNOWU!)
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        content = random.choice(spam_templates)
        
        # LinkedIn formatowanie
        formatted = f"I'm excited to announce that {content}\n\n"
        formatted += "This is not financial advice, but my portfolio is up 10000%.\n\n"
        formatted += "DM me for exclusive insights.\n"
        formatted += "#Entrepreneurship #Hustle #Blessed"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class SpammerTikTokBot:
    """Spammer na TikToku"""
    
    def __init__(self):
        self.bot_type = "Spammer"
        self.platform = "TikTok"
    
    def generate_post(self, topic: str) -> Dict:
        # Spammer generuje spam (4 RAZ!)
        spam_templates = [
            f"NOWY {topic} COIN! 1000x gwarantowane!",
            f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
            f"{topic} MOON SOON! Ostatnia szansa!"
        ]
        content = random.choice(spam_templates)
        
        # TikTok formatowanie
        formatted = f"ok but why is nobody talking about {topic}?? 🤑\n"
        formatted += f"{content}\n"
        formatted += "link in bio bestie trust me im just like you 💅"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


# ============================================================================
# CONSPIRACIST BOTY - wszedzie widza spiski
# ============================================================================

class ConspiracistTwitterBot:
    """Conspiracist na Twitterze"""
    
    def __init__(self):
        self.bot_type = "Conspiracist"
        self.platform = "Twitter"
    
    def generate_post(self, topic: str) -> Dict:
        # Conspiracist generuje teorie spiskowe
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        content = random.choice(conspiracies)
        
        # Twitter formatowanie
        formatted = f"🧵 WATEK: {content} Coincidence? I think NOT! #WakeUp #Truth"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class ConspiracistFacebookBot:
    """Conspiracist na Facebooku"""
    
    def __init__(self):
        self.bot_type = "Conspiracist"
        self.platform = "Facebook"
    
    def generate_post(self, topic: str) -> Dict:
        # Conspiracist generuje teorie spiskowe (DUPLIKACJA!)
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        content = random.choice(conspiracies)
        
        # Facebook formatowanie
        formatted = f"UDOSTEPNIJ ZANIM USUNA!!!\n\n"
        formatted += f"{content}\n\n"
        formatted += "Mainstream media UKRYWA to przed Toba!!! "
        formatted += "Zrobie researcha!!! 👁️👁️👁️"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class ConspiracistLinkedInBot:
    """Conspiracist na LinkedIn"""
    
    def __init__(self):
        self.bot_type = "Conspiracist"
        self.platform = "LinkedIn"
    
    def generate_post(self, topic: str) -> Dict:
        # Conspiracist generuje teorie spiskowe (ZNOWU!)
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        content = random.choice(conspiracies)
        
        # LinkedIn formatowanie
        formatted = f"After 15 years in the industry, I need to share something:\n\n"
        formatted += f"{content}\n\n"
        formatted += "The elites don't want you to know this.\n\n"
        formatted += "Comment 'TRUTH' if you're awake.\n"
        formatted += "#DeepState #FollowTheMoney #QuestionEverything"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class ConspiracistTikTokBot:
    """Conspiracist na TikToku"""
    
    def __init__(self):
        self.bot_type = "Conspiracist"
        self.platform = "TikTok"
    
    def generate_post(self, topic: str) -> Dict:
        # Conspiracist generuje teorie spiskowe (4 RAZ!)
        conspiracies = [
            f"Czy zastanawiales sie KOMU zalezy na {topic}?",
            f"{topic} to przykrywka dla PRAWDZIWEGO planu",
            f"Oni nie chca zebys wiedzial prawde o {topic}"
        ]
        content = random.choice(conspiracies)
        
        # TikTok formatowanie
        formatted = f"wait wait wait... 🤯\n"
        formatted += f"{content}\n"
        formatted += "why is this not on the news?? theyre deleting this video in 3...2... 👁️"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


# ============================================================================
# FAKENEWS BOTY - szerza dezinformacje
# ============================================================================

class FakeNewsTwitterBot:
    """FakeNews na Twitterze"""
    
    def __init__(self):
        self.bot_type = "FakeNews"
        self.platform = "Twitter"
    
    def generate_post(self, topic: str) -> Dict:
        # FakeNews generuje falszywe wiadomosci
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        content = random.choice(fake_news)
        
        # Twitter formatowanie
        formatted = f"⚠️ {content} RETWEET zanim zcenzuruja! #Breaking #News"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class FakeNewsFacebookBot:
    """FakeNews na Facebooku"""
    
    def __init__(self):
        self.bot_type = "FakeNews"
        self.platform = "Facebook"
    
    def generate_post(self, topic: str) -> Dict:
        # FakeNews generuje falszywe wiadomosci (DUPLIKACJA!)
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        content = random.choice(fake_news)
        
        # Facebook formatowanie
        formatted = f"🔴 PILNE 🔴\n\n"
        formatted += f"{content}\n\n"
        formatted += "Media MILCZA! Udostepnij swoim znajomym!!! "
        formatted += "Twoja rodzina MUSI to zobaczyc!!! ⚠️⚠️⚠️"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class FakeNewsLinkedInBot:
    """FakeNews na LinkedIn"""
    
    def __init__(self):
        self.bot_type = "FakeNews"
        self.platform = "LinkedIn"
    
    def generate_post(self, topic: str) -> Dict:
        # FakeNews generuje falszywe wiadomosci (ZNOWU!)
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        content = random.choice(fake_news)
        
        # LinkedIn formatowanie
        formatted = f"🚨 Industry Alert 🚨\n\n"
        formatted += f"{content}\n\n"
        formatted += "My sources in the industry have confirmed this.\n\n"
        formatted += "Share with your network before it's too late.\n"
        formatted += "#BreakingNews #IndustryInsider #MustRead"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


class FakeNewsTikTokBot:
    """FakeNews na TikToku"""
    
    def __init__(self):
        self.bot_type = "FakeNews"
        self.platform = "TikTok"
    
    def generate_post(self, topic: str) -> Dict:
        # FakeNews generuje falszywe wiadomosci (4 RAZ!)
        fake_news = [
            f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
            f"PILNE: Rzad ukrywa prawde o {topic}",
            f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
        ]
        content = random.choice(fake_news)
        
        # TikTok formatowanie
        formatted = f"STORYTIME: so i just found out something crazy 😱\n"
        formatted += f"{content}\n"
        formatted += "share before they take this down!! part 2 if this blows up 👀"
        
        return {
            "bot_type": self.bot_type,
            "platform": self.platform,
            "topic": topic,
            "content": formatted
        }


# ============================================================================
# FUNKCJA POMOCNICZA
# ============================================================================

def get_bot(bot_type: str, platform: str):
    """
    Zwraca odpowiedniego bota dla danego typu i platformy.
    
    SPÓJRZ NA TE IFY! 16 kombinacji! A co jak dodamy Mastodon i Reddit?
    """
    bots: list = bot.Bot.__subclasses__()
    platforms: list = bot.Platform.__subclasses__()
    
    for p in platforms:
        if p.__name__ == platform:
            for b in bots:
                if b.__name__ == bot_type:
                    return b(platform=p)
    
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

            