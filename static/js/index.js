document.addEventListener('DOMContentLoaded', function() {
    // 页面加载完成后执行
    console.log('Page loaded successfully');

    // 获取更多仓库按钮点击事件
    document.getElementById('load-more').addEventListener('click', function() {
        loadMoreRepos();
    });

    // 渲染用户数据
    renderUserData({{ github_data.user | safe }});
    renderUserRepos({{ github_data.repos | safe }});
});

// 渲染用户信息
function renderUserData(user) {
    if (!user) return;

    document.getElementById('avatar').src = user.avatar_url || '';
    document.getElementById('name').textContent = user.name || user.login || '';
    document.getElementById('bio').textContent = user.bio || 'No bio available';
    document.getElementById('repos').textContent = `Repositories: ${user.public_repos || 0}`;
    document.getElementById('followers').textContent = `Followers: ${user.followers || 0}`;
    document.getElementById('following').textContent = `Following: ${user.following || 0}`;
}

// 渲染用户仓库
function renderUserRepos(repos) {
    const reposList = document.getElementById('repos-list');
    
    if (!repos || !repos.length) {
        const li = document.createElement('li');
        li.className = 'list-group-item text-center';
        li.textContent = 'No repositories found.';
        reposList.appendChild(li);
        return;
    }

    // 清空现有列表
    while (reposList.firstChild) {
        reposList.removeChild(reposList.firstChild);
    }

    repos.forEach(repo => {
        const li = document.createElement('li');
        li.className = 'list-group-item repo-item';
        li.innerHTML = `
            <a href="${repo.html_url || ''}" target="_blank">${repo.name || ''}</a>
            <p class="text-muted">${repo.description || ''}</p>
            <small class="text-muted">Updated: ${new Date(repo.updated_at || '').toLocaleDateString()}</small>
        `;
        reposList.appendChild(li);
    });
}

// 加载更多仓库
async function loadMoreRepos() {
    try {
        // 模拟加载更多数据，实际应用中可以通过 API 获取更多数据
        const response = await fetch('/api/load-more-repos/');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const newData = await response.json();
        
        // 获取现有仓库列表
        const reposList = document.getElementById('repos-list');
        const existingRepos = Array.from(reposList.getElementsByClassName('repo-item')).map(item => {
            return {
                name: item.querySelector('a').textContent,
                html_url: item.querySelector('a').href,
                description: item.querySelector('p').textContent,
                updated_at: item.querySelector('small').textContent.split(': ')[1]
            };
        });
        
        // 合并新旧数据并去重
        const combinedRepos = [...existingRepos, ...newData.repos];
        const uniqueRepos = Array.from(new Set(combinedRepos.map(repo => repo.name))).map(name => {
            return combinedRepos.find(repo => repo.name === name);
        });
        
        // 重新渲染仓库列表
        renderUserRepos(uniqueRepos);
        
        // 显示成功消息
        showNotification('Success', 'Loaded more repositories!', 'success');
    } catch (error) {
        console.error('Error loading more repositories:', error);
        showNotification('Error', 'Failed to load more repositories.', 'error');
    }
}

// 显示通知
function showNotification(title, message, type) {
    // 创建通知元素
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed bottom-0 end-0 m-3`;
    notification.style.zIndex = '1000';
    notification.innerHTML = `
        <strong>${title}</strong> ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    // 添加到页面
    document.body.appendChild(notification);
    
    // 自动关闭通知
    setTimeout(() => {
        const alert = new bootstrap.Alert(notification);
        alert.close();
    }, 3000);
}