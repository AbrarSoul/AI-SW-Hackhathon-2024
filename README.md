
# Challenge B: Agricultural Events

## Project Overview

This project provides three Python-based tools for analyzing and interpreting data related to Finland’s CAP (Common Agricultural Policy) goals and event data:

1. **`event_analysis.py`** - Analyzes event data for themes, keyword frequency, and top trends in agricultural and rural events.
2. **`CAP_analysis.py`** - Extracts CAP goals from a policy document, correlates them with event data, and provides insights and recommendations for underrepresented goals.
3. **`search.py`** - A Streamlit-based dashboard for exploring event data and aligning it with CAP goals, offering visualizations and search functionality.

These tools help stakeholders understand CAP policy alignment and identify future event opportunities.

---

## Features

- **Text Analysis:** Tokenizes text to extract meaningful keywords and themes.
- **CAP Goal Alignment:** Matches event themes to CAP goals for strategic planning.
- **Visualization:** Provides bar charts for keyword frequency and event alignment.
- **Interactive Dashboard:** A web-based tool for searching and exploring event data.

---

## Requirements

### Software and Tools
1. **Python 3.8+**
2. **Required Libraries:**
   - `pandas`
   - `numpy`
   - `matplotlib`
   - `nltk`
   - `streamlit`
   - `pdfplumber`
   - `openpyxl`
3. **Additional Tools:**
   - An IDE or code editor (e.g., VSCode, PyCharm).
   - `pip` for Python package installation.

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK Data:**
   Run the following commands in a Python shell:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

---

## Usage

### 1. **Run `event_analysis.py`:**
   Analyze event data and extract keyword insights.
   ```bash
   python event_analysis.py
   ```
   Output: Frequency charts and printed top keywords.

### 2. **Run `CAP_analysis.py`:**
   Extract CAP goals, correlate with event data, and visualize findings.
   ```bash
   python CAP_analysis.py
   ```
   Output: CAP goal matches and recommendations.

### 3. **Run `search.py`:**
   Launch the Streamlit dashboard for interactive analysis.
   ```bash
   python -m streamlit run search.py
   ```
   Navigate to the provided URL in your browser to interact with the dashboard.

---

## Input Files

- **Event Data:** Excel file named `2_tapahtumat_agrihubi.xlsx`.
- **CAP Document:** PDF file titled `2_Suomen_CAP-suunnitelma.pdf`.

Ensure these files are placed in the same directory as the Python scripts.

---

## Outputs

1. **Keyword Frequency Charts**
2. **CAP Goal Alignment Charts**
3. **Dashboard Views and Search Results**

---

## Notes

- Customize file paths in the scripts if your input files are stored elsewhere.
- Review the CAP document to understand the policy goals in detail (provided in Finnish in the uploaded PDF).

---

## License

This project is open source. Contributions and improvements are welcome!
