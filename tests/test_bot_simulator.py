import pytest
import random
from bot_simulator import (
    TikTok, Twitter, Facebook, LinkedIn,  # ZMIANA: Importujemy TikTok zamiast Tiktok
    Troll, Spammer, Conspiracist, FakeNews,
    get_bot, Bot
)

class TestBotBasicInfo:
    def test_troll_twitter_info(self):
        bot = get_bot("Troll", "Twitter")
        assert bot.__class__.__name__ == "Troll"
        assert bot.platform.__class__.__name__ == "Twitter"
    
    def test_troll_facebook_info(self):
        bot = get_bot("Troll", "Facebook")
        assert bot.__class__.__name__ == "Troll"
        assert bot.platform.__class__.__name__ == "Facebook"
    
    def test_troll_linkedin_info(self):
        bot = get_bot("Troll", "LinkedIn")
        assert bot.__class__.__name__ == "Troll"
        assert bot.platform.__class__.__name__ == "LinkedIn"
    
    def test_troll_tiktok_info(self):
        bot = get_bot("Troll", "TikTok")
        assert bot.__class__.__name__ == "Troll"
        assert bot.platform.__class__.__name__ == "TikTok"
    
    def test_spammer_twitter_info(self):
        bot = get_bot("Spammer", "Twitter")
        assert bot.__class__.__name__ == "Spammer"
        assert bot.platform.__class__.__name__ == "Twitter"
    
    def test_spammer_facebook_info(self):
        bot = get_bot("Spammer", "Facebook")
        assert bot.__class__.__name__ == "Spammer"
        assert bot.platform.__class__.__name__ == "Facebook"
    
    def test_conspiracist_linkedin_info(self):
        bot = get_bot("Conspiracist", "LinkedIn")
        assert bot.__class__.__name__ == "Conspiracist"
        assert bot.platform.__class__.__name__ == "LinkedIn"
    
    def test_fakenews_tiktok_info(self):
        bot = get_bot("FakeNews", "TikTok")
        assert bot.__class__.__name__ == "FakeNews"
        assert bot.platform.__class__.__name__ == "TikTok"

class TestBotPostStructure:
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_post_returns_dict(self):
        bot = get_bot("Troll", "Twitter")
        result = bot.generate_post("AI")
        assert isinstance(result, dict)
    
    def test_post_has_required_keys(self):
        bot = get_bot("Spammer", "Facebook")
        result = bot.generate_post("crypto")
        
        assert "bot_type" in result
        assert "platform" in result
        assert "topic" in result
        assert "content" in result
    
    def test_post_preserves_topic(self):
        bot = get_bot("Conspiracist", "LinkedIn")
        result = bot.generate_post("5G")
        assert result["topic"] == "5G"
    
    def test_post_preserves_bot_type(self):
        bot = get_bot("FakeNews", "TikTok")
        result = bot.generate_post("vaccines")
        assert result["bot_type"] == "FakeNews"
    
    def test_post_preserves_platform(self):
        bot = get_bot("Troll", "LinkedIn")
        result = bot.generate_post("blockchain")
        assert result["platform"] == "LinkedIn"

class TestTwitterFormatting:
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_twitter_has_hashtag(self):
        bot = get_bot("Troll", "Twitter")
        result = bot.generate_post("AI")
        assert "#" in result["content"]
    
    def test_twitter_respects_length_limit(self):
        bot = get_bot("Spammer", "Twitter")
        result = bot.generate_post("cryptocurrency")
        assert len(result["content"]) <= 280
    
    def test_twitter_troll_has_ratio(self):
        bot = get_bot("Troll", "Twitter")
        result = bot.generate_post("climate")
        assert "triggered" in result["content"].lower()
    
    def test_twitter_formatted_suffix(self):
        bot = get_bot("FakeNews", "Twitter")
        result = bot.generate_post("economy")
        assert "#triggered" in result["content"]

