(function () {
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else {
        document.body.appendChild(
            document.createElement('script')
        ).src='https://e61d6df345b6.ngrok.io/static/js/bookmarklet.js?r=' + Math.floor(Math.random()*99999999999999999999);
    }
})();