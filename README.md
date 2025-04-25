# Welcome to Serious Talk

A full-featured Django discussion forum with user authentication, email verification, post & comment interactions, voting, profiles, and an admin dashboard—all styled with Bootstrap and deployed on Heroku.

[![Serioustalk-mockup.png](https://i.postimg.cc/CLjywfBL/Serioustalk-mockup.png)](https://postimg.cc/BXQ7gbBd)

## 📖 Overview
Serious Talk is a modern, responsive forum application where users can register, verify their email, create and interact with posts, vote, comment, and manage profiles. Administrators can moderate via a comprehensive admin interface.

**Serious Talk** is a modern, responsive Django forum application built for high-quality, in-depth conversation. Whether you’re sharing code tips, UI/UX best practices, or community announcements, Serious Talk provides the tools you need:

- **Post & Comment** – Create, edit, comment on, and vote posts in real time (AJAX).  
- **Email-Verified Accounts** – Mandatory email confirmation via `django-allauth`.  
- **Custom Profiles** – Per-user profile pages, full name, avatar, and post history.  
- **Categories & Tags** – Organize content into high-level categories and (future) subcategories.  
- **Admin & Permissions** – Django admin with groups (staff, moderators) and custom user management.  
- **Static Asset Pipeline** – WhiteNoise + ManifestStaticFilesStorage, Heroku-ready.  
- **Two-Step ENV Overlay** – Separate `.env` and `.env.production` with `django-environ`.  
- **Secure by Default** – HSTS, X-Frame-Options, secure cookies, and CSRF protection everywhere.  

---

## ✅ Features

### Existing Features

- **User Registration & Authentication**  
  Secure signup/login via **django-allauth**, with username and email support.  
- **Email Confirmation**  
  Mandatory verification emails, customizable templates.  
- **Post Lifecycle**  
  Create, edit, delete posts with rich Bootstrap-styled forms.  
- **Threaded Comments**  
  Reply to posts and comments in threads.  
- **Upvote/Downvote**  
  AJAX-powered voting system with real-time score updates.  
- **Custom Profile Pages**  
  Per-user pages at `/users/<username>/` showing their info & posts.  
- **Category Management**  
  Top-level categories, easy admin CRUD, human-readable names.  
- **Responsive Design**  
  Built with Bootstrap 5 for mobile, tablet, and desktop.  
- **Security Best Practices**  
  HTTPS, HSTS, CSRF, X-Frame-Options, secure cookies.  
- **Heroku-Ready Deployment**  
  WhiteNoise, ManifestStaticFilesStorage, `Procfile`, Postgres support.

### Future Features

- **Tagging System**  
  Allow users to tag posts for finer organization and filtering.  
- **Search & Filtering**  
  Full-text search across posts, comments, and users.  
- **Real-Time Notifications**  
  Alert users to replies, mentions, and votes via WebSockets.  
- **Markdown / Rich Text**  
  Support for Markdown or WYSIWYG editor in posts and comments.  
- **Media Uploads**  
  Image and file attachments on posts/comments.  
- **OAuth & Social Logins**  
  Google, GitHub, Facebook integration via allauth.  
- **Private Messaging**  
  One-to-one chats between registered users.  
- **Dark Mode**  
  Optional night-friendly color scheme.

---

## 🎮 Full Feature Walkthrough

Below is a step-by-step guide to every user flow and UI component in Serious Talk. For each section, insert your real screenshot in place of the placeholder.

---

### 🔹 1. Global Navigation & Layout

- **Responsive Navbar**  
  - Brand logo links home  
  - **Unauthenticated**: Home, Login, Register  
  - **Authenticated**: Home, New Post, My Profile, Logout  
- **Footer**  
  - Copyright, links to About/Contact  

![1. Navbar – Home vs. Authenticated View](docs/images/1_navbar.png)  
*Figure: Responsive navbar in desktop & mobile view.*

---

### 🔹 2. Homepage & Post Listing

- **Latest Posts** displayed as Bootstrap cards  
- Card shows title, author (linked to profile), timestamp, vote score  
- **Voting** controls appear for logged-in users (+1 / −1)  
- **“No posts”** empty state  

![2. Homepage with post cards](docs/images/2_homepage.png)  
*Figure: Homepage listing posts.*

---

### 🔹 3. Search & Category Filtering

- **Search bar** in navbar to filter posts by keyword  
- **Category dropdown** allowing filtering by category  

![3. Search & Categories](docs/images/3_search_category.png)  
*Figure: Searching “django” or selecting “Python” category.*

---

### 🔹 4. Registration Flow

1. **Sign Up**  
   - Fields: Username, Email, Password, Confirm Password  
2. **“Check Your Email”** page after submit  
3. **Confirmation Email** arrives with link  
4. **Email Confirmed** landing page  

![4a. Register Form](docs/images/4a_register_form.png)  
![4b. Email Sent Confirmation](docs/images/4b_email_sent.png)  
![4c. Email Confirm Success](docs/images/4c_email_confirmed.png)  
*Figures: Registration ➔ Confirmation prompt ➔ Success.*

---

### 🔹 5. Authentication & Rate-Limiting

- **Log In** page, redirects to `next` URL if provided  
- **Password Reset**: request, email, reset form, completion  
- **Rate-limiting**: Blocks after 5 failed attempts/5 min  

![5a. Login Page](docs/images/5a_login.png)  
![5b. Password Reset](docs/images/5b_password_reset.png)  
![5c. Rate-Limit Error](docs/images/5c_rate_limit.png)  
*Figures: Login, password reset flow, rate-limit error message.*

---

### 🔹 6. Post Details & Interactions

- **Detail View**: full post content, author, timestamp  
- **Comments**: threaded, add/edit/delete own comments  
- **Voting**: live AJAX updates  
- **Edit/Delete** buttons for post owner  

![6a. Post Detail](docs/images/6a_post_detail.png)  
![6b. Comments & Voting](docs/images/6b_comments_votes.png)  
*Figures: Post detail with comments and vote buttons.*

---

### 🔹 7. Creating & Managing Posts

- **New Post** form: Title, Body, Category, Tags  
- **Edit Post** with pre-filled form  
- **Delete Confirmation**  

![7a. New Post Form](docs/images/7a_new_post.png)  
![7b. Edit Post](docs/images/7b_edit_post.png)  
*Figures: Create and edit post screens.*

---

### 🔹 8. User Profiles

- **Profile Page** shows:  
  - Avatar (if implemented), Full Name (or username), Email verification status  
  - List of user’s posts (linked to detail)  
- **Edit Profile**: form for First Name & Last Name  

![8a. User Profile](docs/images/8a_profile_view.png)  
![8b. Edit Profile](docs/images/8b_edit_profile.png)  
*Figures: Public profile view and edit form.*

---

### 🔹 9. Admin & Moderation

- **Django Admin** (secured at `/admin/`)  
- **Categories**: add/edit/delete with slug auto-populate  
- **Custom User Management**: lock, delete accounts  
- **EmailAddress** admin shows verification status  

![9a. Admin Dashboard](docs/images/9a_admin_dashboard.png)  
![9b. Custom User Management](docs/images/9b_manage_users.png)  
*Figures: Standard admin and custom moderation views.*

---

### 🔹 10. Static & Media Handling

- **Whitenoise** for static asset compression & manifest  
- **Media uploads** saved under `mediafiles/` and served in development  

![10. Static & Media Example](docs/images/10_static_media.png)  
*Figure: Post with uploaded image (if applicable).*

---

### 🔹 11. Error Pages & Edge Cases

- **Custom 404** and **500** pages match site style  
- Graceful empty states (no posts, no comments)  

![11a. 404 Page](docs/images/11a_404.png)  
![11b. Empty State](docs/images/11b_empty_state.png)  
*Figures: 404 page and an empty posts view.*

---

### 🔹 12. Mobile Responsiveness

- Fully responsive layouts via Bootstrap grid  
- Collapsible navbar toggler on small screens  

![12. Mobile View](docs/images/12_mobile.png)  
*Figure: Homepage on mobile with collapsed menu.* 

---

## 🛠 Tech Stack
| Component               | Technology                       |
|-------------------------|----------------------------------|
| Backend Framework       | Django 4.2                       |
| Auth & Email            | django-allauth 65.7              |
| Database (Prod/Local)   | PostgreSQL / SQLite              |
| Static Files            | Whitenoise, Bootstrap 5          |
| Deployment              | Heroku-24 stack, Gunicorn        |
| Language                | Python 3.12                      |
| Version Control         | Git, GitHub                      |

---

## 🚀 Installation & Setup
```bash
git clone https://github.com/creanorcode/project_4.git
cd project_4
python3 -m venv .venv
source .venv/bin/activate    # macOS/Linux
pip install -r requirements.txt
```

### 🔧 Configuration
Copy `.env.example` to `.env` and fill in secrets:
```dotenv
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=https://localhost,https://127.0.0.1
USE_PRODUCTION_ENV=False
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST=smtp.strato.com
EMAIL_PORT=587
EMAIL_HOST_USER=you@domain.com
EMAIL_HOST_PASSWORD=your-password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=no-reply@domain.com
```

---

## 🗄 Database & Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ▶️ Running Locally
```bash
python manage.py runserver
```
Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ☁️ Deployment

### Heroku
1. `heroku login` & `heroku create your-app`
2. Set Config Vars:
   ```bash
   heroku config:set NODE_ENV=production \
     DJANGO_DEBUG=False \
     DJANGO_SECRET_KEY=... \
     DJANGO_ALLOWED_HOSTS=your-app.herokuapp.com \
     CSRF_TRUSTED_ORIGINS=https://your-app.herokuapp.com \
     DATABASE_URL=postgres://... \
     EMAIL_HOST=... \
     EMAIL_PORT=... \
     EMAIL_HOST_USER=... \
     EMAIL_HOST_PASSWORD=... \
     EMAIL_USE_TLS=True \
     DEFAULT_FROM_EMAIL=you@domain.com
   ```
3. Ensure `DATABASE_URL` points to your Heroku Postgres addon.
4. `git push heroku main` & `heroku open`

### Custom Domain
- Add your domain in Heroku
- In DNS provider, CNAME `www` → `<app>.herokudns.com`
- Setup ALIAS/URL-redirect for root domain
- Add domain to `DJANGO_ALLOWED_HOSTS` & `CSRF_TRUSTED_ORIGINS`

---

## 🎨 Styling & Templates
- **Base Layout**: `posts/templates/posts/base.html` with Bootstrap and navbar logic.
- **Allauth Overrides**: Copy allauth templates into `templates/account/`:
  - `login.html`, `signup.html`, `logout.html`
  - Password reset flow (`password_reset.html`, etc.)
  - Email confirmation pages:
    - `email_confirmation_sent.html`
    - `email_confirm.html`
  - Email templates in `templates/account/email/`:
    - `email_confirmation_subject.txt`
    - `email_confirmation_message.txt`
    - (Optional) `email_confirmation_message.html`
- **Custom Filters**: `add_class` filter to inject Bootstrap classes.

---

## 🙋‍♂️ User Profiles
- **Profile View**: `profile(request, username)` shows user info, posts, and email verification status via `allauth.account.models.EmailAddress`.
- **Edit Profile**: Users can update first & last name using `edit_profile` view and form.
- Templates in `posts/templates/posts/profile.html` and `edit_profile.html`.

---

## 📧 Email & Verification
- **Settings**:
  ```python
  ACCOUNT_EMAIL_REQUIRED = True
  ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
  ACCOUNT_LOGIN_METHODS = {'username', 'email'}
  ACCOUNT_SIGNUP_FIELDS = ['username*','email*','password1*','password2*']
  ACCOUNT_RATE_LIMITS = {'login_failed': '5/5m/key'}
  ```
- **Flow**: allauth sends confirmation email; user clicks link to `email_confirm.html`.
- **EmailAddress Model**: displays verified status in profile and admin.

---

## 🛡 Admin & Permissions
- **Admin URL**: `path('admin/', admin.site.urls)` only in root `urls.py`.
- **Category Model**: added `slug` field; auto-populated in `CategoryAdmin` via `prepopulated_fields`.
- **Groups & Staff**: assign permissions and create moderator roles.

---

## 🐞 Bugs & Fixes
A chronological list of major fixes:
- **Staticfiles manifest** missing entries → switched to `CompressedManifestStaticFilesStorage`.
- **Template syntax**: closed all `{% if %}` and `{% for %}` tags.
- **Allauth settings**: migrated deprecated settings to new `ACCOUNT_*` names.
- **Rate limits**: fixed `ACCOUNT_RATE_LIMITS` format to strings (`'5/5m/key'`).
- **Duplicate admin namespace**: removed extra `admin/` route in `posts/urls.py`.
- **CategoryAdmin slug**: added `slug` field to `Category` model and migrations.
- **Register view**: switched to allauth signup and fixed `authenticate` usage.
- **Profile email status**: read from `EmailAddress` model and passed `email_verified` context.
- **Syntax fixes**: added missing commas in context dicts.

---

## 🚧 Future Enhancements
- Live AJAX voting and comments.
- Rich text editor integration (CKEditor/TinyMCE).
- Image uploads with S3 or Cloudinary.
- WebSockets for real-time notifications.
- Analytics dashboard for site metrics.

---

## Credit
- In this section, we provide acknowledgements for resources and inspiration.

### Content

### Media

---

## Acknowledgements


---

*Built with ❤️ by the Serious Talk Team*

