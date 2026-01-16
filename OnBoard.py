"""
AI-Enhanced Employee Onboarding Application
Entry point - Same as app.py with additional startup logic

To run this application:
 python OnBoard.py

Or use the quick-start helper:
 python start.py
"""

from app import app

if __name__ == '__main__':
 print("\n" + "="*70)
 print("onBoard — Smart Onboarding")
 print("="*70)
 print("\n Application Features:")
 print(" • Backboard-style layout with 4 columns")
 print(" • 12 onboarding topic cards across key areas")
 print(" • AI-assisted learning: Summaries, Key Points, Related Topics")
 print(" • Clean, modern design with smooth interactions")
 print(" • Responsible AI: All AI features clearly marked as assistive")
 print("\n Four Content Sections:")
 print(" 1. Welcome & Basics (Company Overview, Mission, Culture)")
 print(" 2. Policies & Compliance (Security, Code of Conduct, Privacy)")
 print(" 3. Benefits & Time-Off (Health, Time-Off, Development)")
 print(" 4. Getting Started (First Week, IT Setup, Team Intro)")
 print("\n🤖 AI-Assisted Learning:")
 print(" • Click 'AI Insights' on any card to reveal:")
 print(" Quick Summary - Condensed topic overview")
 print(" ⭐ Key Points - Important information highlights")
 print(" Related Topics - Suggestions for deeper learning")
 print("\n️ AI Transparency:")
 print(" • All AI features clearly marked as assistive tools")
 print(" • AI never generates, modifies, or replaces official content")
 print(" • Official policies remain the single source of truth")
 print(" • Disclaimer displayed on every insights panel")
 print("\n Server Details:")
 print(" • URL: http://localhost:5000")
 print(" • Debug Mode: Enabled (for development)")
 print(" • Database: None (lightweight & fast)")
 print(" • Authentication: None (demo-friendly)")
 print("\n Tips:")
 print(" • Use arrow keys or scroll to navigate cards")
 print(" • Click related topics to jump to connected cards")
 print(" • Press ESC to close all insights panels")
 print(" • Responsive design works on mobile/tablet")
 print("\n" + "-"*70 + "\n")
 
 app.run(debug=True, port=5000)
