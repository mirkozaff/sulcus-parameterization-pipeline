import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, SimpleImputer
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import os
from os import path

#csv_path = '/home/zaffaro/Desktop/sulcus-parameterization-pipeline/by_subjevct_sulcal_measure.csv'
BVDIR = '/home/zaffaro/Desktop/sulcus-parameterization-pipeline/bv_dir_corrected'
subjects_path = os.path.join(BVDIR, 'subjects')

def z_score(df):
    # Copy the dataframe
    df_std = df.copy()
    # Apply the z-score method
    for column in df_std.columns:
        df_std[column] = (df_std[column] - df_std[column].mean()) / df_std[column].std()
        
    return df_std

def merge_dataframes():
    subjects = [f for f in os.listdir(subjects_path) if (path.isdir(path.join(subjects_path, f))) and ('KK' in f)]

    csv_path = path.join(BVDIR, 'subjects', subjects[0], 'by_subjevct_sulcal_measure.csv')
    df = pd.read_csv(csv_path, delimiter=';')

    for sj in subjects[1:]:
        csv_path = path.join(BVDIR, 'subjects', sj, 'by_subjevct_sulcal_measure.csv')
        df_temp = pd.read_csv(csv_path, delimiter=';')    
        df = pd.concat([df, df_temp], axis=0)

    return df

def main():
    # Read sulci dataframe
    df = merge_dataframes()
    print(df)

    # Convert sulci string to numeric categorical label
    df.label = pd.Categorical(df.label)
    df.label = df.label.cat.codes

    df.side = pd.Categorical(df.side)
    df.side = df.side.cat.codes

    df.sulcus = pd.Categorical(df.sulcus)
    df.sulcus = df.sulcus.cat.codes

    # Remove nan rows
    df = df.dropna()

    # Shuffle dataframe
    df = df.sample(frac=1).reset_index(drop=True)

    # Data Normalization
    std_scaler = StandardScaler()
    df = pd.DataFrame(std_scaler.fit_transform(df), columns=df.columns)
    #df = z_score(df)

    # Create correlation matrix
    corrM = df.corr()
    fig, ax = plt.subplots(figsize=(20,20))  
    sns.heatmap(corrM, annot = True, fmt='.2g', square=True, ax=ax)

    #figure = svm.get_figure()    
    plt.savefig('svm_conf.png', dpi=500)

    # Create test set
    test_size = 50
    y_true = df.tail(test_size).copy().values
    df_test = df.tail(test_size).copy()
    df.drop(df.tail(test_size).index, inplace = True)

    #Randomly imputing nan values
    for col in df_test.columns[3:]:
        df_test[col] = df_test[col].sample(frac=0.7)
    print(df_test)

    # Training Imputer
    imp = IterativeImputer(max_iter=10, random_state=0)
    imp.fit(df)

    # Generate predictions
    y_pred = imp.transform(df_test)

    # Scale back dataframe
    df_imputed = pd.DataFrame(std_scaler.inverse_transform(y_pred), columns=df.columns)
    print(df_imputed)

    # Compute mse
    mse = mean_squared_error(y_true, y_pred)
    print(f'Mean Squared Error: {mse}')


if __name__ == '__main__':
	main()