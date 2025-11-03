# 🧠 LangChain Chains Exploration

> ⚙️ A hands-on project to understand and implement **different types of Chains in LangChain**, including:  
**Simple Chain, Sequential Chain, Parallel Chain, and Conditional Chain**

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue" />
  <img src="https://img.shields.io/badge/LangChain-Framework-green" />
  <img src="https://img.shields.io/badge/HuggingFace-Transformers-yellow" />
  <img src="https://img.shields.io/badge/Category-AI%20%26%20LLMs-orange" />
</p>

---

## 🚀 Project Overview

This project demonstrates the **core working principles of Chains in LangChain**, a powerful framework for building **applications with large language models (LLMs)**.  
You’ll explore how data flows between different **prompt templates, LLMs, and output parsers**, and how to combine multiple chains together for complex reasoning tasks.

---

## 🔗 Types of Chains Implemented

### 1️⃣ Simple Chain
A **basic chain** connecting one input → one prompt → one model → one output.  
Used when you just want a **direct LLM response** from a single prompt.

<p align="center">
  <img src="https://github.com/yourusername/langchain-chains-demo/blob/main/SimpleChain_1.png" width="350" />
  <img src="https://github.com/yourusername/langchain-chains-demo/blob/main/SimpleChain_2.png" width="350" />
</p>

---

### 2️⃣ Sequential Chain
A **multi-step chain** where the output of one step feeds into the next.  
Ideal for workflows like **rephrasing → answering → summarizing**.

<p align="center">
  <img src="https://github.com/yourusername/langchain-chains-demo/blob/main/SequentialChain_1.png" width="350" />
  <img src="https://github.com/yourusername/langchain-chains-demo/blob/main/SequentialChain_2.png" width="350" />
</p>

---

### 3️⃣ Parallel Chain
Runs **multiple chains at the same time**, each performing a unique subtask.  
Best for **multi-output** processing like generating **keywords, summaries, and insights simultaneously**.

<p align="center">
  <img src="https://github.com/yourusername/langchain-chains-demo/blob/main/ParallelChain_1.png" width="350" />
  <img src="https://github.com/yourusername/langchain-chains-demo/blob/main/ParallelChain_2.png" width="350" />
</p>

---

### 4️⃣ Conditional Chain
Executes **different chains based on logical conditions or inputs**.  
Useful when you want **decision-based task routing**, e.g. translation vs. question answering.

<p align="center">
  <img src="https://github.com/yourusername/langchain-chains-demo/blob/main/ConditionalChain_1.png" width="350" />
  <img src="https://github.com/yourusername/langchain-chains-demo/blob/main/ConditionalChain_2.png" width="350" />
</p>

---

## 🧩 Tech Stack

| Component | Description |
|------------|--------------|
| 🐍 **Python** | Core programming language |
| 🔗 **LangChain** | Framework for managing and chaining LLM calls |
| 🤗 **Hugging Face** | Source for pre-trained models used in chains |

---

## ⚡ How It Works

1. Define prompt templates for each chain.  
2. Initialize LLMs using Hugging Face models.  
3. Create chain objects (Simple, Sequential, Parallel, Conditional).  
4. Pass input text through the chain and get structured output.  

---

## 📊 Example Flow

| Chain Type | Description | Example Output |
|-------------|--------------|----------------|
| Simple Chain | One-step LLM response | “LangChain simplifies LLM workflows.” |
| Sequential Chain | Multi-step reasoning | Reformulates question → generates → summarizes |
| Parallel Chain | Multi-output | Returns explanation, keywords, and title |
| Conditional Chain | Branch-based logic | Chooses QA or Translation pipeline |

---

## 💡 Learning Highlights

- 🔍 Understood **data flow** between prompt, LLM, and parser.  
- 🧩 Learned how to **combine and control** multiple chains.  
- ⚙️ Experimented with **dynamic and parallel reasoning**.  
- 🧠 Gained deeper insight into **LangChain’s modular design**.

---

## 🧪 Run It Yourself

Clone the repository and run the examples:

```bash
git clone https://github.com/yourusername/langchain-chains-demo.git
cd langchain-chains-demo
pip install -r requirements.txt
python main.py
