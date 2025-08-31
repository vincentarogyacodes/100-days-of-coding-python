from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import json
import random
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alfred.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class MoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    mood_score = db.Column(db.Integer, nullable=False)  # 1-10 scale
    mood_text = db.Column(db.Text)
    emotion_analysis = db.Column(db.String(100))
    anxiety_level = db.Column(db.Integer)  # 1-10 scale
    notes = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class AnxietyAttack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    intensity = db.Column(db.Integer, nullable=False)  # 1-10 scale
    duration = db.Column(db.Integer)  # minutes
    triggers = db.Column(db.Text)
    symptoms = db.Column(db.Text)
    coping_strategies = db.Column(db.Text)
    experience = db.Column(db.Text)  # New field for detailed description
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)

# Positive quotes database
POSITIVE_QUOTES = {
    'resilience': [
        "The human spirit is stronger than anything that can happen to it. - C.C. Scott",
        "When we are no longer able to change a situation, we are challenged to change ourselves. - Viktor Frankl",
        "The only way to get through life is to laugh your way through it. - Marjorie Pay Hinckley"
    ],
    'hope': [
        "Hope is the thing with feathers that perches in the soul. - Emily Dickinson",
        "Everything will be okay in the end. If it's not okay, it's not the end. - John Lennon",
        "The sun will rise and we will try again. - Twenty One Pilots"
    ],
    'growth': [
        "Growth is painful. Change is painful. But nothing is as painful as staying stuck somewhere you don't belong. - Mandy Hale",
        "Every day is a new beginning. Take a deep breath and start again. - Anonymous",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis"
    ],
    'peace': [
        "Peace comes from within. Do not seek it without. - Buddha",
        "In the midst of movement and chaos, keep stillness inside of you. - Deepak Chopra",
        "Calm mind brings inner strength and self-confidence. - Dalai Lama"
    ],
    'general': [
        "You are enough. You are so enough. It is unbelievable how enough you are. - Sierra Boggess",
        "Be kind to yourself. You're doing the best you can. - Anonymous",
        "Your feelings are valid. Your experiences matter. - Anonymous"
    ]
}

def get_personalized_quote(user_id):
    """Get a personalized quote based on user's recent mood patterns"""
    recent_entries = MoodEntry.query.filter_by(user_id=user_id).order_by(MoodEntry.timestamp.desc()).limit(7).all()
    
    if not recent_entries:
        return random.choice(POSITIVE_QUOTES['general'])
    
    # Analyze recent mood trends
    avg_mood = sum(entry.mood_score for entry in recent_entries) / len(recent_entries)
    
    if avg_mood <= 3:
        category = 'hope'
    elif avg_mood <= 5:
        category = 'resilience'
    elif avg_mood <= 7:
        category = 'growth'
    elif avg_mood <= 9:
        category = 'peace'
    else:
        category = 'general'
    
    return random.choice(POSITIVE_QUOTES[category])

def analyze_emotion(text):
    """Simple emotion analysis without TextBlob dependency"""
    if not text:
        return "neutral"
    
    # Simple keyword-based analysis
    positive_words = ['happy', 'joy', 'excited', 'great', 'wonderful', 'amazing', 'love', 'good', 'positive', 'blessed', 'grateful', 'peaceful', 'calm', 'relaxed', 'content', 'satisfied', 'fulfilled', 'energized', 'motivated', 'inspired']
    negative_words = ['sad', 'angry', 'frustrated', 'anxious', 'worried', 'scared', 'terrified', 'depressed', 'lonely', 'hopeless', 'helpless', 'overwhelmed', 'stressed', 'tired', 'exhausted', 'hurt', 'pain', 'suffering', 'miserable', 'terrible']
    
    text_lower = text.lower()
    
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)
    
    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"

@app.route('/')
def index():
    user_id = request.args.get('user_id', 'default_user')
    quote = get_personalized_quote(user_id)
    
    # Get recent mood data for quick overview
    recent_moods = MoodEntry.query.filter_by(user_id=user_id).order_by(MoodEntry.timestamp.desc()).limit(5).all()
    
    return render_template('index.html', quote=quote, recent_moods=recent_moods, user_id=user_id)

