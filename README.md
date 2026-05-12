# AI-Based Smart Campus Vehicle Detection System
**Course:** BCS407 – Artificial Intelligence | Canadian University Dubai

---

## Project Overview

This repository contains all work for a two-part YOLOv8-based vehicle detection project for a smart campus environment. The system detects four vehicle classes: **bus, car, motorcycle, and truck**.

- **Part 1** – Dataset preparation, baseline model training (YOLOv8n), and evaluation
- **Part 2** – Model improvement through four experiments: backbone upgrade (YOLOv8m), dataset expansion with a second Roboflow source, a combined final model, and a SAHI sliced-inference ablation

---

## Repository Structure

```
vehicle-detection-project/
│
├── README.md                          ← You are here
├── data.yaml                          ← Dataset configuration (classes, paths)
├── annotation_guidelines.md           ← Labelling rules and ethics constraints
├── dataset_summary.md                 ← Dataset statistics and class distribution
├── qc_report.md                       ← Quality control report for annotations
│
├── train/                             ← Training split (714 images + labels)
│   ├── images/
│   └── labels/
│
├── val/                               ← Validation split (80 images + labels)
│   ├── images/
│   └── labels/
│
├── test/                              ← Test split (80 images + labels)
│   ├── images/
│   └── labels/
│
├── scripts/                           ← Part 1 pipeline (3 phases)
│   ├── README.md
│   │
│   ├── part1_dataset_preparation/     ← Phase 1: Dataset setup
│   │   ├── step1_changetype.py        ← Convert image formats
│   │   ├── step2_rename.py            ← Rename images consistently
│   │   └── step3_split.py             ← Split into train/val/test
│   │
│   ├── part2_training/                ← Phase 2: Baseline model training
│   │   ├── train_yolov8.ipynb         ← YOLOv8n training notebook (Colab)
│   │   ├── best.pt                    ← Baseline trained weights (YOLOv8n, 50 epochs)
│   │   ├── training_results.png       ← Loss and mAP curves
│   │   └── sample_predictions.png     ← Sample predictions on validation set
│   │
│   └── part3_evaluation/              ← Phase 3: Baseline evaluation
│       ├── part3_evaluation_pipeline.ipynb
│       ├── confusion_matrix.png
│       ├── metrics_bar_chart.png
│       ├── pr_curve.png
│       ├── performance_summary_table.png
│       ├── overall_metrics.csv        ← Overall P, R, mAP scores
│       └── per_class_metrics.csv      ← Per-class metric breakdown
│
└── project_part2/                     ← Part 2: Model improvement
    ├── vehicle_detection_pipeline.ipynb     ← Full training + evaluation pipeline
    └── vehicle_detection_eval_only.ipynb    ← Evaluation only (no GPU/training needed)
```

---

## Dataset

### Part 1 – Original Dataset (manually curated)

| Split | Images |
|-------|--------|
| Train | 714 |
| Val | 80 |
| Test | 80 |
| **Total** | **874** |

Images were collected manually from multiple publicly available sources, focusing on varied lighting conditions, angles, and object sizes. Labels are in YOLO format (normalised bounding box coordinates). See `annotation_guidelines.md` for labelling rules and `qc_report.md` for quality control details.

### Part 2 – Expanded Dataset (used in Experiments 2 and Final model)

For the dataset expansion experiment, a second dataset was downloaded from Roboflow and merged with the original:

