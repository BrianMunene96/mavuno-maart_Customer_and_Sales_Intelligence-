

# Preview the dataset 
def inspect_dataset(df):

    # 1. First few rows
    print("\n" + "=" * 60)
    print("1. FIRST 3 ROWS")
    print("=" * 60)
    print(df.head())

    # 2. Dataset shape
    print("\n" + "=" * 60)
    print("2. DATASET SHAPE")
    print("=" * 60)
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")

    # 3. Column names
    print("\n" + "=" * 60)
    print("3. COLUMN NAMES")
    print("=" * 60)
    print(df.columns.tolist())

    # 4. Duplicate rows
    print("\n" + "=" * 60)
    print("4. DUPLICATE ROWS")
    print("=" * 60)
    print(f"Number of duplicate rows: {df.duplicated().sum()}")

    # 6. Missing values
    print("\n" + "=" * 60)
    print("6. MISSING VALUES")
    print("=" * 60)
    print(df.isnull().sum())

    print("\n" + "=" * 60)
    print("6. MISSING VALUES PERCENTAGE")
    print("=" * 60)
    print(df.isnull().mean()* 100)

    # 7. Descriptive statistics
    print("\n" + "=" * 60)
    print("7. DESCRIPTIVE STATISTICS")
    print("=" * 60)
    print(df.describe(include="all").T)

    # 8. Dataset information
    print("\n" + "=" * 60)
    print("8. DATASET INFO")
    print("=" * 60)
    df.info()