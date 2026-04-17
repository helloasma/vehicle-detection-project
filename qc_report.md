# Quality Control Report (QC Report)

## 📌 Overview
This report summarizes the quality control process applied to the vehicle detection dataset to ensure consistency, correctness, and usability for training a YOLOv8 model.

---

## ✅ Dataset Structure Verification

- Verified correct folder structure:
  - train/images, train/labels
  - val/images, val/labels
  - test/images, test/labels
- Ensured each image has a corresponding label file

---

## 📊 Data Consistency Checks

- Confirmed equal number of images and labels in each split:
  - Train: 714 images / 714 labels
  - Validation: 80 images / 80 labels
  - Test: 80 images / 80 labels

---

## 🏷️ Label Format Validation

- Verified all label files follow YOLO format:
  - class_id x_center y_center width height
- Checked that:
  - class IDs are within valid range (0–3)
  - bounding box values are normalized (0 to 1)

---

## 🔍 Annotation Quality Review

- Manually inspected a subset of images to ensure:
  - bounding boxes are tight and accurate
  - correct class labels are assigned
  - all visible objects are annotated
- Verified consistency across similar object types

---

## ⚠️ Issues Identified & Fixes

- Duplicate images across splits → fixed by re-splitting dataset
- Incorrect class indexing due to deleted class → fixed by regenerating dataset in Roboflow
- Minor upload inconsistencies → resolved by re-uploading missing images

---

## ⚖️ Ethical Considerations Review

- Attempted to minimize images with:
  - identifiable faces
  - visible license plates
- Preference given to:
  - helmeted motorcycle riders
- Acknowledged that some images may still contain such elements due to source dataset limitations

---

## ✅ Final Status

- Dataset is clean, consistent, and ready for training
- All annotations verified and aligned with YOLOv8 requirements