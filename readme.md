#  AI Image Generator

An AI-powered web application that generates images from natural language text prompts.

The project allows users to enter a description such as *"A futuristic city at night with glowing buildings"* and automatically generates a corresponding image using a pretrained diffusion model.

The application is built using **Python, Streamlit, Hugging Face Diffusers, and Stable Diffusion Turbo**.

---

##  About the Project

The **AI Image Generator** is a text-to-image generation application.

Instead of manually creating an image, the user simply provides a text description called a **prompt**. The application sends this prompt through an AI image-generation pipeline, which uses a diffusion model to create a new image based on the description.

### Example

**Input Prompt:**

> A futuristic city at night with glowing buildings, neon lights, cinematic atmosphere

**Output:**

A generated futuristic city image with buildings, lights, and a night-time atmosphere.

---

##  Purpose of the Project

The main purpose of this project is to understand how modern **Generative AI** systems can convert natural language into visual content.

This project demonstrates:

- Text-to-image generation
- Diffusion models
- Hugging Face pretrained models
- AI pipelines
- Python-based AI application development
- Streamlit web application development
- Prompt-based image generation

---

##  Features

-  Enter a text prompt
-  Generate images using AI
-  Text-to-image generation
-  Fast image generation using Stable Diffusion Turbo
-  Simple and user-friendly Streamlit interface
-  Generate different images using different prompts
-  Display the generated image directly in the application

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Main programming language |
| **Streamlit** | Creates the web interface |
| **Hugging Face Diffusers** | Provides tools for diffusion-based image generation |
| **AutoPipelineForText2Image** | Automatically creates the text-to-image pipeline |
| **Stable Diffusion Turbo** | AI model used to generate images |
| **PyTorch** | Deep learning framework used by the model |
| **Transformers** | Provides AI model components and dependencies |
| **Accelerate** | Helps optimize model execution |

---

![alt text](<Screenshot 2026-09-04 155412-1.png>)

![alt text](<Screenshot 2026-09-04 155456.png>)

# How Does It Work?

The application follows a simple text-to-image workflow.

```text
        User
          │
          │ Enter Text Prompt
          ▼
    Text Prompt
          │
          ▼
 AutoPipelineForText2Image
          │
          ▼
   Diffusion Model
  Stable Diffusion Turbo
          │
          ▼
   Generated Image
          │
          ▼
     Streamlit UI
   