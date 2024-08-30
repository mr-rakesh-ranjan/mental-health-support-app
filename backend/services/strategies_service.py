class CopingStrategiesService:
    def get_coping_strategies(self, text: str) -> list:
        """Returns a list of coping strategies based on the user input."""
        # Simple logic for now, could be expanded to use NLP in the future
        return [
            "Take deep breaths and focus on the present moment.",
            "Engage in a hobby or activity that brings you joy.",
            "Reach out to a trusted friend or family member."
        ]

    def get_emergency_assistance(self) -> list:
        """Returns a list of professional mental health resources."""
        return [
            {"name": "National Suicide Prevention Lifeline", "contact": "1-800-273-8255"},
            {"name": "NATIONAL EMERGENCY NUMBER", "contact":  "112"},
            {"name": "POLICE", "contact":  "100 or 112"},
            {"name": "Women Helpline", "contact":  "1091"},
            {"name": "Women Helpline - ( Domestic Abuse )", "contact":  "181"},
            {"name": "Anti Poison ( New Delhi )", "contact": "1066 or 011-1066"},
            {"name": "Senior Citizen Helpline", "contact":  "14567"},
            {"name": "Road Accident Emergency Service", "contact":  "1073"},
            {"name": "Road Accident Emergency Service On National Highway For Private Operators", "contact": "1033"},
            {"name": "Children In Difficult Situation", "contact": "1098"},
            {"name": "National Poisions Information Centre - AIIMS NEW DELHI ( 24*7 )", "contact": "AIIMS NEW DELHI ( 24*7 )1800116117 , 011-26593677, 26589391"},
            {"name": "KIRAN MENTAL HEALTH Helpline", "contact": "18005990019"},
            {"name": "CYBER CRIME HELPLINE", "contact":  "155620"},
            {"name": "BetterHelp", "website": "https://www.betterhelp.com"},
            {"name": "Talkspace", "website": "https://www.talkspace.com"}
        ]
