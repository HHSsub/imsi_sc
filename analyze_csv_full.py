import pandas as pd
import sys

files = [
    r"c:\Users\User\Downloads\sc_code\sillim_custom_project_1\data\final_anua_reviews.csv",
    r"c:\Users\User\Downloads\sc_code\sillim_custom_project_1\data\anua_reviews_unlimited_6_with_product (2).csv",
    r"c:\Users\User\Downloads\sc_code\sillim_custom_project_1\data\anua_merged_1_4_7_10_11.csv",
    r"c:\Users\User\Downloads\sc_code\sillim_custom_project_1\data\roundlab_comprehensive_reviews.csv"
]

for f in files:
    print(f"\n--- Analyzing {f} ---")
    try:
        # Try different encodings
        for enc in ['utf-8-sig', 'cp949', 'utf-8']:
            try:
                # Read specific columns to save memory if needed, but here we just read the whole thing if possible
                df = pd.read_csv(f, encoding=enc)
                print(f"Total rows: {len(df)}")
                print(f"Columns: {df.columns.tolist()}")
                
                potential_cols = ['product_name', '제품이름', '상품명', 'product']
                name_col = next((c for c in potential_cols if c in df.columns), None)
                
                if name_col:
                    print(f"Unique products in '{name_col}':")
                    unique_names = df[name_col].unique()
                    for name in sorted(unique_names):
                        print(f"  - {name}")
                else:
                    print("No product name column found. First row:")
                    print(df.iloc[0].to_dict())
                break
            except Exception as e:
                if enc == 'utf-8':
                    print(f"Failed to read {f} with any encoding. Last error: {e}")
                continue
    except Exception as e:
        print(f"Error processing {f}: {e}")
