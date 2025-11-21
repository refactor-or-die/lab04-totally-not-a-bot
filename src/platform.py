from abc import ABC, abstractmethod

# Implementacja (JAK formatuje)
class Platform(ABC):
    @abstractmethod
    def format_message(self, topic: str, message: str) -> str:
        pass


class Twitter(Platform):
    platform_type = "Twitter"
    def format_message(self, topic: str, message: str) -> str:
        formatted = f"{message} ratio + L + niemasz racji"
        if len(formatted) > 280:
            formatted = formatted[:277] + "..."
        formatted += " #triggered"
        return formatted

class Facebook(Platform):
    platform_type = "Facebook"
    def format_message(self, topic: str, message: str) -> str:
        formatted = f"{message}... PROSZE SIE OBUDZIC LUDZIE!!! "
        formatted += "Udostepnij zanim USUNĄ!!! "
        formatted += "😠😠😠"
        return formatted

class LinkedIn(Platform):
    platform_type = "LinkedIn"
    def format_message(self, topic: str, message: str) -> str:
        formatted = f"Unpopular opinion: {message}\n\n"
        formatted += "I know this might be controversial, but someone had to say it.\n\n"
        formatted += "Agree? ♻️ Repost to spread awareness\n"
        formatted += "#ThoughtLeadership #Disruption #Controversial"
        return formatted

class TikTok(Platform):
    platform_type = "TikTok"
    def format_message(self, topic: str, message: str) -> str:
        formatted = f"pov: ktos mowi ze {topic} ma sens 💀💀💀\n"
        formatted += f"bestie... {message}\n"
        formatted += "its giving delulu 😭 no cap fr fr"
        return formatted