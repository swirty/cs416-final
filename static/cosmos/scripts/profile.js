const CSRFToken = $('meta[name="_token"]').attr('content')

$(document).ready(() => {

    /* This code implements custom data attributes for HTML elements which temporarily *
     * changes their inner text and disables them before reenabling them after a short *
     * delay.                                                                          */
    disableDelayElements = $('[data-cosmos-disable-delay]')
    for(let index in disableDelayElements) {
        const element = disableDelayElements[index]
        element.addEventListener('click', () => {
            const oldInnerText = element.innerText
            if(element.dataset.cosmosDisableDelay)
                element.innerText = element.dataset.cosmosDisableDelay
            element.setAttribute("disabled", "1")
            setTimeout(() => {
                element.innerText = oldInnerText
                element.removeAttribute("disabled")
            }, parseInt(element.dataset.cosmosDisableDelayDuration))
        })
    }


});



const copyProfileLink = (profileID) => {
    navigator.clipboard.writeText(window.location.host + "/user/" + profileID);
};



const followUser = (userID) => {
    $.post({
        headers: {'X-CSRFToken': CSRFToken},
        // TODO
    })
}