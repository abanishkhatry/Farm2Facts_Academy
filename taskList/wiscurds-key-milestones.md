---
layout: default
title: "Key Milestones draft"
---

# Key Milestones draft

This page lays out the WISCURDS program as a series of phases. Each phase below is its own card. Open a card to see what that phase covers and what you are expected to complete before moving on.

---

<details class="section-card" markdown="1">
<summary>Phase 0: Project Onboarding and Team Setup</summary>

This phase gets you set up with the codebase, the accounts you need, and the ways we communicate as a team. Work through both sections before starting any development work.

### Repositories and Local Setup

Farm2Facts is split across two repositories, and you will work in both over the course of the program.

- **Frontend:** <a href="https://git.doit.wisc.edu/at-trad/farm2facts-frontend" target="_blank" rel="noopener noreferrer">Farm2Facts Frontend</a> -- a Vue 3 data collection and reporting platform.
- **Backend:** <a href="https://git.doit.wisc.edu/at-trad/farmers-coalition" target="_blank" rel="noopener noreferrer">Farm2Facts Backend</a> -- a Rails 6.1 metrics API and web interface.

Step-by-step instructions for cloning each repo and running it locally already live in our onboarding materials. Follow the guide for each repo rather than duplicating the steps here:

- [Frontend setup guide]({{ site.baseurl }}/docs/guides/FRONTEND_GUIDE)
- [Backend setup guide]({{ site.baseurl }}/docs/guides/BACKEND_GUIDE)
- [Student Onboarding Plan]({{ site.baseurl }}/STUDENT_ONBOARDING_PLAN) -- start here for the full picture of Git, the repos, and database access.

Both repositories are hosted on **GitLab**, not GitHub. Before you can access them:

1. If you do not already have one, create a GitLab account using your **@wisc.edu email**.
2. Once your account is set up, share your GitLab username or account with us.
3. We will then grant you the permissions you need on both repositories.

You will not be able to clone or push to the repos until these permissions are in place, so complete this step early.

### Communication and Meetings

We use two main channels to stay in touch:

- **Slack** for quick, day-to-day communication. Each project has its own dedicated channel where most conversation happens.
- **Email** for anything more formal or that needs a lasting record.

Know who to reach out to depending on what you need:

- **Development tasks:** Abanish Khatry is your focal point of contact for anything code or task related.
- **Professional guidance:** Garrett Smith is the professional point of contact.
- **Administrative matters:** Alfonso Morales handles administrative questions.

For meetings:

- **Until the Fall semester begins,** we meet **weekly and virtually** for progress check-ins.
- **Once Fall begins,** we will set the meeting time and frequency together, based on everyone's availability.

</details>

<details class="section-card" markdown="1">
<summary>Phase 1: Understanding F2F and Its Repositories' Current State</summary>

With your environment set up from Phase 0, this phase is about building a clear mental model of how Farm2Facts works today, before you change anything. The goal is to understand the current state of both repositories and how their pieces fit together.

### What to Study

Work through both repositories and get familiar with how each is structured and what its main components do.

- **Frontend repo:** Understand the overall structure, the main components, and how data moves through the Vue 3 application. Start from the [Frontend setup guide]({{ site.baseurl }}/docs/guides/FRONTEND_GUIDE) and explore the codebase alongside it.
- **Backend repo:** Understand the Rails 6.1 structure, the models and services, and how the Grape API exposes data to the frontend. Start from the [Backend setup guide]({{ site.baseurl }}/docs/guides/BACKEND_GUIDE) and explore the codebase alongside it.

Each repository contains an **ADR (Architecture Decision Record) document**. Use these as your primary reference for understanding why the system is built the way it is. The ADRs explain the key architectural decisions, the trade-offs behind them, and the context you cannot get from reading code alone. Read the ADR in each repo and let it guide how you interpret the components you explore.

### Deliverable

A **Current State Understanding Report**. In it, capture your understanding of both repositories as they stand today:

- The main components of the frontend and backend and what each is responsible for.
- How the frontend and backend communicate.
- The key architectural decisions from each ADR and why they were made.
- Any open questions or areas that were unclear as you explored.

This report is your reference point for the rest of the program, and it shows us that you have a solid grasp of the system before you begin contributing to it.

</details>
