<h1>🧾 Vendor Performance Analysis – Retail Inventory & Sales</h1>
<p><i>Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using SQL, Python, and Power BI.</i></p>

<hr>

<h2>📌 Table of Contents</h2>
<ul>
<li><a href="#overview">Overview</a></li>
<li><a href="#business-problem">Business Problem</a></li>
<li><a href="#dataset">Dataset</a></li>
<li><a href="#tools">Tools & Technologies</a></li>
<li><a href="#project-structure">Project Structure</a></li>
<li><a href="#data-cleaning">Data Cleaning & Preparation</a></li>
<li><a href="#eda">Exploratory Data Analysis (EDA)</a></li>
<li><a href="#findings">Research Questions & Key Findings</a></li>
<li><a href="#dashboard">Dashboard</a></li>
<li><a href="#recommendations">Final Recommendations</a></li>
<li><a href="#contact">Author & Contact</a></li>
</ul>

<hr>

<h2 id="overview">Overview</h2>
<p>
This project evaluates vendor performance and retail inventory dynamics to generate actionable insights for purchasing, pricing, and inventory optimization.
A complete data pipeline was built using SQL for ETL, Python for analysis and hypothesis testing, and Power BI for visualization.
</p>

---
<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

Effective inventory and sales management are critical in the retail sector. This project aims to:
- Identify underperforming brands needing pricing or promotional adjustments
- Determine vendor contributions to sales and profits
- Analyze the cost-benefit of bulk purchasing
- Investigate inventory turnover inefficiencies
- Statistically validate differences in vendor profitability

---
<hr>

<h2 id="dataset">Dataset</h2>
<ul>
<li>Multiple CSV files located in <code>/data/</code> folder</li>
<li>Summary table created from ingested data and used for analysis</li>
</ul>

<hr>

<h2 id="tools">Tools & Technologies</h2>
<ul>
<li>SQL (CTEs, Joins, Filtering)</li>
<li>Python (Pandas, Matplotlib, Seaborn, SciPy)</li>
<li>Power BI (Interactive Visualizations)</li>
<li>GitHub</li>
</ul>

<hr>
<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
vendor-performance-analysis/
│
├── README.md 
├── Vendor Performance Report.pdf
│
├── notebooks/                  # Jupyter notebooks
│   ├── exploratory_data_analysis.ipynb
│   ├── vendor_performance_analysis.ipynb
│
├── scripts/                    # Python scripts for ingestion and processing
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
│
├── dashboard/                  # Power BI dashboard file
│   └── vendor_performance_dashboard.pbix
```

---
<hr>

<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning & Preparation</h2>

- Removed transactions with:
  - Gross Profit ≤ 0
  - Profit Margin ≤ 0
  - Sales Quantity = 0
- Created summary tables with vendor-level metrics
- Converted data types, handled outliers, merged lookup tables

---

<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>

**Negative or Zero Values Detected:**
- Gross Profit: Min -52,002.78 (loss-making sales)
- Profit Margin: Min -∞ (sales at zero or below cost)
- Unsold Inventory: Indicating slow-moving stock

**Outliers Identified:**
- High Freight Costs (up to 257K)
- Large Purchase/Actual Prices

**Correlation Analysis:**
- Weak between Purchase Price & Profit
- Strong between Purchase Qty & Sales Qty (0.999)
- Negative between Profit Margin & Sales Price (-0.179)

<hr>

<h2><a class="anchor" id="research-questions--key-findings"></a>Research Questions & Key Findings</h2>

1. **Brands for Promotions**: 198 brands with low sales but high profit margins
2. **Top Vendors**: Top 10 vendors = 65.69% of purchases → risk of over-reliance
3. **Bulk Purchasing Impact**: 72% cost savings per unit in large orders
4. **Inventory Turnover**: $2.71M worth of unsold inventory
5. **Vendor Profitability**:
   - High Vendors: Mean Margin = 31.17%
   - Low Vendors: Mean Margin = 41.55%
6. **Hypothesis Testing**: Statistically significant difference in profit margins → distinct vendor strategies

---

<h2 id="dashboard">Dashboard</h2>
<p>Power BI dashboard showing vendor performance, inventory turnover, and profitability insights.</p>

<img src="image/dashboard.png" alt="Vendor Dashboard" width="700">

<hr>

<h2 id="recommendations">Final Recommendations</h2>
<ul>
<li>Diversify vendor base to reduce dependency risk</li>
<li>Optimize bulk purchasing strategies</li>
<li>Adjust pricing for slow-moving inventory</li>
<li>Improve marketing for underperforming vendors</li>
</ul>

<hr>
<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

**Pavan**  
Data Analyst  
📧 Email: psillal4321@gmail.com  
🔗 [LinkedIn](www.linkedin.com/in/pavan-479173238)  

