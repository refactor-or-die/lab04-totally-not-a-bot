# Lab 04: Totally Not A Bot

## Czy wiesz, ?e...
Wed?ug niekt車rych bada里, nawet 15% kont na Twitterze to boty. Ale ten kod ma wi?kszy problem ni? boty - ma **eksplozj? klas**!

## Twoje zadanie
Dosta?e? kod "symulatora bot車w internetowych" (oczywi?cie w celach edukacyjnych). 

Problem? Poprzedni developer stworzy? **16 osobnych klas** - po jednej dla ka?dej kombinacji typu bota i platformy. TrollTwitterBot, TrollFacebookBot, SpammerLinkedInBot...

Teraz szef m車wi: "Dodaj obs?ug? Mastodona i Wykopu!"

Ty patrzysz na kod i my?lisz: "To b?dzie kolejne **8 klas**. A jak dodamy jeszcze jednego bota, to kolejne **6**. I tak w niesko里czono??..."

**Rozwi?zanie:** Wzorzec Bridge!

## Co zawiera repozytorium
- `bot_simulator.py` - 16 klas kt車re robi? prawie to samo (eksplozja!)
- `test_bot_simulator.py` - testy (NIE RUSZA?!)
- Ten README
- Co?tam

## Problem do rozwi?zania
Mamy 4 typy bot車w:
- **Troll** - prowokuje k?車tnie
- **Spammer** - promuje krypto i "okazje"
- **Conspiracist** - wsz?dzie widzi spiski
- **FakeNews** - szerzy dezinformacj?

I 4 platformy:
- **Twitter** - kr車tko, z hashtagami
- **Facebook** - boomerski styl, du?o emotek
- **LinkedIn** - menad?erski be?kot
- **TikTok** - GenZ slang

**4 ℅ 4 = 16 klas!** A ka?da ma zduplikowany kod generowania tre?ci...

## Instrukcja
1. Sklonuj repo i stw車rz branch `lab4_nazwisko1_nazwisko2`
2. Uruchom testy: `pytest` (powinny przej??)
3. Zrefaktoryzuj kod u?ywaj?c wzorca Bridge:
   - Stw車rz hierarchi? `Platform` (abstrakcja implementacji)
   - Stw車rz hierarchi? `Bot` (abstrakcja)
   - Po??cz je "mostem" - Bot ma referencj? do Platform
4. Uruchom testy ponownie (MUSZ? przej??!)
5. Commit + push na SW車J branch

## Wskaz車wki

### Struktura Bridge
```python
from abc import ABC, abstractmethod

# Implementacja (JAK formatuje)
class Platform(ABC):
    @abstractmethod
    def format_message(self, message: str) -> str:
        pass

# Abstrakcja (CO generuje)
class Bot(ABC):
    def __init__(self, platform: Platform):
        self.platform = platform  # <-- TO JEST MOST!
    
    @abstractmethod
    def generate_content(self, topic: str) -> str:
        pass
    
    def generate_post(self, topic: str) -> Dict:
        content = self.generate_content(topic)
        formatted = self.platform.format_message(content)
        # ...
```

### Co idzie gdzie?
- **Bot** wie CO powiedzie? (trollowanie, spamowanie, teorie spiskowe)
- **Platform** wie JAK to sformatowa? (hashtagi Twittera, emotki Facebooka)
- **Most** ??czy jedno z drugim przez kompozycj?

### Zachowaj API!
Funkcja `get_bot(bot_type, platform)` musi dalej dzia?a?! Mo?esz zmieni? jej implementacj?, ale sygnatura zostaje.

## Co zyskasz?
- **8 klas zamiast 16** (4 boty + 4 platformy)
- Dodanie Mastodona = **1 nowa klasa** (nie 4!)
- Dodanie nowego bota = **1 nowa klasa** (nie 4!)
- Zero duplikacji kodu generowania tre?ci
- Mo?liwo?? zmiany platformy w runtime!

## Kryteria oceny
- Testy przechodz?
- U?yty wzorzec Bridge
- Brak duplikacji kodu
- ?atwo doda? now? platform? (1 klasa)
- ?atwo doda? nowego bota (1 klasa)
- Prowadz?cy nie p?aka?, gdy pr車bowa? czyta? kod

## FAQ

**Q: Czy to naprawd? jest problem?**
A: Tak! 10 bot車w ℅ 10 platform = 100 klas. Z Bridge = 20 klas. R車?nica jest kolosalna.

**Q: Co z t? funkcj? `get_bot()`?**
A: Mo?esz j? zrefaktoryzowa?, ale musi dalej przyjmowa? te same parametry i zwraca? obiekt z metod? `generate_post()`.

**Q: Mog? usun?? te wszystkie klasy typu TrollTwitterBot?**
A: Tak! Po refaktoryzacji nie b?d? potrzebne. Ale `get_bot("Troll", "Twitter")` musi dalej dzia?a?.

**Q: A co z tym randomem w generowaniu tre?ci?**
A: Zostaw go. Boty s? nieprzewidywalne, tak jak prawdziwe.

---

*"Jedyn? rzecz? gorsz? od eksplozji klas jest eksplozja prawdziwych bot車w w internecie"* - Robert Mak?owicz (prawdopodobnie)

**Pro tip:** Je?li po refaktoryzacji dodanie nowej platformy wymaga wi?cej ni? jednej klasy - co? posz?o nie tak. Bridge powinien sprawi?, ?e ka?dy wymiar rozszerza si? niezale?nie!

**Disclaimer:** Ten symulator jest satyr?.