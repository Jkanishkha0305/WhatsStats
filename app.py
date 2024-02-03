# streamlit_app.py
import streamlit as st
from whatsapp_analyzer import process_whatsapp_data, process_word_data
from display_functions import display_results, display_bar_chart, display_pie_chart

# Main Streamlit app
def main():
    st.title("WhatsApp Group Chat Analyzer")

    # File upload
    uploaded_file = st.file_uploader("Choose a file", type=["txt"])

    # Data type options
    data_type = st.radio("Select Data Type:", ['Message Count', 'Sticker Count', 'Only Text Count', 'Message to Sticker Ratio', 'Word Count', 'Image Count', 'Video Count'])

    if data_type == 'Word Count':
        # Input box for entering a word
        word = str(st.text_input("Enter Word:"))
    else:
        word = None
    
    # Options for total or monthly data
    total_or_month = st.radio("Select Total or Month:", ['Total', 'Monthly'])

    # Chart type options
    chart_type = st.radio("Select Chart Type:", ['Bar Chart', 'Pie Chart'])

    # Display results only if a file is uploaded
    if uploaded_file is not None:
        # Process and analyze WhatsApp data
        message_counts, sticker_counts, only_text_counts, image_counts, video_counts = process_whatsapp_data(uploaded_file)

        # Placeholder for word counts (will be updated based on user input)
        if word:
            print(f"Processing word: {word}")
            word_counts = process_word_data(uploaded_file, word)
        else:
            word_counts = None

        print(f"word count: {word_counts}")
        
        # Placeholder for monthly data (will be updated based on user input)
        if total_or_month == 'Monthly':
            # Update this section based on how you want to process monthly data
            pass

        # Display results and charts
        display_results(data_type, word, total_or_month, chart_type, message_counts, sticker_counts, only_text_counts, word_counts, image_counts, video_counts) 

# Run the app
if __name__ == '__main__':
    main()
