# display_functions.py
import streamlit as st
import plotly.express as px

# Function to display results and charts using Streamlit
def display_results(data_type, word, total_or_month, chart_type, message_counts, sticker_counts, only_text_counts, word_counts, image_counts, video_counts):
    st.header("WhatsApp Group Chat Statistics")

    if data_type == 'Message Count':
        st.subheader("Total Message Count")
        st.write(message_counts.reset_index(name='Count'))
        if chart_type == 'Bar Chart':
            display_bar_chart(data_type, message_counts)
        elif chart_type == 'Pie Chart':
            display_pie_chart(data_type, message_counts)
    elif data_type == 'Sticker Count':
        st.subheader("Sticker Count")
        st.write(sticker_counts.reset_index(name='Count'))
        if chart_type == 'Bar Chart':
            display_bar_chart(data_type, sticker_counts)
        elif chart_type == 'Pie Chart':
            display_pie_chart(data_type, sticker_counts)
    elif data_type == 'Only Text Count':
        st.subheader("Only Text Count")
        st.write(only_text_counts.reset_index(name='Count'))
        if chart_type == 'Bar Chart':
            display_bar_chart(data_type, only_text_counts)
        elif chart_type == 'Pie Chart':
            display_pie_chart(data_type, only_text_counts)
    elif data_type == 'Message to Sticker Ratio':
        ratio_series = message_counts / sticker_counts
        ratio_series = ratio_series.dropna()
        ratio_series = ratio_series.sort_values(ascending=True)
        st.subheader("Message to Sticker Ratio")
        st.write(ratio_series)
        # Ratio doesn't make sense for Pie Chart, so only display Bar Chart
        if chart_type == 'Bar Chart':
            display_bar_chart(data_type, ratio_series)
    elif data_type == 'Word Count':
        st.subheader(f"Word Count for '{word}'")
        st.write(word_counts)
        if chart_type == 'Bar Chart':
            display_bar_chart(data_type, word_counts)
        elif chart_type == 'Pie Chart':
            display_pie_chart(data_type, word_counts)
    elif data_type == 'Image Count':
        st.subheader("Image Count")
        st.write(image_counts.reset_index(name='Count'))
        if chart_type == 'Bar Chart':
            display_bar_chart(data_type, image_counts)
        elif chart_type == 'Pie Chart':
            display_pie_chart(data_type, image_counts)
    elif data_type == 'Video Count':
        st.subheader("Video Count")
        st.write(video_counts.reset_index(name='Count'))
        if chart_type == 'Bar Chart':
            display_bar_chart(data_type, video_counts)
        elif chart_type == 'Pie Chart':
            display_pie_chart(data_type, video_counts)
            
# Function to display Bar Chart
def display_bar_chart(data_type, counts):
    fig = px.bar(x=counts.index, y=counts.values, labels={'x': 'Names', 'y': f'{data_type} Count'},
                 title=f"{data_type} vs Names Bar Chart")
    fig.update_layout(xaxis=dict(tickangle=45))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.plotly_chart(fig)

# Function to display Pie Chart
def display_pie_chart(data_type, counts):
    fig = px.pie(counts, values=counts.values, names=counts.index, title=f"{data_type} Distribution Pie Chart",
                 labels={'names': 'Names', 'values': f'{data_type} Count'})
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.plotly_chart(fig)