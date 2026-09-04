import streamlit as st
from diffusers import AutoPipelineForText2Image

# Page configuration
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="centered"
)

# Application title
st.title("🎨 AI Image Generator")
st.write("Create an image from your text prompt using AI.")

# Get prompt from the user
prompt = st.text_input(
    "Enter your image prompt:",
    placeholder="Example: A beautiful sunset over the mountains"
)

# Generate button
if st.button("✨ Generate Image"):

    if prompt:

        # Show loading message
        with st.spinner("Creating your image..."):

            # Load the AI image generation model
            pipe = AutoPipelineForText2Image.from_pretrained(
                "stabilityai/sd-turbo"
            )

            # Generate the image
            image = pipe(
                prompt=prompt,
                num_inference_steps=1,
                guidance_scale=0.0
            ).images[0]

        # Display generated image
        st.image(
            image,
            caption="AI Generated Image",
            use_container_width=True
        )

    else:
        st.warning("Please enter a prompt first.")