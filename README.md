🇩🇿 Algeria Real Estate Market Analysis
========================================

**Open-source data analysis project exploring price trends, spatial patterns, and market insights in the Algerian real estate sector.**

This project aims to build the **first fully open-source, data-driven analysis of the Algerian real-estate market** using publicly accessible listing data, official statistics, and reproducible Python workflows.\
It is designed as a **professional-level data analytics portfolio project** demonstrating skills in:

-   Data collection (scraping & APIs)

-   Data cleaning & transformation (ETL)

-   Exploratory data analysis (EDA)

-   Geospatial analysis

-   Machine learning for price estimation

-   Dashboard building (Streamlit)

-   Documentation & open-source practices

All analysis, code, visualizations, and methodologies are published openly so anyone can learn, replicate, or contribute.

* * * * *

📌 Project Objectives
=====================

### 🎯 Main Goals

-   Create a **clean, standardized dataset** of Algerian real-estate listings.

-   Study **price levels**, **price/m²**, **rental vs sale**, and **spatial variations**.

-   Identify **trends**, **anomalies**, **supply signals**, and **market structure**.

-   Build **visual dashboards** for exploration and reporting.

-   Prototype a simple **price estimation model** (predict price based on features).

-   Document the entire workflow for educational and research purposes.

### 🧠 Why this project?

The Algerian real estate market suffers from:

-   lack of accessible structured data

-   fragmented listings

-   limited official publications

-   no open intelligence tools

This project aims to fill the gap by creating the **first transparent, reproducible data pipeline** that analyzes the market using modern data science methods.

* * * * *

🗂 Data Sources
===============

### 1) **Public listings portals**

*(Only metadata is collected; no personal info is stored.)*

-   **Ouedkniss -- Immobilier** (classified ads)
> ⚠️ **Respect for robots.txt & Terms of Use:**\
> Raw HTML is **never** published. Only **aggregated, cleaned, or synthetic** data samples are shared.

### 2) **Official statistics**

-   Office National des Statistiques (ONS): housing stock, construction, regional stats.

### 3) **Supplementary datasets**

-   Geospatial datasets (Wilaya, Commune boundaries)

-   Voluntary public datasets (e.g., curated samples from Kaggle)

* * * * *

🏗 Project Architecture
=======================

`algeria-real-estate/
├── README.md
├── LICENSE
├── requirements.txt
├── data/
│   ├── raw/          # Raw scraped data (NOT committed)
│   ├── processed/    # Cleaned datasets (CSV/Parquet)
│   └── external/     # Public sample datasets
├── src/
│   ├── etl/
│   │   ├── ouedkniss_scraper.py
│   │   ├── mubawab_scraper.py
│   │   └── ons_downloader.py
│   ├── features.py
│   ├── models.py
│   └── viz.py
├── notebooks/
│   ├── 01-data-exploration.ipynb
│   ├── 02-feature-engineering.ipynb
│   └── 03-price-modeling.ipynb
├── dashboard/
│   └── app.py        # Streamlit dashboard
└── docs/
    ├── methodology.md
    ├── data_sources.md
    └── contributing.md`

* * * * *

🔧 Tech Stack
=============

**Languages & Tools**

-   Python 3.10+

-   Pandas, NumPy

-   BeautifulSoup / Playwright

-   GeoPandas, Folium, Pydeck

-   Scikit-Learn

-   Streamlit

-   PostgreSQL/PostGIS (optional)

-   GitHub Actions (CI)

* * * * *

📊 Key Features
===============

### ✔️ **1\. Automated Data Collection**

-   Scrapers for property listings

-   Caching, pagination, rate-limiting

-   Saves raw → cleaned → processed pipeline

-   Reproducible scripts to rebuild entire dataset

### ✔️ **2\. Data Cleaning & Standardization**

-   Unified schema

-   Extraction of structured fields:

    -   price (DZD), price_per_m2

    -   location (city, wilaya, lat/lon)

    -   type (rent / sale), property type

    -   rooms, area, features

-   Geocoding & fuzzy matching for city names

### ✔️ **3\. Exploratory Data Analysis (EDA)**

-   Price distributions

-   Price/m² heatmaps

-   Supply trends by time

-   City-level comparisons

-   Outlier detection

### ✔️ **4\. Spatial Analysis**

-   Price heatmaps across wilayas

-   Neighborhood-level clustering

-   Distance to city centers

### ✔️ **5\. Machine Learning**

-   Linear Regression

-   RandomForestRegressor

-   KNN price estimators

-   Evaluation: RMSE, MAE, MAPE

### ✔️ **6\. Interactive Dashboard**

A user-friendly **Streamlit app** to:

-   Explore listings on an interactive map

-   Filter by wilaya, price, rooms, area

-   Visualize trends & KPIs

-   Test the price estimator

### ✔️ **7\. Full Documentation**

-   Methodology

-   Data limitations

-   Ethical considerations

-   Reproducibility instructions

-   Step-by-step explanation for beginners

* * * * *

🚀 Getting Started
==================

### 1\. Clone the repository

`git clone https://github.com/<your-username>/algeria-real-estate.git
cd algeria-real-estate`

### 2\. Install dependencies

`pip install -r requirements.txt`

### 3\. Run scrapers (sample)

`python src/etl/ouedkniss_scraper.py`

### 4\. Run the dashboard

`streamlit run dashboard/app.py`

* * * * *

📈 Example KPIs Produced
========================

-   Median price by wilaya

-   Median price/m² by city

-   Top expensive areas

-   Rental vs sale distribution

-   Average listing sizes

-   Seasonal trends

-   Price anomalies

* * * * *

⚠️ Data Ethics & Legal Notes
============================

This project follows responsible data practices:

-   No personal or sensitive data is stored.

-   Raw HTML content from scraped websites is **not published**.

-   Only aggregated, cleaned, or synthetic datasets are shared.

-   Scraping obeys rate limits and Terms of Use.

-   Users must comply with laws in their jurisdiction.

* * * * *

🧩 Roadmap
==========

### **Milestone 1 --- Data ingestion (v0.1)**

-   ✔ Basic scrapers

-   ✔ Standardized schema

-   ✔ Clean sample dataset

-   ☐ Initial EDA Notebook

### **Milestone 2 --- Full EDA (v0.2)**

-   ☐ Price analysis

-   ☐ Spatial mapping

-   ☐ Time trends

### **Milestone 3 --- Dashboard (v0.3)**

-   ☐ Streamlit dashboard

-   ☐ Interactive maps

### **Milestone 4 --- Modeling (v0.4)**

-   ☐ Baseline model

-   ☐ ML price estimator

### **Milestone 5 --- Release (v1.0)**

-   ☐ Full documentation

-   ☐ Public dataset

-   ☐ Contributions open

* * * * *

🤝 Contributing
===============

Contributions are welcome!

Please read:

-   `docs/contributing.md`

-   Open an Issue before a major change

-   Follow PEP8 and write small, tested PRs

* * * * *

📄 License
==========

-   Code: **MIT License**

-   Data: depends on source terms (see `docs/data_sources.md`).

-   Public derived datasets are shared under **ODbL** when allowed.

* * * * *