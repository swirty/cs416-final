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
        url: "/post/react",
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
        url: "/post/react",
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
        url: "/post/react",
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
        url: "/post/create",
        data: {postID: postID, userID: userID, operation: 'SET', goal: 'DISLIKE'},
        success: function (data){
            //alert(data);
            post.text(data);
        }
    })
}



//AJAX call for deleting a post
const deletePost = (postID, userID) => {
    const post = $("#post-body-" + postID)
    $.post({
        headers: {'X-CSRFToken': CSRFToken},
        url: "/post/delete",
        data: {postID: postID, userID: userID},
        success: function (data){
            if(parseInt(data) === 0) {
                post.attr('style', 'color: red').text("Post Deleted!")
            }
        }
    })
}



/* This function copies to the clipboard a link to the post with the specified post ID. */
const copyPostLink = (postID) => {
    navigator.clipboard.writeText(window.location.host + "/post/" + postID);
};



/* This function makes an AJAX request which retrieves a number of posts that come after the specified ID. */
const retrieveMorePosts = (afterID, userID, number) => {
    $.post({
        headers: {'X-CSRFToken': CSRFToken},
        url: "/post/loadmore",
        data: {postID: afterID, userID: userID, numberOfPosts: number},
        success: function (data){
            //alert(data);
            $('#load-more-posts-container').remove()
            $('[data-cosmos-post=' + afterID + ']').after(data)
        }
    })
}