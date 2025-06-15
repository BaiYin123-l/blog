// 确保页面加载完成后再执行脚本
document.addEventListener("DOMContentLoaded", function() {
    // 获取所有的导航链接
    const navLinks = document.querySelectorAll('.nav-link');

    // 遍历每个链接
    navLinks.forEach(link => {
        // 如果链接的 href 属性与当前页面的 URL 匹配，则添加 'active' 类
        if (link.href === window.location.href) {
            link.classList.add('active');
            link.setAttribute('aria-current', 'page');
        }
        // 如果当前页面 属性为./blog/，则给blogs添加 'active' 类
        if (window.location.href.split('/')[3] === 'blog') {
            t = document.querySelector("body > div:nth-child(1) > header > ul > li:nth-child(2) > a");
            t.classList.add('active');
            t.setAttribute('aria-current', 'page');
        }
    });
});