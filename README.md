# BookMatch AI

BookMatch AI is an end-to-end Data Science and Machine Learning project focused on automated web scraping, data cleaning, feature engineering, exploratory data analysis (EDA), predictive modeling for book price estimation, and deployment through an interactive Streamlit application.

## Repository Structure

```text
bookmatch-ai/
├── notebooks/
│   └── bookmatch_ai (3).ipynb
├── data/
│   ├── raw_books.csv
│   └── clean_books_advanced.csv
├── models/
│   └── book_price_model.pkl
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

### Project Files

- `notebooks/bookmatch_ai (3).ipynb` — Main Jupyter notebook containing the complete pipeline, including web scraping, data preprocessing, exploratory data analysis, feature engineering, and machine learning model training.
- `data/raw_books.csv` — Raw dataset collected through web scraping.
- `data/clean_books_advanced.csv` — Cleaned and feature-engineered dataset prepared for machine learning.
- `models/book_price_model.pkl` — Trained and serialized machine learning model used for book price predictions.
- `app.py` — Streamlit application providing an interactive interface for exploring book price predictions.
- `requirements.txt` — List of Python dependencies required to run the project.
- `LICENSE` — License governing the use and distribution of the project.

## Getting Started

Follow the instructions below to set up and run BookMatch AI locally.

### Prerequisites

Make sure you have the following installed:

- Python 3.8 or later
- Git
- pip

### Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/biljanaak/bookmatch-ai.git
cd bookmatch-ai
```

**2. Install the required dependencies**

```bash
pip install -r requirements.txt
```

### Running the Application

**3. Launch the Streamlit application**

Run the following command from the project's root directory:

```bash
streamlit run app.py
```

Once the application starts, open the local URL displayed in the terminal to access the interactive web interface.

### Exploring the Jupyter Notebook

**4. Open the main notebook**

To explore the web scraping process, data preprocessing, exploratory data analysis, and model training pipeline, run:

```bash
jupyter notebook
```

Then navigate to `notebooks/bookmatch_ai (3).ipynb` and open the notebook.

Alternatively, if Jupyter is installed and the notebook path is supported by your environment, you can run:

```bash
jupyter notebook "notebooks/bookmatch_ai (3).ipynb"
```

## Project Workflow

The BookMatch AI pipeline consists of the following stages:

1. **Web Scraping** — Automated collection of book data from online sources.
2. **Data Cleaning** — Processing raw data and handling inconsistencies.
3. **Feature Engineering** — Transforming the collected data into relevant features for modeling.
4. **Exploratory Data Analysis (EDA)** — Analyzing data distributions, patterns, and relationships.
5. **Machine Learning** — Training a predictive model to estimate book prices.
6. **Deployment** — Integrating the trained model into an interactive Streamlit application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
