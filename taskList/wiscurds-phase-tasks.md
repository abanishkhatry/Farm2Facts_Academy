---
layout: default
title: "Tasks by Phase"
---

# Tasks by Phase

The concrete work for each WISCURDS phase, in checklist form. This is the "what do I actually do" view. For why a phase exists and how it fits the arc of the program, open the matching card on [Project Milestones]({{ site.baseurl }}/taskList/wiscurds-key-milestones).

From Phase 2 onward the four students split into **two teams of two**, each on its own project:

- **Project A -- Admin Dashboard.** Works on the platform's own data in the local database.
- **Project B -- Wisconet API.** Works on the external data source and the Market Profile.

---

## Phase Summary

| Phase | Focus | Deliverable |
| --- | --- | --- |
| [0](#phase-0-tasks) | Onboarding and team setup | Accounts and both repos running locally |
| [1](#phase-1-tasks) | Understanding the current state | Current State Understanding Report |
| [2](#phase-2-tasks) | Data source investigation | A proposal report from each team |
| [3](#phase-3-tasks) | Data cleaning and feature integration | Cleaned and extended database; new Market Profile tab |
| [4](#phase-4-tasks) | Data analytics and usability testing | Agreed visualizations implemented; evaluation and testing results |
| [5](#phase-5-tasks) | Documentation and handoff | Final documentation and handoff report |

---

<details id="phase-0-tasks" class="section-card" markdown="1">
<summary>Phase 0: Onboarding and Team Setup</summary>

Everyone does all of this. Nothing else starts until it is done.

- [ ] Create a GitLab account on your `@wisc.edu` email and send us your username.
- [ ] Confirm you have access to both repos once permissions are granted.
- [ ] Clone and run the frontend locally. See the [Frontend guide]({{ site.baseurl }}/docs/guides/FRONTEND_GUIDE).
- [ ] Clone and run the backend locally. See the [Backend guide]({{ site.baseurl }}/docs/guides/BACKEND_GUIDE).
- [ ] Read the [Development Structure Overview]({{ site.baseurl }}/taskList/wiscurds-development-structure) so you know how the pieces fit and how work gets merged.
- [ ] Join the project Slack channel and confirm you know who to contact for what.

[Full phase context]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-0)

</details>

<details id="phase-1-tasks" class="section-card" markdown="1">
<summary>Phase 1: Understanding the Current State</summary>

Still everyone, individually. Build the mental model before changing anything.

- [ ] Explore the frontend codebase: overall structure, main components, how data moves through the Vue app.
- [ ] Explore the backend codebase: Rails structure, models and services, how the Grape API exposes data.
- [ ] Read the ADR in each repo and note the key decisions and their trade-offs.
- [ ] Write the **Current State Understanding Report** covering:
  - [ ] The main components of each repo and what each is responsible for.
  - [ ] How the frontend and backend communicate.
  - [ ] The key architectural decisions from each ADR and why they were made.
  - [ ] Your open questions and anything that stayed unclear.

[Full phase context]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-1)

</details>

<details id="phase-2-tasks" class="section-card" markdown="1">
<summary>Phase 2: Data Source Investigation</summary>

Teams split here. Each team investigates its own data source and ends with a proposal.

### Project A -- Local Database

- [ ] Get phpMyAdmin access. See the [Database section of the Onboarding Plan]({{ site.baseurl }}/STUDENT_ONBOARDING_PLAN#database).
- [ ] Map the schema: what tables exist, how they relate, what each stores.
- [ ] Examine the market and market organization records, and how markets connect to the data collected around them.
- [ ] Assess how active the data is: which markets are submitting, which records are stale or empty.
- [ ] Note data quality problems: gaps, duplicates, malformed entries.

### Project B -- Wisconet API

- [ ] Work through the [LASER Task 2.1 Guide]({{ site.baseurl }}/taskList/task2_1/) to learn the API's structure, endpoints, and field naming.
- [ ] Map how the API is organized: stations, measures, and how data would flow into Farm2Facts.
- [ ] Identify useful data points beyond the watershed data already in use, and evaluate which are worth surfacing.

### Both teams

- [ ] Write a **proposal report** covering the current state of your data source and what needs fixing or introducing. This defines what you build in Phase 3.

[Full phase context]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-2)

</details>

<details id="phase-3-tasks" class="section-card" markdown="1">
<summary>Phase 3: Data Cleaning and Feature Integration</summary>

The first build phase. From here on, every change follows the issue-branch-merge request cycle. See [How Work Moves]({{ site.baseurl }}/taskList/wiscurds-development-structure#how-work-moves).

### Both teams, for every change

- [ ] Work from an assigned GitLab issue.
- [ ] Branch from an up-to-date `dev`, named after the issue.
- [ ] Open a merge request into `dev` and assign it for review.

### Project A -- Clean and Extend the Database

- [ ] Fix the data quality issues from your proposal: stale records, gaps, duplicates, malformed entries.
- [ ] Add new fields or tables where the proposal identified missing data, but only where it holds up against the actual schema and how the data is used. Not every proposed addition has to ship.

### Project B -- Integrate Wisconet into the Market Profile

- [ ] Add a new tab to the Market Profile navigation bar.
- [ ] Pull the data points identified in Phase 2 from the Wisconet API and display them in that tab.
- [ ] Follow the existing frontend patterns so the tab fits the current navigation.

[Full phase context]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-3)

</details>

<details id="phase-4-tasks" class="section-card" markdown="1">
<summary>Phase 4: Data Analytics and Usability Testing</summary>

Both teams follow the same four parts on their own project.

### Part 1: Propose

- [ ] Identify how your data could be processed and which visualizations would communicate it best.
- [ ] For each one, state what it shows, who it helps, and why it belongs on the platform.
- [ ] Review the proposal with the Market and Research team. Their input decides what gets built.

### Part 2: Implement

- [ ] Build the agreed processing and visualizations into your project: the Admin Dashboard for Project A, the Market Profile for Project B.
- [ ] Keep to the same issue-branch-merge request flow from Phase 3.

### Part 3: Usability Evaluation

- [ ] Run usability evaluations with all members of the Kaufman Lab on the features your team built.
- [ ] Where feasible, run the same evaluation with the markets themselves.
- [ ] Record the feedback in a form the team can act on: what worked, what confused people, what should change.

### Part 4: Functionality Testing

- [ ] Test the functionality delivered in every prior phase, across both projects.
- [ ] Cover the data cleaning, new fields and tables, the Wisconet integration, and the analytics, including edge cases and unexpected input.
- [ ] Log every bug as an issue so it can be tracked and fixed through the normal flow.

[Full phase context]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-4)

</details>

<details id="phase-5-tasks" class="section-card" markdown="1">
<summary>Phase 5: Documentation and Handoff</summary>

Each team documents its own project so the next cohort can pick it up.

- [ ] Document what your team built: the changes to the database or platform, how the features work, and what a future developer needs in order to extend them.
- [ ] Describe the process from investigation to proposal to implementation, so the reasoning survives alongside the code.
- [ ] Note any open issues, known limitations, and unfinished ideas.
- [ ] Put the documentation somewhere the team can actually find it.
- [ ] Submit the **final report**: the process and your team's involvement, an overview of what was built and how it works, and your reflections on what went well, what you liked, what could have been better, and what you would recommend going forward.

[Full phase context]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-5)

</details>
