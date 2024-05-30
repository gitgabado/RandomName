import streamlit as st
import pandas as pd
import random
import base64
from PIL import Image

def load_data(uploaded_file):
    try:
        if uploaded_file.name.endswith('.csv'):
            return pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xls') or uploaded_file.name.endswith('.xlsx'):
            return pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a .csv or .xls/.xlsx file.")
            return None
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def get_image_as_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def main():
    st.title("Random Winner Selector")
    
    uploaded_file = st.file_uploader("Upload a file", type=['csv', 'xls', 'xlsx'])
    
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        
        if data is not None:
            st.write("Here is the list of names uploaded:")
            st.dataframe(data)
            
            if st.button("Select a Random Winner"):
                winner = random.choice(data.iloc[:, 0])
                st.success(f"{winner} is the winner!")
                
                # Load trophy image and encode it to base64
                trophy_base64 = get_image_as_base64("trophy.png")
                
                # Display winner name and trophy side by side
                st.markdown(f"""
                    <div style="display: flex; align-items: center;">
                        <h2 style="margin: 0;">{winner} is the winner!</h2>
                        <img src="data:image/png;base64,{trophy_base64}" width="50" height="50" style="margin-left: 10px;">
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Failed to load data.")
    
if __name__ == "__main__":
    main()

