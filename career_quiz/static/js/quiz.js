// Quiz logic
let currentQuestionIndex = 0;
let questions = [];
let answers = {};

async function loadQuestions() {
    try {
        const response = await fetch('/api/quiz/questions');
        if (!response.ok) {
            if (response.status === 401) {
                window.location.href = '/login';
                return;
            }
            throw new Error('Failed to load questions');
        }
        questions = await response.json();
        displayQuestion();
    } catch (error) {
        console.error('Error:', error);
        alert('Lỗi tải câu hỏi: ' + error.message);
    }
}

function displayQuestion() {
    if (currentQuestionIndex >= questions.length) {
        submitQuiz();
        return;
    }

    const question = questions[currentQuestionIndex];
    const container = document.getElementById('question-container');
    
    const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
    document.getElementById('progress').style.width = progress + '%';

    let optionsHTML = '';
    for (let key in question.options) {
        optionsHTML += `
            <div class="option" onclick="selectOption('${key}')">
                <input type="radio" name="answer" value="${key}" id="option-${key}">
                <label for="option-${key}">${key}. ${question.options[key]}</label>
            </div>
        `;
    }

    container.innerHTML = `
        <div>
            <p class="profession-label">Ngành nghề: ${question.profession}</p>
            <h3>Câu ${currentQuestionIndex + 1}/${questions.length}: ${question.question}</h3>
            <div class="options">
                ${optionsHTML}
            </div>
            <div class="button-group">
                <button class="btn btn-secondary" onclick="previousQuestion()" ${currentQuestionIndex === 0 ? 'disabled' : ''}>Câu Trước</button>
                <button class="btn btn-primary" onclick="nextQuestion()">Câu Tiếp Theo</button>
            </div>
        </div>
    `;

    // Restore previous answer if exists
    if (answers[question.id]) {
        document.getElementById('option-' + answers[question.id]).checked = true;
        document.querySelector('.option input[value="' + answers[question.id] + '"]').parentElement.classList.add('selected');
    }
}

function selectOption(key) {
    const question = questions[currentQuestionIndex];
    answers[question.id] = key;
    
    // Update UI
    document.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));
    document.querySelector('.option input[value="' + key + '"]').parentElement.classList.add('selected');
}

function nextQuestion() {
    const question = questions[currentQuestionIndex];
    if (!answers[question.id]) {
        alert('Vui lòng chọn một đáp án');
        return;
    }
    currentQuestionIndex++;
    displayQuestion();
}

function previousQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        displayQuestion();
    }
}

async function submitQuiz() {
    // Check all questions are answered
    if (Object.keys(answers).length < questions.length) {
        alert('Vui lòng trả lời tất cả câu hỏi');
        return;
    }

    try {
        const response = await fetch('/api/quiz/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ answers: answers })
        });

        if (!response.ok) {
            throw new Error('Failed to submit quiz');
        }

        const data = await response.json();
        localStorage.setItem('lastResultId', data.result_id);
        window.location.href = '/results?result_id=' + data.result_id;
    } catch (error) {
        console.error('Error:', error);
        alert('Lỗi gửi bài trắc nghiệm: ' + error.message);
    }
}

// Load questions when page loads
document.addEventListener('DOMContentLoaded', () => {
    const isLoggedIn = localStorage.getItem('logged_in') === 'true';
    if (!isLoggedIn) {
        window.location.href = '/login';
    } else {
        loadQuestions();
    }
});
