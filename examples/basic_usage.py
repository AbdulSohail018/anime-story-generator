from src.generator import generate_and_print_story, AnimeStoryGenerator

def basic_example():
    print("=== Basic Usage Example ===")
    story = generate_and_print_story()
    print("\n" + "="*50 + "\n")

def custom_example():
    print("=== Custom Usage Example ===")
    generator = AnimeStoryGenerator()
    
    # Generate multiple stories
    for i in range(3):
        story = generator.generate_story()
        print(f"\nStory {i+1}: {story['title']}")
        print(f"Setting: {story['setting']}")
        print(f"Protagonist: {story['characters']['protagonist']['name']}")
        print("-" * 30)

if __name__ == "__main__":
    basic_example()
    custom_example()