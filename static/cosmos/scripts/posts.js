//
//* Does AJAX database calls related to likes and dislikes
//
//* AJAX calls conform to the standard below
//* operation can be either 'GET' or 'SET', meaning a getter or setter db operation
//* goal can be either 'LIKE' or 'DISLIKE', meaning what is the above operation acting on
//



//for page initialization
function retrievePostReactions(postID){
    retrievePostLikes(postID);
    retrievePostDislikes(postID);
}



function retrievePostLikes(postID){
    const post = $(`#` + postID.toString() + `-likes`);
    $.post({
        headers: {'X-CSRFToken': CSRFToken},
        url: "/post/ajax",
        data: {postID: postID, operation: 'GET', goal: 'LIKE'},
        success: function (data){
            //alert(data);
            post.text(data);
        }
    })
}



function retrievePostDislikes(postID){
    const post = $(`#` + postID.toString() + `-dislikes`);
    $.post({
        headers: {'X-CSRFToken': CSRFToken},
        url: "/post/ajax",
        data: {postID: postID, operation: 'GET', goal: 'DISLIKE'},
        success: function (data){
            //alert(data);
            post.text(data);
        }
    })
}



function setLikes(postID, userID){
    const post = $(`#` + postID.toString() + `-likes`);
    $.post({
        headers: {'X-CSRFToken': CSRFToken},
        url: "/post/ajax",
        data: {postID: postID, userID: userID, operation: 'SET', goal: 'LIKE'},
        success: function (data){
            //alert(data);
            post.text(data);
        }
    })
}



function setDislikes(postID, userID){
    const post = $(`#` + postID.toString() + `-dislikes`);
    $.post({
        headers: {'X-CSRFToken': CSRFToken},
        url: "/post/ajax",
        data: {postID: postID, userID: userID, operation: 'SET', goal: 'DISLIKE'},
        success: function (data){
            //alert(data);
            post.text(data);
        }
    })
}



// AJAX call for adding and removing a follow
function setFollow(followerID, followedID){

}



const retrieveProfileFollows = (profileID) => {
    // TODO
}



//AJAX call for deleting a post
function deletePost(postID){

}



/* This function copies to the clipboard a link to the post with the specified post ID. */
const copyPostLink = (postID) => {
    navigator.clipboard.writeText(window.location.host + "/post/" + postID);
};