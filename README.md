#  AI Recipe Generator (Ingredient-Based) [live](https://cookbott.streamlit.app/)

An interactive web app that generates complete recipes based on ingredients you provide. Built using **LangChain**, **Hugging Face LLMs**, and **Streamlit**, this project turns your available ingredients into delicious, structured recipes instantly.

---

##  Features

-  Generate recipes from available ingredients  
-  Structured output:
  - Recipe title  
  - Ingredients with quantities  
  - Step-by-step instructions  
  - Optional tips & variations  
-  Chat-based interface  
-  Powered by LLM (`Llama 3.1 8B Instruct`)  
-  Adapts recipes to regional preferences (e.g., Nepali, vegetarian, quick meals)

---

##  Tech Stack

- Python  
- LangChain  
- Hugging Face Hub  
- Streamlit  
- dotenv  

---

## Installation

### 1. Clone the repository
```bash
git clone hhttps://github.com/Mr-AshishBhandari/CookBot
cd CookBot

# configure project using uv
uv init
uv venv

uv sync 

streamlit run main.py 
