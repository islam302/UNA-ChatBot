<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <div class="container">
        <h1>Question Answering Django Application</h1>
        <p>This Django application allows users to upload questions and answers from an Excel file into a database, find the most similar question to a user's query, and get responses using a chatbot API.</p>
        
<h2>Features</h2>
        <ul>
            <li>Upload questions and answers from an Excel file.</li>
            <li>Store questions and answers in a database.</li>
            <li>Find the most similar question in the database to a user's query using fuzzy matching.</li>
            <li>Fallback to a chatbot API for responses if no similar question is found in the database.</li>
            <li>Handle Arabic language inputs and queries.</li>
        </ul>
        
<h2>Prerequisites</h2>
        <ul>
            <li>Python 3.x</li>
            <li>Django 3.x</li>
            <li>Django REST framework</li>
            <li>Openpyxl</li>
            <li>Fuzzywuzzy</li>
            <li>SpaCy</li>
            <li>Requests</li>
        </ul>
        
<h2>Setup</h2>
        
<h3>Clone the Repository</h3>
        <pre><code>git clone https://github.com/yourusername/question-answering-django.git
          cd question-answering-django</code></pre>
        
 <h3>Create and Activate a Virtual Environment</h3>
        <pre><code>python -m venv venv
          source venv/bin/activate   # On Windows: venv\Scripts\activate</code></pre>
        
 <h3>Install Dependencies</h3>
        <pre><code>pip install -r requirements.txt</code></pre>
        
 <h3>Set Up the Django Project</h3>
        
 <h4>Apply Migrations:</h4>
        <pre><code>python manage.py migrate</code></pre>
        
 <h4>Create a Superuser:</h4>
        <pre><code>python manage.py createsuperuser</code></pre>
        
<h4>Run the Server:</h4>
        <pre><code>python manage.py runserver</code></pre>
        
 <h3>Configure Environment Variables</h3>
        <p>Create a <span class="highlight">.env</span> file in the root directory and add your OpenAI API key:</p>
        <pre><code>GPT4V_KEY='your_openai_api_key'</code></pre>
        
<h3>Download SpaCy Model</h3>
<pre><code>python -m spacy download en_core_web_md</code></pre>

<h2>Usage</h2>

<h3>Upload Questions and Answers</h3>
<ol>
    <li>Navigate to the upload page at <a href="http://127.0.0.1:8000/upload/">http://127.0.0.1:8000/upload/</a>.</li>
    <li>Upload an Excel file with <span class="highlight">question</span> and <span class="highlight">answer</span> columns.</li>
    <li>Processed data will be saved to the database and displayed on the page.</li>
</ol>
        
<h3>Ask a Question</h3>
<ol>
    <li>Navigate to the question page at <a href="http://127.0.0.1:8000/question/">http://127.0.0.1:8000/question/</a>.</li>
    <li>Enter your question in the form.</li>
    <li>The system will find the most similar question in the database and return the corresponding answer, or fallback to the chatbot API for a response.</li>
</ol>

<h2>Project Structure</h2>
<ul>
    <li><code>models.py</code>: Contains the <span class="highlight">QuestionAnswer</span> model.</li>
    <li><code>serializers.py</code>: Contains the <span class="highlight">QuestionAnswerSerializer</span>.</li>
    <li><code>utils.py</code>: Contains utility functions for saving Excel data to the database and finding the most similar question.</li>
    <li><code>views.py</code>: Contains the views for handling file uploads and user queries.</li>
    <li><code>forms.py</code>: Contains the forms for file upload and question submission.</li>
    <li><code>openai_utils.py</code>: Contains the function for fetching responses from the chatbot API.</li>
</ul>

</div>
</body>
</html>
