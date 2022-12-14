$(document).ready(() => {

    /* This code implements custom data attributes for HTML elements which temporarily *
     * changes their inner text and disables them before reenabling them after a short *
     * delay.                                                                          */
    disableDelayElements = $('[data-cosmos-disable-delay]')
    for(let index in disableDelayElements) {
        const element = disableDelayElements[index]
        element.addEventListener('click', () => {
            const oldInnerHTML = element.innerHTML
            if(element.dataset.cosmosDisableDelay)
                element.innerHTML = element.dataset.cosmosDisableDelay
            element.setAttribute("disabled", "1")
            setTimeout(() => {
                if(element.dataset.cosmosDisableDelay)
                    element.innerHTML = oldInnerHTML
                element.removeAttribute("disabled")
            }, parseInt(element.dataset.cosmosDisableDelayDuration))
        })
    }


});