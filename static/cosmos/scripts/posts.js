function getBoth(postID){
    getLikes(postID);
    getDislikes(postID);
}

function getLikes(postID){
    var post = $(`#` + postID.toString() + `-likes`);
    $.post({
        url: "/post/ajax",
        data: {postID: postID, operation: 'GETLIKES'},
        success: function (data){
            //alert(data);
            post.text(data);
        }
    })
}

function getDislikes(postID){
    var post = $(`#` + postID.toString() + `-dislikes`);
    $.post({
        url: "/post/ajax",
        data: {postID: postID, operation: 'GETDISLIKES'},
        success: function (data){
            //alert(data);
            post.text(data);
        }
    })
}

function setLikes(postID, userID){
    var post = $(`#` + postID.toString() + `-likes`);
    $.post({
        url: "/post/ajax",
        data: {postID: postID, userID: userID, operation: 'SETLIKES'},
        success: function (data){
            //alert(data);
            post.text(data);
        }
    })
}

function setDislikes(postID, userID){
    var post = $(`#` + postID.toString() + `-dislikes`);
    $.post({
        url: "/post/ajax",
        data: {postID: postID, userID: userID, operation: 'SETDISLIKES'},
        success: function (data){
            //alert(data);
            post.text(data);
        }
    })
}