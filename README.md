# 📊 Advanced Exploratory Data Analysis (EDA) Case Study

An end-to-end Exploratory Data Analysis (EDA) project that demonstrates
how to transform raw, unclean customer data into a clean, insightful,
and machine learning--ready dataset using Python. This project follows a
structured EDA roadmap including data cleaning, visualization,
statistical analysis, feature engineering, and dimensionality reduction.

------------------------------------------------------------------------

## 🚀 Project Highlights

-   ✔ Data profiling with missing value count & percentage\
-   ✔ Column-wise missing value imputation (Median, Mean, KNN)\
-   ✔ Duplicate removal & outlier treatment (IQR method)\
-   ✔ Univariate, bivariate & multivariate visualizations\
-   ✔ Descriptive statistics & hypothesis testing\
-   ✔ Feature engineering (`AgeGroup`)\
-   ✔ One-Hot Encoding for categorical variables\
-   ✔ Scaling & log transformation\
-   ✔ PCA for dimensionality reduction\
-   ✔ ML-ready dataset generation\
-   ✔ All plots saved for reporting

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Language:** Python 3.10+\
-   **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn,
    SciPy\
-   **Tool:** Jupyter Notebook

------------------------------------------------------------------------

## 📂 Project Structure

``` text
advanced_eda_case_study/
│
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
│
├── notebooks/
│   └── eda_analysis.ipynb
│
├── outputs/
│   └── plots/
│       ├── age_before_imputation.png
│       ├── age_after_imputation.png
│       ├── annualincome_before_imputation.png
│       ├── annualincome_after_imputation.png
│       ├── spendingscore_before_imputation.png
│       ├── spendingscore_after_imputation.png
│       ├── age_boxplot_final_outliers.png
│       ├── annualincome_boxplot_final_outliers.png
│       ├── spendingscore_boxplot_final_outliers.png
│       ├── top_features_correlation.png
│       └── annual_income_vs_purchase.png
│
├── src/
│   └── generate_data.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

------------------------------------------------------------------------

## 📈 Key Insights

-   **AnnualIncome** has a strong positive relationship with purchase
    behavior.\
-   **SpendingScore** significantly influences customer engagement.\
-   Adult and Mid-Age groups show higher purchase tendencies.\
-   PCA reveals that most variance can be captured using fewer
    dimensions.\
-   The cleaned dataset is suitable for building ML classification
    models.

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/your-username/advanced_eda_case_study.git
cd advanced_eda_case_study
```

### 2️⃣ (Optional) Create Virtual Environment

``` bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4️⃣ (Optional) Generate Raw Dataset

``` bash
python src/generate_data.py
```

### 5️⃣ Launch Jupyter Notebook

``` bash
jupyter notebook notebooks/eda_analysis.ipynb
```

------------------------------------------------------------------------

## 📁 Outputs

-   📄 Cleaned dataset → `data/cleaned_data.csv`\
-   🖼️ All saved plots → `outputs/plots/`\
-   📓 Full analysis → `notebooks/eda_analysis.ipynb`

------------------------------------------------------------------------

## 👤 Author

**Shyam Ji**\
🎓 B.Tech in Computer Science Engineering\
💼 Aspiring **Data Analyst \| Data Scientist \| AI Engineer**\
🧠 Skills: Python, Pandas, SQL, Data Analytics, Machine Learning, EDA\
📍 India

------------------------------------------------------------------------

If you find this project useful, feel free to ⭐ star the repository!
