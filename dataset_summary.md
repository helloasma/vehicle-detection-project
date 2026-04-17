# Dataset Summary – Vehicle Object Detection

## 📌 Overview
This dataset was created for a Computer Vision Object Detection project using YOLOv8. The goal is to detect different types of vehicles in real-world campus environments.

---

## 🎯 Classes
The dataset includes 4 object classes:

| Class ID | Class Name   |
|----------|-------------|
| 0        | bus         |
| 1        | car         |
| 2        | motorcycle  |
| 3        | truck       |

---

## 📊 Dataset Size

| Split | Number of Images |
|------|-----------------|
| Train | 714 |
| Validation | 80 |
| Test | 80 |
| **Total** | **874** |

---

## 📊 Dataset Split

The dataset was divided into three subsets:

- Training set: 81.8% (714 images)
- Validation set: 9.1% (80 images)
- Test set: 9.1% (80 images)

The split was performed manually to ensure balanced distribution across all classes.

---

## 📁 Dataset Structure
DATASET/
├── train/
│ ├── images/
│ └── labels/
├── val/
│ ├── images/
│ └── labels/
├── test/
│ ├── images/
│ └── labels/
├── data.yaml


---

## 📷 Data Collection

- Images were collected from multiple publicly available datasets.
- The selection process focused on:
  - Different lighting conditions (day/night)
  - Various angles and perspectives
  - Different object sizes and distances
- Only relevant vehicle classes (bus, car, motorcycle, truck) were included.

---

## 🏷️ Annotation Details

- Annotation format: **YOLO format**
- Bounding boxes are:
  - Axis-aligned (rectangular)
  - Normalized (values between 0 and 1)
- Each image has a corresponding `.txt` file.

---

## ⚖️ Ethical Considerations

- Efforts were made to minimize the presence of identifiable faces and license plates.
- Due to the nature of publicly available datasets, some images may still contain:
  - partially visible faces
  - vehicles with visible license plates
- To reduce ethical concerns:
  - preference was given to images where faces are not clearly visible
  - for motorcycle images, riders wearing helmets were prioritized
- No personal data was intentionally collected or used.

---

## ⚠️ Notes

- Dataset was curated to balance quality, diversity, and ethical considerations.
- Some limitations remain due to reliance on external datasets.

---

## 🚀 Usage

This dataset is ready for training using YOLOv8:

```bash
yolo detect train data=data.yaml model=yolov8n.pt