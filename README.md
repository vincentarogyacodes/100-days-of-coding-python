# Alfred - Every feeling matters

A compassionate, web-based mental health tracking application that helps users monitor their emotional well-being, track anxiety attacks, and gain insights into their mental health patterns.

## 🌟 Features

### **Core Functionality**
- **Mood Tracking**: Log daily moods on a 1-10 scale with optional text descriptions
- **Anxiety Attack Logging**: Track anxiety/panic attacks with intensity, duration, triggers, and symptoms
- **NLP Emotion Analysis**: Automatic emotion detection from text input using TextBlob
- **Personalized Quotes**: Context-aware positive messages from renowned figures based on mood patterns

### **Data Visualization**
- **Interactive Charts**: Beautiful, responsive charts showing mood and anxiety trends over time
- **Customizable Date Ranges**: View data for weeks, months, years, or custom periods
- **Real-time Analytics**: Comprehensive statistics and insights about your mental health journey
- **Trend Analysis**: Identify patterns and progress in your emotional well-being

### **User Experience**
- **Welcoming Interface**: Calming, muted color scheme designed for mental health support
- **Responsive Design**: Works beautifully on desktop, tablet, and mobile devices
- **Touch-Friendly**: Smooth animations and tactile interactions that feel natural
- **Accessibility**: Easy-to-use interface with clear navigation and supportive messaging

### **Mental Health Support**
- **Coping Techniques**: Quick access to breathing exercises, grounding techniques, and support resources
- **Emergency Information**: Crisis hotlines and emergency contact information
- **Supportive Messaging**: Encouraging, non-judgmental language throughout the application
- **Progress Tracking**: Celebrate improvements and understand setbacks in your mental health journey

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd alfred-mental-health-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

### First Time Setup
- The application will automatically create a SQLite database (`alfred.db`) on first run
- No additional configuration required - just start tracking your mental health!

## 🎨 Design Philosophy

### **Colors & Visuals**
- **Muted, calming palette**: Soft grays, sage greens, and warm beiges
- **Easy on the eyes**: Low saturation colors that reduce visual stress
- **Comforting aesthetics**: Warm undertones that promote feelings of safety and calm

### **User Interface**
- **Simple & intuitive**: Clean, uncluttered design that's easy to navigate
- **Touch-friendly**: Generous touch targets and smooth animations
- **Responsive**: Adapts beautifully to all device sizes and orientations
- **Accessible**: High contrast text and clear visual hierarchy

### **Mental Health Focus**
- **Non-judgmental**: Welcoming language that validates all emotional experiences
- **Supportive**: Encouraging messages and helpful resources throughout
- **Safe space**: Emergency information and crisis resources readily available
- **Growth-oriented**: Focus on progress, patterns, and self-understanding

## 📱 How to Use

### **Logging Your Mood**
1. Click "Log Your Mood" from the home page
2. Select your mood level (1-10) using the intuitive emoji scale
3. Rate your anxiety level (1-10)
4. Optionally describe how you're feeling
5. Add any additional notes or context
6. Save your entry

### **Tracking Anxiety Attacks**
1. Click "Log Anxiety Attack" from the home page
2. Rate the intensity of the attack (1-10)
3. Record how long it lasted
4. Note what triggered it (optional)
5. Check off symptoms you experienced
6. Document what helped you cope
7. Save the entry

### **Viewing Your Progress**
1. Click "Analytics" from the home page
2. Choose your desired time range
3. Explore interactive charts and statistics
4. Read personalized insights and recommendations
5. Review your recent entries

## 🔧 Technical Details

### **Backend**
- **Framework**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **NLP**: TextBlob for emotion analysis
- **API**: RESTful endpoints for data retrieval

### **Frontend**
- **HTML/CSS**: Bootstrap 5 for responsive design
- **JavaScript**: Chart.js for data visualization
- **Icons**: Font Awesome for consistent iconography
- **Fonts**: Inter font family for excellent readability

### **Data Storage**
- **Mood Entries**: Score, text, emotion analysis, anxiety level, notes, timestamp
- **Anxiety Attacks**: Intensity, duration, triggers, symptoms, coping strategies, timestamp
- **User Data**: Basic user information and preferences

## 🌟 Key Benefits

### **For Users**
- **Self-awareness**: Better understanding of emotional patterns and triggers
- **Progress tracking**: Visual representation of mental health journey
- **Coping strategies**: Document what works for future reference
- **Professional insights**: Data that can be shared with mental health professionals
- **Emergency support**: Quick access to crisis resources when needed

### **For Mental Health**
- **Reduced stigma**: Normalizing mental health tracking and self-care
- **Early intervention**: Identifying patterns that may need professional attention
- **Empowerment**: Taking an active role in mental health management
- **Education**: Learning about triggers, symptoms, and coping mechanisms

## 🤝 Contributing

This project is designed to support mental health and well-being. If you'd like to contribute:

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

### **Areas for Enhancement**
- Additional chart types and visualizations
- Export functionality for data sharing
- Mobile app development
- Integration with wearable devices
- Advanced NLP and sentiment analysis
- Community features and support groups

## 📞 Support & Resources

### **Crisis Resources**
- **Emergency**: 911
- **Crisis Line**: 988 (US)
- **Text Crisis Line**: Text HOME to 741741
- **International Resources**: Check your local mental health organizations

### **Mental Health Support**
- **Professional Help**: Seek support from licensed mental health professionals
- **Support Groups**: Connect with others experiencing similar challenges
- **Educational Resources**: Learn about mental health conditions and treatments
- **Self-Care**: Practice daily wellness activities and stress management

## 📄 License

This project is open source and available under the MIT License. See the LICENSE file for details.

## 🙏 Acknowledgments

- **Mental Health Community**: For inspiration and feedback
- **Open Source Contributors**: For the amazing tools and libraries used
- **Mental Health Professionals**: For guidance on best practices
- **Users**: For trusting us with their mental health journey

---

**Remember**: Every feeling matters. You are not alone in your mental health journey. This application is a tool to support you, but it's not a substitute for professional mental health care. If you're struggling, please reach out for help.

**Alfred** - Your mental health companion, every step of the way. 💙


