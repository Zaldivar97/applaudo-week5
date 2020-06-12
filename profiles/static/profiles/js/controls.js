let controls = document.querySelectorAll(".controls")
controls.forEach(control => {
    console.log(control)
    control.onclick = e => {
        let tab = e.target
        for (let i = 0; i < controls.length; i++) {
            controls[i].classList.remove("selected")
        }
        tab.classList.add("selected");
        let main = document.querySelector("#my-posts")
        let list = document.querySelector("#list")

        if (tab.id == "posts-tab") {
            list.classList.add("hide")
            main.classList.remove("hide")

        } else if (tab.id == "list-tab") {
            main.classList.add("hide")
            list.classList.remove("hide")
        }
    }

})