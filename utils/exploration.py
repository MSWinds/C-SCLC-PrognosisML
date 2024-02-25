# Made by: Yuri Yu
# This is a function for data exploration. It takes in a dataframe, a column name and an optional hue column name.
def data_exploration(df, column, hue=None):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np

    # Check if hue is valid
    hue_condition = hue and df[hue].nunique() < 10
    if hue and not hue_condition:
        return "Hue has more than 10 unique values."

    # Determine the column type and unique value count
    col_type = df[column].dtype
    unique_values = df[column].nunique()

    # Handling categorical data or numerical with less than 10 unique values
    if col_type == 'object' or col_type == 'category':
        count_pct = pd.concat([df[column].value_counts(), df[column].value_counts(normalize=True) * 100], axis=1)
        count_pct.columns = ['Count', 'Percentage']
        print(f"Counts and percentages of unique values in {column}:\n{count_pct}")

        # Plotting
        if hue_condition:
            sns.countplot(data=df, x=column, hue=hue)
        else:
            sns.countplot(data=df, x=column, hue=column)
        plt.title(f"Distribution of {column}")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    # Handling numerical data with 10 or more unique values
    elif unique_values > 10:
        # Statistical summary
        mean = df[column].mean()
        median = df[column].median()
        std_dev = df[column].std()
        mode = df[column].mode()[0]

        # Interquartile range for outlier detection
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        outlier_range = (q1 - 1.5 * iqr, q3 + 1.5 * iqr)
        extreme_outlier_range = (q1 - 3 * iqr, q3 + 3 * iqr)

        # Outliers calculation
        outliers = df[(df[column] < outlier_range[0]) | (df[column] > outlier_range[1])]
        extreme_outliers = df[(df[column] < extreme_outlier_range[0]) | (df[column] > extreme_outlier_range[1])]

        # Output statistical information
        print(f"Mean of {column}: {mean:.2f}")
        print(f"Median of {column}: {median:.2f}")
        print(f"Standard deviation of {column}: {std_dev:.2f}")
        print(f"Mode of {column}: {mode}")
        print(f"Number of outliers in {column}: {len(outliers)}")
        print(f"Number of extreme outliers in {column}: {len(extreme_outliers)}")
        plt.figure(figsize=(16, 6))
        # Box plot as the first subplot
        plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
        if hue_condition:
            sns.boxplot(data=df, x=column, hue=hue)
        else:
            sns.boxplot(data=df, x=column)
        plt.title(f"Box plot of {column}")
        plt.grid(True)

        # Histogram as the second subplot
        plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
        bins_num = int(np.ceil(np.sqrt(df[column].nunique())))  # Sturges' formula
        if hue_condition:
            sns.histplot(data=df, x=column, bins=bins_num, kde=True, hue=hue)
        else:
            sns.histplot(data=df, x=column, bins=bins_num, kde=True)
        plt.title(f"Histogram of {column}")
        plt.grid(True)

        # Display the combined figure with both subplots
        plt.tight_layout()
        plt.show()
    elif unique_values <= 10:
        count_pct = pd.concat([df[column].value_counts(), df[column].value_counts(normalize=True) * 100], axis=1)
        count_pct.columns = ['Count', 'Percentage']
        print(f"Counts and percentages of unique values in {column}:\n{count_pct}")

        # Plotting
        if hue_condition:
            sns.countplot(data=df, x=column, hue=hue)
        else:
            sns.countplot(data=df, x=column, hue=column)
        plt.title(f"Distribution of {column}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
# Example of usage:
# data_exploration(your_dataframe, 'your_column_name', hue='your_hue_column')
