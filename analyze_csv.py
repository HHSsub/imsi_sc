import pandas as pd
import sys

files = [
    r"c:\Users\User\Downloads\sc_code\sillim_custom_project_1\data\final_anua_reviews.csv",
    r"c:\Users\User\Downloads\sc_code\sillim_custom_project_1\data\anua_reviews_unlimited_6_with_product (2).csv",
    r"c:\Users\User\Downloads\sc_code\sillim_custom_project_1\data\anua_merged_1_4_7_10_11.csv"
]

for f in files:
    print(f"\n--- Analyzing {f} ---")
    try:
        # Try different encodings
        for enc in ['utf-8-sig', 'cp949', 'utf-8']:
            try:
                df = pd.read_csv(f, encoding=enc, nrows=1000) # Read first 1000 to check columns
                print(f"Columns: {df.columns.tolist()}")
                if 'product_name' in df.columns:
                    print("Unique products (top 20):")
                    print(df['product_name'].value_counts().head(20))
                elif '상품명' in df.columns:
                    print("Unique products (top 20):")
                    print(df['상품명'].value_counts().head(20))
                else:
                    # Just print the first few rows to see what's there
                    print("First 2 rows:")
                    print(df.head(2))
                break
            except Exception:
                continue
    except Exception as e:
        print(f"Error: {e}")
