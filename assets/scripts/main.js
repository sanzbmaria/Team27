// HTML ELEMENTS

// TODO: implement boards and likes
// Aside: Contains profile info, all boards, and likes
class Aside extends HTMLElement{
    connectedCallback(){
        this.innerHTML =`
            <div class="offcanvas-header">
                <!-- Title and Close button will only be shown on smaller screens -->
                <h5 class="offcanvas-title" id="staticBackdropLabel">Preferences</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvasResponsive" aria-label="Close"></button>
                <!-- This will be shown everywhere-->
                </div>
                    <profile-info></profile-info>
                    <!-- Todo: implement -->
                    <div class="boards">
                        <div class="title">Boards<i class="bi bi-list"></i></div>
                        <div id="list-boards"></div>
                    </div>
                    <div class="likes">
                        <div class="title">Likes<i class="bi bi-list"></i></div>
                        <div id="list-likes"></div>
                    </div>
                </div>
            </div>
                `
    }
}

// TODO: Profile: User should be able to change name, dept and pic
class Profile extends HTMLElement {
    connectedCallback(){
        this.innerHTML =
            `
            <div class="profile">
                <div id="settings"></div>
                    <i class="bi bi-pen"></i>
                </div>
                <div class="profile-pic">
                    <img src="assets/images/blank-profile-pic.jpg" alt="profile-pic">
                </div>
                <div class="profile-info">
                    <p><b>Name</b></p>
                    <p><b>Department</b></p>
                </div>
            </div>`
    }
}


// NewNotices: recient posted notices from the selected notice-boards should be shown here
class NewNotices extends HTMLElement {
    connectedCallback(){
        this.innerHTML =
            `<div class="title">Notice<i class="bi bi-bell-fill"></i></div>
                <div class="list-group">
                    <notice-post></notice-post>
            </div>`
    }
}

// SavedNotices: saved notices should be shown here
class SavedNotices extends HTMLElement {
    connectedCallback(){
        this.innerHTML =
            `
                <div class="title">Saved <i class="bi bi-star-fill"></i></div>
                <div class="list-group">
                    <notice-post></notice-post>
                    <notice-post></notice-post>
                </div>`
    }
}
// NoticePost: standard post template
class NoticePost extends HTMLElement {
    connectedCallback(){
        this.innerHTML =
            `<a href="#" class="list-group-item list-group-item-action" aria-current="true">
                <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">List group item heading</h5>
                    <small>3 days ago</small>
                </div>
                <p class="mb-1">Some placeholder content in a paragraph.</p>
                <small>And some small print.</small>
            </a> `
    }
}

// Define elements to use them in the HTML
customElements.define('new-notices', NewNotices)
customElements.define('saved-notices', SavedNotices)
customElements.define('notice-post', NoticePost)
customElements.define('profile-info', Profile)
customElements.define('settings-aside', Aside)