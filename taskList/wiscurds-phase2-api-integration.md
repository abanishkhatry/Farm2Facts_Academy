---
layout: default
title: "Phase 2 Task Guide -- Wisconet API"
permalink: /taskList/wiscurds-phase2-api/
---

# Phase 2 Task Guide -- Project B: Wisconet API Integration

**Program:** WISCURDS | **Phase:** 2 -- Data Source Investigation | **Team:** Dhruv and Soham

---

This is the task companion to the [Phase 2 milestone card]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-2). That card describes what the phase covers; this guide is what you actually do, in order.

Phase 2 splits into two projects. This guide is **Project B, the Wisconet API**, and it belongs to **Dhruv and Soham**. Project A works on the Admin Dashboard and the local database, and has its own guide.

Your goal for this phase comes down to one question, asked in two halves:

- **What does the Wisconet API need from us** in order to return data that is actually relevant to a given market? A station code, coordinates, a county, a zip code, something else?
- **Do we already hold that information** in our own database, in a good enough state to use?

Everything in this guide builds toward answering both. If the answer to the second question turns out to be no, that is not a failure. It is the single most useful finding you could bring back, because it changes what Phase 3 has to build.

**You are investigating, not building.** No integration code this phase, no changes to the database, and nothing wired into the platform. You are establishing what is possible and what it would cost. The working Market Profile tab comes in Phase 3, and it will go much faster because of what you write down now.

The one piece of code you do write is in Card 8: an empty WISCONET tab on the Market Profile, with nothing behind it. It calls no API and touches no data, and it exists so the place Phase 3 builds into is already there.

**This is one team deliverable, not two.** The two of you work on a single feature branch and produce a single report. Agree up front on who investigates what and keep each other current. You can branch further off your feature branch if you want, but everything lands back in the one feature branch. Card 2 covers how to split it.

**Use an LLM or coding agent. We recommend it.** Reading unfamiliar API documentation and working out what a parameter does is a good use of one. The same rule from Phase 1 applies: verify every claim against the actual documentation or an actual response before it goes in the report. An agent will confidently describe API parameters that do not exist. One addition for this phase, and it is not optional: **never paste database credentials into an agent prompt, a browser tool, or anything else.** Card 1 covers how to handle them.

Phase 2 assumes you have finished [Phase 1]({{ site.baseurl }}/taskList/wiscurds-phase1/). You will also lean on the [LASER Task 2.1 Guide]({{ site.baseurl }}/taskList/task2_1/), which walks through exploring this same API with a browser and Postman. Work through it early; it will save you most of a day.

