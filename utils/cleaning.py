import pandas as pd


def detect_outliers(df):
    ignore_cols = ["row_id", "postal_code"]
    numeric_cols = [col for col in df.select_dtypes(include='number').columns if col not in ignore_cols] 
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        mask = (df[col] < lower_bound) | (df[col] > upper_bound)
        count = mask.sum()
        percent = (count / len(df)) * 100

        print(f"{col:<5} ---> {count:>5} outliers ({percent:.2f}%)")
        print(f"bounds: [{lower_bound:,.2f} , {upper_bound:,.2f}]")

        if count > 0:
            outlier_values = df.loc[mask, col].sort_values()
            print(f"lowest: {outlier_values.head(10).tolist()}")
            print(f"highest: {outlier_values.tail(10).tolist()}")
        print()