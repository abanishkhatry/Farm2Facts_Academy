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

<details class="section-card" markdown="1">
<summary>Phase 2: Data Source Investigation</summary>

In this phase the four WISCURDS students split into **two projects, with a team of two on each**. Each team investigates a different data source that feeds the Farm2Facts platform. The goal is to understand what data we have, where it comes from, and what condition it is in before anyone proposes changes.

### Project A: Admin Dashboard -- Local Database Analysis

This team investigates the platform's own data by analyzing the local database.

- **Get access first.** The database access steps are already documented. Follow the [Database section of the Student Onboarding Plan]({{ site.baseurl }}/STUDENT_ONBOARDING_PLAN#database) to reach phpMyAdmin, rather than repeating the steps here.
- **Assess the current state of the database.** Get familiar with the schema: what tables exist, how they relate, and what each one stores.
- **Look at the market records.** Find the records for markets and market organizations. Understand what a market record contains and how markets connect to the data collected around them.
- **Judge how active the data is.** Check how current and complete the records are. Are markets actively submitting data, or are many entries stale or empty? Which markets are active and which are not?
- **Other understanding steps.** Note data quality issues, gaps, duplicates, or anything that looks off as you explore.

### Project B: Getting Data from the Wisconet API

This team investigates an external data source, the Wisconet API. This work overlaps with the LASER program's API task, so use that as a starting point.

- **Reference the LASER API work.** The [LASER Task 2.1 Guide]({{ site.baseurl }}/taskList/task2_1/) walks through exploring the Wisconet API with the browser and Postman. Work through it to build your understanding of the API's structure, endpoints, and field naming.
- **Understand the external source.** Learn how the Wisconet API is organized, what stations and measures it exposes, and how data would flow from it into the Farm2Facts platform.
- **Identify useful data points.** Beyond the watershed data already in use, investigate what other data points the API offers (for example soil temperature, air temperature, and other station measures) and evaluate which of them could be valuable to the Farm2Facts platform and its users.

### Deliverable

Each team produces a **proposal report** covering:

- The **current state** of their data source, based on what they found during their investigation.
- What they see that **needs to be fixed** (data quality issues, gaps, stale records) or **introduced** (new data points, integrations, or improvements).

This proposal is the bridge into the build phases: it defines what each team will actually work on next.

</details>

<details class="section-card" markdown="1">
<summary>Phase 3: Data Cleaning and Feature Integration</summary>

This is the first build phase. Each team turns the proposal from Phase 2 into actual changes in the codebase. Both teams stay on their respective projects.

### Working Flow and Branching Practices

Because this is the first phase where you write code, follow our standard working flow from the start. Both teams work the same way:

- Work is tracked as **issues on the GitLab issue board** and assigned to you. See [How We Work]({{ site.baseurl }}/docs/guides/#how-we-work) for the full issue-to-PR cycle.
- The repos use a four-level branch structure: `main`, `staging`, `dev`, and feature branches. **Never commit directly to `main` or `dev`.** Always branch off an up-to-date `dev` for your work.
- Create one feature branch per issue, named after that issue, for example `feature/issue-12-clean-market-records`. The full branch strategy and commit message rules are in the [Git Workflow Reference]({{ site.baseurl }}/docs/guides/#git-workflow-reference).
- When your work is ready, open a Pull Request into `dev` and assign it for review. Follow the [Pull Requests guide]({{ site.baseurl }}/docs/guides/#pull-requests).

### Project A: Admin Dashboard -- Clean and Extend the Database

This team acts on their database findings from Phase 2.

- **Clean the local database.** Address the data quality issues surfaced in the proposal: stale records, gaps, duplicates, and inconsistent or malformed entries. The goal is a database that accurately reflects the real state of the markets.
- **Introduce new fields and tables.** Where the Phase 2 proposal identified missing data, add the new fields or tables needed to capture it, **but only where it makes sense**. Validate each proposed addition against the actual schema and how the data is used before adding it. Not every idea from the proposal has to ship; part of this phase is judging what genuinely improves the data model.

### Project B: Wisconet API -- Integrate Into the Market Profile

This team moves from investigation into software development, integrating the Wisconet API data points into the platform's frontend.

- **Add a new tab to the Market Profile.** Create a new tab in the **Market Profile navigation bar** to surface the Wisconet data.
- **Integrate the API data points.** Pull the useful data points identified in Phase 2 from the Wisconet API and display them within the new tab, so a market profile can show relevant external data alongside its own information.
- Follow the frontend structure and patterns already in the repo (see the [Frontend setup guide]({{ site.baseurl }}/docs/guides/FRONTEND_GUIDE)) so the new tab fits naturally into the existing navigation.

</details>

<details class="section-card" markdown="1">
<summary>Phase 4: Data Analytics</summary>

By now each team has a strong understanding of its data source. This phase turns that data into insight: deciding how to process and visualize it, and then building those visualizations into the platform. Both teams follow the same two-part structure on their respective projects.

### Part 1: Propose Data Processing and Visualizations

Each team proposes the data processing and visualization options they think make the most sense for their platform.

- **Explore the alternatives.** Based on your understanding of the data, identify how it could be processed and what visualizations (charts, summaries, dashboards, and so on) would best communicate it to users.
- **Recommend what makes the most sense.** For each proposed analytic or visualization, explain what it shows, who it helps, and why it is worth displaying on the platform.
- **Coordinate with the Market and Research team.** Review your proposal with the Market and Research team. They understand what our users and stakeholders actually need, so their input decides which analytics and visualizations are worth building. The goal of this part is a clear, agreed-upon set of visualizations to implement.

### Part 2: Implement the Agreed Visualizations

Once the proposal is agreed upon, each team builds it.

- **Implement the agreed data processing and visualizations** into the actual platform, on the respective project (the Admin Dashboard for the database team, the Market Profile for the Wisconet API team).
- Follow the same working flow and branching practices from Phase 3: track the work as issues, branch off `dev`, and open PRs for review.

</details>

<details class="section-card" markdown="1">
<summary>Phase 5: Usability Evaluation and Testing</summary>

This phase puts the work in front of real users and validates that everything built across the earlier phases actually functions as intended.

### Usability Evaluation

- **Evaluate with the Kaufman Lab.** Run usability evaluations with all members of the Kaufman Lab. Have them work through the features your teams built and gather their feedback on how clear, useful, and easy to use everything is.
- **Include the markets if possible.** Where feasible, run the same evaluation with the markets themselves, since they are the end users of much of this data. Their feedback is especially valuable for the market-facing features.
- Capture the feedback in a form the teams can act on: what worked, what confused people, and what should change.

### Functionality Testing

- **Test each development thoroughly.** Use this phase to do extra testing on the functionality delivered in every prior phase, across both projects (the Admin Dashboard and the Market Profile work).
- Confirm the data cleaning, new fields and tables, the Wisconet integration, and the analytics and visualizations all behave correctly, including edge cases and unexpected input.
- Log any bugs or issues found so they can be tracked and fixed through the standard issue-to-PR flow.

</details>

<details class="section-card" markdown="1">
<summary>Phase 6: Documentation and Handoff</summary>

The final phase captures everything that was built and reflects on the experience, so the work can be picked up cleanly by the next cohort or team. Both teams document their own project.

### Documentation

- **Document the work you built.** Write up what your team created across the program: the changes made to the database or platform, how the features work, and anything a future developer would need to understand or extend them.
- **Describe the process.** Capture the whole process you went through, from investigation to proposal to implementation, so the reasoning behind the work is preserved alongside the code.
- **Reflect on the experience.** Include your honest reflections on the project: what you liked about it, what you think could have been better, and any lessons or suggestions for future cohorts.

### Handoff

- Make sure the documentation lives somewhere the team can find it, and that any open issues, known limitations, or unfinished ideas are clearly noted for whoever continues the work.

### Deliverable

A **final report** submitted by each team, covering:

- A description of the whole process and the team's involvement across the phases.
- An overview of what was built and how it works.
- Reflections: what went well, what you liked, what could have been better, and recommendations going forward.

</details>

---

## Outcomes, Deliverables, and Success Criteria

This section frames what the WISCURDS program is expected to produce and how we will judge whether it succeeded.

### Anticipated Outcomes

By the end of the program, we expect:

- A **cleaner, more reliable database** backing the Admin Dashboard, with a data model that better reflects the real state of the markets.
- The **Wisconet API integrated into the Market Profile**, giving markets access to relevant external data alongside their own.
- **Meaningful analytics and visualizations** in both the Admin Dashboard and the Market Profile, shaped by what the Market and Research team and end users actually need.
- Students who can **investigate an unfamiliar codebase, propose changes, and ship them** through a real team workflow.
- A project that is **documented and ready to hand off** to the next cohort or team without loss of context.

### Anticipated Deliverables

| Phase | Deliverable |
| ----- | ----------- |
| Phase 1 | Current State Understanding Report for both repositories |
| Phase 2 | Data source investigation proposal from each team (database and Wisconet API) |
| Phase 3 | A cleaned and extended local database; a new Market Profile tab integrating Wisconet data |
| Phase 4 | An agreed analytics and visualization proposal, implemented in each platform |
| Phase 5 | Usability evaluation feedback and functionality testing results |
| Phase 6 | Final documentation and a handoff report from each team |

### Success Criteria

The program is successful if:

- Both teams **complete their build work** and it is merged into the codebase through the standard issue-branch-PR workflow.
- The database team's cleaning and schema changes **improve data quality** without breaking existing functionality.
- The Wisconet integration and the analytics features **work reliably** and are validated through Phase 5 testing.
- The features are **usable and valuable to real users**, confirmed by the Kaufman Lab and, where possible, the markets during usability evaluation.
- The work is **clearly documented**, so a future developer can understand and extend it.
- Students demonstrate growth in **technical skills, collaboration, and working within a real development team**.
