>>> import streamlit as st
... import pandas as pd
... import random
... 
... def load_data(uploaded_file):
...     if uploaded_file.name.endswith('.csv'):
...         return pd.read_csv(uploaded_file)
...     elif uploaded_file.name.endswith('.xls') or uploaded_file.name.endswith('.xlsx'):
...         return pd.read_excel(uploaded_file)
...     else:
...         st.error("Unsupported file type. Please upload a .csv or .xls/.xlsx file.")
...         return None
... 
... def main():
...     st.title("Random Winner Selector")
...     
...     uploaded_file = st.file_uploader("Upload a file", type=['csv', 'xls', 'xlsx'])
...     
...     if uploaded_file is not None:
...         data = load_data(uploaded_file)
...         
...         if data is not None:
...             st.write("Here is the list of names uploaded:")
...             st.dataframe(data)
...             
...             if st.button("Select a Random Winner"):
...                 winner = random.choice(data.iloc[:, 0])
...                 st.success(f"{winner} is the winner!")
...         else:
...             st.error("Failed to load data.")
...     
... if __name__ == "__main__":
...     main()
