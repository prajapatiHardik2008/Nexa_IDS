# Nexa_IDS
# Nexa IDS (Intrusion Detection System) 🛡️

Nexa IDS is a Python-based network security tool designed to capture live traffic, analyze packet patterns, and provide AI-generated security reports.

## 🚀 Features
- **Live Packet Sniffing:** Uses Scapy to monitor network interfaces in real-time.
- **Automated Logging:** Saves traffic data (IPs, Ports, Protocols, Length) into structured CSV files.
- **AI-Powered Analysis:** Integrates with OpenAI models via Pollinations AI to generate SOC Analyst reports.
- **Data Persistence:** Moves temporary logs to a Master Dataset for future Machine Learning training.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Scapy, Pandas, Requests
- **Analysis:** OpenAI (via Pollinations API)

## 📁 Project Structure
- `main.py`: The entry point for the sniffer.
- `engine/analyzer.py`: Logic for packet parsing.
- `engine/ai_model.py`: AI integration and log processing.
- `logs/`: Directory for stored traffic data.

## 📝 How to Use
1. Clone the repository:
   ```bash
   git clone [https://github.com/prajapatiHardik2008/Nexa_IDS.git](https://github.com/prajapatiHardik2008/Nexa_IDS.git)
