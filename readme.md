# PyTorch Workshop @MBUST

This repository was created for a **PyTorch workshop for AI/DS Graduate Students at MBUST, Chitlang**.

It provides a clean, research-grade PyTorch project structure for deep learning experiments, reproducibility, and modular development.

---

## 🎯 Objective

The goal of this template is to teach:

- Research-grade PyTorch project structure
- Reproducible machine learning experiments
- Separation of concerns in ML codebases
- Configuration-driven development using YAML
- Proper use of scripts, notebooks, and source code
- Industry-style ML project organization

---

## 🚀 How to Run Training

After setting up the environment, run training using:

```bash
python scripts/train.py
```

## ⚙️ Configuration

All experiments are controlled via:

```bash
config/experiment.yaml
```

## 📓 Notebooks

Used for:
- Data exploration
- Visualization
- Error analysis
(Not for training code)

## 🔁 Reproducibility
 - Fixed seeds
 - YAML configs
 - Modular design

## 📦 Notes for Students
- Do NOT write all code in one file
- Do NOT hardcode hyperparameters & Always use configuration files
- Keep training code separate from model code
- Use notebooks only for analysis and visualization



## Student Submission — Rupesh Maharjan

### Dataset: Flowers Recognition.

# PyTorch Data Pipeline — Flowers Recognition

## Dataset
The dataset used for this assignment is the Flowers Recognition dataset downloaded 
from Kaggle. It contains 4317 images organized into 5 classes: daisy, dandelion, 
rose, sunflower, and tulip. Each class is stored in its own folder, which allowed 
the custom Dataset class to automatically discover and label them without any 
hardcoding.

## Challenges Faced
The most challenging part of this assignment was working inside a cloned repository 
for the first time. Understanding the project structure and knowing where to write 
code was difficult at first, but gradually made sense as I worked through each file. 
One specific issue I faced was forgetting to place the dataset inside the train/ 
folder, which caused the Dataset to detect the wrong folder structure and find 0 
images. This was fixed by reorganizing the folders correctly and updating the path 
in the code.

## Dataset vs DataLoader
The way I understand it, the Dataset class is like a file management system — it 
organizes all the images in order so that any single image can be retrieved quickly 
and efficiently when needed. The DataLoader on the other hand is like deciding how 
much of that data you want to feed at a time during training — it controls the batch 
size, shuffles the data randomly each epoch, and handles loading in the background 
so training runs smoothly.

## Setup Instructions
1. Clone the repository
2. Run: conda env create -f environment.yaml
3. Run: conda activate dl-workshop
4. Download Flowers Recognition dataset from Kaggle
5. Place it in raw_data/flowers/train/
6. Open notebooks/data_pipeline.ipynb and run all cells