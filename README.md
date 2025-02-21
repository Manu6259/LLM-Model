# GenAI Application for Food Access: Donor and Distribution Management Tool

## Overview

This project aims to streamline **donation tracking, donor engagement, and outreach management** using **generative AI**. The application leverages **LLM-powered insights** to facilitate real-time donation tracking, automate donor communication, and provide data-driven outreach recommendations.

## Features

### 1. **Donor Management Interface**
   - Records new donations and updates donor information.
   - Detects **repeat donors** and acknowledges them accordingly.
   - Generates **automated thank-you messages** for donors.
   - Provides **summary statistics** (total donations, average donation, unique donors).

### 2. **Outreach Management**
   - Enables **natural language querying** of food demand data.
   - Provides insights into **regional outreach** activities.
   - Assists in **strategic allocation** of food distribution.

### 3. **AI-Powered Insights**
   - Uses **LangChain agents** for querying donor and outreach data.
   - Generates personalized **thank-you emails** based on donation impact.
   - Supports **real-time monitoring** of donor and outreach trends.

---

## File Structure

| File | Description |
|------|------------|
| `donor_interface.py` | Handles donor submissions, tracks donations, and generates thank-you messages. |
| `user_interface.py` | Monitors donation data, provides query-based insights, and generates impact-based messages. |
| `outreach.py` | Analyzes outreach demand data using LLM queries. |
| `data_generator.ipynb` | Generates simulated donor and outreach data for testing. |
| `donor_data.csv` | Stores donor information, including names, emails, and donation amounts. |
| `distribution_data.csv` | Contains food distribution records for outreach planning. |
| `food_demand_data.csv` | Provides food demand statistics for different regions. |
| `simulated_outreach_demand_data.csv` | Sample dataset for testing the outreach module. |

---

## Installation & Setup

### **Prerequisites**
- Python 3.8+
- Streamlit
- Pandas
- Matplotlib
- LangChain
- OpenAI API key

### **Installation**
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up the **OpenAI API Key**:
   ```sh
   export OPENAI_API_KEY="your-api-key"
   ```

---

## Usage

### **Run Donor Management Interface**
```sh
streamlit run donor_interface.py
```

### **Run Outreach Insights Interface**
```sh
streamlit run outreach.py
```

### **Run User Tracking and Query Interface**
```sh
streamlit run user_interface.py
```

---

## Expected Outcomes

- **Improved Donor Engagement**: Automated thank-you messages for personalized acknowledgment.
- **Efficient Operations**: AI-driven donation tracking reduces manual efforts.
- **Data-Driven Decisions**: Natural language queries provide actionable insights for outreach planning.
- **Scalable & Adaptable**: Easily integrates new data sources and organizational needs.

---

## Contributors

- **Manu Jain** (Simon Business School)

---

## Future Enhancements
- Implement **real-time dashboards** for donor engagement tracking.
- Enhance **predictive analytics** for food demand forecasting.
- Improve **security measures** for donor data privacy.

---

## License
This project is licensed under the MIT License.

