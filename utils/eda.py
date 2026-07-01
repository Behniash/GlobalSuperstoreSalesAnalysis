def detect_mixed_types(df):
    mixed_types = {}
    for column in df.columns:
        types = df[column].apply(lambda v: type(v).__name__).value_counts()
        if len(types) > 1:
            mixed_types[column] = types.to_dict()
    return mixed_types
