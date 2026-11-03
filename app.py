import streamlit as st

from generator import generate_code
from validator import validate_python

from rag import retrieve_context

st.set_page_config(
    page_title="AI Code Generator",
    page_icon="💻"
)

st.title("💻 AI Python Code Generator")

requirement = st.text_area(
    "Enter Requirement",
    height=200
)

if st.button("Generate Code"):

    if requirement.strip() == "":
        st.warning("Please enter a requirement.")
        st.stop()

    with st.spinner("Generating Code..."):

        
        context = retrieve_context(requirement)
        st.subheader("Retrieved Context")
        st.text(context)
        code = generate_code(requirement,context)

        st.subheader("Generated Code")

        st.code(
            code,
            language="python"
        )

        if not code.startswith("ERROR"):

            if validate_python(code):
                st.success("✅ Syntax Valid")
            else:
                st.warning("⚠ Syntax Validation Failed")

            st.download_button(
                label="Download Python File",
                data=code,
                file_name="generated_code.py",
                mime="text/plain"
            )

        else:
            st.error(code)