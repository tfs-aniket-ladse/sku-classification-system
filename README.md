# 🤖 SKU Classification System

An intelligent SKU classification system built with Streamlit that uses machine learning to classify product SKUs with enhanced user feedback and model retraining capabilities.

## ✨ Features

### 🔍 **Single SKU Classification**
- Real-time SKU classification with confidence scores
- Exact and fuzzy matching algorithms
- Enhanced visual indicators for retrained predictions
- User feedback system with likes/dislikes and corrections

### 📂 **Bulk Classification**
- Process hundreds of SKUs in seconds
- CSV/Excel file upload support
- Downloadable results with detailed predictions
- Performance metrics and success rates

### 📈 **Analytics Dashboard**
- Comprehensive feedback analytics
- Model performance tracking
- User activity monitoring
- Correction tracking and audit trails

### 🔄 **Model Retraining**
- Admin-only model enhancement functionality
- Incorporates user feedback (likes and corrections)
- Complete audit trail of model improvements
- Teams notifications for all activities

### 🌟 **Enhanced Visual Indicators**
- **🌟 ENHANCED** - Green styling for user-confirmed predictions
- **🔄 RETRAINED** - Yellow styling for user-corrected predictions
- Complete feedback history and model retrain information
- Differentiated indicators for various feedback types

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/tfs-aniket-ladse/sku-classification-system.git
cd sku-classification-system
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up data files:**
   - Place `Training_Set.xlsx` in the project root
   - Place `Business_Rule.xlsx` in the project root
   - Place `reference_file_hierechy.xlsx` in the project root
   - Add your company logo as `logo2.png`

4. **Configure Teams notifications:**
   - Update `teams_config.py` with your Teams webhook URL

## 🏃‍♂️ Usage

1. **Start the application:**
```bash
streamlit run main.py
```

2. **Login:**
   - Use your ThermoFisher email address
   - System supports saved user credentials

3. **Classify SKUs:**
   - **Single SKU**: Enter SKU number/name for instant classification
   - **Bulk Processing**: Upload CSV/Excel files for batch processing

4. **Provide Feedback:**
   - Like correct predictions to reinforce the model
   - Dislike incorrect predictions and provide corrections
   - Add comments for detailed feedback

5. **Admin Functions:**
   - Retrain model with accumulated feedback
   - Monitor analytics and user activity
   - Download feedback data for analysis

## 📁 Project Structure

```
sku-classification-bot/
├── main.py                          # Main Streamlit application
├── teams_config.py                  # Teams webhook configuration
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
├── Training_Set.xlsx               # Training data (not included)
├── Business_Rule.xlsx              # Business rules (not included)
├── reference_file_hierechy.xlsx    # Reference hierarchy (not included)
├── logo2.png                       # Company logo (not included)
├── feedback_data/                  # User feedback storage
│   ├── bulk_user_feedback.json    # JSON feedback data
│   └── bulk_user_feedback.csv     # CSV feedback data
├── user_credentials/               # Saved user credentials
│   └── saved_users.json           # User login data
└── model_retrain_info.json        # Model retraining tracking
```

## 🔧 Configuration

### **Admin Users**
Update the admin user list in `main.py`:
```python
admin_users = ['your.email@thermofisher.com']
```

### **Teams Integration**
Configure Teams webhook in `teams_config.py`:
```python
TEAMS_WEBHOOK_URL = "your-teams-webhook-url"
```

### **Email Validation**
Update allowed domains in `main.py`:
```python
allowed_domains = ['@thermofisher.com', '@yourdomain.com']
```

## 🎯 Key Capabilities

### **Machine Learning Features**
- TF-IDF vectorization for text similarity
- Cosine similarity for fuzzy matching
- Volume-based 2D/3D product line mapping
- Continuous learning through user feedback

### **User Experience**
- Intuitive web interface with Streamlit
- Real-time predictions with confidence scores
- Enhanced visual indicators for improved predictions
- Comprehensive feedback system

### **Enterprise Features**
- User authentication and session management
- Teams integration for notifications
- Admin controls for model management
- Complete audit trails and analytics

## 📊 Analytics & Monitoring

The system provides comprehensive analytics including:
- **Feedback Metrics**: Total feedback, likes/dislikes, accuracy rates
- **User Activity**: Feedback by user, recent activity tracking
- **Model Performance**: Success rates, confidence score distributions
- **Correction Tracking**: User corrections, model improvements

## 🔄 Model Retraining Process

1. **Feedback Collection**: Users provide likes/dislikes with corrections
2. **Data Preparation**: System converts feedback to training format
3. **Model Enhancement**: Admin triggers retraining with accumulated feedback
4. **Visual Indicators**: Enhanced predictions show with special styling
5. **Audit Trail**: Complete tracking of who, when, and what was improved

## 🛡️ Security Features

- Email domain validation for user access
- Admin-only functionality for sensitive operations
- Session-based authentication
- Secure credential storage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is proprietary to Thermo Fisher Scientific.

## 👥 Authors

- **Aniket Ladse** - *Lead Developer* - [tfs-aniket-ladse](https://github.com/tfs-aniket-ladse)

## 🙏 Acknowledgments

- Thermo Fisher Scientific for project support
- Streamlit team for the excellent framework
- scikit-learn for machine learning capabilities

---

**Note**: This system requires proprietary data files (`Training_Set.xlsx`, `Business_Rule.xlsx`, `reference_file_hierechy.xlsx`) that are not included in this repository for security reasons.