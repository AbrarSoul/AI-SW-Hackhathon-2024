# AI-SW-Hackhathon-2024
# Challenge B: Agricultural Events

## Project Overview

This project analyzes agricultural event data from **maaseutuverkosto.fi/AgriHubi.fi** to assess their alignment with the EU's CAP plan. It provides insights into event distribution, keyword frequencies, and future event recommendations, along with an interactive search functionality.

---

## Features

1. **Requirement 1: Event Analysis**:
   - Tokenizes event data to identify the most common keywords.
   - Filters and visualizes keyword frequencies.
     
1. **Requirement 2: CAP Plan Analysis**: 
   - Extracts key themes from the CAP plan and matches them with event data.
   - Visualizes keyword co-occurrences and CAP goal matches.

3. **Requirement 3: Search event**:
   - Displays CAP alignment, top themes, and recommendations.
   - Includes a search functionality to browse event data by keywords.

---

## File Descriptions

### 1. **event_analysis.py**
- Tokenizes event data to identify frequent keywords.
- Uses NLTK to clean and filter text for analysis.
- Visualizes top keywords with bar charts.
  
### 2. **CAP_analysis.py**
- Extracts CAP goals from a PDF file and analyzes event data for alignment.
- Performs co-occurrence analysis of keywords and generates visualizations.
- Recommends underrepresented themes based on CAP goals.

### 3. **search.py**
- Streamlit-based dashboard.
- Provides an interactive interface to:
  - Visualize CAP goal alignment.
  - Display keyword distributions.
  - Perform free-text search on event data.

---

## Setup Instructions

### Prerequisites
1. Python 3.9 or later.
2. Libraries:
   - `pandas`
   - `matplotlib`
   - `nltk`
   - `pdfplumber`
   - `streamlit`
   - `openpyxl`

Install required libraries with:
```bash
pip install pandas matplotlib nltk pdfplumber streamlit openpyxl
