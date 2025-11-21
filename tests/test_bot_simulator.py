"""
Testy jednostkowe dla symulatora botow internetowych.
NIE MODYFIKUJ TESTÓW! Powinny przechodzić zarówno przed jak i po refaktoryzacji, 
jeśli refaktoryzacja polega na wprowadzeniu wzorca Bridge z klasami abstrakcyjnymi.
"""
import pytest
import random
from bot_simulator import (
    Tiktok,Twitter,Facebook,LinkedIn,Troll,Spammer,Conspiracist,FakeNews,
    get_bot, Bot
)

def get_bot_instance(bot_type: str, platform: str) -> Bot:
    """Tworzy instancję Bota za pomocą funkcji get_bot."""
    return get_bot(bot_type, platform)

class TestBotBasicInfo:
    """Testy podstawowych informacji o botach (sprawdzają typ Bota i typ Platformy)."""
    
    def test_troll_twitter_info(self):
        bot = get_bot_instance("Troll", "Twitter")
        assert bot.__class__.__name__ == "Troll"
        assert bot.platform.__class__.__name__ == "Twitter"
    
    def test_troll_facebook_info(self):
        bot = get_bot_instance("Troll", "Facebook")
        assert bot.__class__.__name__ == "Troll"
        assert bot.platform.__class__.__name__ == "Facebook"
    
    def test_troll_linkedin_info(self):
        bot = get_bot_instance("Troll", "LinkedIn")
        assert bot.__class__.__name__ == "Troll"
        assert bot.platform.__class__.__name__ == "LinkedIn"
    
    def test_troll_tiktok_info(self):
        bot = get_bot_instance("Troll", "TikTok")
        assert bot.__class__.__name__ == "Troll"
        assert bot.platform.__class__.__name__ == "Tiktok" 
    
    def test_spammer_twitter_info(self):
        bot = get_bot_instance("Spammer", "Twitter")
        assert bot.__class__.__name__ == "Spammer"
        assert bot.platform.__class__.__name__ == "Twitter"
    
    def test_spammer_facebook_info(self):
        bot = get_bot_instance("Spammer", "Facebook")
        assert bot.__class__.__name__ == "Spammer"
        assert bot.platform.__class__.__name__ == "Facebook"
    
    def test_conspiracist_linkedin_info(self):
        bot = get_bot_instance("Conspiracist", "LinkedIn")
        assert bot.__class__.__name__ == "Conspiracist"
        assert bot.platform.__class__.__name__ == "LinkedIn"
    
    def test_fakenews_tiktok_info(self):
        bot = get_bot_instance("FakeNews", "TikTok")
        assert bot.__class__.__name__ == "FakeNews"
        assert bot.platform.__class__.__name__ == "Tiktok"


class TestBotPostStructure:
    """Testy struktury postów (sprawdzają wynik działania generate_post)."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_post_returns_dict(self):
        bot = get_bot_instance("Troll", "Twitter")
        result = bot.generate_post("AI")
        assert isinstance(result, dict)
    
    def test_post_has_required_keys(self):
        bot = get_bot_instance("Spammer", "Facebook")
        result = bot.generate_post("crypto")
        
        assert "bot_type" in result
        assert "platform" in result
        assert "topic" in result
        assert "content" in result
    
    def test_post_preserves_topic(self):
        bot = get_bot_instance("Conspiracist", "LinkedIn")
        result = bot.generate_post("5G")
        assert result["topic"] == "5G"
    
    def test_post_preserves_bot_type(self):
        bot = get_bot_instance("FakeNews", "TikTok")
        result = bot.generate_post("vaccines")
        assert result["bot_type"] == "FakeNews"
    
    def test_post_preserves_platform(self):
        bot = get_bot_instance("Troll", "LinkedIn")
        result = bot.generate_post("blockchain")
        assert result["platform"] == "LinkedIn"


class TestTwitterFormatting:
    """Testy formatowania na Twitterze"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_twitter_has_hashtag(self):
        platform = Twitter()
        message = platform.format_message("Test bez hashtagu")
        assert "#" in message

    def test_twitter_respects_length_limit(self):
        bot = get_bot_instance("Spammer", "Twitter")
        result = bot.generate_post("cryptocurrency")
        assert len(result["content"]) <= 280
    
    def test_twitter_troll_content(self):
        bot = get_bot_instance("Troll", "Twitter")
        result = bot.generate_post("climate")
        assert "Serio wierzysz w climate?" in result["content"]

    def test_twitter_spammer_content(self):
        bot = get_bot_instance("Spammer", "Twitter")
        result = bot.generate_post("NFT")
        assert "NOWY NFT COIN!" in result["content"]

    def test_twitter_conspiracist_content(self):
        bot = get_bot_instance("Conspiracist", "Twitter")
        result = bot.generate_post("government")
        assert "Czy zastanawiales sie KOMU zalezy na government?" in result["content"]

    def test_twitter_fakenews_content(self):
        bot = get_bot_instance("FakeNews", "Twitter")
        result = bot.generate_post("economy")
        assert "BREAKING: Naukowcy potwierdzili ze economy jest niebezpieczne" in result["content"]


