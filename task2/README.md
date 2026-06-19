
Task 2 — Authentication Overview
================================

Key files
---------
- [task2/app.py](task2/app.py) — main Flask app and route handlers
- [task2/templates/login.html](task2/templates/login.html) — login form
- [task2/templates/register.html](task2/templates/register.html) — registration form
- [task2/templates/dashboard.html](task2/templates/dashboard.html) — protected dashboard

Authentication Workflow
-----------------------
1. Registration
	- User submits the registration form (`/register`) with email and password.
	- Server validates input, hashes the password (e.g. bcrypt) and stores the user record in the database.
	- On success the server redirects the user to the login page.

2. Login
	- User submits credentials to `/login`.
	- Server locates the user by email and verifies the password against the stored hash.
	- If verification succeeds, the server creates an authenticated session for the user:
	  - Cookie-based sessions: server stores the user id in the session and returns a session cookie (set `HttpOnly`, `Secure` in production, and `SameSite` as appropriate).
	  - Token-based (optional): server returns a signed JWT which the client stores and sends on subsequent requests.
	- The user is redirected to a protected page such as `/dashboard` after login.

3. Session & Protected Routes
	- Protected routes check the session or token to confirm authentication before granting access.
	- If a request is unauthenticated, the app redirects to the login page.
	- Typical check: confirm `session.get('user_id')` (cookie session) or verify JWT signature and expiration.

4. Logout
	- Hitting `/logout` clears the server-side session or instructs the client to remove the token, then redirects to `/login`.

Implementation details (what `app.py` uses)
------------------------------------------
- Password hashing: `app.py` uses `werkzeug.security.generate_password_hash` to hash passwords and `check_password_hash` to verify them on login.
- Session storage: on successful login the app sets `session['user'] = user['username']` and uses that key to track authentication state.
- Protected route check: the `/dashboard` route verifies authentication with `if 'user' not in session: redirect('/login')`.
- Database: users are stored in a local SQLite file `database.db` in the `task2` folder with a `users(username, password)` table.
- Secret key: `app.secret_key` is set in `app.py` (currently a static string in development). Replace with an environment-provided secret in production.

Frontend 
-------------
- `login.html` and `register.html` present simple forms that POST to the corresponding endpoints.
- Server-side templates conditionally render navigation (login/register vs. logout/dashboard) based on the authenticated state.