@app.route('/log_mood', methods=['GET', 'POST'])
def log_mood():
    if request.method == 'POST':
        data = request.get_json()
        
        # Validate that we have the essential text input
        if not data.get('mood_text', '').strip():
            return jsonify({'success': False, 'message': 'Please share how you\'re feeling. Your words are what matter most.'}), 400
        
        # Analyze emotion from text
        emotion = analyze_emotion(data.get('mood_text', ''))
        
        new_entry = MoodEntry(
            user_id=data['user_id'],
            mood_score=data.get('mood_score', 5),  # Default to 5 if not provided
            mood_text=data.get('mood_text', ''),
            emotion_analysis=emotion,
            anxiety_level=data.get('anxiety_level', 5),  # Default to 5 if not provided
            notes=data.get('notes', '')
        )
        
        db.session.add(new_entry)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Your thoughts have been saved successfully!'})
    
    return render_template('log_mood.html')

@app.route('/log_anxiety', methods=['GET', 'POST'])
def log_anxiety():
    if request.method == 'POST':
        data = request.get_json()
        
        # Validate that we have the essential text input
        if not data.get('experience', '').strip():
            return jsonify({'success': False, 'message': 'Please describe your experience. Your words are what matter most for understanding and tracking your journey.'}), 400
        
        new_attack = AnxietyAttack(
            user_id=data['user_id'],
            intensity=data.get('intensity', 5),  # Default to 5 if not provided
            duration=data.get('duration', 0),
            triggers=data.get('triggers', ''),
            symptoms=data.get('symptoms', ''),
            coping_strategies=data.get('coping_strategies', ''),
            experience=data.get('experience', '')  # New field for detailed description
        )
        
        db.session.add(new_attack)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Anxiety experience logged successfully!'})
    
    return render_template('log_anxiety.html')

@app.route('/analytics')
def analytics():
    user_id = request.args.get('user_id', 'default_user')
    
    # Get date range from request
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    if start_date and end_date:
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        mood_data = MoodEntry.query.filter(
            MoodEntry.user_id == user_id,
            MoodEntry.timestamp >= start,
            MoodEntry.timestamp <= end
        ).order_by(MoodEntry.timestamp).all()
        
        anxiety_data = AnxietyAttack.query.filter(
            AnxietyAttack.user_id == user_id,
            AnxietyAttack.timestamp >= start,
            AnxietyAttack.timestamp <= end
        ).order_by(AnxietyAttack.timestamp).all()
    else:
        # Default to last 30 days
        thirty_days_ago = datetime.utcnow() - timedelta(days=30)
        mood_data = MoodEntry.query.filter(
            MoodEntry.user_id == user_id,
            MoodEntry.timestamp >= thirty_days_ago
        ).order_by(MoodEntry.timestamp).all()
        
        anxiety_data = AnxietyAttack.query.filter(
            AnxietyAttack.user_id == user_id,
            AnxietyAttack.timestamp >= thirty_days_ago
        ).order_by(AnxietyAttack.timestamp).all()
    
    return render_template('analytics.html', 
                         mood_data=mood_data, 
                         anxiety_data=anxiety_data,
                         user_id=user_id)

@app.route('/api/mood_data')
def get_mood_data():
    user_id = request.args.get('user_id', 'default_user')
    days = int(request.args.get('days', 30))
    
    start_date = datetime.utcnow() - timedelta(days=days)
    entries = MoodEntry.query.filter(
        MoodEntry.user_id == user_id,
        MoodEntry.timestamp >= start_date
    ).order_by(MoodEntry.timestamp).all()
    
    data = []
    for entry in entries:
        data.append({
            'date': entry.timestamp.strftime('%Y-%m-%d'),
            'mood_score': entry.mood_score,
            'anxiety_level': entry.anxiety_level,
            'emotion': entry.emotion_analysis
        })
    
    return jsonify(data)

@app.route('/api/anxiety_data')
def get_anxiety_data():
    user_id = request.args.get('user_id', 'default_user')
    days = int(request.args.get('days', 30))
    
    start_date = datetime.utcnow() - timedelta(days=days)
    attacks = AnxietyAttack.query.filter(
        AnxietyAttack.user_id == user_id,
        AnxietyAttack.timestamp >= start_date
    ).order_by(AnxietyAttack.timestamp).all()
    
    data = []
    for attack in attacks:
        data.append({
            'date': attack.timestamp.strftime('%Y-%m-%d'),
            'intensity': attack.intensity,
            'duration': attack.duration
        })
    
    return jsonify(data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
