document.addEventListener('DOMContentLoaded', function () {

    let mainPosts = document.querySelectorAll(".main-post");
    let posts = document.querySelectorAll(".post");

    let i = 0;
    let postIndex = 0;
    let currentPost = posts[postIndex];
    let currentMainPost = mainPosts[postIndex];

    let progressInterval = setInterval(progress, 100); // 180

    function progress() {
        if (i === 100) {
            i = -5;
            // reset progress bar
            currentPost.querySelector(".progress-bar__fill").style.width = 0;
            document.querySelector(
                ".progress-bar--primary .progress-bar__fill"
            ).style.width = 0;
            currentPost.classList.remove("post--active");

            postIndex++;

            currentMainPost.classList.add("main-post--not-active");
            currentMainPost.classList.remove("main-post--active");

            // reset postIndex to loop over the slides again
            if (postIndex === posts.length) {
                postIndex = 0;
            }

            currentPost = posts[postIndex];
            currentMainPost = mainPosts[postIndex];
        } else {
            i++;
            currentPost.querySelector(".progress-bar__fill").style.width = `${i}%`;
            document.querySelector(
                ".progress-bar--primary .progress-bar__fill"
            ).style.width = `${i}%`;
            currentPost.classList.add("post--active");

            currentMainPost.classList.add("main-post--active");
            currentMainPost.classList.remove("main-post--not-active");
        }
    }

    let hearts = document.querySelectorAll(".heart");
    let heartsNum = document.querySelectorAll(".heart-num")
    for (let i = 0; i < hearts.length; i++) {
        hearts[i].addEventListener("click", function () {
            this.classList.toggle("is-active");
            if (this.classList.contains("is-active")) {
                heartsNum[i].innerText = parseInt(heartsNum[i].innerText) + 1
            } else {
                heartsNum[i].innerText = parseInt(heartsNum[i].innerText) - 1
            }
        });
    }

    let bookmark = document.querySelectorAll('.bookmark')

    for (let i = 0; i < bookmark.length; i++) {
        bookmark[i].addEventListener("click", function () {
            this.classList.toggle("saved")
            if (this.classList.contains("saved")) {
                bookmark[i].innerHTML = `<svg class="w-8 h-8" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#FF1616" class="bi bi-bookmark-check-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm8.854-9.646a.5.5 0 0 0-.708-.708L7.5 7.793 6.354 6.646a.5.5 0 1 0-.708.708l1.5 1.5a.5.5 0 0 0 .708 0l3-3z"/></svg>`
            } else {
                bookmark[i].innerHTML = `<svg class="w-8 h-8" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bookmark-plus" viewBox="0 0 16 16"><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z" /><path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4z" /></svg>`
            }
        })
    }

    let clip = document.querySelectorAll('#link')

    for (let i = 0; i < clip.length; i++) {
        clip[i].addEventListener("click", function () {
            navigator.clipboard.writeText(clip[i].dataset.value);
        })
    }

    let categoryBtn = document.querySelectorAll(".categories-btn")
    let categorySpanBtn = document.querySelectorAll(".categories-span-btn")
    let categoryDefaultBtn = 0

    let filterBtn = document.querySelectorAll(".filter-btn")
    let filterSpanBtn = document.querySelectorAll(".filter-span-btn")
    let filterDefaultBtn = 0


    for (let i = 0; i < categoryBtn.length; i++) {

        categoryBtn[categoryDefaultBtn].dataset.selected = "true"
        categorySpanBtn[categoryDefaultBtn].style.background = 'linear-gradient(102.28deg, #FF6767 10.52%, rgba(241, 6, 6, 0.81) 86.96%)'


        categoryBtn[i].addEventListener("click", function () {
            categoryBtn[categoryDefaultBtn].dataset.selected = "false"
            categorySpanBtn[categoryDefaultBtn].style.background = "linear-gradient(102.22deg, #04C500 10.82%, rgba(4, 197, 0, 0.81) 97.95%)"
            categoryBtn[i].dataset.selected = "true"
            categorySpanBtn[i].style.background = 'linear-gradient(102.28deg, #FF6767 10.52%, rgba(241, 6, 6, 0.81) 86.96%)'
            categoryDefaultBtn = i
        })
    }

    for (let i = 0; i < filterBtn.length; i++) {

        filterBtn[filterDefaultBtn].dataset.selected = "true"
        filterSpanBtn[filterDefaultBtn].style.background = 'linear-gradient(102.28deg, #FF6767 10.52%, rgba(241, 6, 6, 0.81) 86.96%)'

        filterBtn[i].addEventListener("click", function () {

            filterBtn[filterDefaultBtn].dataset.selected = "false"
            filterSpanBtn[filterDefaultBtn].style.background = "linear-gradient(102.22deg, #04C500 10.82%, rgba(4, 197, 0, 0.81) 97.95%)"
            filterBtn[i].dataset.selected = "true"
            filterSpanBtn[i].style.background = 'linear-gradient(102.28deg, #FF6767 10.52%, rgba(241, 6, 6, 0.81) 86.96%)'
            filterDefaultBtn = i

        })
    }


})  