- **Source:** [Vehicles dataset – traffic-camera workspace on Roboflow](https://roboflow.com/), project `vehicles-22g3b`, version 7
- **Class mapping:** Roboflow class names were matched dynamically to our 4 target classes (`bus`, `car`, `motorcycle`, `truck`). Images whose labels contained no matching classes after remapping were discarded.
- **Balancing:** To prevent the model being dominated by distant traffic-camera shots (the Roboflow pool is much larger), the expanded dataset was **balanced**: each split was built so that the number of original images and sampled Roboflow images are equal. Final dataset size is approximately 2× the original per split.
- **Ethics:** Newly added images follow the same ethical constraints as the original dataset.

**Classes:** `0: bus` · `1: car` · `2: motorcycle` · `3: truck`

---

## Part 1 – Baseline Model

**Model:** YOLOv8n, fine-tuned from pretrained COCO weights  
**Epochs:** 50 | **Image size:** 640×640 | **Batch size:** 16 | **Patience:** 10  
**Dataset:** Original 874-image dataset

See `scripts/part3_evaluation/overall_metrics.csv` and `per_class_metrics.csv` for baseline results.

### Reproduce Part 1

1. Run `scripts/part1_dataset_preparation/step1_changetype.py`
2. Run `scripts/part1_dataset_preparation/step2_rename.py`
3. Run `scripts/part1_dataset_preparation/step3_split.py`
4. Open `scripts/part2_training/train_yolov8.ipynb` in Google Colab (GPU runtime) and run all cells
5. Open `scripts/part3_evaluation/part3_evaluation_pipeline.ipynb` in Colab and run all cells

---

## Part 2 – Improvement Experiments

Four experiments were run and compared against the Part 1 baseline. All training used **50 epochs, batch 16, image size 640×640, seed 42**.

| # | Run name | Model | Dataset | Purpose |
|---|----------|-------|---------|---------|
| Baseline | `yolov8n_vehicle` | YOLOv8n | Original | Reference (Part 1 re-evaluated) |
| Exp 1 | `yolov8m_exp1` | YOLOv8m | Original | Larger backbone only |
| Exp 2 | `yolov8n_expanded` | YOLOv8n | Balanced expanded | More diverse data only |
| **Final** | `yolov8m_final` | **YOLOv8m** | **Balanced expanded** | **Both improvements combined** |
| Ablation | Final + SAHI | YOLOv8m | Expanded test set | Sliced inference (no retraining) |

**SAHI (Sliced Aided Hyper Inference)** is an inference-time technique applied on top of the Final model weights — it does not involve any additional training. It tiles each test image into overlapping patches, runs inference per patch, then merges predictions. It is evaluated as a separate ablation to assess its effect on small/distant objects.

**Recommended model:** `Final (YOLOv8m on the balanced expanded dataset)` — best performance on the expanded test set across all metrics. This is the model deployed to HuggingFace.

### Reproduce Part 2

**Full pipeline (GPU required):**
1. Open `project_part2/vehicle_detection_pipeline.ipynb` in Google Colab
2. Connect to a GPU runtime: Runtime → Change runtime type → T4 GPU
3. Upload the original dataset to Google Drive at `MyDrive/vehicle_detection/vehicle-detection-project/`
4. Run all cells — the notebook handles installation, Roboflow download, balanced dataset construction, all four training runs, evaluation, cross-experiment comparison, and SAHI ablation

**Evaluation only (no GPU or retraining needed):**
1. Open `project_part2/vehicle_detection_eval_only.ipynb` in Google Colab
2. Ensure the four trained weight files already exist on your Drive (see Cell 9 for expected paths)
3. Run all cells — reproduces the full evaluation pipeline including SAHI without any training

### Environment

| Dependency | Notes |
|------------|-------|
| Python 3.10+ | |
| ultralytics 8.x | YOLOv8 training and evaluation |
| roboflow | Dataset download (Exp 2 and Final) |
| sahi | Sliced inference ablation |
| torch 2.x | CUDA GPU recommended for training |
| Google Colab | GPU runtime for training; CPU runtime sufficient for eval-only |

---

## Ethical Constraints

- No identifiable human faces in any image (original or Roboflow-sourced)
- No visible license plates intentionally included
- No personal or location-identifying data
- Motorcycle images with helmeted riders were prioritised where possible
- All constraints apply equally to the original dataset and the Roboflow expansion

---

## Live Demo

**[https://huggingface.co/spaces/helloasma/vehicle-detection](https://huggingface.co/spaces/helloasma/vehicle-detection)**

Upload any vehicle image — the Final model returns bounding box predictions with class labels and confidence scores.
