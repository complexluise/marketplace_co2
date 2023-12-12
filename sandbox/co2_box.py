import streamlit as st


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
