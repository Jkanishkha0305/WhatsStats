# whatsapp_analyzer.py
import re
import pandas as pd 

def process_whatsapp_data(uploaded_file):
    # Read the contents of the uploaded file
    chat_data = uploaded_file.read().decode('utf-8')

    # Extracting names
    name_pattern = re.compile(r'\[(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2})\] (\w+):')
    names = re.findall(name_pattern, chat_data)

    df = pd.DataFrame(names, columns=['Timestamp', 'Name'])
    message_counts = df['Name'].value_counts()

    # Define a regex pattern to extract names and messages with "sticker omitted"
    sticker_pattern = re.compile(r"\[\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2}\] ([^:]+):.*sticker omitted")

    # Use the regex pattern to find all occurrences in the chat_data
    sticker_matches = re.finditer(sticker_pattern, chat_data)

    # Extract and count sticker names
    sticker_names = [match.group(1) for match in sticker_matches]
    sticker_counts = pd.Series(sticker_names).value_counts()
    
    only_text_counts = message_counts - sticker_counts
    only_text_counts = only_text_counts.sort_values(ascending=False)
    
    # Define a regex pattern to extract names and messages with "image omitted"
    image_pattern = re.compile(r"\[\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2}\] ([^:]+):.*image omitted")

    # Use the regex pattern to find all occurrences in the chat_data
    image_matches = re.finditer(image_pattern, chat_data)

    # Extract and count image names
    image_names = [match.group(1) for match in image_matches]
    image_counts = pd.Series(image_names).value_counts()
    
    # Define a regex pattern to extract names and messages with "media omitted"
    video_pattern = re.compile(r"\[\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2}\] ([^:]+):.*video omitted")

    # Use the regex pattern to find all occurrences in the chat_data
    video_matches = re.finditer(video_pattern, chat_data)

    # Extract and count media names
    video_names = [match.group(1) for match in video_matches]
    video_counts = pd.Series(video_names).value_counts()

    return message_counts, sticker_counts, only_text_counts, image_counts, video_counts

def process_word_data(uploaded_file, word):
    input_file_path = '/Users/kanishkhajaisankar/Downloads/WhatsStats/group_chat.txt'  # Replace with your input file path
    output_file_path = '../filtered.txt'  # Replace with your desired output file path
    
    # Open the input and output files
    with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Iterate through each line in the input file
        for line in input_file:
            # Check if the line contains "sticker omitted"
            if word in line.lower():
                # If yes, write the line to the output file
                output_file.write(line.lower())

    # Close the files
    input_file.close()
    output_file.close()
    file_path = '../filtered.txt'

    with open(file_path, 'r', encoding='utf-8') as file:
        chat_data = file.read()

    # Define a regex pattern to extract names
    name_pattern = re.compile(r'\[(\d{2}\/\d{2}\/\d{4}, \d{2}:\d{2}:\d{2})\] (\w+):')

    # Use the regex pattern to find all name occurrences in the chat
    names = re.findall(name_pattern, chat_data)
    
    df = pd.DataFrame(names, columns=['Timestamp', 'Name'])
    word_counts = df['Name'].value_counts()
    
    return word_counts

