$(document).ready(() => {

})



const copyProfileLink = (profileID) => {
    navigator.clipboard.writeText(window.location.host + "/user/" + profileID);
};



const followUser = (fromUserID, toUserID) => {
    const followButton = $("#follow-button")
    $.post({
        headers: {'X-CSRFToken': CSRFToken},
        url: "/user/follow",
        data: {fromUserID: fromUserID, toUserID: toUserID, operation: 'SET'},
        success: function (data){
            followButton.text(data)
        }
    })
}



const submitForm = (formID) => {
    $('#' + formID).submit()
}



const retrieveFollowState = (fromUserID, toUserID) => {
    const followButton = $("#follow-button")
    $.post({
        headers: {'X-CSRFToken': CSRFToken},
        url: 'user/follow',
        data: {fromUserID: fromUserID, toUserID: toUserID, operation: 'GET'},
        success: function (data){
            followButton.text(data)
        }
    })
}