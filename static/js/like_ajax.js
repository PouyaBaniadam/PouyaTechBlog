function like(slug, id) {
    var element = document.getElementById("like")
    var count = document.getElementById("count")
    $.get(`/like/${slug}/${id}`).then(response => {
        if (response['response'] === "liked") {
            element.style = "color: black"
            count.innerText = Number(count.innerText) + 1
        } else {
            element.style = "color: red"
            count.innerText = Number(count.innerText) - 1

        }
    })
}