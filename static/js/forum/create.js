document.addEventListener('DOMContentLoaded', function () {
    const newsCategoriesSpan = document.getElementsByClassName("categories-badge-span")
    const newsCategoriesBtn = document.getElementsByClassName("categories-badge-btn")
    const newsCategoriesSvg = document.getElementsByClassName("categories-badge-svg")
    const newsCategories = document.getElementById('categories')


    const user = document.getElementById("user")
    const submitBtn = document.getElementById("btn-submit")

    const description = document.getElementById("description")
    const title = document.getElementById("title")
    const descriptionCount = document.getElementById('char')


    function selectBtn(span, btn, svg, data) {
        let new_value = []
        for (let index = 0; index < btn.length; index++) {
            btn[index].addEventListener('click', function (e) {
                if (btn[index].dataset.selected === "False") {
                    new_value.push(span[index].innerText)
                    span[index].style.background = 'linear-gradient(102.28deg, #FF6767 10.52%, rgba(241, 6, 6, 0.81) 86.96%)'
                    svg[index].style.transform = 'rotate(45deg)';
                    svg[index].style.transition = 'transform 0.2s ease-in-out';
                    btn[index].dataset.selected = "True"
                } else {
                    new_value.pop(span[index].innerText)
                    svg[index].style.transform = 'rotate(0deg)';
                    svg[index].style.transition = 'transform 0.2s ease-in-out';
                    btn[index].dataset.selected = "False"
                    span[index].style.background = 'linear-gradient(102.22deg, #04C500 10.82%, rgba(4, 197, 0, 0.81) 97.95%)'
                }
                data.value = new_value
            })
        }
    }

    function formValidate() {

        if (newsCategories.value.split(',').length < 1 || description.value === '' || title.value === '') {
            return false;
        } else {
            return true;
        }

    }

    submitBtn.addEventListener('click', function (e) {
        if (formValidate()) {
            e.preventDefault()
            user.submit()
        }
    })


    selectBtn(newsCategoriesSpan, newsCategoriesBtn, newsCategoriesSvg, newsCategories)

    description.addEventListener("input", function (e) {
        descriptionCount.innerText = `You inserted ${description.value.length} characters`
    })

});