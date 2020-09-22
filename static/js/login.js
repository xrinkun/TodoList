function submit() {
    document.forms[0].submit();
}

function keyDown(e) {
    if (e.key === "Enter") {
        document.forms[0].submit();
    }
}

function registeAction() {
    window.location.href = "/register/"
}