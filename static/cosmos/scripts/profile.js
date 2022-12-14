



const copyProfileLink = (profileID) => {
    navigator.clipboard.writeText(window.location.host + "/user/" + profileID);
};



const followUser = (userID) => {
    $.post({
        headers: {'X-CSRFToken': CSRFToken},
        // TODO
    })
}