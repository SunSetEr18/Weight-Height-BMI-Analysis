import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(
    page_title="Height & Weight Analysis",
    page_icon="📊",
    layout="wide"
)

# Load data function with caching
@st.cache_data
def load_data():
    return pd.read_csv("data/SOCR-HeightWeight_metric.csv")

def main():
    st.title("📊 Height and Weight Analysis")
    st.markdown("Analyzing the relationship between height and weight in metric units")
    
    # Load data
    df = load_data()
    
    # Show raw data
    with st.expander("View Raw Data"):
        st.dataframe(df)
    
    # Basic statistics
    st.subheader("Basic Statistics")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Average Height", f"{df['Height(cm)'].mean():.1f} cm")
        st.metric("Minimum Height", f"{df['Height(cm)'].min():.1f} cm")
        st.metric("Maximum Height", f"{df['Height(cm)'].max():.1f} cm")
    
    with col2:
        st.metric("Average Weight", f"{df['Weight(kg)'].mean():.1f} kg")
        st.metric("Minimum Weight", f"{df['Weight(kg)'].min():.1f} kg")
        st.metric("Maximum Weight", f"{df['Weight(kg)'].max():.1f} kg")
    
    # Visualization
    st.subheader("Data Visualization")
    
    # Scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='Height(cm)', y='Weight(kg)', alpha=0.6, ax=ax)
    ax.set_title("Height vs Weight")
    st.pyplot(fig)
    
    # Distribution plots
    col1, col2 = st.columns(2)
    
    with col1:
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        sns.histplot(df['Height(cm)'], kde=True, ax=ax1)
        ax1.set_title("Height Distribution")
        st.pyplot(fig1)
    
    with col2:
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.histplot(df['Weight(kg)'], kde=True, ax=ax2)
        ax2.set_title("Weight Distribution")
        st.pyplot(fig2)
    
    # BMI calculation and analysis
    st.subheader("BMI Analysis")
    df['BMI'] = df['Weight(kg)'] / (df['Height(cm)']/100)**2
    
    # BMI categories
    def get_bmi_category(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    df['BMI Category'] = df['BMI'].apply(get_bmi_category)
    
    # BMI distribution
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    sns.histplot(df['BMI'], kde=True, bins=30, ax=ax3)
    ax3.set_title("BMI Distribution")
    st.pyplot(fig3)
    
    # BMI category counts
    st.write("BMI Category Distribution:")
    bmi_counts = df['BMI Category'].value_counts()
    st.bar_chart(bmi_counts)
    
    # Correlation analysis
    st.subheader("Correlation Analysis")
    corr = df[['Height(cm)', 'Weight(kg)', 'BMI']].corr()
    
    fig4, ax4 = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax4)
    st.pyplot(fig4)

if __name__ == "__main__":
    main()