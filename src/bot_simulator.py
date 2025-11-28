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
from social_platform import *
from bot import *


# ============================================================================
# FUNKCJA POMOCNICZA
# ============================================================================

def create_bot_adapter(bot_class, platform_class, class_name):
    """Factory Method - generuje klase adaptera o odpowiedniej nazwie"""

    def __init__(self):
        self._bot = bot_class(platform_class())
        self.bot_type = self._bot.bot_type
        self.platform = self._bot.platform

    def generate_post(self, topic):
        return self._bot.generate_post(topic)

    return type(class_name, (object,), {
        "__init__": __init__,
        "generate_post": generate_post,
    })


bot_types = {
    "Troll": Troll,
    "Spammer": Spammer,
    "Conspiracist": Conspiracist,
    "FakeNews": FakeNews
}

platforms = {
    "Twitter": Twitter,
    "Facebook": Facebook,
    "LinkedIn": LinkedIn,
    "TikTok": TikTok
}

# Magia!
for bot_name, bot_class in bot_types.items():
    for platform_name, platform_class in platforms.items():
        class_name = f"{bot_name}{platform_name}Bot"
        globals()[class_name] = create_bot_adapter(bot_class, platform_class, class_name)



def get_bot(bot_type: str, platform: str):
    class_name = f"{bot_type}{platform}Bot"

    if class_name not in globals():
        raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform}'")

    return globals()[class_name]()



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
