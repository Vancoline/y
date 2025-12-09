// Admin dashboard logic
let currentUserId = null;
let currentResultId = null;

async function loadAdminDashboard() {
    const isLoggedIn = localStorage.getItem('logged_in') === 'true';
    const isAdmin = localStorage.getItem('is_admin') === 'true';

    if (!isLoggedIn || !isAdmin) {
        window.location.href = '/admin';
        return;
    }

    try {
        const response = await fetch('/api/admin/dashboard');
        if (!response.ok) {
            throw new Error('Failed to load dashboard');
        }

        const users = await response.json();
        displayUsersList(users);
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('admin-container').innerHTML = '<p>Lỗi tải dữ liệu: ' + error.message + '</p>';
    }
}

function displayUsersList(users) {
    const tbody = document.getElementById('users-tbody');
    tbody.innerHTML = '';

    users.forEach((user, index) => {
        const row = `
            <tr>
                <td>${user.user_id}</td>
                <td>${user.username} ${user.is_admin ? '(Admin)' : ''}</td>
                <td>${user.total_attempts}</td>
                <td>${user.latest_score} / 10</td>
                <td>${user.average_score} / 10</td>
                <td>
                    <button class="btn btn-primary" onclick="viewUserResults(${user.user_id}, '${user.username}')">Xem Chi Tiết</button>
                </td>
            </tr>
        `;
        tbody.innerHTML += row;
    });
}

async function viewUserResults(userId, username) {
    currentUserId = userId;
    
    try {
        const response = await fetch(`/api/admin/user/${userId}/results`);
        if (!response.ok) {
            throw new Error('Failed to load user results');
        }

        const results = await response.json();
        displayUserResults(results, username);
    } catch (error) {
        console.error('Error:', error);
        alert('Lỗi tải kết quả: ' + error.message);
    }
}

function displayUserResults(results, username) {
    document.getElementById('admin-container').style.display = 'none';
    document.getElementById('detail-container').style.display = 'block';
    document.getElementById('detail-title').textContent = `Kết Quả của ${username}`;

    const tbody = document.getElementById('results-tbody');
    tbody.innerHTML = '';

    results.forEach((result, index) => {
        const row = `
            <tr>
                <td>${index + 1}</td>
                <td>${result.score}</td>
                <td>${result.total}</td>
                <td>${result.percentage}%</td>
                <td>${new Date(result.completed_at).toLocaleString('vi-VN')}</td>
                <td>
                    <button class="btn btn-primary" onclick="viewAnswerDetails(${result.result_id})">Xem Câu Trả Lời</button>
                </td>
            </tr>
        `;
        tbody.innerHTML += row;
    });
}

async function viewAnswerDetails(resultId) {
    currentResultId = resultId;
    
    try {
        const response = await fetch(`/api/quiz/result/${resultId}`);
        if (!response.ok) {
            throw new Error('Failed to load answer details');
        }

        const result = await response.json();
        displayAnswerDetails(result);
    } catch (error) {
        console.error('Error:', error);
        alert('Lỗi tải chi tiết: ' + error.message);
    }
}

function displayAnswerDetails(result) {
    document.getElementById('detail-container').style.display = 'none';
    document.getElementById('answer-detail').style.display = 'block';

    let answersHTML = '';
    result.answers.forEach((answer, index) => {
        const isCorrect = answer.is_correct;
        const statusClass = isCorrect ? 'correct' : 'incorrect';
        const statusText = isCorrect ? '✓ Đúng' : '✗ Sai';

        answersHTML += `
            <div class="answer-detail-item ${statusClass}">
                <h4>Câu ${index + 1}: ${statusText}</h4>
                <p><strong>Ngành nghề:</strong> ${answer.profession}</p>
                <p><strong>Câu hỏi:</strong> ${answer.question}</p>
                <p><strong>Đáp án của người dùng:</strong> ${answer.user_answer}. ${answer.options[answer.user_answer]}</p>
                <p><strong>Đáp án đúng:</strong> ${answer.correct_answer}. ${answer.options[answer.correct_answer]}</p>
            </div>
        `;
    });

    const content = document.getElementById('answer-detail-content');
    content.innerHTML = `
        <div style="background-color: #e7f3ff; padding: 20px; border-radius: 4px; margin-bottom: 20px;">
            <p><strong>Điểm:</strong> ${result.score}/${result.total}</p>
            <p><strong>Tỷ lệ:</strong> ${result.percentage}%</p>
            <p><strong>Ngày làm bài:</strong> ${new Date(result.completed_at).toLocaleString('vi-VN')}</p>
        </div>
        ${answersHTML}
    `;
}

function showUsersList() {
    document.getElementById('admin-container').style.display = 'block';
    document.getElementById('detail-container').style.display = 'none';
    document.getElementById('answer-detail').style.display = 'none';
    loadAdminDashboard();
}

function goBackToResults() {
    document.getElementById('detail-container').style.display = 'block';
    document.getElementById('answer-detail').style.display = 'none';
    if (currentUserId) {
        viewUserResults(currentUserId, '');
    }
}

// Load dashboard when page loads
document.addEventListener('DOMContentLoaded', loadAdminDashboard);
