import random
from typing import List, Dict, Optional

class Character:
    def __init__(self, name: str, archetype: str, traits: List[str], special_ability: Optional[str] = None):
        self.name = name
        self.archetype = archetype
        self.traits = traits
        self.special_ability = special_ability

class AnimeStoryGenerator:
    def __init__(self):
        self.first_names = [
            "Yuki", "Hiro", "Sakura", "Kai", "Rin", "Akira", "Mei", "Sora",
            "Kento", "Aoi", "Ryu", "Hana", "Takashi", "Mika", "Ken", "Luna"
        ]
        
        self.last_names = [
            "Tanaka", "Yamamoto", "Nakamura", "Sato", "Suzuki", "Takahashi",
            "Watanabe", "Ito", "Saito", "Kobayashi", "Kato", "Yoshida"
        ]

        self.character_archetypes = {
            "Protagonist": [
                "determined", "compassionate", "brave", "optimistic",
                "stubborn", "natural leader", "underdog"
            ],
            "Deuteragonist": [
                "loyal", "skilled", "mysterious", "protective",
                "conflicted", "strategic", "resourceful"
            ],
            "Rival": [
                "competitive", "proud", "talented", "complex",
                "ambitious", "driven", "misunderstood"
            ],
            "Mentor": [
                "wise", "experienced", "strict", "caring",
                "mysterious", "powerful", "eccentric"
            ]
        }

        self.special_abilities = [
            "control over elements", "supernatural strength",
            "healing powers", "time manipulation", "energy projection",
            "psychic abilities", "transformation", "ancient magic",
            "technological genius", "spiritual power"
        ]

        self.settings = [
            "prestigious academy", "futuristic metropolis",
            "hidden magical realm", "post-apocalyptic world",
            "alternate dimension", "ancient kingdom",
            "space colony", "virtual reality world"
        ]

        self.plot_hooks = [
            "discovers hidden powers",
            "enters a prestigious tournament",
            "protects a mysterious artifact",
            "uncovers a dark conspiracy",
            "seeks revenge against ancient evil",
            "tries to save their loved ones",
            "aims to become the strongest",
            "works to restore balance to the world"
        ]

        self.plot_twists = [
            "betrayal by a close ally",
            "hidden identity revealed",
            "prophecy comes true in unexpected way",
            "mentor figure sacrifices themselves",
            "rival becomes an ally",
            "true villain emerges",
            "powers come with a terrible price",
            "time travel changes everything"
        ]

    def generate_name(self) -> str:
        return f"{random.choice(self.last_names)} {random.choice(self.first_names)}"

    def generate_character(self, role: str) -> Character:
        name = self.generate_name()
        traits = random.sample(self.character_archetypes[role], 3)
        special_ability = random.choice(self.special_abilities) if role in ["Protagonist", "Rival"] else None
        return Character(name, role, traits, special_ability)

    def generate_story(self) -> Dict:
        protagonist = self.generate_character("Protagonist")
        deuteragonist = self.generate_character("Deuteragonist")
        rival = self.generate_character("Rival")
        mentor = self.generate_character("Mentor")
        
        setting = random.choice(self.settings)
        main_plot = random.choice(self.plot_hooks)
        plot_twist = random.choice(self.plot_twists)
        
        story = {
            "title": f"{protagonist.name}'s {random.choice(['Journey', 'Quest', 'Legend', 'Destiny', 'Chronicle'])}",
            "setting": setting,
            "characters": {
                "protagonist": {
                    "name": protagonist.name,
                    "traits": protagonist.traits,
                    "special_ability": protagonist.special_ability
                },
                "deuteragonist": {
                    "name": deuteragonist.name,
                    "traits": deuteragonist.traits,
                    "special_ability": deuteragonist.special_ability
                },
                "rival": {
                    "name": rival.name,
                    "traits": rival.traits,
                    "special_ability": rival.special_ability
                },
                "mentor": {
                    "name": mentor.name,
                    "traits": mentor.traits,
                    "special_ability": mentor.special_ability
                }
            },
            "plot_summary": self._generate_plot_summary(
                protagonist, deuteragonist, rival, mentor,
                setting, main_plot, plot_twist
            )
        }
        
        return story

    def _generate_plot_summary(
        self, protagonist: Character, deuteragonist: Character,
        rival: Character, mentor: Character, setting: str,
        main_plot: str, plot_twist: str
    ) -> str:
        return f"""In a {setting}, {protagonist.name}, a {', '.join(protagonist.traits)} young person, 
{main_plot}. Accompanied by their loyal friend {deuteragonist.name} and guided by the {', '.join(mentor.traits)} 
mentor {mentor.name}, they face numerous challenges. Their greatest obstacle is {rival.name}, 
a {', '.join(rival.traits)} rival with {rival.special_ability}. As they master their 
{protagonist.special_ability}, the story takes an unexpected turn when {plot_twist}. Now, 
{protagonist.name} must overcome their limitations and face their destiny to achieve their goals."""

def generate_and_print_story():
    generator = AnimeStoryGenerator()
    story = generator.generate_story()
    
    print(f"=== {story['title']} ===\n")
    print("Setting:")
    print(story['setting'], "\n")
    
    print("Characters:")
    for role, char in story['characters'].items():
        print(f"\n{role.title()}:")
        print(f"Name: {char['name']}")
        print(f"Traits: {', '.join(char['traits'])}")
        if char['special_ability']:
            print(f"Special Ability: {char['special_ability']}")
    
    print("\nPlot Summary:")
    print(story['plot_summary'])
    
    return story

if __name__ == "__main__":
    generate_and_print_story()