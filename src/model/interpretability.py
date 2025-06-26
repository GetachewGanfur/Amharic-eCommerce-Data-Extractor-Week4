import shap
import torch
from transformers import pipeline

# Load model and tokenizer
ner_pipeline = pipeline("ner", model="ner_finetuned_model", tokenizer="xlm-roberta-base", aggregation_strategy="simple")

# Example: SHAP for a single  prediction
explainer = shap.Explainer(ner_pipeline)
shap_values = explainer(["ሶፋ ዋጋ 1000 ብር ቦሌ ላይ አለ"])

shap.plots.text(shap_values) 