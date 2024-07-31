# utils.py
import openpyxl
from .models import QuestionAnswer
from difflib import SequenceMatcher

def save_excel_to_db(uploaded_file):
    wb = openpyxl.load_workbook(uploaded_file)
    sheet = wb.active

    header = {cell.value: idx for idx, cell in enumerate(sheet[1])}
    question_col = header.get('question')
    answer_col = header.get('answer')

    if question_col is None or answer_col is None:
        raise ValueError("Excel file must contain 'question' and 'answer' columns")

    processed_data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        question = row[question_col]
        answer = row[answer_col]
        if question and answer:
            if not QuestionAnswer.objects.filter(question=question, answer=answer).exists():
                question_answer = QuestionAnswer(question=question, answer=answer)
                question_answer.save()
                processed_data.append({'question': question, 'answer': answer})
    wb.close()
    return processed_data


def get_most_similar_question(user_question, questions):
    most_similar_question = None
    highest_similarity = 0

    for question in questions:
        similarity = SequenceMatcher(None, user_question, question.question).ratio()
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_question = question

    return most_similar_question