class TestFacebookFormatting:
    """Testy formatowania na Facebooku"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_facebook_troll_has_caps(self):
        bot = get_bot_instance("Troll", "Facebook")
        result = bot.generate_post("politics")
        # Treść Trolla zawiera CAPS w treści
        assert "SERIO" in result["content"]
    
    def test_facebook_spammer_mentions_cousin(self):
        bot = get_bot_instance("Spammer", "Facebook")
        result = bot.generate_post("investment")
        assert "Zarobiles na investment? JA TAK!" in result["content"]
    
    def test_facebook_conspiracist_has_question(self):
        bot = get_bot_instance("Conspiracist", "Facebook")
        result = bot.generate_post("media")
        assert "Czy zastanawiales sie KOMU zalezy na media?" in result["content"]
    
    def test_facebook_fakenews_has_urgent(self):
        bot = get_bot_instance("FakeNews", "Facebook")
        result = bot.generate_post("health")
        assert "PILNE" in result["content"]


class TestLinkedInFormatting:
    """Testy formatowania na LinkedIn"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_linkedin_has_professional_hashtags(self):
        bot = get_bot_instance("Troll", "LinkedIn")
        result = bot.generate_post("remote work")
        assert "Serio wierzysz w remote work?" in result["content"]
    
    def test_linkedin_troll_content(self):
        bot = get_bot_instance("Troll", "LinkedIn")
        result = bot.generate_post("AI")
        assert "Serio wierzysz w AI?" in result["content"]
    
    def test_linkedin_spammer_content(self):
        bot = get_bot_instance("Spammer", "LinkedIn")
        result = bot.generate_post("startup")
        assert "NOWY startup COIN!" in result["content"]
    
    def test_linkedin_conspiracist_content(self):
        bot = get_bot_instance("Conspiracist", "LinkedIn")
        result = bot.generate_post("industry")
        assert "Czy zastanawiales sie KOMU zalezy na industry?" in result["content"]
    
    def test_linkedin_fakenews_content(self):
        bot = get_bot_instance("FakeNews", "LinkedIn")
        result = bot.generate_post("tech")
        assert "BREAKING: Naukowcy potwierdzili ze tech jest niebezpieczne" in result["content"]