class TestFacebookFormatting:
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_facebook_caps_and_delete_warning(self):
        bot = get_bot("Troll", "Facebook")
        result = bot.generate_post("politics")
        assert "USUNĄ" in result["content"]
        assert "OBUDZIC" in result["content"]

    def test_facebook_structure(self):
        bot = get_bot("Spammer", "Facebook")
        result = bot.generate_post("investment")
        assert "PROSZE SIE OBUDZIC LUDZIE" in result["content"]

class TestLinkedInFormatting:
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_linkedin_has_professional_hashtags(self):
        bot = get_bot("Troll", "LinkedIn")
        result = bot.generate_post("remote work")
        assert "#ThoughtLeadership" in result["content"]
    
    def test_linkedin_structure_intro(self):
        bot = get_bot("Troll", "LinkedIn")
        result = bot.generate_post("AI")
        assert "Unpopular opinion:" in result["content"]
    
    def test_linkedin_structure_outro(self):
        bot = get_bot("Spammer", "LinkedIn")
        result = bot.generate_post("startup")
        assert "Agree?" in result["content"]
        assert "🚀" in result["content"]

class TestTikTokFormatting:
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_tiktok_has_genz_slang(self):
        bot = get_bot("Troll", "TikTok")
        result = bot.generate_post("school")
        content_lower = result["content"].lower()
        assert any(slang in content_lower for slang in ["bestie", "delulu", "fr", "no cap"])
    
    def test_tiktok_structure(self):
        bot = get_bot("Spammer", "TikTok")
        result = bot.generate_post("money")
        assert "its giving delulu" in result["content"]

class TestGetBotFunction:
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
        assert isinstance(bot.platform, TikTok) # ZMIANA: użycie klasy TikTok
    
    def test_get_all_combinations(self):
        bot_types = ["Troll", "Spammer", "Conspiracist", "FakeNews"]
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        
        for bot_type in bot_types:
            for platform in platforms:
                bot = get_bot(bot_type, platform)
                assert bot.__class__.__name__ == bot_type
                assert bot.platform.__class__.__name__ == platform
    
    def test_invalid_bot_type_raises(self):
        with pytest.raises(ValueError):
            get_bot("Influencer", "Twitter")
    
    def test_invalid_platform_raises(self):
        with pytest.raises(ValueError):
            get_bot("Troll", "MySpace")

class TestContentGeneration:
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_topic_appears_in_content(self):
        bot = get_bot("Troll", "Twitter")
        result = bot.generate_post("pizza")
        assert "pizza" in result["content"].lower()
    
    def test_different_topics_different_content(self):
        bot1 = get_bot("Spammer", "Facebook")
        result1 = bot1.generate_post("crypto")
        
        bot2 = get_bot("Spammer", "Facebook")
        result2 = bot2.generate_post("NFT")
        
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
    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)
    
    def test_troll_is_provocative(self):
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        provocative_words = ["serio", "wierzysz"]
        
        for platform in platforms:
            bot = get_bot("Troll", platform)
            result = bot.generate_post("topic")
            content_lower = result["content"].lower()
            assert any(word in content_lower for word in provocative_words)
    
    def test_spammer_promotes_something(self):
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        promo_words = ["coin", "zarobiles", "1000x", "gwarantowane"]
        
        for platform in platforms:
            bot = get_bot("Spammer", platform)
            result = bot.generate_post("coin")
            content_lower = result["content"].lower()
            assert any(word in content_lower for word in promo_words)
    
    def test_conspiracist_questions_reality(self):
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        conspiracy_words = ["komu", "zalezy", "ukrywa", "prawde"]
        
        for platform in platforms:
            bot = get_bot("Conspiracist", platform)
            result = bot.generate_post("government")
            content_lower = result["content"].lower()
            assert any(word in content_lower for word in conspiracy_words)
    
    def test_fakenews_sounds_urgent(self):
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        urgent_words = ["breaking", "pilne", "niebezpieczne"]
        
        for platform in platforms:
            bot = get_bot("FakeNews", platform)
            result = bot.generate_post("news")
            content_lower = result["content"].lower()
            assert any(word in content_lower for word in urgent_words)