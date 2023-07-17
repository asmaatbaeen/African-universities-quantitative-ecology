# African Universities and Quantitative Ecology Programs

This repository contains notebooks focused on obtaining a comprehensive list of universities in Africa and analyzing the current state of environmental and quantitative ecology programs on the continent.

## Objective:
The primary objective of this project is to compare and evaluate the current situation of quantitative ecology programs in Africa. By collecting data on universities and their environmental and quantitative ecology programs.


## Getting Started:
To manage the project dependencies, Poetry is used. If you haven't installed Poetry yet, please install it first. Then, follow these steps to set up the project and install the necessary dependencies:

```
$ poetry shell    # Activate the virtual environment
$ poetry install  # Install dependencies
```

# Dataset Used:
using data from two different sources:

    1. local parquet file: This file contains university information, including name, country, longitude, and latitude. The data was scraped from Google.
    
    2. [universities library](https://pypi.org/project/universities/): This library provides access to a vast collection of global universities information. 

## Scripts:
The `scripts` directory contains a script that is used to make the plots in the notebook based on the presented data.

## Notebooks:
The `notebook` folder contain the following:

1. **all_african_universities**: This notebook aims to compile a list of universities in Africa, including relevant details such as names, locations, and additional information. Please note that this list may not be exhaustive, as it is based on available data sources.

2. **environmental_ecology_programs**: This notebook focuses on exploring environmental ecology programs offered by African universities. The data presented in this notebook is gathered through Google searches using these specific keywords: top 20 environmental ecology programs in Africa and the top 20 ecology programs in Africa.

3. **quantitative_statistical_ecology_programs**: This notebook is specifically dedicated to quantitative statistical ecology programs in Africa. The data presented in this notebook is obtained through Google searches using these specific keywords: top 20 quantitative statistical ecology programs in Africa and the top 20 statistical ecology programs in Africa.


## Results and Analysis:
The notebook contains the results of the analysis, including any generated graphs. There is an option to save these results for further use or reference.

Please refer to the notebook and the provided scripts for more detailed information on running the code and exploring the results.