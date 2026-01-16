"""
Quick Start Guide - Run this to get started immediately
"""

import subprocess
import sys
import os
from pathlib import Path

def check_python_version():
    """Verify Python 3.7+ is installed"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def check_flask():
    """Check if Flask is installed"""
    try:
        import flask
        print(f"✅ Flask {flask.__version__} is installed")
        return True
    except ImportError:
        print("❌ Flask is not installed")
        return False

def install_flask():
    """Install Flask if needed"""
    print("\n📦 Installing Flask...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "-q"])
        print("✅ Flask installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install Flask")
        return False

def start_server():
    """Start the Flask development server"""
    print("\n🚀 Starting AI-Enhanced Onboarding Application...")
    print("📍 Server running at: http://localhost:5000")
    print("📱 Open this URL in your web browser")
    print("\n💡 Tip: Click 'AI Insights' on any card to see learning enhancements")
    print("🔗 Click 'Related' to see connected topics")
    print("\n⏹️  Press Ctrl+C to stop the server\n")
    
    try:
        import app
        app.app.run(debug=True, port=5000, use_reloader=False)
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return False
    return True

def main():
    """Main startup sequence"""
    print("\n" + "="*60)
    print("🎓 AI-Enhanced Employee Onboarding Application")
    print("="*60 + "\n")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check and install Flask
    if not check_flask():
        if not install_flask():
            print("\n❌ Cannot proceed without Flask")
            print("   Please install manually: pip install flask")
            sys.exit(1)
    
    # Start the server
    print("\n" + "-"*60)
    if not start_server():
        print("\n❌ Failed to start the application")
        sys.exit(1)

if __name__ == "__main__":
    main()
