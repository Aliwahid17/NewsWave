document.addEventListener('DOMContentLoaded', function () {
    const newsCategoriesSpan = document.getElementsByClassName("categories-badge-span")
    const newsCategoriesBtn = document.getElementsByClassName("categories-badge-btn")
    const newsCategoriesSvg = document.getElementsByClassName("categories-badge-svg")
    const newsCategories = document.getElementById('categories')

    const newsSourcesSpan = document.getElementsByClassName("sources-badge-span")
    const newsSourcesBtn = document.getElementsByClassName("sources-badge-btn")
    const newsSourcesSvg = document.getElementsByClassName("sources-badge-svg")
    const newsSources = document.getElementById('sources')

    const user = document.getElementById("user")
    const submitBtn = document.getElementById("btn-submit")

    const country = document.getElementById('country')
    const DOB = document.getElementById('DOB')

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

        if (country.value === '' || DOB.value === '' || newsCategories.value.split(',').length < 2 || newsSources.value.split(',').length < 5) {
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
    selectBtn(newsSourcesSpan, newsSourcesBtn, newsSourcesSvg, newsSources)

});