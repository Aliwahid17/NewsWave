document.addEventListener('DOMContentLoaded', function () {

    let categoryBtn = document.querySelectorAll(".categories-btn")
    let categorySpanBtn = document.querySelectorAll(".categories-span-btn")
    let categoryDefaultBtn = 0

    let upvote = document.querySelectorAll('.upvote')
    let downvote = document.querySelectorAll('.downvote')
    let vote = document.querySelectorAll('.vote')


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    function dataAjax(votes , title , voteCategory) {
        let xhr = new XMLHttpRequest()
        let csrftoken = getCookie('csrftoken')
        xhr.open("POST", '/forum/', true)
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.setRequestHeader('X-CSRFToken', csrftoken)
        let data = JSON.stringify({
            votes : votes,
            title: title,
            voteCategory : voteCategory
        })

        xhr.send(data)
        xhr.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                console.log("success")
            }
        }
    }


    document.getElementById(window.dataJson[categoryDefaultBtn].replace(/^\w/, c => c.toUpperCase())).classList.remove('hidden')


    for (let i = 0; i < categoryBtn.length; i++) {

        categoryBtn[categoryDefaultBtn].dataset.selected = "true"
        categorySpanBtn[categoryDefaultBtn].style.background = 'linear-gradient(102.28deg, #FF6767 10.52%, rgba(241, 6, 6, 0.81) 86.96%)'


        categoryBtn[i].addEventListener("click", function () {
            categoryBtn[categoryDefaultBtn].dataset.selected = "false"
            categorySpanBtn[categoryDefaultBtn].style.background = "linear-gradient(102.22deg, #04C500 10.82%, rgba(4, 197, 0, 0.81) 97.95%)"
            document.getElementById(window.dataJson[categoryDefaultBtn].replace(/^\w/, c => c.toUpperCase())).classList.add('hidden')
            document.getElementById(window.dataJson[i].replace(/^\w/, c => c.toUpperCase())).classList.remove('hidden')
            categoryBtn[i].dataset.selected = "true"
            categorySpanBtn[i].style.background = 'linear-gradient(102.28deg, #FF6767 10.52%, rgba(241, 6, 6, 0.81) 86.96%)'
            categoryDefaultBtn = i
        })
    }

    for (let index = 0; index < upvote.length; index++) {

        upvote[index].addEventListener('click', function(e){

            if (vote[index].dataset.vote === "Up"){
                vote[index].value = parseInt(vote[index].value) - 1
                vote[index].dataset.vote = "No"
                upvote[index].firstElementChild.style.fill = "black"
            } else if (vote[index].dataset.vote === "No" || vote[index].dataset.vote === "" ){
                vote[index].value = parseInt(vote[index].value) + 1
                vote[index].dataset.vote = "Up"
                upvote[index].firstElementChild.style.fill = "green"
            } else{
                vote[index].value = parseInt(vote[index].value) + 2
                vote[index].dataset.vote = "Up"
                upvote[index].firstElementChild.style.fill = "green"
                downvote[index].firstElementChild.style.fill = "black"
            }

            dataAjax(vote[index].value , vote[index].dataset.title , vote[index].dataset.vote)
            
        })
        
    }
    
    for (let index = 0; index < downvote.length; index++) {
        
        downvote[index].addEventListener('click', function(e){
            if (vote[index].dataset.vote === "Down"){
                vote[index].value = parseInt(vote[index].value) + 1
                vote[index].dataset.vote = "No"
                downvote[index].firstElementChild.style.fill = "black"
            } else if (vote[index].dataset.vote === "No" || vote[index].dataset.vote === ""){
                vote[index].value = parseInt(vote[index].value) - 1
                vote[index].dataset.vote = "Down"
                downvote[index].firstElementChild.style.fill = "red"
            } else{
                vote[index].value = parseInt(vote[index].value) - 2
                vote[index].dataset.vote = "Down"
                downvote[index].firstElementChild.style.fill = "red"
                upvote[index].firstElementChild.style.fill = "black"
            }

            dataAjax(vote[index].value, vote[index].dataset.title, vote[index].dataset.vote)

        })
        
    }



})