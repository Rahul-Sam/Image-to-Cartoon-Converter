# Image-to-Cartoon-Converter
---

#  Introduction

Image to Cartoon Converter is a computer vision project that transforms a normal image into a cartoon-style image using image processing techniques.

The system applies:

* Grayscale conversion
* Noise reduction
* Edge detection
* Color smoothing (bilateral filtering)

The result looks like a cartoon drawing.

---

#  Objective

* Convert real images into cartoon-style images
* Understand image processing fundamentals
* Implement OpenCV filters and edge detection
* Display original and cartoon output

---

#  Technologies Used

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Programming language |
| OpenCV     | Image processing     |
| NumPy      | Numerical operations |
| Matplotlib | Display images       |

---

#  Working Principle

### Step 1: Load Image

Read input image using OpenCV.

### Step 2: Convert to Grayscale

Reduces image complexity.

### Step 3: Apply Median Blur

Removes noise while preserving edges.

### Step 4: Edge Detection

Use Adaptive Thresholding to detect cartoon-like edges.

### Step 5: Apply Bilateral Filter

Smooths colors while keeping edges sharp.

### Step 6: Combine Edges + Color Image

Final cartoon output generated.

---

#  Project Structure

```
image_to_cartoon/
│
├── input.jpg
├── cartoon_converter.py
```

---

#  How To Run

### Install Requirements

```bash
pip install opencv-python numpy matplotlib
```

### Run Program

```bash
python cartoon_converter.py
```

#  Output

The program will display:

* Original Image
* Cartoon Converted Image

---

#  Algorithm Explanation

## Adaptive Thresholding

Used to detect strong edges.

## Bilateral Filtering

Unlike normal blur, it:

* Smooths colors
* Preserves edges

This creates the cartoon-style look.

---

#  Applications

* Social media filters
* Photo editing apps
* Entertainment apps
* Art transformation tools
* Preprocessing for animation software

---

#  Advantages

* Simple implementation
* Fast processing
* Works on most images
* No deep learning required

---

#  Limitations

* Not true AI-based cartoonization
* Works best on high-quality images
* May fail on very complex backgrounds

---

#  Future Enhancements

* Add GUI using Tkinter
* Add webcam live cartoon filter
* Convert to web application (Flask)
* Use Deep Learning for advanced cartoon effect
* Add download/save option

---

# Conclusion

This project demonstrates how basic image processing techniques can transform real-world images into cartoon-style images. It uses OpenCV filtering and edge detection to create a visually appealing effect efficiently.



