# EthioMart-Amharic-Entity-Recognition

## Project Overview

EthioMart aims to revolutionize e-commerce in Ethiopia by becoming the primary hub for Telegram-based transactions. With the growing use of Telegram for business, this project addresses the challenge of decentralization by consolidating real-time data from multiple e-commerce Telegram channels into a unified platform. 

This system fine-tunes large language models (LLMs) for Amharic Named Entity Recognition (NER) to extract crucial business entities like product names, prices, and locations from text, images, and documents. The extracted data populates EthioMart's centralized database, creating a seamless experience for vendors and customers.

---

## Key Features
- **Real-Time Data Extraction:** Automated scraping of messages, images, and documents from multiple Telegram channels.
- **Amharic Named Entity Recognition (NER):** Fine-tuned models to extract entities like products, prices, and locations.
- **Data Centralization:** Unified repository for all extracted e-commerce data.
- **Model Comparison & Interpretability:** Performance analysis using metrics and interpretability tools like SHAP and LIME.

---

## Repository Structure
```
EthioMart-Amharic-Entity-Recognition/
├── data/                # Raw and preprocessed datasets
├── models/              # Fine-tuned NER models
├── scripts/             # Data scraping and processing scripts
├── notebooks/           # Jupyter notebooks for model training and evaluation
├── results/             # Model evaluation metrics and interpretability reports
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── LICENSE              # Licensing information
```

---

## Getting Started

### Prerequisites
- **Python 3.8+**
- Libraries: Install dependencies using `pip install -r requirements.txt`.
- Access to Telegram API for data scraping.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/EthioMart-Amharic-Entity-Recognition.git
   cd EthioMart-Amharic-Entity-Recognition
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Telegram API credentials in a `.env` file:
   ```
   TELEGRAM_API_ID=your_api_id
   TELEGRAM_API_HASH=your_api_hash
   ```

### Usage

#### 1. Data Ingestion
- Run the data scraper to collect messages from specified Telegram channels:
  ```bash
  python scripts/data_scraper.py --channels @qnashcom @Fashiontera @kuruwear @gebeyaadama @MerttEka @forfreemarket @classybrands
  ```

#### 2. Data Preprocessing
- Tokenize, normalize, and clean the scraped data:
  ```bash
  python scripts/preprocess_data.py
  ```

#### 3. Model Fine-Tuning
- Fine-tune the NER model using the labeled dataset:
  ```bash
  python scripts/train_ner_model.py
  ```

#### 4. Evaluation and Comparison
- Evaluate and compare model performance:
  ```bash
  python scripts/evaluate_models.py
  ```

#### 5. Model Interpretability
- Generate interpretability reports:
  ```bash
  python scripts/model_interpretability.py
  ```

---

## Key Objectives

### Task 1: Data Ingestion and Preprocessing
- Scrape data from Telegram channels.
- Preprocess and structure the data for entity extraction.

### Task 2: Label Dataset in CoNLL Format
- Label entities like product names, prices, and locations in Amharic text.
- Save labeled data in CoNLL format.

### Task 3: Fine-Tune NER Model
- Fine-tune pre-trained models such as XLM-Roberta or AfroXLMR for Amharic NER tasks.

### Task 4: Model Comparison and Selection
- Compare models based on metrics such as F1-score, precision, and recall.

### Task 5: Model Interpretability
- Use SHAP and LIME to explain model predictions.

---

## Future Improvements
- Expand support for multimodal data (e.g., image and text integration).
- Incorporate more Telegram channels to enhance data diversity.
- Deploy the NER model as an API for real-time usage.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- [Hugging Face](https://huggingface.co/) for pre-trained models and tools.
- Telegram API for enabling real-time data scraping.
- The Ethiopian e-commerce community for inspiration and data.
