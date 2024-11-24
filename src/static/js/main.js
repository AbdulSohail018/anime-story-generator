class StoryManager {
    constructor() {
        this.currentStory = null;
        this.savedStories = JSON.parse(localStorage.getItem('savedStories') || '[]');
        this.setupEventListeners();
        this.initializeUI();
    }

    setupEventListeners() {
        // Generate button
        document.getElementById('generateBtn').addEventListener('click', () => this.generateStory());
        
        // Save button
        document.getElementById('saveBtn').addEventListener('click', () => this.saveStory());
        
        // Theme toggle
        document.getElementById('themeToggle').addEventListener('click', () => this.toggleTheme());
        
        // Share button
        document.getElementById('shareBtn').addEventListener('click', () => this.shareStory());
        
        // Export button
        document.getElementById('exportBtn').addEventListener('click', () => this.exportStories());
    }

    async generateStory() {
        try {
            this.showLoading(true);
            const response = await fetch('/generate');
            const story = await response.json();
            this.currentStory = story;
            this.updateStoryDisplay(story);
            this.showLoading(false);
        } catch (error) {
            console.error('Error generating story:', error);
            this.showError('Failed to generate story. Please try again.');
            this.showLoading(false);
        }
    }

    updateStoryDisplay(story) {
        // Update title and setting
        document.getElementById('storyTitle').textContent = story.title;
        document.getElementById('storySetting').textContent = story.setting;

        // Update characters
        const characters = ['protagonist', 'deuteragonist', 'rival', 'mentor'];
        characters.forEach(char => {
            const element = document.getElementById(char);
            const character = story.characters[char];
            element.innerHTML = this.formatCharacter(character);
        });

        // Update plot summary
        document.getElementById('plotSummary').textContent = story.plot_summary;

        // Show story container and save button
        document.getElementById('storyContainer').classList.remove('hidden');
        document.getElementById('saveBtn').classList.remove('hidden');
    }

    formatCharacter(char) {
        return `
            <div class="space-y-2">
                <div class="font-semibold">${char.name}</div>
                <div class="text-sm">
                    <span class="font-medium">Traits:</span> 
                    ${char.traits.join(', ')}
                </div>
                ${char.special_ability ? `
                    <div class="text-sm">
                        <span class="font-medium">Special Ability:</span> 
                        ${char.special_ability}
                    </div>
                ` : ''}
            </div>
        `;
    }

    saveStory() {
        if (!this.currentStory) return;

        const timestamp = new Date().toISOString();
        this.savedStories.unshift({
            ...this.currentStory,
            savedAt: timestamp
        });

        localStorage.setItem('savedStories', JSON.stringify(this.savedStories));
        this.updateSavedStoriesList();
        this.showNotification('Story saved successfully!');
    }

    updateSavedStoriesList() {
        const container = document.getElementById('savedStoriesList');
        if (!this.savedStories.length) {
            container.innerHTML = `
                <div class="text-center text-gray-500 py-4">
                    No saved stories yet
                </div>
            `;
            return;
        }

        container.innerHTML = this.savedStories.map((story, index) => `
            <div class="story-card bg-white bg-opacity-90 p-6 rounded-xl shadow-lg mb-4">
                <div class="flex justify-between items-center mb-3">
                    <h4 class="text-xl font-semibold text-purple-800">${story.title}</h4>
                    <div class="space-x-2">
                        <button onclick="storyManager.viewStory(${index})" 
                                class="text-blue-600 hover:text-blue-800">
                            <i class="fas fa-eye"></i>
                        </button>
                        <button onclick="storyManager.deleteStory(${index})" 
                                class="text-red-600 hover:text-red-800">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </div>
                <p class="text-sm text-gray-600">
                    Saved: ${new Date(story.savedAt).toLocaleString()}
                </p>
            </div>
        `).join('');
    }

    deleteStory(index) {
        if (confirm('Are you sure you want to delete this story?')) {
            this.savedStories.splice(index, 1);
            localStorage.setItem('savedStories', JSON.stringify(this.savedStories));
            this.updateSavedStoriesList();
            this.showNotification('Story deleted successfully!');
        }
    }

    viewStory(index) {
        const story = this.savedStories[index];
        this.currentStory = story;
        this.updateStoryDisplay(story);
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    async shareStory() {
        if (!this.currentStory) return;

        if (navigator.share) {
            try {
                await navigator.share({
                    title: this.currentStory.title,
                    text: this.currentStory.plot_summary,
                    url: window.location.href
                });
            } catch (error) {
                console.error('Error sharing:', error);
            }
        } else {
            // Fallback to copying to clipboard
            const text = `${this.currentStory.title}\n\n${this.currentStory.plot_summary}`;
            await navigator.clipboard.writeText(text);
            this.showNotification('Story copied to clipboard!');
        }
    }

    exportStories() {
        const dataStr = JSON.stringify(this.savedStories, null, 2);
        const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
        
        const exportFileDefaultName = 'anime_stories.json';
        
        const linkElement = document.createElement('a');
        linkElement.setAttribute('href', dataUri);
        linkElement.setAttribute('download', exportFileDefaultName);
        linkElement.click();
    }

    toggleTheme() {
        document.body.classList.toggle('dark-theme');
        const icon = document.querySelector('#themeToggle i');
        icon.classList.toggle('fa-moon');
        icon.classList.toggle('fa-sun');
        
        // Save theme preference
        const isDark = document.body.classList.contains('dark-theme');
        localStorage.setItem('darkTheme', isDark);
    }

    showLoading(show) {
        const overlay = document.getElementById('loadingOverlay');
        if (show) {
            overlay.classList.remove('hidden');
        } else {
            overlay.classList.add('hidden');
        }
    }

    showNotification(message) {
        const notification = document.createElement('div');
        notification.className = `
            fixed bottom-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg
            transform transition-transform duration-300 ease-in-out
        `;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // Animate in
        setTimeout(() => {
            notification.style.transform = 'translateY(-20px)';
        }, 100);
        
        // Remove after 3 seconds
        setTimeout(() => {
            notification.style.transform = 'translateY(100%)';
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 3000);
    }

    showError(message) {
        const notification = document.createElement('div');
        notification.className = `
            fixed bottom-4 right-4 bg-red-500 text-white px-6 py-3 rounded-lg shadow-lg
            transform transition-transform duration-300 ease-in-out
        `;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.transform = 'translateY(-20px)';
        }, 100);
        
        setTimeout(() => {
            notification.style.transform = 'translateY(100%)';
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 3000);
    }

    initializeUI() {
        // Load saved stories
        this.updateSavedStoriesList();
        
        // Load theme preference
        const isDark = localStorage.getItem('darkTheme') === 'true';
        if (isDark) {
            document.body.classList.add('dark-theme');
            document.querySelector('#themeToggle i').classList.replace('fa-moon', 'fa-sun');
        }
    }
}

// Initialize the story manager
const storyManager = new StoryManager();