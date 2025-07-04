
# Feistiness Analysis with Apache Spark  
*Big Data Project | Hadoop · Spark · HDFS · Python*

## Overview

This project implements a scalable data pipeline using Apache Spark and Hadoop to calculate custom "feistiness" scores for Pokémon based on their attributes. The pipeline identifies the feistiest Pokémon in each Type 1 category and outputs the results to HDFS in CSV format.

The project demonstrates distributed data processing using Spark's DataFrame API with seamless HDFS integration.

---

## Tech Stack

- **Apache Spark** 3.5.5  
- **Hadoop** 3.4.0 (pseudo-distributed mode)  
- **HDFS** for distributed storage  
- **Python** 3.9.6 (PySpark)  
- **macOS** (ARM-64, Apple M1)

---

## Features

✔ Distributed data processing using Spark  
✔ Integration with Hadoop HDFS for input and output  
✔ Custom feistiness metric calculation  
✔ Robust data validation (handles null/zero values)  
✔ Clean CSV output ready for downstream analysis  

---

## Project Structure

```
.
├── pokemon_spark.py       # Spark job for feistiness calculation
├── pokemon.csv            # Input dataset (example)
└── README.md              # Project documentation
```

---

## Setup Instructions

### Prerequisites

- Hadoop and Spark installed  
- Hadoop configurations properly set (HDFS, YARN)  
- `pokemon.csv` and `pokemon_spark.py` in the project directory  

### Steps

1. **Start Hadoop services:**

```bash
start-all.sh
jps  # Confirm services: Namenode, Datanode, ResourceManager, etc.
```

2. **Create HDFS directory and upload dataset:**

```bash
hdfs dfs -mkdir /pokemon
hdfs dfs -put pokemon.csv /pokemon
```

3. **Run the Spark job:**

```bash
spark-submit --master yarn pokemon_spark.py
```

4. **Copy output CSV from HDFS to local storage:**

```bash
hdfs dfs -copyToLocal /pokemon/pokemon_output.csv /path/to/local/storage
```

---

## Key Implementation Details

- Uses Spark DataFrame API for concise, efficient processing  
- Handles missing/invalid weight values to avoid division errors  
- Processes all Pokémon, even with missing Type 2 information  
- Drops unnecessary columns before output to simplify results  

---

## License

This project is for academic and learning purposes.

---

## Author

Digvijay Jondhale
