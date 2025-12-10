# 🏘️ Comprehensive Real Estate Analysis: Key Questions

This document outlines the most crucial questions for understanding the Algerian real estate market using the Ouedkniss dataset. These insights are structured to serve the interests of buyers, sellers, investors, and general public interested in market trends.

## 1. 💰 Core Metrics & Regional Price Comparison

These questions focus on determining the true value of property and comparing affordability across the country.

| Question | Audience Benefit | Key Columns Involved |
| :--- | :--- | :--- |
| **1. Regional Price Benchmark:** What are the **top 5 most expensive** and **least expensive** cities in Algeria when measuring the **median price per square meter** ($\text{DA}/\text{m}^2$)? | **General Public/Buyers:** Quickly identifies regions of wealth concentration and high-value areas. | `price`, cleaned `area`, `city` |
| **2. Inter-City Affordability:** How significant are the price differences (in percentage) for a standard property (e.g., F3 apartment) between the capital (Algiers) and other major regional hubs (Oran, Constantine)? | **Buyers/Investors:** Helps decide if investing outside the capital offers significantly better value or entry price. | `price`, `city`, extracted `type` |
| **3. Property Value by Size:** How does the total sale price of a specific property type (e.g., F4) correlate with its total **size ($\text{area}$)** across the top-listed cities? | **Buyers/Sellers:** Provides the expected price increase for every additional square meter in a specific location. | `price`, cleaned `area`, `city`, extracted `type` |
| **4. Agency vs. Private Pricing:** Is there a noticeable price difference (premium or discount) between listings posted by **professional real estate agencies** (`store`) versus individual sellers? | **Buyers/Sellers:** Guides the choice of listing method; informs buyers where to expect more negotiation flexibility. | `price`, `store` (as boolean feature) |

## 2. 📈 Market Dynamics and Investment Trends

These questions address the health and movement of the market over time, essential for timing a transaction or investment.

| Question | Audience Benefit | Key Columns Involved |
| :--- | :--- | :--- |
| **5. Price Trend Over Time:** How has the median listing price per square meter changed **over the entire period captured** in the dataset (e.g., quarter-over-quarter)? | **Investors/General Public:** Reveals the underlying inflation or appreciation rate of real estate assets in the Algerian market. | `price`, cleaned `area`, `createdAt` |
| **6. Supply Trend & Competition:** Has the **volume of new listings** (supply) increased or decreased over the available time period, indicating a change in market liquidity and competition? | **Sellers:** Crucial for timing a sale; a drop in volume suggests less competition. | Count of listings by `createdAt` |
| **7. Seasonal Transaction Pattern:** Is there a **seasonal pattern** in the number of listings (`availability`)? (e.g., do listings spike in summer months when the diaspora visits?) | **Buyers/Sellers:** Helps determine the best time to list (low supply) or to search (high supply). | Monthly/Quarterly count of listings by `createdAt` |
| **8. Highest Growth Segments:** Which property types (e.g., 'F5 apartment' vs. 'land plot' vs. 'villa') have shown the **highest price growth** over the available time period? | **Investors:** Directs capital toward the most profitable and fastest-appreciating segments of the market. | `price`, `createdAt`, extracted `property_type` |

## 3. 🎯 Property Specifics and Value Drivers

These questions help sellers optimize their listing features and guide developers on market demand.

| Question | Audience Benefit | Key Columns Involved |
| :--- | :--- | :--- |
| **9. Key Value Drivers:** What are the primary features (e.g., number of rooms, presence of a garden/garage, etc.) **driving the price** of a property in a given city (Feature Importance)? | **Sellers/Builders:** Informs renovation and construction decisions to maximize sale price. | `price`, all engineered features (rooms, amenities, type, city) |
| **10. Optimal Listing Price Range (for Sellers):** What is the typical **price range** (25th to 75th percentile) for an F4 apartment of 100$\text{m}^2$ in the most listed city? | **Sellers:** Allows for setting an accurate, competitive, and realistic listing price. | `price`, cleaned `area`, extracted `type`, `city` |
| **11. Market Demand (for Developers):** What is the **most frequently advertised property size** (median $\text{area}$) across the top 10 most listed cities? | **Builders/Developers:** Indicates the most popular product size that the market is currently demanding. | Cleaned `area`, `city` |
| **12. Property Type Popularity:** What is the **most commonly listed type** of property (apartment type Fx, villa, or land) in high-demand coastal cities? | **Investors:** Gauges market supply for specific property types, revealing potential shortages or oversupply. | Extracted `type`/room count from `title` or `slug`, `city` |

## 4. ⚠️ Data Quality and Reliability

These questions establish the integrity of the data and the reliability of the resulting analysis.

| Question | Audience Benefit | Key Columns Involved |
| :--- | :--- | :--- |
| **13. Data Reliability:** Which cities or regions have the most severe **data gaps** (missing values) in crucial features like `price` and `area`? | **General Public / Analysts:** Advises users to treat data from certain regions with higher skepticism, requiring reliance on local agents instead. | Missing value count in `price` and `area` grouped by `city` |
| **14. Outlier Impact:** Are there any severe outliers (e.g., impossibly tiny area or extremely high price) that could be skewing the calculated average prices? | **Analysts:** Ensures that extreme errors do not mislead the calculated averages and medians. | Statistical analysis of `price` and cleaned `area` distributions |