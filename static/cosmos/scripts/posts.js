//
//* Does AJAX database calls related to likes and dislikes
//
//* AJAX calls conform to the standard below
//* operation can be either 'GET' or 'SET', meaning a getter or setter db operation
//* goal can be either 'LIKE' or 'DISLIKE', meaning what is the above operation acting on
//

//grab the CSRF Token
const CSRFToken = $('meta[name="_token"]').attr('content')

//for page initialization
function getBoth(postID){
    getLikes(postID);
    getDislikes(postID);
}

function getLikes(postID){
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

function getDislikes(postID){
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

//AJAX call for deleting a post
function deletePost(postID){

}

// Copies link to clipboard
function copyLink(copyLink){
    navigator.clipboard.writeText(copyLink.toString())
}