<div class="task-card-grid">

  <details class="task-card">
    <summary>1. Get Your Access and Your Bearings</summary>
    <div class="card-body">

      <p>Two things to get hold of before you start: the API documentation, which is public, and the dummy database, which is not.</p>

      <details>
        <summary>1.1 The Wisconet API Documentation</summary>
        <div class="section-body">
          <p>Wisconet is Wisconsin's statewide environmental monitoring network. Its API is open, so there is nothing to request and no key to wait for. Start here:</p>
          <p><a href="https://wisconet.wisc.edu/data/api" target="_blank" rel="noopener noreferrer">Wisconet API documentation</a></p>
          <p>Read it properly before you start clicking. You are looking for the shape of the thing: which endpoints exist, what each one returns, and what it expects you to supply. Do not stop at the first endpoint that returns something interesting.</p>
        </div>
      </details>

      <details>
        <summary>1.2 The Dummy Database</summary>
        <div class="section-body">
          <p>You get to the database the same way the Admin Dashboard team does. Everything you need is in <strong>1Password</strong>: the username and password for the dummy database, and the <strong>link to the database GUI</strong> on the web server.</p>
          <p>Nothing to install. The GUI runs in your browser, so open the link from the 1Password item and sign in with the credentials stored alongside it. It is the same kind of interface as the phpMyAdmin you have seen in the <a href="{{ site.baseurl }}/STUDENT_ONBOARDING_PLAN#database">Student Onboarding Plan</a>.</p>
          <p>You are working against a <strong>dummy database</strong>, a copy of the platform's structure with non-production data in it, so you can look around freely. Treat the credentials as seriously as production credentials anyway.</p>
          <h3>Rules for handling them</h3>
          <ul>
            <li><strong>Never commit them.</strong> Not in the report, not in a config file, not in a screenshot, not in a comment. Anything committed to Git is permanent even if a later commit deletes it.</li>
            <li><strong>Never paste them into Slack, email, or a document.</strong> They live in 1Password and nowhere else.</li>
            <li><strong>Never paste them into an LLM or coding agent.</strong> If you need help with a connection problem, describe the error and redact the host and password.</li>
            <li><strong>Screenshots count.</strong> Before any GUI screenshot goes in the report, check that the URL bar, the host name, and the username are not visible in it.</li>
          </ul>
          <p>If you cannot see the 1Password item, or the link does not let you in, tell Abanish in the WISCURDS Slack channel the same day rather than waiting.</p>
          <p><strong>Done when:</strong> both of you can open the documentation and the database GUI.</p>
        </div>
      </details>

    </div>

  </details>

  <details class="task-card">
    <summary>2. Open Your Team Branch and Split the Work</summary>
    <div class="card-body">

      <p>Your report goes into the <strong>backend repository</strong>, <code>farmers-coalition</code>, the same place the Admin Dashboard team puts theirs. Both Phase 2 reports live side by side so the investigation from this phase is in one place. One branch, shared between the two of you. Card 8 has you open a branch of the same name in the frontend repo for the placeholder tab, but everything up to that point happens here.</p>

      <details>
        <summary>2.1 Pull dev and Cut the Team Branch</summary>
        <div class="section-body">
          <p>Start from an up-to-date <code>dev</code>, exactly as you did in Phase 1. Your Phase 1 branch is merged and finished; do not build on it.</p>
          <pre><code>git checkout dev

git pull
git checkout -b feat-wis-p2-api-integration</code></pre>

<p>One of you creates the branch and pushes it first:</p>
<pre><code>git push -u origin feat-wis-p2-api-integration</code></pre>
<p>The other then checks it out rather than creating their own copy:</p>
<pre><code>git checkout dev
git pull
git checkout feat-wis-p2-api-integration</code></pre>
<p>Agree between yourselves who does this first, in Slack, before either of you runs anything.</p>
<p><strong>Done when:</strong> both of you are on <code>feat-wis-p2-api-integration</code>, and it exists on GitLab.</p>
</div>
</details>

      <details>
        <summary>2.2 Create the Report Directory</summary>
        <div class="section-body">
          <p>Inside the <code>wiscurds/</code> directory you worked in during Phase 1, create a directory for this project's reports. The report file goes <strong>inside</strong> that new directory, not loose at the root of <code>wiscurds/</code>:</p>
          <pre><code>wiscurds/
└──&nbsp;api_integration_reports/
&nbsp;&nbsp;&nbsp;&nbsp;└──&nbsp;wisconet_api_current_state_report.md</code></pre>
          <p>So the full path to your report is <code>wiscurds/api_integration_reports/wisconet_api_current_state_report.md</code>.</p>

