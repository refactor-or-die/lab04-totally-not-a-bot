"""
Testy jednostkowe dla symulatora botow internetowych (wersja Bridge).
"""

import pytest
import random

from bot_simulator import (
    TrollBot, SpammerBot, ConspiracistBot, FakeNewsBot,
    TwitterImplementation, FacebookImplementation, LinkedInImplementation, TikTokImplementation,
    get_bot
)

class TestBotBasicInfo:
    """Testy podstawowych informacji o botach"""

    def test_troll_twitter_info(self):
        bot = get_bot("Troll", "Twitter")
        assert bot.bot_type == "Troll"
        assert bot.platfrom.get_platfrom_name() == "Twitter"
    
    def test_troll_facebook_info(self):
        bot = get_bot("Troll", "Facebook")
        assert bot.bot_type == "Troll"
        assert bot.platfrom.get_platfrom_name() == "Facebook"
    
    def test_troll_linkedin_info(self):
        bot = get_bot("Troll", "LinkedIn")
        assert bot.bot_type == "Troll"
        assert bot.platfrom.get_platfrom_name() == "LinkedIn"
    
    def test_troll_tiktok_info(self):
        bot = get_bot("Troll", "TikTok")
        assert bot.bot_type == "Troll"
        assert bot.platfrom.get_platfrom_name() == "TikTok"


class TestBotPostStructure:
    """Testy struktury postow"""

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
        assert set(result.keys()) == {"bot_type", "platform", "topic", "content"}

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
    """Testy formatowania na Twitterze"""

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
        assert "ratio" in result["content"].lower() or "triggered" in result["content"].lower()

    def test_twitter_spammer_has_rocket_emoji(self):
        bot = get_bot("Spammer", "Twitter")
        result = bot.generate_post("NFT")
        assert "🚀" in result["content"]

    def test_twitter_conspiracist_has_thread(self):
        bot = get_bot("Conspiracist", "Twitter")
        result = bot.generate_post("government")
        assert "🧵" in result["content"] or "WATEK" in result["content"]

    def test_twitter_fakenews_has_breaking(self):
        bot = get_bot("FakeNews", "Twitter")
        result = bot.generate_post("economy")
        assert "⚠️" in result["content"] or "breaking" in result["content"].lower()


class TestFacebookFormatting:
    """Testy formatowania na Facebooku"""

    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)

    def test_facebook_troll_has_caps(self):
        bot = get_bot("Troll", "Facebook")
        result = bot.generate_post("politics")
        assert any(word.isupper() and len(word) > 2 for word in result["content"].split())

    def test_facebook_spammer_mentions_cousin(self):
        bot = get_bot("Spammer", "Facebook")
        result = bot.generate_post("investment")
        assert "kuzynka" in result["content"].lower() or "info" in result["content"].lower()

    def test_facebook_has_share_call(self):
        bot = get_bot("Conspiracist", "Facebook")
        result = bot.generate_post("media")
        content_lower = result["content"].lower()
        assert "udostepnij" in content_lower or "usun" in content_lower

    def test_facebook_fakenews_has_urgent(self):
        bot = get_bot("FakeNews", "Facebook")
        result = bot.generate_post("health")
        assert "pilne" in result["content"].lower() or "🔴" in result["content"]


class TestLinkedInFormatting:
    """Testy formatowania na LinkedIn"""

    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)

    def test_linkedin_has_professional_hashtags(self):
        bot = get_bot("Troll", "LinkedIn")
        result = bot.generate_post("remote work")
        assert "#" in result["content"]

    def test_linkedin_troll_has_unpopular_opinion(self):
        bot = get_bot("Troll", "LinkedIn")
        result = bot.generate_post("AI")
        assert "unpopular opinion" in result["content"].lower() or "agree?" in result["content"]

    def test_linkedin_spammer_has_announcement(self):
        bot = get_bot("Spammer", "LinkedIn")
        result = bot.generate_post("startup")
        assert "excited" in result["content"].lower() or "announce" in result["content"].lower()

    def test_linkedin_conspiracist_has_years_experience(self):
        bot = get_bot("Conspiracist", "LinkedIn")
        result = bot.generate_post("industry")
        assert "years" in result["content"].lower() or "industry" in result["content"].lower()

    def test_linkedin_has_newlines(self):
        bot = get_bot("FakeNews", "LinkedIn")
        result = bot.generate_post("tech")
        assert "\n" in result["content"]


