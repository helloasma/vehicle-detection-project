# Scripts Overview

This folder contains scripts organized by project stages:

## Part 1 – Dataset Preparation
- step1_changetype.py → converts image formats
- step2_rename.py → renames images consistently
- step3_split.py → splits dataset into train/val/test

## Part 2 – Model Training
- train_yolov8.ipynb → full YOLOv8n training notebook (Google Colab)
- best.pt → trained model weights (YOLOv8n, 50 epochs)
- training_results.png → loss and mAP curves across epochs
- sample_predictions.png → sample bounding box predictions on validation images

## Part 3 – Evaluation & Pipeline
- part3_evaluation_pipeline.ipynb → full evaluation and demo notebook (Google Colab)
- confusion_matrix.png → per-class confusion matrix (raw and normalised)
- metrics_bar_chart.png → precision, recall, AP@0.5 per class
- pr_curve.png → precision-recall curve per class
- performance_summary_table.png → overall test set results summary
- overall_metrics.csv → overall precision, recall, mAP scores
- per_class_metrics.csv → per-class breakdown of all metrics
