### An assignment completed in class and expanded upon to deepen my understanding on Passport.js' various authentication strategies.

<br/>  


#### **Usage:**
1. Type `npm install` in a command-line interpreter in the same location that this directory is located.  
2. [Create a new OAuth application on GitHub.](https://github.com/settings/applications/new) (Homepage URL is `http://localhost:8000` and Authorization callback URL is `http://localhost:8000/auth/github/callback`)
3. Copy and paste the `Client ID` and `Client secrets` that you see on the GitHub web page to `.env`, located in the root directory. 
4. Type in `node server.js` or `nodemon server.js` in a command-line interpreted program in the root directory.
5. Type in the URL `http://localhost:8000/auth/login` in your web browser.
6. Click either `Login with GitHub` (GitHub strategy) or `Login` (local strategy).  
Note: Local strategy login information can be found in `models/userModel.js`. (*DO NOT USE in production* without hashing and migrating the sensitive information to a database beforehand, storing passwords in plain text files is extremely unsecure)
   
#### **Features:**  
-Login (local strategy method)  
-Login with GitHub (GitHub authentication strategy method)  
-Set registered users' role (user or admin)  
-Admin-only page at `http://localhost:8000/admin` (Registered accounts with the role of `user` will be redirected back to `http://localhost:8000/dashboard`)  
-Generate a unique session ID for each logged in account  
-Assign each registered account with a unique user ID  
-Ability for admins to revoke any logged in session (user will be forcefully signed out and will need to login again to access the site's resources)


#### **Programs required**:
- Node.js v14.x.x LTS
- Visual Studio Code (Optional)
- A web browser 
- A command-line interpreter program (Windows PowerShell, Command Prompt, Windows Terminal, etc.)


#### **Node library dependencies:**
- Simply type `npm install` in a command-line interpreter in the same location that this directory is located  


