function submit() {
    document.forms[0].submit();
}

function keyDown(e) {
    alert("我被调用了");
    if (e.key = "Enter") {
        submit();
    }
}

function registeAction() {
    window.location.href = "/register/"
}