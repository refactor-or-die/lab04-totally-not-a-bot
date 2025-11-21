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

def get_bot(bot_type: str, platform: str):
    """
    Zwraca odpowiedniego bota dla danego typu i platformy.
    
    SPÓJRZ NA TE IFY! 16 kombinacji! A co jak dodamy Mastodon i Reddit?
    """

    if platform == "Twitter":
        platformObj = Twitter()
    elif platform == "Facebook":
        platformObj = Facebook()
    elif platform == "LinkedIn":
        platformObj = LinkedIn()
    elif platform == "TikTok":
        platformObj = TikTok()
    else:
        raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform}'")

    if bot_type == "Troll":
        return Troll(platformObj)
    elif bot_type == "Spammer":
        return Spammer(platformObj)
    elif bot_type == "Conspiracist":
        return Conspiracist(platformObj)
    elif bot_type == "FakeNews":
        return FakeNews(platformObj)
    
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