<p>That directory holds this project's written work for the rest of the program, so later phases add their reports alongside this one. This phase produces a single file, written by both of you.</p>
<p>If you include a screenshot in the report, save the image in the same directory and reference it from the Markdown.</p>
</div>
</details>

      <details>
        <summary>2.3 Agree Who Does What</summary>
        <div class="section-body">
          <p>Two people committing to one branch and one file will collide unless you decide in advance who owns what. Spend ten minutes on this before you start Card 3.</p>
          <h3>A split that works for this project</h3>
          <p>The natural division here is by side of the question: one of you goes deep on the API and what it requires, the other on the users table and what we actually hold. You then write the gap analysis in Card 6 together, because that section needs both halves in one head. Any split works as long as it is explicit and written down in Slack.</p>
          <p>Whoever takes the API side should still read the other's findings before the report is finalised, and the other way round. The conclusion in Card 6 is the part we will act on, and it only holds up if you both believe it.</p>
          <h3>Rules that keep the branch clean</h3>
          <ul>
            <li><strong>Pull before you start, pull before you push.</strong> Most conflicts come from working on a stale copy for two days.</li>
            <li><strong>Commit small and often.</strong> A section at a time, pushed the same day.</li>
            <li><strong>Stay out of each other's sections.</strong> If you think your teammate's section is wrong, tell them; do not rewrite it.</li>
            <li><strong>Say what you are doing.</strong> A message in Slack saying which section you are on prevents you both writing the same thing.</li>
          </ul>
          <p>If you hit a conflict, do not delete the file and start over. Post it in Slack and we will walk through resolving it.</p>
        </div>
      </details>

    </div>

  </details>

  <details class="task-card">
    <summary>3. Learn the Shape of the API</summary>
    <div class="card-body">

      <p>Before you can ask what the API needs from us, you need a working picture of what it offers. This card is the survey; Card 4 is the specific question.</p>

      <h3>What to Establish</h3>
      <ul>
        <li><strong>The endpoints.</strong> What can you ask for? Group them: things that describe the network itself, and things that return readings.</li>
        <li><strong>The base URL and versioning.</strong> What does a full request look like, and is there a version in the path that could change under us later?</li>
        <li><strong>Authentication.</strong> Is any needed? If none is needed today, say so explicitly in the report, because "no key required" is a real advantage worth recording.</li>
        <li><strong>The measures available.</strong> What does the network actually record? Soil temperature, air temperature, rainfall, and whatever else. Note which of these look relevant to a farmers market audience.</li>
        <li><strong>Time.</strong> How do you ask for a range rather than the latest value, and what format does it expect?</li>
        <li><strong>Limits.</strong> Anything the documentation says about rate limits, maximum ranges per request, or data retention. Find this now rather than in Phase 3.</li>
      </ul>

      <p><strong>Done when:</strong> you can describe what the API offers without looking, and you have called each endpoint that matters at least once yourself.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>4. Find What the API Needs From Us</summary>
    <div class="card-body">

      <p>This is the central question of the phase, so give it real time.</p>
      <p>Wisconet reports from <strong>physical stations</strong> at fixed locations. Our markets are somewhere else. So something has to connect a market to the readings that are relevant to it, and your job is to work out what that something is and what input it demands.</p>

      <h3>The Question, Precisely</h3>
      <p>To get a valid and relevant response for a given market, what does the API require us to supply? Work through the possibilities rather than assuming:</p>
      <ul>
        <li>A <strong>station identifier</strong>, which would mean we have to decide which station belongs to which market.</li>
        <li><strong>Coordinates</strong>, a latitude and longitude.</li>
        <li>A <strong>county</strong>.</li>
        <li>A <strong>zip code</strong>.</li>
        <li>Something else entirely, or several of these in combination.</li>
      </ul>
      <p>Do not answer this from the documentation alone. Test each form that looks plausible and record what actually comes back: the status code, whether the data is genuinely local to the place you asked about, and what happens when you supply something the API does not expect.</p>

      <h3>Also Establish</h3>
      <ul>
        <li><strong>Which input gives the most useful answer.</strong> Two inputs may both return a 200 while one gives you a station forty miles away. Relevance matters more than success here.</li>
        <li><strong>What happens at the edges.</strong> A location with no nearby station, a malformed value, a county with several stations in it. The error behaviour decides how much defensive work Phase 3 needs.</li>
        <li><strong>Whether we need a lookup step.</strong> If the API only accepts station identifiers, then somebody has to map location to station, and that mapping becomes part of the work. Say whether the API can help with that or whether we build it ourselves.</li>
        <li><strong>Coverage.</strong> Do stations exist near the places our markets actually are? A network that covers rural Wisconsin well and urban Milwaukee poorly is a finding that shapes the whole feature.</li>
      </ul>

      <p>Write the conclusion as a plain sentence you could hand to a developer: to get relevant readings for a market, we must supply X, in Y format, and we will get back Z.</p>

      <p><strong>Done when:</strong> you can state exactly what input the API needs for a relevant response, backed by requests you made yourself, including what happens when the input is wrong.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>5. Check What the Users Table Actually Holds</summary>
    <div class="card-body">

      <p>Now turn around and look at our side. The API needs a location input. The question is whether we already have it.</p>
      <p>Go to the <strong>users table</strong> in the database GUI. Confirm the exact table name first, since the platform may separate login accounts from the market and organization records they belong to, and the location data may sit on either. If it is not on the users table, follow the relationship to wherever it lives and say so in the report.</p>

      <h3>What to Look For</h3>
      <ul>
        <li><strong>Which location columns exist at all.</strong> Zip code, county, city, state, street address, latitude and longitude, anything else. List them exactly as named.</li>
        <li><strong>Which of them match what Card 4 said the API needs.</strong> This is the point of the whole exercise.</li>
        <li><strong>How complete each one is.</strong> A county column that is populated for 11 percent of rows is not a usable input. Get the number.</li>
        <li><strong>How clean the values are.</strong> Are zip codes all five digits, or are there four-digit ones missing a leading zero and some with a plus-four suffix? Are county names spelled consistently, with or without the word "County"? Is the state always Wisconsin?</li>
        <li><strong>Whether it differs by identity.</strong> Market organizations, markets, and individual producers may each carry different location fields, or the same field filled in at very different rates. Check each rather than sampling one.</li>
      </ul>

      <h3>Getting the Numbers From the GUI</h3>
      <p>Same approach as the Admin Dashboard team. Sorting a column groups the empty values at one end, the search or filter view counts rows matching a condition, and the row count on a filtered table is the number you want. Record how you got each number, for example "users table, filtered to county not empty, 240 of 1,842 rows".</p>
      <p>Page through the actual values for a minute too. Formatting problems are obvious on sight and invisible in a summary.</p>

      <p><strong>Done when:</strong> you have a list of every location column we hold, with a completeness number and a note on value quality for each.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>6. Close the Gap</summary>
    <div class="card-body">

      <p>You now have both halves: what the API wants, and what we have. This card is where you put them together and say whether this integration is straightforward, awkward, or blocked.</p>

      <h3>Sort Every Required Input Into One of Three</h3>
      <ul>
        <li><strong>We have it.</strong> The column exists, it is populated well enough, and the values are in a usable format. Say how well enough, with the number.</li>
        <li><strong>We can derive it.</strong> We hold something adjacent that could produce it: a zip code that maps to a county, an address that could be geocoded to coordinates, a city that identifies a region. Say what the derivation would take and how reliable it would be.</li>
        <li><strong>We do not have it.</strong> Nothing in the database supplies this, and getting it means asking users for it, importing it from somewhere, or building a mapping by hand.</li>
      </ul>

      <h3>Then Recommend a Path</h3>
      <p>Given the above, what is the most sensible way to connect a market to its readings? Consider the options and say which you would choose and why:</p>
      <ul>
        <li>Use what we already hold, accepting that it only works for the subset of markets with good data.</li>
        <li>Derive the input from something adjacent, accepting the accuracy cost.</li>
        <li>Add a field and collect it going forward, accepting that it is empty until people fill it in.</li>
        <li>Build a fixed mapping of market to station once, and maintain it.</li>
      </ul>
      <p>For your recommendation, say what it means for the markets whose data is missing or bad. A feature that silently shows nothing for half our markets is worse than one that tells them why.</p>

      <h3>Two Warnings</h3>
      <ul>
        <li><strong>Do not build any of it yet.</strong> No integration code, no database changes, not even a small one. The proposal gets reviewed before anything happens, and that is the point of writing it first.</li>
        <li><strong>Do not assume the missing data is missing by accident.</strong> A column that is empty for most markets may never have been asked for on any form. Before proposing that we collect it, check whether there is anywhere in the app that could collect it. If you are unsure, that is an open question rather than a recommendation.</li>
      </ul>

      <p><strong>Done when:</strong> every input the API requires is sorted into have, can derive, or do not have, and you have one recommended path with its consequences stated.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>7. Write the Report</summary>
    <div class="card-body">

      <p>The deliverable for this phase is one report, written by both of you, saved as:</p>
      <pre><code>wiscurds/api_integration_reports/wisconet_api_current_state_report.md</code></pre>
      <p>It is the reference you will work from for the rest of the program, and it is what we read when deciding what Phase 3 actually builds. Aim for six to eight pages including the tables.</p>

      <h3>What Makes It a Good Report</h3>
      <ul>
        <li><strong>Show real requests and real responses.</strong> A trimmed example beats any amount of description. Someone should be able to copy a URL out of your report and run it.</li>
        <li><strong>Numbers, not impressions.</strong> Every claim about our data carries a count and a note of how you got it.</li>
        <li><strong>Name real columns and endpoints.</strong> A reader should be able to check any statement in under a minute.</li>
        <li><strong>One voice.</strong> You are writing one document, not stapling two halves together. Read each other's sections at the end.</li>
        <li><strong>No credentials anywhere.</strong> Check the screenshots too.</li>
      </ul>

      <h3>Report Template</h3>
      <pre class="pre-scroll"><code># Wisconet API -- Current State and Integration Feasibility

