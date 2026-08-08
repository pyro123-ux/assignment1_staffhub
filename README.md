# StaffHub Starter Application

This is the starter application for the IT2512 Practical Assignment: Secure Application Project.

The application is intentionally simple. It is provided so that you can run, inspect, secure, test, and extend a StaffHub-style Flask application.

Do not assume that the starter application is already secure or complete. You are responsible for reviewing the code, improving security controls, implementing your assigned feature variation, testing your work, and explaining your decisions.

## 0. Implementation Status (this submission)

Assigned variation: **Variation E — Basic Audit Event Viewer**.

- Common core security controls have been implemented and tested: authentication/session checks on all protected routes, role-based access control and ownership/department scope checks on records, server-side validation and allowlist checks on record submission, safe display (stored XSS on record descriptions fixed), and consistent 400/403/404/500 error handling.
- Variation E is implemented and integrated: an `/audit` route and Audit Log page, reachable from the dashboard and navigation for Manager and Admin roles only, with server-side allowlist/date validation on all filters and department scope enforced for Managers regardless of client-submitted filter values.
- The audit log is not seed-data-only: the application writes real audit events at the following points, in addition to the original seeded rows, so the viewer reflects genuine application activity:
  - failed login attempts (wrong password, or unknown username);
  - record submissions rejected by server-side validation;
  - record views blocked by the ownership/department scope check;
  - attempts to open the audit event viewer by a role without permission (Employee).
- See the project's Git history for the progressive development record (common core, then variation route, then variation template/UI, then live audit logging, then testing, then cleanup).

## 1. Application Overview

StaffHub is an internal web application used by employees, managers, and administrators.

The starter application currently includes:

- login and logout;
- a dashboard, including an Audit Log entry point for Manager/Admin roles;
- record submission, with server-side validation and allowlist checks;
- record listing and record details, scoped by role/ownership/department;
- a basic profile page;
- an audit event viewer (`/audit`), restricted to Manager and Admin roles, with
  filtering by event type, severity, department, and date range.

Your assignment may require you to create or modify routes, templates, forms, database tables, database queries, validation logic, access-control checks, and supporting code.

## 2. Setup Instructions

Open a terminal in this folder and run the following commands.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python init_db.py
python app.py
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python init_db.py
python app.py
```

After starting the app, open the local address shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## 3. Resetting the Database

To reset the starter database to its original seeded state, stop the Flask app and run:

```bash
python init_db.py
```

This will recreate the SQLite database in the `instance` folder.

## 4. Test Accounts

All seeded accounts use the same password:

```text
Password123!
```

| Username | Role | Department |
|---|---|---|
| alice | Employee | HR |
| ben | Employee | IT |
| maya | Manager | IT |
| mina | Manager | HR |
| adam | Admin | Corporate |

Audit Log (`/audit`) access by role: Employee — no access (403); Manager — own department only; Admin — all departments.

## 5. Project Structure

```text
staffhub_starter/
├── app.py
├── config.py
├── init_db.py
├── requirements.txt
├── README.md
├── static/
│   └── styles.css
├── templates/
│   ├── audit_events.html
│   ├── base.html
│   ├── dashboard.html
│   ├── error.html
│   ├── login.html
│   ├── profile.html
│   ├── record_detail.html
│   ├── record_form.html
│   └── records.html
└── instance/
    └── staffhub.db   # created after running init_db.py
```

## 6. Assignment Work

You are expected to secure and enhance the application according to the assignment brief.

Your work should include:

- improving security controls in the common core application;
- implementing your assigned feature variation;
- integrating the assigned feature into the relevant StaffHub workflow;
- creating or modifying necessary pages, routes, forms, database tables, templates, and supporting code;
- producing meaningful test evidence;
- running and interpreting required security tools;
- explaining your security decisions, misuse cases, limitations, and remediation work.

## 7. Variation Integration Pointers

The starter app does not implement the six assigned feature variations for you.

Depending on your assigned variation, you may need to work with areas such as:

| Variation Area | Likely StaffHub Integration Area |
|---|---|
| Record Category Management | Record submission, record listing, record details, manager/admin record review, category management pages |
| Priority Change Request | Record details, priority request submission, user record view, manager/admin review area |
| Department Announcement Feature | Dashboard, announcement page, announcement management pages, navigation |
| Notification Preference Management | Profile/account page, preference page, user-specific preference storage |
| Basic Audit Event Viewer | **Implemented in this submission** — see `/audit` route, dashboard/nav entry, filters, seeded audit events plus live events written by the app itself |
| Support Resource Management | Help/support/resource pages, resource management pages, dashboard/navigation |

Follow the assignment brief and your assigned variation card for the exact expectations.

## 8. Important Notes

- The starter app is for development and learning only.
- The app uses SQLite for simplicity.
- The development secret key in `config.py` is not suitable for production use.
- You should not submit only cosmetic changes.
- You should not submit code that you cannot explain during the Demo and Q&A.
- You should keep your work organised and update your README or setup notes if your changes affect how the app is run.

## 9. Suggested Development Practice

You are encouraged to use Git or a clear change log.

Useful commit or change-log milestones include:

- initial starter app setup;
- common security improvements;
- assigned variation database or route changes;
- assigned variation template or form changes;
- testing and remediation changes;
- final submission cleanup.
