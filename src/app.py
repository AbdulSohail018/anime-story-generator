from flask import Flask, render_template, jsonify, request, abort
from generator import AnimeStoryGenerator
from config import Config
import os

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')
app.config.from_object(Config)

generator = AnimeStoryGenerator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate_story():
    try:
        story = generator.generate_story()
        return jsonify(story)
    except Exception as e:
        app.logger.error(f"Error generating story: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])