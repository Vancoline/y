// Results logic
async function loadResults() {
    const isLoggedIn = localStorage.getItem('logged_in') === 'true';
    if (!isLoggedIn) {
        window.location.href = '/login';
        return;
    }

    const params = new URLSearchParams(window.location.search);
    const resultId = params.get('result_id') || localStorage.getItem('lastResultId');

    if (!resultId) {
        document.getElementById('results-container').innerHTML = '<p>Không tìm thấy kết quả. <a href="/quiz">Làm bài trắc nghiệm</a></p>';
        return;
    }

    try {
        const response = await fetch('/api/quiz/result/' + resultId);
        if (!response.ok) {
            throw new Error('Failed to load results');
        }

        const result = await response.json();
        displayResults(result);
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('results-container').innerHTML = '<p>Lỗi tải kết quả: ' + error.message + '</p>';
    }
}

function displayResults(result) {
    const container = document.getElementById('results-container');
    
    let answersHTML = '';
    result.answers.forEach((answer, index) => {
        const isCorrect = answer.is_correct;
        const statusClass = isCorrect ? 'correct' : 'incorrect';
        const statusText = isCorrect ? '✓ Đúng' : '✗ Sai';

        answersHTML += `
            <div class="answer-item ${statusClass}">
                <h4>Câu ${index + 1}: ${statusText}</h4>
                <p class="profession-label">Ngành nghề: ${answer.profession}</p>
                <p><strong>Câu hỏi:</strong> ${answer.question}</p>
                <div class="answer-detail">
                    <p><strong>Đáp án của bạn:</strong> ${answer.user_answer}. ${answer.options[answer.user_answer]}</p>
                    ${!isCorrect ? `<p><strong>Đáp án đúng:</strong> ${answer.correct_answer}. ${answer.options[answer.correct_answer]}</p>` : ''}
                </div>
            </div>
        `;
    });

    container.innerHTML = `
        <div class="score-summary">
            <h1>Kết Quả Trắc Nghiệm</h1>
            <div class="big-score">${result.score}/${result.total}</div>
            <div class="percentage">${result.percentage}%</div>
            <p>${result.percentage >= 70 ? 'Tuyệt vời!' : result.percentage >= 50 ? 'Khá tốt!' : 'Tiếp tục cố gắng!'}</p>
        </div>
        <div>
            <h2>Chi Tiết Câu Trả Lời</h2>
            ${answersHTML}
        </div>
        <div style="text-align: center; margin-top: 30px;">
            <a href="/quiz" class="btn btn-primary">Làm Bài Mới</a>
            <a href="/results" class="btn btn-secondary" style="margin-left: 10px;">Xem Lịch Sử</a>
        </div>
    `;
}

// Load results when page loads
document.addEventListener('DOMContentLoaded', loadResults);