**Authors:** [Name], [Name]
**Program:** WISCURDS | **Phase:** 2 -- Data Source Investigation
**Sources:** Wisconet API documentation; dummy database via the web GUI
**Date:** [Date]

## 1. Summary

[Half a page. What the Wisconet API offers, what it needs from us, and
whether our data can supply it. State the answer here rather than making
the reader find it in section 6. Write this section last.]

## 2. How We Worked

[How you split the investigation between the two of you, what tools you
used, and anything about the process worth recording. Two or three
sentences.]

## 3. The API in Brief

### 3.1 Endpoints

[What you can ask for. One line each.]

| Endpoint | What it returns | Notes |
| -------- | --------------- | ----- |
|          |                 |       |

### 3.2 Request Basics

[Base URL, versioning, whether authentication is required, and how you
ask for a time range rather than the latest reading.]

### 3.3 Measures Available

[What the network records, and which of these are relevant to a farmers
market audience.]

### 3.4 Limits

[Rate limits, maximum range per request, retention, or "the
documentation does not say" where that is the honest answer.]

### 3.5 Example Request and Response

[One real URL and a trimmed sample of what came back.]

## 4. What the API Needs From Us

### 4.1 The Answer

[One plain sentence: to get relevant readings for a market we must
supply X, in Y format, and we get back Z.]

### 4.2 What We Tested

[Each input form you tried, and what actually happened.]

| Input tried | Example value | Status | Was the result relevant? |
| ----------- | ------------- | ------ | ------------------------ |
|             |               |        |                          |

### 4.3 Edge Cases

[Locations with no nearby station, malformed values, ambiguous
locations. What the API does in each case.]

### 4.4 Coverage

[Whether stations exist near the places our markets actually are, and
anywhere they clearly do not.]

## 5. What We Hold

### 5.1 Where the Location Data Lives

[Which table or tables carry it, and how they relate to markets and
organizations.]

### 5.2 The Columns

| Column | Table | Filled | Value quality | How we checked |
| ------ | ----- | ------ | ------------- | -------------- |
|        |       |        |               |                |

### 5.3 Differences by Identity

[Whether market organizations, markets, and producers carry different
location fields or the same fields at different fill rates.]

## 6. The Gap

### 6.1 Input by Input

| API needs | We have it / can derive / do not have | Evidence |
| --------- | ------------------------------------- | -------- |
|           |                                       |          |

### 6.2 Recommended Path

[Which option you would take and why. What it means for markets whose
data is missing or poor. What it would take to implement, roughly.]

### 6.3 Options We Rejected

[The alternatives you considered and why they are worse. A reviewer who
disagrees needs to see that you looked.]

## 7. Open Questions

[Anything you could not resolve: documentation that was unclear, a
decision that needs someone who knows the markets, data that might be
correct but looks wrong. Number them so we can answer them
individually.]

## 8. Working With an LLM

[Which tool you used, where it helped, where it was wrong, and what you
would prompt differently next time. Three or four sentences.]</code></pre>

      <p>Sections 6 and 7 are the ones we read most closely. Section 6 is the proposal that decides what Phase 3 builds, and Section 7 is where you tell us what you need from us to keep moving.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>8. Add the WISCONET Tab Placeholder</summary>
    <div class="card-body">

      <p>This is the one piece of code you write in Phase 2, and it is deliberately small. The Wisconet readings you have been investigating will eventually be shown to each market inside its own <strong>Market Profile</strong>. Before Phase 3 can put anything there, the tab has to exist. Your job is to add a <strong>WISCONET</strong> tab to the Market Profile and give it a page to open, even though that page has nothing in it yet.</p>
      <p>The value is not the feature. It is proving you can find your way around an unfamiliar frontend and ship a change through review while the change itself carries no risk. Get the workflow wrong here and it costs nothing. Get it wrong in Phase 3 and it costs a rollback.</p>

      <h3>What You Are Building</h3>
      <ul>
        <li>A new tab labelled <strong>WISCONET</strong> in the Market Profile, sitting alongside the tabs already there: <strong>Summary</strong>, <strong>Management</strong>, <strong>Vendors</strong>, <strong>Accessibility</strong>, and <strong>Community</strong>. Put it at the end of that row unless the code makes another position obviously correct.</li>
        <li>A page for it to open. For now that page is blank, or carries the heading <strong>WISCONET</strong> and nothing else.</li>
        <li>Nothing else. No API calls, no data, no charts, no styling work. An empty tab is the correct outcome. The moment you find yourself fetching a reading, you have crossed into Phase 3.</li>
      </ul>

      <h3>Where the Work Happens</h3>
      <p>This one is in the <strong>frontend repository</strong>, <code>farm2facts-frontend</code>, not the backend repo where your report lives. Branch from <code>dev</code> exactly as before:</p>
      <pre><code>git checkout dev
git pull
git checkout -b feat-wis-p2-api-integration</code></pre>
      <p>Same branch name as your backend branch, in a different repository. The team rules from Card 2.3 still apply: one of you creates and pushes it, the other checks it out rather than making their own.</p>

      <h3>Find the Placement Before You Create Anything</h3>
      <p>Do not start by making files. Start by finding the code that renders the tabs you can already see, because the fastest way to add something to an unfamiliar codebase is to copy what is already working next to it.</p>
      <ol>
        <li>Open the running frontend, go to a <strong>market profile</strong>, and look at the tab row. Note the labels exactly as they appear.</li>
        <li><strong>Search the repo for those labels.</strong> A visible string is the quickest way into frontend code you do not know. Your Phase 1 report may already point you at the right area, since the profile views were part of what you mapped.</li>
        <li>Read how one existing tab is defined: its label, what it renders, its position in the row, and any condition controlling who sees it.</li>
        <li>Follow it to the <strong>component or view</strong> that tab loads, and to the <strong>route</strong> if each tab has one of its own. Some tab bars swap components without changing the URL; find out which kind this is, because it decides where your new file goes.</li>
      </ol>
      <p>By the end of this step you should be able to name the component holding the tab row, how a tab maps to what it displays, and where the displayed component lives. Write those paths down. They go in your merge request description.</p>

      <h3>Then Build It by Copying the Pattern</h3>
      <ul>
        <li><strong>Add the tab</strong> to the row, following the exact shape of the tabs around it.</li>
        <li><strong>Add whatever the tab needs to resolve to a page</strong>, matching how the existing tabs do it: a route if they use routes, an entry in the component list if they do not.</li>
        <li><strong>Create the component or view file</strong> in the same place and the same structure as the neighbouring tabs. If those are split across several files, match that; if they are one file, match that.</li>
        <li><strong>Respect any visibility rules.</strong> If certain tabs only appear for certain account types, work out which rule your tab should follow and apply it.</li>
      </ul>
      <p>Keep the label as <strong>WISCONET</strong> for now. If the other tabs use a different casing convention, match the convention and note the change in your merge request rather than deciding silently.</p>

      <h3>Check It Works</h3>
      <ul>
        <li>Open a market profile and see <strong>WISCONET</strong> in the tab row, in the position you intended.</li>
        <li>Click it. The tab becomes active and the page loads with no errors in the browser console.</li>
        <li>Click through <strong>Summary</strong>, <strong>Management</strong>, <strong>Vendors</strong>, <strong>Accessibility</strong>, and <strong>Community</strong> afterwards and confirm they all still work. A change to a shared tab row is exactly the kind of thing that quietly breaks its neighbours.</li>
        <li>Check it on more than one market, and on a market with little or no data, so you know the tab is not depending on something that happens to exist for the first profile you opened.</li>
      </ul>

      <h3>Open the Merge Request</h3>
      <p>Same flow as the report, in the frontend repo this time:</p>
      <ol>
        <li><strong>Code &rarr; Merge requests &rarr; New merge request</strong>.</li>
        <li><strong>Source:</strong> <code>feat-wis-p2-api-integration</code>. <strong>Target:</strong> <code>dev</code>.</li>
        <li>Title it <code>Add WISCONET tab placeholder to the Market Profile</code>.</li>
        <li>In the description, name the <strong>files</strong> you found and changed, say how tabs map to pages in this codebase, and state plainly that the page is intentionally empty and gets filled in Phase 3. A reviewer seeing an empty tab with no explanation will assume something is missing.</li>
        <li>Attach a <strong>screenshot</strong> of the tab row with WISCONET visible.</li>
        <li>Assign <strong>Abanish</strong> as the reviewer, and read the <strong>Changes</strong> tab before you submit.</li>
      </ol>
      <p>This is a separate merge request from the report one. Two repos, two branches, two merge requests, and they are reviewed independently.</p>

      <p><strong>Done when:</strong> the WISCONET tab appears in the Market Profile, it opens a page without errors, the existing tabs still work, and the merge request is open against <code>dev</code> and assigned.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>9. Commit and Submit the Report</summary>
    <div class="card-body">

      <p>This card is about the <strong>report</strong>, which lives in the backend repo. You submit it by <strong>merge request</strong> into <code>dev</code>, the same way you submitted Phase 1. One merge request for the team, from your shared branch. The frontend merge request from Card 8 is separate and travels on its own.</p>

      <details>
        <summary>9.1 Commit as You Go</summary>
        <div class="section-body">
          <p>Do not save this for the last day. Commit each section of the report as it becomes usable:</p>
          <pre><code>git pull

git status
git add wiscurds/api_integration_reports/
git commit -m "Add API endpoint survey to the Wisconet current state report"</code></pre>

<p><code>git status</code> before every <code>git add</code>, same as Phase 1. Two things to confirm in its output: you are on <code>feat-wis-p2-api-integration</code>, and the only files listed are inside <code>wiscurds/api_integration_reports/</code>. Nothing from <code>app/</code>, <code>config/</code>, or <code>db/</code> should appear in this phase's commits. If something does, you changed a file by accident.</p>
<p>Check one more thing before every commit: <strong>no credentials in the diff</strong>. Read what you are committing.</p>
<p>Push the same day you commit, so your teammate is never working against a stale branch.</p>
</div>
</details>

      <details>
        <summary>9.2 Open the Merge Request</summary>
        <div class="section-body">
          <p>When the report is complete and both of you have read it end to end, open one merge request in <code>farmers-coalition</code>:</p>
          <ol>
            <li>In the left sidebar, go to <strong>Code &rarr; Merge requests</strong>.</li>
            <li>Click <strong>New merge request</strong>.</li>
            <li><strong>Source branch:</strong> <code>feat-wis-p2-api-integration</code>.</li>
            <li><strong>Target branch:</strong> <code>dev</code>. Never <code>main</code>.</li>
            <li>Title it <code>Phase 2 Wisconet API current state report</code>.</li>
            <li>Fill out the description using the <a href="{{ site.baseurl }}/docs/guides/#pull-requests">Pull Requests guide</a>, and name both authors in it.</li>
            <li>Assign <strong>Abanish</strong> as the reviewer.</li>
          </ol>
          <p>In the description, include the <strong>one-sentence answer</strong> from section 4.1, your <strong>recommended path</strong>, and your <strong>open questions</strong>, so they are visible without opening the file.</p>
          <p>Open the <strong>Changes</strong> tab and read the diff before you submit. Both of you, not just whoever clicked the button.</p>
          <p><strong>Done when:</strong> one merge request is open against <code>dev</code>, assigned to Abanish, with both of you named.</p>
        </div>
      </details>

      <details>
        <summary>9.3 Respond to Review</summary>
        <div class="section-body">
          <p>Expect comments, and expect some of them to ask for a request you did not include or a number you did not check. Commit the changes on the same branch and push again; the merge request updates itself. Reply to each comment saying what you changed.</p>
          <p>Once it is approved we merge it into <code>dev</code>, and your recommended path becomes the starting point for the Market Profile work in Phase 3.</p>
        </div>
      </details>

      <p>Bring your open questions to the weekly check-in rather than waiting for the review. Several of them will be questions about how the markets actually work, and those are faster to answer out loud than in a comment thread.</p>

    </div>

  </details>

</div>
