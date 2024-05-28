import pandas as pd
from .models import UploadFile


def save_excel_to_db(file_path):
    try:
        df = pd.read_excel(file_path)
        processed_data = []

        for _, row in df.iterrows():
            question = row['question']
            answer = row['answer']
            UploadFile.objects.create(question=question, answer=answer)
            processed_data.append({'question': question, 'answer': answer})

        return processed_data
    except Exception as e:
        print(f"Error processing file: {e}")
        return None

