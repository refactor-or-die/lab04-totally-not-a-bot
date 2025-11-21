"""
Testy jednostkowe dla symulatora botow internetowych.
NIE MODYFIKUJ TESTOW! Powinny przechodzic zarowno przed jak i po refaktoryzacji.
"""
import pytest
import random
from bot_simulator import *
from bot import *
from social_platform import *


class TestBotBasicInfo:
    """Testy podstawowych informacji o botach"""
    
    def test_troll_twitter_info(self):
        bot = Troll(Twitter())
        assert bot.bot_type == "Troll"
        assert bot.platform.platform_type == "Twitter"
    
    def test_troll_facebook_info(self):
        bot = Troll(Facebook())
        assert bot.bot_type == "Troll"
        assert bot.platform.platform_type == "Facebook"
    
    def test_troll_linkedin_info(self):
        bot = Troll(LinkedIn())
        assert bot.bot_type == "Troll"
        assert bot.platform.platform_type == "LinkedIn"
    
    def test_troll_tiktok_info(self):
        bot = Troll(TikTok())
        assert bot.bot_type == "Troll"
        assert bot.platform.platform_type == "TikTok"
    
    def test_spammer_twitter_info(self):
        bot = Spammer(Twitter())
        assert bot.bot_type == "Spammer"
        assert bot.platform.platform_type == "Twitter"
    
    def test_spammer_facebook_info(self):
        bot = Spammer(Facebook())
        assert bot.bot_type == "Spammer"
        assert bot.platform.platform_type == "Facebook"
    
    def test_conspiracist_linkedin_info(self):
        bot = Conspiracist(LinkedIn())
        assert bot.bot_type == "Conspiracist"
        assert bot.platform.platform_type == "LinkedIn"
    
    def test_fakenews_tiktok_info(self):
        bot = FakeNews(TikTok())
        assert bot.bot_type == "FakeNews"
        assert bot.platform.platform_type == "TikTok"


class TestBotPostStructure:
    """Testy struktury postow"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_post_returns_dict(self):
        bot = Troll(Twitter())
        result = bot.generate_post("AI")
        assert isinstance(result, dict)
    
    def test_post_has_required_keys(self):
        bot = Spammer(Facebook())
        result = bot.generate_post("crypto")
        
        assert "bot_type" in result
        assert "platform" in result
        assert "topic" in result
        assert "content" in result
    
    def test_post_preserves_topic(self):
        bot = Conspiracist(LinkedIn())
        result = bot.generate_post("5G")
        assert result["topic"] == "5G"
    
    def test_post_preserves_bot_type(self):
        bot = FakeNews(TikTok())
        result = bot.generate_post("vaccines")
        assert result["bot_type"] == "FakeNews"
    
    def test_post_preserves_platform(self):
        bot = Troll(LinkedIn())
        result = bot.generate_post("blockchain")
        assert result["platform"] == "LinkedIn"


class TestTwitterFormatting:
    """Testy formatowania na Twitterze"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_twitter_has_hashtag(self):
        bot = Troll(Twitter())
        result = bot.generate_post("AI")
        assert "#" in result["content"]
    
    def test_twitter_respects_length_limit(self):
        bot = Spammer(Twitter())
        result = bot.generate_post("cryptocurrency")
        assert len(result["content"]) <= 280
    
    def test_twitter_troll_has_ratio(self):
        bot = Troll(Twitter())
        result = bot.generate_post("climate")
        assert "ratio" in result["content"].lower() or "triggered" in result["content"].lower()
    
    def test_twitter_spammer_has_rocket_emoji(self):
        bot = Spammer(Twitter())
        result = bot.generate_post("NFT")
        assert "🚀" in result["content"]
    
    def test_twitter_conspiracist_has_thread(self):
        bot = Conspiracist(Twitter())
        result = bot.generate_post("government")
        assert "🧵" in result["content"] or "WATEK" in result["content"]
    
    def test_twitter_fakenews_has_breaking(self):
        bot = FakeNews(Twitter())
        result = bot.generate_post("economy")
        assert "⚠️" in result["content"] or "Breaking" in result["content"]


class TestFacebookFormatting:
    """Testy formatowania na Facebooku"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_facebook_troll_has_caps(self):
        bot = Troll(Facebook())
        result = bot.generate_post("politics")
        # Facebook trolls use CAPS for emphasis
        assert any(word.isupper() and len(word) > 2 for word in result["content"].split())
    
    def test_facebook_spammer_mentions_cousin(self):
        bot = Spammer(Facebook())
        result = bot.generate_post("investment")
        assert "kuzynka" in result["content"].lower() or "INFO" in result["content"]
    
    def test_facebook_has_share_call(self):
        bot = Conspiracist(Facebook())
        result = bot.generate_post("media")
        content_lower = result["content"].lower()
        assert "udostepnij" in content_lower or "usuna" in content_lower
    
    def test_facebook_fakenews_has_urgent(self):
        bot = FakeNews(Facebook())
        result = bot.generate_post("health")
        assert "PILNE" in result["content"] or "🔴" in result["content"]


class TestLinkedInFormatting:
    """Testy formatowania na LinkedIn"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_linkedin_has_professional_hashtags(self):
        bot = Troll(LinkedIn())
        result = bot.generate_post("remote work")
        assert "#" in result["content"]
    
    def test_linkedin_troll_has_unpopular_opinion(self):
        bot = Troll(LinkedIn())
        result = bot.generate_post("AI")
        assert "Unpopular opinion" in result["content"] or "Agree?" in result["content"]
    
    def test_linkedin_spammer_has_announcement(self):
        bot = Spammer(LinkedIn())
        result = bot.generate_post("startup")
        assert "excited" in result["content"].lower() or "announce" in result["content"].lower()
    
    def test_linkedin_conspiracist_has_years_experience(self):
        bot = Conspiracist(LinkedIn())
        result = bot.generate_post("industry")
        assert "years" in result["content"].lower() or "industry" in result["content"].lower()
    
    def test_linkedin_has_newlines(self):
        bot = FakeNews(LinkedIn())
        result = bot.generate_post("tech")
        assert "\n" in result["content"]


