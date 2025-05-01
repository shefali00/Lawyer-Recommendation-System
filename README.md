# Lawyer-Recommendation-System

# ⚖️ AI-Powered Lawyer Recommendation System

This project uses **Google's Gemini 1.5 Flash** model to analyze user-inputted legal case descriptions and recommend the most suitable **type of lawyer**, **type of court**, and **legal location in India**. It then filters from a dataset of Indian legal professionals to suggest lawyers who best match the user's needs.

---

## 📌 Introduction

Navigating the Indian legal system can be overwhelming. This AI-based system simplifies the process by:
- Understanding natural language legal issues using a large language model.
- Recommending the ideal legal expertise, court type, and jurisdiction.
- Providing a curated list of lawyers from an Excel-based database.

---

## ✨ Features

- 🧠 **AI-powered legal understanding** using Gemini 1.5 Flash.
- 🔍 **Recommends**:
  - Lawyer specialization  
  - Relevant court type  
  - Suitable Indian location  
- 📊 **Filters and ranks lawyers** from a dataset based on match and rating.
- 📍 Optional integration with **Geo-location API** (via Nominatim).
- 🖥️ Easy-to-use **Streamlit web app** frontend.

---

## 🧾 Prerequisites

- Python 3.8+
- A valid [Google AI Studio API Key](https://aistudio.google.com/app/apikey)
- Required libraries (installed via `requirements.txt`)
- Dataset: `output_data.xlsx` with the following columns:
  - `Name`, `Location`, `Type_of_Court`, `Type_of_Lawyer`, `Stars`

---

## ⚙️ Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/lawyer-recommendation-ai.git
   cd lawyer-recommendation-ai
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** and add your API key:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   ```

4. **Add the dataset**:  
   Place your `output_data.xlsx` file inside the project root.

---

## 🚀 Usage

To run the Streamlit app:
```bash
streamlit run app.py
```

### Example Input:
> "My father was assaulted and I live in Uttar Pradesh. I want to proceed legally through a district court."

### Output:
- Type of Lawyer: Criminal Defense  
- Court Type: District Court  
- Location: Uttar Pradesh  
- ✅ Top lawyer matches from dataset based on rating

---

## 🔍 How It Works

1. **User inputs** a free-text legal scenario.
2. **Gemini API** processes the description and returns:
   - Recommended lawyer type  
   - Recommended court type  
   - Likely jurisdiction
3. **Data is filtered** from `output_data.xlsx` to find lawyers matching all three.
4. **Results** are sorted by rating (`Stars`) and displayed in a table.

---

## 🛠 Tech Stack

- Python
- Google Gemini API
- Pandas
- Streamlit
- OpenAI-compatible prompt design
- Geopy (optional, for enhanced location relevance)



