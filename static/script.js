document.addEventListener("DOMContentLoaded", function () {
    const result = document.querySelector(".result");

    if (result) {
        result.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });
    }
});