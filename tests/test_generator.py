import pytest
from src.generator import AnimeStoryGenerator, Character

@pytest.fixture
def generator():
    return AnimeStoryGenerator()

def test_character_creation(generator):
    character = generator.generate_character("Protagonist")
    
    assert isinstance(character, Character)
    assert character.name is not None
    assert len(character.name.split()) == 2
    assert len(character.traits) == 3
    assert character.special_ability is not None

def test_story_generation(generator):
    story = generator.generate_story()
    
    assert isinstance(story, dict)
    assert 'title' in story
    assert 'setting' in story
    assert 'characters' in story
    assert 'plot_summary' in story

def test_name_generation(generator):
    name = generator.generate_name()
    assert isinstance(name, str)
    assert len(name.split()) == 2

def test_plot_summary(generator):
    story = generator.generate_story()
    assert isinstance(story['plot_summary'], str)
    assert len(story['plot_summary']) > 0