class TestTikTokFormatting:
    """Testy formatowania na TikToku"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_tiktok_has_genz_slang(self):
        bot = Troll(TikTok())
        result = bot.generate_post("school")
        content_lower = result["content"].lower()
        assert any(slang in content_lower for slang in ["bestie", "pov", "delulu", "fr", "cap", "💀"])
    
    def test_tiktok_spammer_has_bestie(self):
        bot = Spammer(TikTok())
        result = bot.generate_post("money")
        assert "bestie" in result["content"].lower() or "link in bio" in result["content"].lower()
    
    def test_tiktok_conspiracist_has_emoji(self):
        bot = Conspiracist(TikTok())
        result = bot.generate_post("truth")
        assert "🤯" in result["content"] or "👁️" in result["content"]
    
    def test_tiktok_fakenews_has_storytime(self):
        bot = FakeNews(TikTok())
        result = bot.generate_post("news")
        content_lower = result["content"].lower()
        assert "storytime" in content_lower or "part 2" in content_lower


class TestGetBotFunction:
    """Testy funkcji get_bot"""
    
    def test_get_troll_twitter(self):
        bot = get_bot("Troll", "Twitter")
        assert isinstance(bot, Troll)
        assert isinstance(bot.platform, Twitter)
    
    def test_get_spammer_facebook(self):
        bot = get_bot("Spammer", "Facebook")
        assert isinstance(bot, Spammer)
        assert isinstance(bot.platform, Facebook)
    
    def test_get_conspiracist_linkedin(self):
        bot = get_bot("Conspiracist", "LinkedIn")
        assert isinstance(bot, Conspiracist)
        assert isinstance(bot.platform, LinkedIn)
    
    def test_get_fakenews_tiktok(self):
        bot = get_bot("FakeNews", "TikTok")
        assert isinstance(bot, FakeNews)
        assert isinstance(bot.platform, TikTok)
    
    def test_get_all_combinations(self):
        bot_types = ["Troll", "Spammer", "Conspiracist", "FakeNews"]
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        
        for bot_type in bot_types:
            for platform in platforms:
                bot = get_bot(bot_type, platform)
                assert bot.bot_type == bot_type
                assert bot.platform.platform_type == platform
    
    def test_invalid_bot_type_raises(self):
        with pytest.raises(ValueError):
            get_bot("Influencer", "Twitter")
    
    def test_invalid_platform_raises(self):
        with pytest.raises(ValueError):
            get_bot("Troll", "MySpace")


class TestContentGeneration:
    """Testy generowania tresci"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_topic_appears_in_content(self):
        bot = Troll(Twitter())
        result = bot.generate_post("pizza")
        assert "pizza" in result["content"].lower()
    
    def test_different_topics_different_content(self):
        random.seed(42)
        bot1 = Spammer(Facebook())
        result1 = bot1.generate_post("crypto")
        
        random.seed(42)
        bot2 = Spammer(Facebook())
        result2 = bot2.generate_post("NFT")
        
        # Same seed but different topic should produce different content
        assert result1["content"] != result2["content"]
    
    def test_content_not_empty(self):
        bot_types = ["Troll", "Spammer", "Conspiracist", "FakeNews"]
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        
        for bot_type in bot_types:
            for platform in platforms:
                bot = get_bot(bot_type, platform)
                result = bot.generate_post("test")
                assert len(result["content"]) > 0


class TestBotBehaviorConsistency:
    """Testy spojnosci zachowania botow"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_troll_is_provocative(self):
        """Troll powinien byc prowokacyjny na kazdej platformie"""
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        provocative_words = ["wierzysz", "przekret", "pojecia", "ratio", "idioci", "wrong", "delulu"]
        
        for platform in platforms:
            bot = get_bot("Troll", platform)
            result = bot.generate_post("topic")
            content_lower = result["content"].lower()
            assert any(word in content_lower for word in provocative_words), \
                f"Troll on {platform} should be provocative"
    
    def test_spammer_promotes_something(self):
        """Spammer powinien cos promowac na kazdej platformie"""
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        promo_words = ["1000x", "gwarantowane", "zarobil", "moon", "link", "dm", "bio"]
        
        for platform in platforms:
            bot = get_bot("Spammer", platform)
            result = bot.generate_post("coin")
            content_lower = result["content"].lower()
            assert any(word in content_lower for word in promo_words), \
                f"Spammer on {platform} should promote something"
    
    def test_conspiracist_questions_reality(self):
        """Conspiracist powinien kwestionowac rzeczywistosc"""
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        conspiracy_words = ["prawda", "prawde", "ukrywa", "plan", "coincidence", "obudz", "truth", "wake", "chca"]
        
        for platform in platforms:
            bot = get_bot("Conspiracist", platform)
            result = bot.generate_post("government")
            content_lower = result["content"].lower()
            assert any(word in content_lower for word in conspiracy_words), \
                f"Conspiracist on {platform} should question reality"
    
    def test_fakenews_sounds_urgent(self):
        """FakeNews powinien brzmiec pilnie"""
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        urgent_words = ["breaking", "pilne", "szok", "alert", "confirmed", "potwierdz"]
        
        for platform in platforms:
            bot = get_bot("FakeNews", platform)
            result = bot.generate_post("news")
            content_lower = result["content"].lower()
            assert any(word in content_lower for word in urgent_words), \
                f"FakeNews on {platform} should sound urgent"