class TestTikTokFormatting:
    """Testy formatowania na TikToku"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_tiktok_troll_content(self):
        bot = get_bot_instance("Troll", "TikTok")
        result = bot.generate_post("school")
        assert "Serio wierzysz w school?" in result["content"]
    
    def test_tiktok_spammer_content(self):
        bot = get_bot_instance("Spammer", "TikTok")
        result = bot.generate_post("money")
        assert "NOWY money COIN!" in result["content"]
    
    def test_tiktok_conspiracist_content(self):
        bot = get_bot_instance("Conspiracist", "TikTok")
        result = bot.generate_post("truth")
        assert "Czy zastanawiales sie KOMU zalezy na truth?" in result["content"]
    
    def test_tiktok_fakenews_content(self):
        bot = get_bot_instance("FakeNews", "TikTok")
        result = bot.generate_post("news")
        assert "BREAKING: Naukowcy potwierdzili ze news jest niebezpieczne" in result["content"]


class TestGetBotFunction:
    """Testy funkcji get_bot"""
    
    def test_get_troll_twitter(self):
        bot = get_bot_instance("Troll", "Twitter")
        assert isinstance(bot, Troll)
        assert isinstance(bot.platform, Twitter)
    
    def test_get_spammer_facebook(self):
        bot = get_bot_instance("Spammer", "Facebook")
        assert isinstance(bot, Spammer)
        assert isinstance(bot.platform, Facebook)
    
    def test_get_conspiracist_linkedin(self):
        bot = get_bot_instance("Conspiracist", "LinkedIn")
        assert isinstance(bot, Conspiracist)
        assert isinstance(bot.platform, LinkedIn)
    
    def test_get_fakenews_tiktok(self):
        bot = get_bot_instance("FakeNews", "TikTok")
        assert isinstance(bot, FakeNews)
        assert isinstance(bot.platform, Tiktok)
    
    def test_get_all_combinations(self):
        bot_types = ["Troll", "Spammer", "Conspiracist", "FakeNews"]
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        
        for bot_type in bot_types:
            for platform in platforms:
                bot = get_bot_instance(bot_type, platform)
                result = bot.generate_post("test_topic")
                assert result["bot_type"] == bot_type
                
                expected_platform_name = "Tiktok" if platform == "TikTok" else platform
                assert result["platform"] == expected_platform_name
    
    def test_invalid_bot_type_raises(self):
        with pytest.raises(ValueError):
            get_bot_instance("Influencer", "Twitter")
    
    def test_invalid_platform_raises(self):
        with pytest.raises(ValueError):
            get_bot_instance("Troll", "MySpace")


class TestContentGeneration:
    """Testy generowania tresci"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_topic_appears_in_content(self):
        bot = get_bot_instance("Troll", "Twitter")
        result = bot.generate_post("pizza")
        assert "pizza" in result["content"].lower()
    
    def test_different_topics_different_content(self):
        random.seed(42)
        bot1 = get_bot_instance("Spammer", "Facebook")
        result1 = bot1.generate_post("crypto")
        
        random.seed(42)
        bot2 = get_bot_instance("Spammer", "Facebook")
        result2 = bot2.generate_post("NFT")
        
        assert result1["content"] != result2["content"]
    
    def test_content_not_empty(self):
        bot_types = ["Troll", "Spammer", "Conspiracist", "FakeNews"]
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        
        for bot_type in bot_types:
            for platform in platforms:
                bot = get_bot_instance(bot_type, platform)
                result = bot.generate_post("test")
                assert len(result["content"]) > 0


class TestBotBehaviorConsistency:
    """Testy spojnosci zachowania botow (sprawdzają surową treść bota)."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_troll_is_provocative(self):
        """Troll powinien byc prowokacyjny na kazdej platformie"""
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        provocative_words = ["wierzysz", "przekret", "pojecia"]
        
        for platform in platforms:
            bot = get_bot_instance("Troll", platform)
            raw_content = bot.generate_content("topic").lower()
            assert any(word in raw_content for word in provocative_words), \
                f"Troll on {platform} should be provocative"
    
    def test_spammer_promotes_something(self):
        """Spammer powinien cos promowac na kazdej platformie"""
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        promo_words = ["1000x", "gwarantowane", "zarobil", "moon"]
        
        for platform in platforms:
            bot = get_bot_instance("Spammer", platform)
            raw_content = bot.generate_content("coin").lower()
            assert any(word in raw_content for word in promo_words), \
                f"Spammer on {platform} should promote something"
    
    def test_conspiracist_questions_reality(self):
        """Conspiracist powinien kwestionowac rzeczywistosc"""
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        conspiracy_words = ["prawda", "ukrywa", "plan", "zastanawiales"]
        
        for platform in platforms:
            bot = get_bot_instance("Conspiracist", platform)
            raw_content = bot.generate_content("government").lower()
            assert any(word in raw_content for word in conspiracy_words), \
                f"Conspiracist on {platform} should question reality"
    
    def test_fakenews_sounds_urgent(self):
        """FakeNews powinien brzmiec pilnie"""
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        urgent_words = ["breaking", "pilne", "szok"]
        
        for platform in platforms:
            bot = get_bot_instance("FakeNews", platform)
            raw_content = bot.generate_content("news").lower()
            assert any(word in raw_content for word in urgent_words), \
                f"FakeNews on {platform} should sound urgent"