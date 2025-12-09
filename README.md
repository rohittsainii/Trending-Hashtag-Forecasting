# 📈 Hashtag Trend Forecasting using Python & Power BI

A comprehensive data analytics project that identifies and forecasts hashtag trends using **Facebook Prophet**, **Python**, and **Power BI** to deliver actionable insights for brands, marketers, and content creators.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Prophet](https://img.shields.io/badge/Prophet-Forecasting-orange.svg)
![Power BI](https://img.shields.io/badge/Power%20BI-Visualization-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🎯 Project Overview

This project analyzes social media hashtag performance across multiple platforms (Twitter/X, Instagram, TikTok) to:
- Identify trending hashtags and their performance metrics
- Forecast future engagement levels using time-series analysis
- Provide interactive visualizations for data-driven decision-making
- Enable brands to align content strategies with emerging trends

**Key Achievement**: Successfully predicted hashtag engagement trends with accuracy metrics of MAE, RMSE, and R² scores, enabling proactive marketing strategies.

---

## ✨ Features

- **🔍 Trend Identification**: Analyzes top-performing hashtags by likes, shares, views, and comments
- **📊 Predictive Modeling**: Forecasts hashtag performance up to 2.5 years using Facebook Prophet
- **🎨 Interactive Dashboards**: Power BI visualizations for real-time insight exploration
- **📈 Multi-Platform Analysis**: Tracks trends across Instagram, Twitter/X, TikTok, and YouTube
- **🌍 Regional Insights**: Geographic breakdown of hashtag performance
- **📉 Engagement Levels**: Categorizes content into High, Medium, and Low engagement tiers

---

## 🛠️ Tech Stack

- **Python 3.8+**
  - pandas (Data manipulation)
  - Prophet (Time-series forecasting)
  - scikit-learn (Model evaluation)
  - matplotlib (Visualization)
  - numpy (Numerical operations)
- **Power BI** (Interactive dashboards)
- **CSV** (Data storage and exchange)

---

## 📁 Project Structure

```
hashtag-trend-forecasting/
│
├── README.md
├── requirements.txt
│
├── Step 2 preprocess/
│   ├── viral.py                    # Data cleaning and preprocessing
│   └── trend2.py                   # Hashtag grouping by topics
│
├── step 3 TREND IDENTIFICATION/
│   └── identified.py               # EDA and trend analysis
│
├── Step 4 forecasting/
│   ├── forecast.py                 # Main forecasting script
│   ├── forecasting_model.py        # Enhanced Prophet model with smoothing
│   └── forecast_accuracy.py        # Model validation and metrics
│
├── Step-5 actual_vs_predicted/
│   ├── actual_predcited.py         # Tuned model with evaluation
│   └── actual_vs_predicted_fixed.csv  # Comparison results
│
├── Step-6 engagemnt level/
│   ├── engagement.py               # Engagement level aggregation
│   └── engagement_level_summary.csv   # Summary statistics
│
└── data/
    ├── Step-2.csv                  # Cleaned dataset
    ├── grouped_hashtag_trends.csv  # Topic-grouped hashtags
    └── forecast_mentions_2027.csv  # Forecast output
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Power BI Desktop (for visualizations)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hashtag-trend-forecasting.git
   cd hashtag-trend-forecasting
   ```

2. **Install required packages**
   ```bash
   pip install pandas numpy prophet scikit-learn matplotlib
   ```

3. **Prepare your data**
   - Place your raw social media data in the project root
   - Ensure it contains: `Post_Date`, `Hashtag`, `Likes`, `Shares`, `Comments`, `Views`, `Platform`, `Content_Type`, `Region`, `Engagement_Level`

---

## 📖 Usage

### Step 1: Data Preprocessing
Clean and standardize your raw data:
```bash
python "Step 2 preprocess/viral.py"
```
This generates `Step-2.csv` with cleaned data.

### Step 2: Group Related Hashtags
Organize hashtags by topics (AI, fitness, fashion, etc.):
```bash
python "Step 2 preprocess/trend2.py"
```

### Step 3: Exploratory Data Analysis
Identify top-performing hashtags and trends:
```bash
python "step 3 TREND IDENTIFICATION/identified.py"
```

### Step 4: Generate Forecasts
Create predictive models for future trends:
```bash
python "Step 4 forecasting/forecasting_model.py"
```

### Step 5: Validate Model Accuracy
Compare predictions against actual values:
```bash
python "Step-5 actual_vs_predicted/actual_predcited.py"
```

### Step 6: Analyze Engagement Levels
Generate summary statistics by engagement tier:
```bash
python "Step-6 engagemnt level/engagement.py"
```

### Step 7: Import to Power BI
- Open Power BI Desktop
- Import generated CSV files (`actual_vs_predicted_fixed.csv`, `engagement_level_summary.csv`, etc.)
- Create interactive dashboards and reports

---

## 📊 Key Insights

The model provides:
- **Accuracy Metrics**: MAE, RMSE, and R² scores for forecast validation
- **Trend Patterns**: Seasonal and weekly trends in hashtag performance
- **Platform Performance**: Comparative analysis across social media platforms
- **Content Type Analysis**: Which formats (Video, Image, Text) perform best
- **Regional Trends**: Geographic hotspots for specific hashtags

---

## ⚠️ Limitations

- **No Real-Time Data**: Relies on historical static data; can't detect sudden viral spikes
- **No Sentiment Analysis**: Lacks emotional context without raw text data
- **Short-Term Fluctuations**: Prophet excels at long-term trends but struggles with breaking events
- **External Factors**: Cannot account for influencer endorsements or platform algorithm changes

---

## 🔮 Future Enhancements

- [ ] **Real-Time API Integration** with Twitter/X, Instagram, and TikTok
- [ ] **Hybrid Modeling** combining Prophet with LSTM/Transformers
- [ ] **Sentiment Analysis** using NLP techniques
- [ ] **Multimodal Analysis** incorporating image and video content
- [ ] **Automated Alerts** for early virality detection
- [ ] **A/B Testing Framework** for content strategy optimization

---

## 📈 Model Performance

Sample evaluation metrics (last 30 days):
- **MAE**: Mean Absolute Error in engagement predictions
- **RMSE**: Root Mean Square Error for forecast accuracy
- **R² Score**: Model fit quality (0-1 scale)

See `actual_vs_predicted_fixed.csv` for detailed day-by-day comparisons.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👥 Authors

- **Rohit Saini** - *Initial work* - [YourGitHub](https://github.com/rohittsainii)

---

## 🙏 Acknowledgments

- Facebook Prophet team for the forecasting library
- Power BI community for visualization inspiration
- Social media platforms for providing trend data
- Open-source Python community

---

## 📧 Contact

For questions or collaboration opportunities:
- **Email**: rohittsainii75@gmail.com
- **LinkedIn**: [Rohit Saini](https://linkedin.com/in/rohittsainii)
- **Project Link**: [https://github.com/yourusername/hashtag-trend-forecasting](https://github.com/rohittsainii/hashtag-trend-forecasting)

---

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

---

**Built with ❤️ for data-driven marketing**
