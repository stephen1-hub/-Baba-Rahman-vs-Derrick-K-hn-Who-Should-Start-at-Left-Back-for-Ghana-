# 🇬🇭 Baba Rahman vs Derrick Köhn: Who Should Start at Left-Back for Ghana?

A football analytics project comparing the 2025/26 club performances of Ghanaian left-backs Baba Rahman and Derrick Köhn to evaluate who has the stronger statistical case to start for the Black Stars.

---

## 📌 Project Objective

The Ghana national team has two strong left-back options:

* Baba Rahman (PAOK)
* Derrick Köhn (Union Berlin)

This project uses club performance data to move beyond fan opinions and answer a simple question:

> Based on the data, who should start at left-back for Ghana?

---
## 🚀 Live Dashboard

🔗 https://kjhmfhmpunakexxpfmzsaa.streamlit.app/

## 📊 Data Sources

Data was collected from:

* FBref
* FotMob

Metrics included:

### Attacking

* Goals
* Assists
* Expected Goals (xG)
* Expected Assists (xA)
* Chances Created
* Successful Crosses

### Possession

* Pass Accuracy
* Dribbles
* Duels Won
* Aerial Duels Won
* Touches
* Ball Retention

### Defensive

* Tackles
* Interceptions
* Recoveries
* Clearances
* Defensive Contributions
* Clean Sheets

### Discipline

* Yellow Cards
* Red Cards

---

## ⚙️ Methodology

The comparison was divided into four key areas:

### 1. Attacking Output

Evaluated:

* Goals
* Assists
* xG
* xA
* Chance Creation

### 2. Possession & Ball Security

Evaluated:

* Pass Accuracy
* Duel Success
* Aerial Success
* Dispossessions

### 3. Defensive Performance

Evaluated:

* Tackles
* Interceptions
* Recoveries
* Clearances

### 4. Discipline

Evaluated:

* Yellow Cards
* Red Cards

---

## 📈 Dashboard Features

The Streamlit dashboard includes:

* Player Overview
* Attacking Comparison
* Defensive Comparison
* Possession Analysis
* Discipline Analysis
* Radar Chart
* Left-Back Readiness Index
* Final Analyst Verdict
---

## 🔍 Key Findings

### Baba Rahman

Strengths:

* Higher goal contribution output
* Better discipline
* Better aerial presence
* Stronger possession security
* More interceptions
* More clearances
* Europa League experience

### Derrick Köhn

Strengths:

* Higher expected assists (xA)
* More chances created
* Better crossing volume
* Strong Bundesliga competition level
* Greater creative involvement

---
## 🧮 Readiness Index Model

The final Readiness Index was calculated using a weighted scoring model:

- Attack: 30%
- Defense: 35%
- Possession: 25%
- Discipline: 10%

Category scores were generated using per-90 metrics and normalized for comparison.

This weighting reflects the responsibilities of a modern full-back, where defensive contribution remains the primary role while still rewarding attacking involvement and ball progression.

## 🏆 Final Verdict

The analysis reveals two distinct left-back profiles.

### Baba Rahman

Strengths:

- Better defensive balance
- Better possession security
- Better discipline
- Stronger aerial presence
- More interceptions and clearances
- Proven European experience with PAOK

### Derrick Köhn

Strengths:

- Superior attacking output
- Higher expected assists (xA)
- More chances created
- Greater crossing threat
- More creative involvement in the final third
- Regular Bundesliga experience

The Readiness Index combines attacking contribution, creativity, defensive performance, possession impact, and discipline into a single weighted score.

### Readiness Index

| Player | Score |
|----------|----------:|
| Derrick Köhn | 93.4 |
| Baba Rahman | 86.3 |

### Analyst Conclusion

The model identifies Derrick Köhn as the highest-rated left-back due to his superior attacking and creative output.

However, Baba Rahman remains the stronger defensive and possession-oriented option.

The decision ultimately depends on Ghana's tactical priorities:

- Need more creativity and attacking width? → Derrick Köhn
- Need greater defensive stability and control? → Baba Rahman

Rather than proving one player is objectively better, the analysis highlights how each player offers a different solution for the Black Stars.

## 🛠️ Tech Stack

* Python
* Pandas
* Streamlit
* Plotly
* PIL

---

## 📷 Dashboard Preview

<img width="1591" height="773" alt="image" src="https://github.com/user-attachments/assets/e4173d92-a88a-4c65-bdfa-a0b8cb66edc6" />



```

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📬 Author

Stephen Yaw Ayamah

Football Data Analyst | Python | Streamlit | Football Analytics

- GitHub: https://github.com/stephen1-hub
- LinkedIn: https://www.linkedin.com/in/ayamah-stephen

GitHub: https://github.com/stephen1-hub/
LinkedIn: www.linkedin.com/in/ayamah-stephen


