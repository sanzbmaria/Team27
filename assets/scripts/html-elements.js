// HTML ELEMENTS

// TODO: implement boards and likes
// Aside: Contains profile info, all boards, and likes
class Aside extends HTMLElement {
	connectedCallback() {
		this.innerHTML = `
            <div class="offcanvas-header">
                <!-- Title and Close button will only be shown on smaller screens -->
                <h5 class="offcanvas-title" id="staticBackdropLabel">Preferences</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#offcanvasResponsive" aria-label="Close"></button>
                <!-- This will be shown everywhere-->
                </div id="user-profile">
                    <user-info class="profile-info"></user-info>
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
                `;
	}
}

// TODO: Profile: User should be able to change name, dept and pic
class Profile extends HTMLElement {
	connectedCallback() {
		this.innerHTML = `
                <div id="settings"></div>
                    <button type="button" class="btn" aria-label="Settings" id="user-settings" ><i class="bi bi-pen"></i></button>
                </div>
                <div class="scale-profile-pic">
                    <img src="assets/images/blank-profile-pic.jpg" class="profile-pic alt="profile-pic">
                </div>
                <div class="profile-info">
                    <p><b>Name</b></p>
                    <p><b>Department</b></p>
                </div>`;
	}
}

class LoginRegisterMenu extends HTMLElement {
	connectedCallback() {
		this.innerHTML = `
            <div>
              <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
                  <li class="nav-item" role="presentation">
                      <button class="nav-link active" id="pills-home-tab" data-bs-toggle="pill" data-bs-target="#pills-login" type="button" role="tab" aria-controls="pills-login" aria-selected="true">Login</button>
                  </li>
                  <li class="nav-item" role="presentation">
                      <button class="nav-link" id="pills-profile-tab" data-bs-toggle="pill" data-bs-target="#pills-register" type="button" role="tab" aria-controls="pills-register" aria-selected="false">Register</button>
                  </li>
              </ul>
              <div class="tab-content" id="pills-tabContent">
                  <div class="tab-pane fade show active" id="pills-login" role="tabpanel" aria-labelledby="pills-home-tab" tabindex="0">
                      <user-login></user-login>
                  </div>
                  <div class="tab-pane fade" id="pills-register" role="tabpanel" aria-labelledby="pills-register-tab" tabindex="0">
                      <user-register></user-register>
                  </div>
              </div>
            </div>
        `;
	}
}

class Login extends HTMLElement {
	connectedCallback() {
		this.innerHTML = `
        <form>
          <div class="mb-3">
            <!-- Email Input -->
            <label for="exampleInputEmail1" class="form-label">Email</label>
            <input type="email" class="form-control" id="login-input-email" aria-describedby="emailHelp" />
          </div>
          <!-- Password Input -->
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">
              Password
            </label>
            <input type="password" class="form-control" id="login-input-password"
            />
          </div>
          <!-- Submit Button -->
          <button type="submit" class="btn btn-primary" id="login-button" >Login</button>
        </form>
        `;
	}
}

class Register extends HTMLElement {
	connectedCallback() {
		this.innerHTML = `
        <form>
          <div class="mb-3">
            <!-- Email input -->
            <div class="form-outline mb-4">
                <label class="form-label" for="registerEmail">Email</label>
                <input type="email" id="registerEmail" class="form-control" />
            </div>

            <!-- Password input -->
            <div class="form-outline mb-4">
                <label class="form-label" for="registerPassword">Password</label>
                <input type="password" id="registerPassword" class="form-control" />
            </div>

            <!-- Confirm Password input -->
            <div class="form-outline mb-4">
                <label class="form-label" for="registerRepeatPassword">
                    Repeat password
                </label>
                <input type="password" id="registerRepeatPassword" class="form-control"/>
            </div>
          </div>

          <!-- Submit button -->
          <button type="submit" class="btn btn-primary btn-block mb-3">
            Register
          </button>
        </form>
            `;
	}
}

// NewNotices: recient posted notices from the selected notice-boards should be shown here
class NewNotices extends HTMLElement {
	connectedCallback() {
		this.innerHTML = `<div class="title">Notice<i class="bi bi-bell-fill"></i></div>
                <div class="list-group" id="new-notices-list">
                    <notice-post></notice-post>
            </div>`;
	}
}

// SavedNotices: saved notices should be shown here
class SavedNotices extends HTMLElement {
	connectedCallback() {
		this.innerHTML = `
                <div class="title">Saved <i class="bi bi-star-fill"></i></div>
                <div class="list-group" id="saved-notices-list">
                    <notice-post></notice-post>
                    <notice-post></notice-post>
                </div>`;
	}
}
// NoticePost: standard post template
class NoticePost extends HTMLElement {
	connectedCallback() {
		this.innerHTML = `<a href="#" class="list-group-item list-group-item-action" aria-current="true" data-bs-toggle="modal">

                <div class="d-flex w-100 justify-content-between">
                    <div>
                        <h5 class="mb-1 notice-post-title">Notice Title</h5>
                        <sup class="notice-post-board"> Notice Board Name</sup>
                    </div>
                    <small class="notice-post-time">3 days ago</small>
                </div>

            </a> `;
	}
}

// Define elements to use them in the HTML
customElements.define("new-notices", NewNotices);
customElements.define("saved-notices", SavedNotices);
customElements.define("notice-post", NoticePost);
customElements.define("user-info", Profile);
customElements.define("settings-aside", Aside);
customElements.define("user-register", Register);
customElements.define("user-login", Login);
customElements.define("login-register-menu", LoginRegisterMenu);
