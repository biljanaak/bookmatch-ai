import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import streamlit as st


class BookPriceCopilot:

  def __init__(
      self,
      data_path="data/clean_books_advanced.csv",
      model_path="models/book_price_model.pkl",
  ):
    self.df = pd.read_csv(data_path)

    try:
      self.model = joblib.load(model_path)
    except Exception:
      st.warning(
          "⚠️ Incompatibility detected with the saved model. The system is"
          " automatically generating a stable prediction model based on your"
          " data..."
      )
      self._train_fallback_model()

    if hasattr(self.model, "feature_names_in_"):
      self.model_features = list(self.model.feature_names_in_)
    else:
      df_encoded = pd.get_dummies(self.df, columns=["category"], dtype=int)
      self.model_features = list(
          df_encoded.drop(columns=["title", "price"], errors="ignore").columns
      )

  def _train_fallback_model(self):
    df_ml = self.df.copy()
    if "title" in df_ml.columns:
      df_ml["title_length"] = df_ml["title"].astype(str).apply(len)
      df_ml = df_ml.drop(columns=["title"])

    df_ml = pd.get_dummies(df_ml, columns=["category"], dtype=int)

    if "price" in df_ml.columns:
      X = df_ml.drop(columns=["price"])
      y = df_ml["price"]
    else:
      X = df_ml.iloc[:, :-1]
      y = df_ml.iloc[:, -1]

    self.model = RandomForestRegressor(n_estimators=50, random_state=42)
    self.model.fit(X, y)

  def search_books(self, category=None, min_rating=0, top_n=3):
    results = self.df.copy()
    if category:
      results = results[results["category"].str.lower() == category.lower()]
    results = results[results["rating_num"] >= min_rating]
    return results[["title", "category", "rating_num", "price"]].head(top_n)

  def predict_book_price(self, category, rating_num, title):
    input_data = {
        "rating_num": [rating_num],
        "in_stock": [1],
        "title_length": [len(title)],
    }
    input_df = pd.DataFrame(input_data)
    for col in self.model_features:
      if col not in input_df.columns:
        input_df[col] = 0
    target_col = f"category_{category}"
    if target_col in input_df.columns:
      input_df[target_col] = 1

    for col in getattr(self.model, "feature_names_in_", self.model_features):
      if col not in input_df.columns:
        input_df[col] = 0
    input_df = input_df[
        getattr(self.model, "feature_names_in_", self.model_features)
    ]

    predicted_price = self.model.predict(input_df)[0]
    return round(float(predicted_price), 2)


@st.cache_resource
def load_copilot():
  return BookPriceCopilot()


copilot = load_copilot()

st.title("📚 BookMatch AI Copilot")
st.markdown(
    "**Smart Book Valuation & Publishing Intelligence Copilot** — Your personal"
    " system for book market valuation."
)

option = st.sidebar.selectbox(
    "Select Option", ["AI Book Price Prediction", "Book Database Search"]
)

if option == "AI Book Price Prediction":
  st.header("💰 AI Book Market Valuation")

  title_input = st.text_input(
      "Book Title", placeholder="Enter the title of your book here..."
  )

  categories = list(copilot.df["category"].unique())
  category_input = st.selectbox("Select Category (Genre)", categories)
  rating_input = st.slider("Book Rating (1-5 stars)", 1, 5, 5)

  if st.button("Calculate Estimated Price"):
    
    if not title_input.strip():
      st.warning("⚠️ Please enter a book title first!")
    else:
      est_price = copilot.predict_book_price(
          category=category_input, rating_num=rating_input, title=title_input
      )
      st.success(
          f"The model estimated the optimal market price for '{title_input}' to"
          f" be: **£ {est_price}**"
      )

elif option == "Book Database Search":
  st.header("🔍 Smart Catalog Search")

  categories = list(copilot.df["category"].unique())
  search_cat = st.selectbox("Category", categories)
  min_rat = st.slider("Minimum Rating", 1, 5, 4)

  if st.button("Show Results"):
    results = copilot.search_books(category=search_cat, min_rating=min_rat)
    if not results.empty:
      st.dataframe(results)
    else:
      st.warning("No books match the given criteria.")