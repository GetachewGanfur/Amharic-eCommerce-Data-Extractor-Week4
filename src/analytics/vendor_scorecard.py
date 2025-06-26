import pandas as pd
import glob
import os

def calculate_metrics(df):
    posts_per_week = df.groupby('week').size().mean()
    avg_views = df['views'].mean()
    top_post = df.loc[df['views'].idxmax()]
    avg_price = df['price'].mean() if 'price' in df else None
    return posts_per_week, avg_views, top_post, avg_price

def main():
    files = glob.glob('data/processed/*.csv')
    summary = []
    for file in files:
        df = pd.read_csv(file)
        df['date'] = pd.to_datetime(df['date'])
        df['week'] = df['date'].dt.isocalendar().week
        # Extract price using your NER model or regex
        # df['price'] = ...
        posts_per_week, avg_views, top_post, avg_price = calculate_metrics(df)
        summary.append({
            'vendor': os.path.basename(file).replace('_messages.csv', ''),
            'posts_per_week': posts_per_week,
            'avg_views': avg_views,
            'top_post': top_post['text'],
            'top_post_views': top_post['views'],
            'avg_price': avg_price,
            'lending_score': (avg_views * 0.5) + (posts_per_week * 0.5)
        })
    summary_df = pd.DataFrame(summary)
    summary_df.to_csv('data/vendor_scorecard.csv', index=False)
    print(summary_df)

if __name__ == "__main__":
    main() 