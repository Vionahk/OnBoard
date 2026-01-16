"""
Configuration file for the AI-Enhanced Onboarding Application
Customize these settings to match your organization
"""

# Application Settings
APP_CONFIG = {
 'app_name': 'Backboard Onboarding',
 'company_name': 'Your Company Name',
 'version': '1.0.0',
 'debug': True,
 'port': 5000
}

# Backboard API Configuration
BACKBOARD_CONFIG = {
 'api_key': 'espr_aIF6pf0ZrBoGNieW3O4o9jUsh8oCSJ1jNFoESmI03Cc', # Replace with your actual Backboard API key
 'base_url': 'https://app.backboard.io/api',
 'enabled': True, # Set to False to use pre-generated insights
 'timeout': 30, # Request timeout in seconds
}

# AI Assistant Configuration
AI_ASSISTANT_CONFIG = {
 'name': 'Onboarding Assistant',
 'system_prompt': """You are an expert employee onboarding assistant for our company. 
Your role is to provide clear, concise, and helpful information about company policies, benefits, culture, and getting started.

Guidelines:
1. Always be professional and friendly
2. Provide accurate, official company information
3. If asked about policies, refer to official documentation
4. Keep responses concise (2-3 sentences for summaries, 4-6 bullet points for key points)
5. Never make up information about company policies
6. Always respect confidentiality and privacy""",
 'enable_memory': True, # Enable conversation memory
}

# UI Configuration
UI_CONFIG = {
 # Color theme (hex codes)
 'primary_color': '#667eea', # Purple
 'secondary_color': '#764ba2', # Dark purple
 'accent_color': '#f0f3ff', # Light purple background
 
 # Company branding (replace with your company)
 'logo_emoji': '', # Change to your company icon
 'company_emoji': '', # Company icon
 
 # Text customization
 'header_title': ' Backboard Onboarding',
 'header_subtitle': 'Welcome! Your interactive learning journey starts here.',
 'footer_text': ' Welcome to our team! Questions? Contact your onboarding mentor or HR department.',
}

# Onboarding Content Structure
# Each section can have multiple cards
# Cards are displayed in columns on the board
CONTENT_STRUCTURE = {
 'sections_per_row': 4, # How many columns to display
 'cards_per_column': None, # None = unlimited (scroll if needed)
 'responsive_breakpoints': {
 'desktop': 1200, # pixels
 'tablet': 768,
 'mobile': 480
 }
}

# AI Learning Features Configuration
AI_CONFIG = {
 'enabled': True, # Enable/disable AI features
 'use_backboard_api': True, # Use real API instead of pre-generated insights
 'show_disclaimer': True, # Show AI responsibility disclaimer
 'features': {
 'summary': True, # Quick summary feature
 'key_points': True, # Key points highlighting
 'related_cards': True # Related topics suggestions
 },
 'disclaimer_text': 'This AI-assisted content is for learning support only. The AI analyzes official company content to provide helpful summaries and key points. Always refer to official company policies for authoritative guidance.',
}

# Customizable Messages
MESSAGES = {
 'ai_insights': '🤖 AI Insights',
 'quick_summary': ' Quick Summary',
 'key_points': '⭐ Key Points',
 'related_topics': ' Related Topics',
 'loading': 'Loading AI insights...',
 'no_results': 'No content available',
 'error': 'Unable to load AI insights. Please try again.',
 'cards_count_singular': 'topic',
 'cards_count_plural': 'topics',
}

# Demo Mode Settings
DEMO_CONFIG = {
 'auto_load_board': True, # Load board automatically on startup
 'show_loading_messages': True, # Show "Loading..." states
 'animation_speed': 0.3, # Seconds (CSS transitions)
 'scroll_behavior': 'smooth', # 'smooth' or 'auto'
 'keyboard_shortcuts_enabled': True, # ESC to close, etc.
}

# Demo user for quick testing (INSECURE: only for local demos)
# Do NOT use these credentials in production. Replace with proper auth.
DEMO_USER = {
 'username': 'KingHack',
 'password': '12345'
}

# Memory options for Backboard usage
MEMORY_OPTIONS = {
 # 'Auto' enables search+write memory operations (recommended for this demo)
 'default_mode': 'Auto',
 # When true, the app will record learner mistakes as memories so the assistant
 # can surface prior mistakes and remediation suggestions later.
 'record_mistakes': True,
 # When true, the app will record preferred techniques per user so the assistant
 # can suggest the user's stronger techniques for future learning tasks.
 'record_preferred_techniques': True,
}

# Customization Tips
"""
To customize this application:

1. BACKBOARD API:
 - Get your API key from https://app.backboard.io
 - Replace 'your_api_key_here' with your actual key
 - Set 'enabled': True to use the API
 - Set 'use_backboard_api': True in AI_CONFIG

2. AI ASSISTANT:
 - Customize system_prompt for specific behavior
 - Change assistant name as needed
 - Enable/disable memory for conversation history

3. COMPANY BRANDING:
 - Change 'logo_emoji' to your company's icon
 - Update 'header_title' with your company name
 - Modify color codes in UI_CONFIG

4. CONTENT STRUCTURE:
 - Change 'sections_per_row' for column layout
 - Adjust responsive breakpoints for your screens

5. FEATURES:
 - Toggle AI features in AI_CONFIG
 - Show/hide disclaimer as needed
 - Enable/disable keyboard shortcuts

Example API configuration:

BACKBOARD_CONFIG = {
 'api_key': 'sk-xxxxxxxxxxxxxxxxxxxxxxxx',
 'base_url': 'https://app.backboard.io/api',
 'enabled': True,
 'timeout': 30,
}
"""

if __name__ == '__main__':
 print(" Onboarding Application Configuration")
 print("\nTo use these settings, import in your Flask app:")
 print(" from config import APP_CONFIG, BACKBOARD_CONFIG, AI_CONFIG")
 print("\nTo customize, edit the values above and reload the app")

