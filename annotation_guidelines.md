
---

# 📄 2. `annotation_guidelines.md`

```markdown
# Annotation Guidelines – Vehicle Detection Dataset

## 📌 Purpose
These guidelines ensure consistent and high-quality annotations for training an object detection model.

---

## 🎯 Classes

| Class Name   | Description |
|-------------|------------|
| bus         | Large passenger vehicles used for public transport |
| car         | Standard passenger vehicles (including vans and SUVs) |
| motorcycle  | Two-wheeled motor vehicles including sport bikes, scooters, and cruisers, observed in both stationary and riding conditions |
| truck       | Vehicles primarily designed for transporting goods, including small delivery trucks, large cargo trucks, and semi-trailer trucks |

---

## 📦 General Rules

### 1. Label All Relevant Objects
- Every visible object belonging to the defined classes must be annotated.
- Multiple objects in one image must each have a bounding box.

---

### 2. Bounding Box Rules

✔ Draw tight bounding boxes around objects  
✔ Include only the object (no excessive background)  
✔ Use rectangular (axis-aligned) boxes only  

❌ Do not draw rotated boxes  
❌ Do not include large empty space  

---

### 3. Partially Visible Objects

✔ Annotate if the object is clearly recognizable  
✔ Draw the box around the visible portion only  

❌ Do not guess hidden parts  

---

### 4. Occlusion Handling

- If an object is partially blocked:
  - Still annotate it if identifiable
  - Keep bounding box tight around visible area

---

### 5. Small Objects

✔ Annotate if clearly identifiable  
❌ Skip if too small or unclear  

---

### 6. Special Cases

#### Vehicles with People
- Annotate only the vehicle  
- Do NOT include the person in the bounding box  

---

#### Vans
- Always labeled as **car** for consistency  

---

#### Large Close-up Objects
- Include them
- Ensure bounding box covers entire visible object

---

### 7. Consistency Rules

- Always use the same class for similar objects
- Do not switch labeling between classes
- Maintain uniform annotation style across dataset

---

### 8. What NOT to Annotate

- Objects outside defined classes
- Unclear or ambiguous objects
- Extremely small or indistinguishable objects

---

## ⚠️ Common Mistakes to Avoid

- Missing objects in crowded scenes
- Incorrect class labeling
- Loose or oversized bounding boxes
- Inconsistent labeling of similar objects
- Including humans inside vehicle boxes

---

## ✅ Final Check Before Submission

- Each image has a label file
- All objects are labeled correctly
- Bounding boxes are tight and accurate
- Class labels are consistent

---

## 🎯 Goal

Ensure high-quality annotations to improve:
- Model accuracy
- Generalization
- Evaluation metrics (Precision, Recall, mAP)