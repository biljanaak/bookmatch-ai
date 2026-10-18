# BookMatch AI

BookMatch AI is an end-to-end Data Science and Machine Learning project focused on automated data acquisition, rigorous data cleaning, feature engineering, exploratory data analysis (EDA), predictive modeling for book price estimation, and deployment via an interactive Streamlit application.

## Repository Structure

- `notebooks/bookmatch_ai (3).ipynb` — Main Jupyter notebook containing the complete pipeline: web scraping, data preprocessing, EDA, and machine learning modeling.
- `data/raw_books.csv` — Raw dataset extracted directly from the target website.
- `data/clean_books_advanced.csv` — Processed and feature-engineered dataset used for modeling.
- `models/book_price_model.pkl` — Trained and serialized machine learning model.
- `app.py` — Streamlit web application interface for model interaction.
- `requirements.txt` — Python dependencies required to run the project.

## Getting Started (Local Setup)

### 1. Install Dependencies

Clone the repository and install the required Python packages:

```bash
pip install -r requirements.txt