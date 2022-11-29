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

// Define elements to use them in the HTML
customElements.define("new-notices", NewNotices);
customElements.define("notice-post", NoticePost);
customElements.define("user-info", Profile);
customElements.define("settings-aside", Aside);
customElements.define("user-register", Register);
customElements.define("user-login", Login);
customElements.define("login-register-menu", LoginRegisterMenu);

// Test
customElements.define("flask-test", FlaskTest);
