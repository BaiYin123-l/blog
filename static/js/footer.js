// 确保页面加载完成后再执行脚本
document.addEventListener("DOMContentLoaded", function() {
    // 获取所有的导航链接
    const navLinks = document.querySelectorAll('.nav-link');

    // 遍历每个链接
    navLinks.forEach(link => {
        const linkpath = new URL(link.href).pathname;
        const linkFirstLevelPath = linkpath.split('/')[1] ? '/' + linkpath.split('/')[1]:'.';
        // 如果链接的 href 属性与当前页面的 URL 匹配，则添加 'active' 类
        if (link.href === window.location.href) {
            link.classList.add('active');
            link.setAttribute('aria-current', 'page');
        }
    });
});