# Pseudocode for comparing multiple models
from transformers import AutoModelForTokenClassification, Trainer

# You need to define label2id, id2label, args, data_collator, tokenized_datasets before running this script
# This is a template for model comparison

models = [
    "xlm-roberta-base",
    "distilbert-base-multilingual-cased",
    "bert-base-multilingual-cased"
]

results = {}
for model_name in models:
    model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=len(label2id), id2label=id2label, label2id=label2id)
    trainer = Trainer(
        model,
        args, 
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["test"],
        data_collator=data_collator,
        tokenizer=tokenizer,
    )
    trainer.train()
    eval_result = trainer.evaluate()
    results[model_name] = eval_result

print(results) 