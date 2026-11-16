// Shows the (rendered, with clickable links) description of the currently
// selected track below the track dropdown in the proposal form.
const setupTrackDescription = () => {
    const select = document.querySelector("select[name='track']")
    const source = document.getElementById("track-descriptions")
    if (!select || !source) return

    const display = document.createElement("div")
    display.id = "track-description-display"
    display.className = "mt-2"
    const formGroup = select.closest(".form-group")
    const anchor = formGroup ? formGroup.lastElementChild || formGroup : select
    anchor.appendChild(display)

    const update = () => {
        display.innerHTML = ""
        const description = source.querySelector(
            `.track-description[data-track="${CSS.escape(select.value)}"]`,
        )
        if (description) display.appendChild(description.cloneNode(true))
    }
    select.addEventListener("change", update)
    update()
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupTrackDescription)
} else {
    setupTrackDescription()
}