class TestTikTokFormatting:
    """Testy formatowania na TikToku"""

    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)

    def test_tiktok_has_genz_slang(self):
        bot = get_bot("Troll", "TikTok")
        result = bot.generate_post("school")
        content_lower = result["content"].lower()
        assert any(slang in content_lower for slang in ["bestie", "pov", "delulu", "fr", "cap", "💀"])

    def test_tiktok_spammer_has_bestie(self):
        bot = get_bot("Spammer", "TikTok")
        result = bot.generate_post("money")
        assert "bestie" in result["content"].lower() or "link in bio" in result["content"].lower()

    def test_tiktok_conspiracist_has_emoji(self):
        bot = get_bot("Conspiracist", "TikTok")
        result = bot.generate_post("truth")
        assert "🤯" in result["content"] or "👁️" in result["content"]

    def test_tiktok_fakenews_has_storytime(self):
        bot = get_bot("FakeNews", "TikTok")
        result = bot.generate_post("news")
        content_lower = result["content"].lower()
        assert "storytime" in content_lower or "part 2" in content_lower


class TestGetBotFunction:
    """Testy funkcji get_bot"""

    def test_get_troll_twitter(self):
        bot = get_bot("Troll", "Twitter")
        assert isinstance(bot, TrollBot)
        assert bot.platfrom.get_platfrom_name() == "Twitter"

    def test_get_spammer_facebook(self):
        bot = get_bot("Spammer", "Facebook")
        assert isinstance(bot, SpammerBot)
        assert bot.platfrom.get_platfrom_name() == "Facebook"

    def test_get_conspiracist_linkedin(self):
        bot = get_bot("Conspiracist", "LinkedIn")
        assert isinstance(bot, ConspiracistBot)
        assert bot.platfrom.get_platfrom_name() == "LinkedIn"

    def test_get_fakenews_tiktok(self):
        bot = get_bot("FakeNews", "TikTok")
        assert isinstance(bot, FakeNewsBot)
        assert bot.platfrom.get_platfrom_name() == "TikTok"

    def test_get_all_combinations(self):
        bot_types = ["Troll", "Spammer", "Conspiracist", "FakeNews"]
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]

        for bot_type in bot_types:
            for platform in platforms:
                bot = get_bot(bot_type, platform)
                assert bot.bot_type == bot_type
                assert bot.platfrom.get_platfrom_name() == platform

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
        bot = get_bot("Troll", "Twitter")
        result = bot.generate_post("pizza")
        assert "pizza" in result["content"].lower()

    def test_different_topics_different_content(self):
        random.seed(42)
        bot1 = get_bot("Spammer", "Facebook")
        result1 = bot1.generate_post("crypto")

        random.seed(42)
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
    """Testy spojnosci zachowania botow"""

    @pytest.fixture(autouse=True)
    def setup(self):
        random.seed(42)

    def test_troll_is_provocative(self):
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        provocative_words = ["wierzysz", "przekret", "pojecia", "ratio", "delulu"]

        for platform in platforms:
            bot = get_bot("Troll", platform)
            content = bot.generate_post("topic")["content"].lower()
            assert any(w in content for w in provocative_words)

    def test_spammer_promotes_something(self):
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        promo_words = ["1000x", "gwarantowane", "zarobil", "moon", "link", "dm", "bio"]

        for platform in platforms:
            bot = get_bot("Spammer", platform)
            content = bot.generate_post("coin")["content"].lower()
            assert any(w in content for w in promo_words)

    def test_fakenews_sounds_urgent(self):
        platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
        urgent_words = ["breaking", "pilne", "szok", "alert", "confirmed", "potwierdz"]

        for platform in platforms:
            bot = get_bot("FakeNews", platform)
            content = bot.generate_post("news")["content"].lower()
            assert any(w in content for w in urgent_words)