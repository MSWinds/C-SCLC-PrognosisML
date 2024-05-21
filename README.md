**Project Title: Combined Small Cell Lung Cancer (C-SCLC) Survival Analysis and Prediction**

**Abstract**

Combined Small Cell Lung Cancer (C-SCLC), a rare variant subtype of lung cancer, has distinct characteristics and prognosis challenges. Despite its clinical significance, there exists a knowledge gap in the diagnosis, treatment, and prognosis of C-SCLC. Utilizing the SEER database, an authoritative source of cancer data in the United States, we applied advanced machine learning techniques to analyze the overall survival (OS) of C-SCLC patients from 2004 to 2020 across multiple staging systems. Our findings provide significant insights and contributions into the survival outcomes of C-SCLC patients, for their distinction within lung cancer classifications. We present a model to predict OS for patients with this rare subtype from 2004 to 2015, using the AJCC 6th edition, alongside visualizations and code to reproduce these results. Our model achieves 81% recall for high-risk patients (less than 9 months survival), with key contributing factors being Metastasis, Chemotherapy, Radiation, Surgery, and Tumor Size.

**How to Use the Files**

1. **Data:** The "Data" folder contains:
    * Raw data (as obtained from SEER)
    * Pre-processed data (ready for modeling)

2. **Models:** The "Models" folder contains saved models for reproducing results.

3. **Utils:** The "utils" folder contains functions used throughout the project.

4. **SEERStat Receipts:** Images "data_collection1.png", etc. provide proof of data access through SEERStat.

5. **Reproducing the Analysis:**
    * Start with "data_cleaning.ipynb" for initial data cleaning.
    * Proceed to "data1_preprocessing.ipynb" for further preprocessing.
    * Finally, use "data1_modeling.ipynb" to run the modeling process.

**Important Notes**

* This project focuses on data from 2004-2015 for consistency with the AJCC 6th Edition staging system. 
* Other files in the repository represent exploratory work or  tests.

**Disclaimer**

This project is for research and analysis purposes only.  Do not use the results for making clinical decisions. Data cannot be shared due to privacy issues, please create an account with SEER to access the data 
