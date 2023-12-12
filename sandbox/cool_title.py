import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# Custom CSS for title and paragraph styling
st.markdown(
    """
<style>
.title {
    color: #FF4C29; /* Color of the title text */
    font-size: 26px; /* Size of the title font */
    font-weight: bold; /* Make the title font bold */
    padding-bottom: 0.25em; /* Space below the title */
}
.paragraph {
    color: #333333; /* Color of the paragraph text */
    font-size: 18px; /* Size of the paragraph font */
}
</style>
""",
    unsafe_allow_html=True,
)

# Title with custom CSS class
st.markdown('<div class="main_title">MARKETPLACE PROJECTS</div>', unsafe_allow_html=True)

# Decorative star (using an emoji as a placeholder)
st.markdown(":star:", unsafe_allow_html=True)

# Paragraph with custom CSS class
st.markdown(
    """
<div class="paragraph">
    In this space, we present a wide variety of projects designed to reduce carbon emissions and contribute to a cleaner and more sustainable planet. Each project in our Marketplace has been carefully selected for its positive impact on the environment and its ability to offset carbon emissions.
</div>
""",
    unsafe_allow_html=True,
)

# Custom CSS for shadow box
st.markdown(
    """
<style>
.shadow-box {
    border-radius: 10px; /* rounded corners */
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* horizontal offset, vertical offset, blur radius, spread radius, color */
    padding: 20px; /* space inside the box */
    margin: 20px; /* space outside the box */
    background: #ffffff; /* background color */
}
</style>
""",
    unsafe_allow_html=True,
)

# Text inside the shadow box
st.markdown(
    """
<div class="shadow-box">
    <h2>CO2 Tons Reduced</h2>
    <p>Explore our options and discover how you can be part of the change. By participating in these 
    projects, you are taking concrete steps to offset your carbon footprint and help protect our 
    precious planet.</p>
</div>
""",
    unsafe_allow_html=True,
)
