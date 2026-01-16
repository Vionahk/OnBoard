#!/bin/bash
# Quick Start Script for Mac/Linux
# Run this to start the application: bash run.sh

echo "🚀 AI-Enhanced Onboarding Application"
echo "======================================"
echo ""

# Check Python version
echo "🐍 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.7+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo "✅ Python $PYTHON_VERSION found"

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📚 Installing dependencies..."
pip install -r requirements.txt -q

# Start the app
echo ""
echo "🌟 Starting Onboarding Application..."
echo "📍 Open your browser to: http://localhost:5000"
echo "⏹️  Press Ctrl+C to stop the server"
echo ""

python3 OnBoard.py
