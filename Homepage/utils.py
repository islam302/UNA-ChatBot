from .models import QuestionAnswer
from fuzzywuzzy import fuzz
import openpyxl
import spacy


nlp = spacy.load('en_core_web_md')


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


def get_similar_questions(user_question, questions, threshold=50):
    similar_questions = []

    for question in questions:
        similarity = fuzz.ratio(user_question, question.question)
        if similarity >= threshold:
            similar_questions.append({
                'id': question.id,
                'question': question.question,
                'answer': question.answer,
                'similarity': similarity
            })

    return sorted(similar_questions, key=lambda x: x['similarity'], reverse=True)


