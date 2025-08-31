#!/usr/bin/env python3
"""
Alfred Mood Tracker - Startup Script
Run this file to start the Alfred mood tracking application.
"""

if __name__ == "__main__":
    from app import app
    print("🌟 Starting Alfred Mood Tracker...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    app.run(debug=True, host='127.0.0.1', port=5000)

