class CopingStrategiesService:
    def get_coping_strategies(self, text: str) -> list:
        """Returns a list of coping strategies based on the user input."""
        # Simple logic for now, could be expanded to use NLP in the future
        return [
            "Take deep breaths and focus on the present moment.",
            "Engage in a hobby or activity that brings you joy.",
            "Reach out to a trusted friend or family member."
        ]

    def get_professional_resources(self) -> list:
        """Returns a list of professional mental health resources."""
        return [
            {"name": "National Suicide Prevention Lifeline", "contact": "1-800-273-8255"},
            {"name": "BetterHelp", "website": "https://www.betterhelp.com"},
            {"name": "Talkspace", "website": "https://www.talkspace.com"}
        ]
