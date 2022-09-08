var i = 0;
bannerList = ['banner1.jpg', 'banner2.jpg', 'banner3.jpg'];


function setbackground() {
    var gradientBackground = 'linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),';
    document.querySelector('.banner-container').style.backgroundImage = gradientBackground + 'url(/static/images/' + bannerList[i] + ')';
    
    i++;
    if (i == bannerList.length) {
        i = 0;
    }
}

window.onload = () => {
    setbackground();
    setInterval(function () {
        setbackground();
    }, 5000);
};