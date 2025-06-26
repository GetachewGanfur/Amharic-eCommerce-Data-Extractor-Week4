# Amharic-eCommerce-Data-Extractor-Week4

## 🔍 Project Overview

This project develops a **smart FinTech engine** that transforms unstructured Telegram messages into structured business data — helping EthioMart identify the most promising vendors for micro-lending.
Building a Named Entity Recognition (NER) system to extract:

- 📦 **Product Names**
- 💲 **Prices**
- 📍 **Locations**

1. **Automate Telegram Data Extraction**
2. **Fine-Tune NER Models**
3. **Evaluate & Interpret** model predictions
4. **Score Vendors**
5. **Support Micro-Lending**

## Setup

1. Clone the repository and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up your Telegram API credentials in `src/data_collection/telegram_scraper.py`.

## Data Collection

- Run the Telegram scraper:
  ```bash
  python src/data_collection/telegram_scraper.py
  ```

## Preprocessing

- Run the preprocessing script:
  ```bash
  python src/preprocessing/text_preprocessing.py
  ```

## Manual Labeling

- Use `notebooks/conll_labeling.ipynb` or a text editor to label at least 30-50 messages in CoNLL format and save as `data/ner_labels.conll`.

## Model Training

- Use `notebooks/model_training.ipynb` (Colab recommended) to fine-tune and evaluate NER models.

## Model Comparison

- Use `src/model/model_comparison.py` to compare different NER models.

## Interpretability

- Use `src/model/interpretability.py` for model interpretability with SHAP.

## Vendor Analytics

- Use `src/analytics/vendor_scorecard.py` to generate the vendor scorecard and analytics.
