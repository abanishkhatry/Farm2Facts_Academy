---
layout: default
title: "Phase 1 Task Guide"
permalink: /taskList/wiscurds-phase1/
---

# Phase 1 Task Guide

**Program:** WISCURDS | **Phase:** 1 -- Understanding F2F and Its Repositories' Current State

---

This is the task companion to the [Phase 1 milestone card]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-1). That card describes what the phase covers; this guide is what you actually do, in order.

Phase 1 has one goal: by the end of it you can explain how Farm2Facts works today, in your own words, without opening the code. That means knowing what lives in each repository, how the frontend and the backend talk to each other, and where a single piece of data comes from and goes.

**You are reading, not building.** Nothing in this phase changes the codebase. No branches, no commits, no pull requests -- that starts in Phase 3. If you find something broken or badly written, write it down instead of fixing it. Those notes are useful later; an unplanned fix this early is not.

**You will not understand everything, and you are not supposed to.** This is a real application built over several years by people who are no longer on the project. Parts of it will be confusing, inconsistent, or apparently unused. Reading a codebase you did not write is a skill, and being able to say precisely what you do not understand is most of it. Keep a running list of open questions as you go -- that list is a graded part of the deliverable, not an admission of failure.

Everyone does this phase **individually**. All four of you write your own report. The split into two project teams happens in Phase 2, and the understanding you build here is what you bring to whichever team you land on.

Phase 1 assumes both repos are running on your machine from [Phase 0]({{ site.baseurl }}/taskList/wiscurds-phase0/). If they are not, finish that first -- most of this phase depends on being able to click through the running app.

<div class="task-card-grid">

  <div class="task-card">
    <p class="card-title">1. Orient Before You Read Code</p>
    <div class="card-body">

      <p>Opening a large repository and scrolling through folders is the slowest possible way to learn a system. Spend the first part of this phase getting the shape of the thing from the outside, so that when you do open the code you already know what you are looking at.</p>

      <details>
        <summary>1.1 Read the Development Structure Overview</summary>
        <div class="section-body">
          <p>Start with the <a href="{{ site.baseurl }}/taskList/wiscurds-development-structure">Development Structure Overview</a>. It is three diagrams and a page of text, and it gives you the model everything else hangs off:</p>
          <ul>
            <li><strong>The three layers</strong> -- a Vue frontend, a Rails backend, a MySQL database, with requests travelling in both directions.</li>
            <li><strong>Who the users are</strong> -- individual producers and vendors, farmers markets, and market organizations, nested inside one another.</li>
            <li><strong>How data moves</strong> -- entered through instruments at the vendor level, flowing up to the market, and up again to the market organization.</li>
          </ul>
          <p>That nesting is the single most important idea in the system. Almost every screen, model, and permission check in both repos exists to serve it. If you only remember one thing before opening the code, remember that a market organization contains markets, and a market contains vendors and producers.</p>
          <p><strong>Done when:</strong> you can draw the three layers and the user hierarchy from memory, without looking at the page.</p>
        </div>
      </details>

      <details>
        <summary>1.2 Use the App as a User</summary>
        <div class="section-body">
          <p>Start both servers from Phase 0 and spend a solid half hour clicking through the running frontend at <code>localhost:8080</code>. Behave like a market manager who has just been given the tool, not like a developer.</p>
          <p>As you go, write down:</p>
          <ul>
            <li>The <strong>main sections</strong> of the app, as they are named in the navigation.</li>
            <li>What each section appears to be <strong>for</strong>, in one line.</li>
            <li>Anything that <strong>surprises you</strong> -- an empty screen, a section you cannot reach, a label you do not understand.</li>
          </ul>
          <p>Try to submit or open an <strong>instrument</strong> (a vendor application, a sales slip, a visitor survey). Instruments are how data gets into the platform, so seeing one from the user's side makes the code around them far easier to read.</p>
          <p>Keep your browser's <strong>Network</strong> tab open while you click. Every screen that shows data is making a request to <code>localhost:3000</code>, and watching those requests appear is the fastest way to learn which screen maps to which endpoint. You will come back to this in Card 4.</p>
          <p><strong>Done when:</strong> you have a written list of the app's main sections and what each one does, in your own words.</p>
        </div>
      </details>

      <details>
        <summary>1.3 Set Up Your Notes Before You Start</summary>
        <div class="section-body">
          <p>Create one file for this phase now and write into it as you work. The report in Card 6 is assembled from these notes, and reconstructing them at the end of the phase never works.</p>
          <p>Keep it wherever you like -- a Markdown file, a Google Doc, a notebook. Four running sections is enough:</p>
          <ul>
            <li><strong>Frontend</strong> -- what each part is responsible for.</li>
            <li><strong>Backend</strong> -- what each part is responsible for.</li>
            <li><strong>Traces</strong> -- the path a piece of data takes, from Card 4.</li>
            <li><strong>Open questions</strong> -- anything you could not work out.</li>
          </ul>
          <p>When you note something about the code, <strong>write down the file path</strong>. "The store handles authentication" is a note you cannot use in three weeks. "<code>src/store/index.js</code> holds the auth state" is one you can.</p>
        </div>
      </details>

    </div>
  </div>

  <details class="task-card">
    <summary>2. Map the Frontend</summary>
    <div class="card-body">

      <p>The frontend is <a href="https://git.doit.wisc.edu/at-trad/farm2facts-frontend" target="_blank" rel="noopener noreferrer">farm2facts-frontend</a>, a Vue 3 application using Pinia for state and the MDB Vue UI Kit for components. Work in your local clone on the <code>dev</code> branch.</p>
      <p>Your aim in this card is a map, not a full reading. For each part of the app you should be able to say what it is responsible for and where it lives. You do not need to understand every file.</p>

      <details>
        <summary>2.1 Map the Top Level of src/</summary>
        <div class="section-body">
          <p>Open <code>src/</code> and go one level deep. For each folder, work out what belongs in it and write a one-line description. You are looking for the usual Vue divisions:</p>
          <ul>
            <li><strong>Views</strong> -- the screens, one per route.</li>
            <li><strong>Components</strong> -- the reusable pieces the views are built from.</li>
            <li><strong>Router</strong> -- which URL loads which view, and who is allowed there.</li>
            <li><strong>Store</strong> -- the shared state the whole app reads from.</li>
            <li><strong>API or services</strong> -- where HTTP requests to the backend are actually made.</li>
          </ul>
          <p>Also read <code>package.json</code> to see what the app depends on, and open the <code>CLAUDE.md</code> at the repo root if you have not already -- it describes the conventions this codebase follows.</p>
          <p><strong>Done when:</strong> you have a one-line description of every top-level folder in <code>src/</code>.</p>
        </div>
      </details>

      <details>
        <summary>2.2 Walk the Main Views</summary>
        <div class="section-body">
          <p>Most of the app's surface area is in <code>src/views/</code>. Go through the directories below and write down what each one is responsible for and which part of the running app it produces. Connect them back to the sections you listed in Card 1.2.</p>
          <p>Describe these in full:</p>
          <ol>
            <li><code>LandingPage</code></li>
            <li><code>MarketOrg</code></li>
            <li><code>SelectMetrics</code></li>
            <li><code>MemberResources</code></li>
            <li><code>DownloadDocuments</code></li>
          </ol>
          <p>For these, a high-level overview is enough -- they are large, and you do not need to go into their sub-folders:</p>
          <ol>
            <li><code>Analysis</code></li>
            <li><code>Instrument</code></li>
            <li><code>Instrument_MarketOrg</code></li>
            <li><code>Profiles</code></li>
            <li><code>Users</code></li>
          </ol>
          <p>Pay particular attention to <strong>Profiles</strong> and <strong>Instrument</strong>. Project B adds a new tab to the Market Profile in Phase 3, and both project teams work with instrument data, so time spent here pays off later.</p>
          <p>Note the pattern rather than the detail: how a view is put together, where it gets its data, and how it is split between view files and components. Once you see the pattern in two or three views, the rest read quickly.</p>
          <p><strong>Done when:</strong> every directory above has a written description, and you can point to the folder responsible for any screen you saw in Card 1.2.</p>
        </div>
      </details>

      <details>
        <summary>2.3 Find Where Data Enters the App</summary>
        <div class="section-body">
          <p>Views display data; they rarely fetch it. Find the layer that does.</p>
          <ul>
            <li>Find where the <strong>base URL of the backend</strong> is configured. It comes from the <code>.env</code> file you set in Phase 0 -- find the code that reads it.</li>
            <li>Find where <strong>HTTP requests</strong> are actually made. Look for a shared client or service module rather than requests scattered through components.</li>
            <li>Find where the <strong>logged-in user</strong> is stored, and how the app knows which role that user has.</li>
            <li>Find how a request is <strong>authenticated</strong> -- what gets attached to it so the backend knows who is asking.</li>
          </ul>
          <p>Then open the <strong>router</strong> and work out how access is controlled. Different user types see different parts of the app, and the router is usually where that is enforced. Write down how a route is restricted, and to whom.</p>
          <p><strong>Done when:</strong> you can name the file a request goes through on its way out of the frontend, and explain in a sentence how the backend knows who sent it.</p>
        </div>
      </details>

    </div>
  </details>

  <details class="task-card">
    <summary>3. Map the Backend</summary>
    <div class="card-body">

      <p>The backend is <a href="https://git.doit.wisc.edu/at-trad/farmers-coalition" target="_blank" rel="noopener noreferrer">farmers-coalition</a>, a Rails 6.1 application with a MySQL database and a Grape API. Work in your local clone on the <code>dev</code> branch.</p>
      <p>Rails is heavily convention-based, which cuts both ways: the layout will be familiar if you have seen a Rails app before, and quietly confusing if you have not, because a lot happens without being written down anywhere. Take this card slowly.</p>

      <details>
        <summary>3.1 Map the Rails Layout</summary>
        <div class="section-body">
          <p>Go one level deep into <code>app/</code> and write a one-line description of each folder. In a Rails application you can expect models, controllers, views, and often services, with the Grape API classes in a folder of their own -- find where they live in this repo rather than assuming.</p>
          <p>Then open these three files, which tell you more about the system than any amount of browsing:</p>
          <ul>
            <li><strong><code>config/routes.rb</code></strong> -- every URL the backend answers, in one file. Find where the API routes are mounted.</li>
            <li><strong><code>db/schema.rb</code></strong> -- every table and column in the database, generated from the migrations. This is the most honest description of the data model that exists.</li>
            <li><strong><code>Gemfile</code></strong> -- what the application depends on, including Grape and the MySQL adapter.</li>
          </ul>
          <p><strong>Done when:</strong> you have a one-line description of each folder in <code>app/</code>, and you can say where the API routes are mounted.</p>
        </div>
      </details>

      <details>
        <summary>3.2 Read the Data Model</summary>
        <div class="section-body">
          <p>This is the most valuable part of Phase 1 for both project teams, so do not rush it.</p>
          <p>Using <code>db/schema.rb</code> and the model files together, work out how the user hierarchy from Card 1.1 is actually stored:</p>
          <ul>
            <li>Which table holds <strong>market organizations</strong>, which holds <strong>markets</strong>, and which holds <strong>vendors and producers</strong>?</li>
            <li>How is the relationship between them expressed -- which table carries the foreign key to which?</li>
            <li>Where does <strong>instrument</strong> data live? What does one submitted instrument look like as a row, or as a set of rows?</li>
            <li>Which tables look central, in the sense that many others point at them?</li>
          </ul>
          <p>The Rails models add the part the schema cannot show you: <code>has_many</code>, <code>belongs_to</code>, and the validations that decide what a valid record is. Read those declarations at the top of each model -- they are a compact statement of the relationships.</p>
          <p>Sketch the result. A rough entity diagram of the main tables and the lines between them is worth several pages of prose, and it goes straight into your report.</p>
          <p>You already have <strong>phpMyAdmin</strong> access documented in the <a href="{{ site.baseurl }}/STUDENT_ONBOARDING_PLAN#database">Student Onboarding Plan</a>. Looking at real rows alongside the schema makes the model concrete. Read only -- change nothing.</p>
          <p><strong>Done when:</strong> you have a sketch of the main tables and their relationships, and can trace the path from a market organization down to a single vendor's submitted data.</p>
        </div>
      </details>

      <details>
        <summary>3.3 Read the Grape API</summary>
        <div class="section-body">
          <p>Grape is a Ruby framework for building APIs, mounted inside the Rails app. It is the layer the frontend actually talks to, so this is the seam between the two repositories.</p>
          <ul>
            <li>Find the API classes and see <strong>how endpoints are declared</strong> -- the resource, the HTTP method, the path, the parameters it accepts.</li>
            <li>Note whether the API is <strong>versioned</strong> (for example a <code>/v1</code> in the path), and what the base path looks like.</li>
            <li>Find how an endpoint <strong>authenticates</strong> the caller, and how that connects to what you found in Card 2.3.</li>
            <li>Pick two or three endpoints and follow them <strong>inward</strong>: what does the endpoint call, what does that call in turn, and which table does the data ultimately come from?</li>
          </ul>
          <p><strong>Done when:</strong> you can describe, in a sentence, what happens between a request arriving at the backend and a row being read from the database.</p>
        </div>
      </details>

      <details>
        <summary>3.4 Call the API Yourself</summary>
        <div class="section-body">
          <p>Reading endpoint code tells you what it is supposed to return. Calling it tells you what it does return.</p>
          <p>With your backend running on <code>localhost:3000</code>, use Postman or your browser to call two or three of the endpoints you read in 3.3. If they require authentication, use your browser's Network tab to see what an authenticated request from the frontend looks like and reproduce it.</p>
          <ul>
            <li>What does the <strong>JSON response</strong> actually contain? How does it compare to what you expected from the code?</li>
            <li>What <strong>status code</strong> comes back? What happens if you ask for a record that does not exist?</li>
            <li>Does the response include everything the screen shows, or is the frontend combining several calls?</li>
          </ul>
          <p>If you are unfamiliar with Postman, the <a href="{{ site.baseurl }}/taskList/task2_1/">LASER Task 2.1 Guide</a> walks through installing it and making requests. Project B works with the Wisconet API in Phase 2, so this is worth getting comfortable with now either way.</p>
          <p><strong>Done when:</strong> you have called at least two backend endpoints yourself and recorded what came back.</p>
        </div>
      </details>

    </div>
  </details>

  <details class="task-card">
    <summary>4. Trace One Feature End to End</summary>
    <div class="card-body">

      <p>This card is the centrepiece of Phase 1. Cards 2 and 3 gave you two maps; this one joins them into a single path you have followed yourself, all the way from a click to a database row and back.</p>

      <h3>Pick a Feature</h3>
      <p>Choose one screen that displays real data. Good candidates:</p>
      <ul>
        <li>Opening a <strong>market profile</strong> and seeing its details.</li>
        <li>Loading a <strong>list of instruments</strong> or submissions for a market.</li>
        <li>Any <strong>analysis or metrics</strong> screen that renders stored data.</li>
      </ul>
      <p>Pick something small and concrete. A screen with one table on it teaches you more than a dashboard with nine widgets, because you can hold the whole path in your head.</p>

      <h3>Follow the Path</h3>
      <p>With both servers running and the Network tab open, load the screen and then follow every step:</p>
      <ol>
        <li>Which <strong>route</strong> did you land on, and which <strong>view file</strong> does it load?</li>
        <li>What triggers the data fetch -- a lifecycle hook, a store action, a user event?</li>
        <li>Which <strong>store or service</strong> makes the request, and what URL does it build?</li>
        <li>What does the <strong>request</strong> look like in the Network tab: method, full URL, parameters, headers?</li>
        <li>Which <strong>backend route and endpoint</strong> receives it?</li>
        <li>What does the endpoint <strong>do</strong> -- which model or service, which query?</li>
        <li>Which <strong>tables</strong> does the data come from?</li>
        <li>What comes back, and how does the view <strong>render</strong> it?</li>
      </ol>
      <p>Every one of those steps is a file you can open. If a step is a guess, it does not count -- go and find the file.</p>

      <h3>Draw It</h3>
      <p>Turn the trace into a diagram: boxes for the pieces, arrows for the calls, each arrow labelled with what is being sent or returned, and each box labelled with the file it corresponds to. Paper, a drawing tool, or slides -- it does not matter which. The diagram goes into your report.</p>

      <p><strong>Done when:</strong> you have a labelled diagram of one feature's full path and can walk someone through it without opening the code.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>5. Using Claude Code to Explore</summary>
    <div class="card-body">

      <p>Claude Code is genuinely good at the task in front of you: summarising an unfamiliar folder, finding where something is defined, and explaining a framework convention you have not met before. Use it. It will save you hours in both repos.</p>
      <p>What it will not do is understand the system on your behalf. The report in Card 6 is a record of <strong>your</strong> understanding, and a report assembled from pasted answers reads exactly like one.</p>

      <h3>Prompts Worth Using</h3>
      <p>Open Claude Code at the root of whichever repo you are exploring, so it can read the actual files:</p>
      <pre class="pre-scroll"><code>What does src/views/Profiles do? List the files and explain what
feature this folder supports.

Where in this codebase is the HTTP client configured, and how does
the base URL get set?

This is a Rails app with a Grape API. Where are the API endpoints
defined, and how are they mounted into the Rails routes?

Explain the associations on the Market model and which tables they
map to in db/schema.rb.

I clicked a button and the Network tab shows a GET to
/api/v1/markets/12. Which endpoint handles that, and what does it
query?</code></pre>

      <h3>Three Rules</h3>
      <ul>
        <li><strong>Verify before you believe.</strong> Claude will occasionally describe a file that does not exist or a function that was deleted two years ago. Every claim that goes into your report should be one you have confirmed by opening the file. If you cannot find the file, the claim does not go in.</li>
        <li><strong>Write in your own words.</strong> Use what Claude gives you as a starting point, then say it yourself. If you cannot restate it without the answer in front of you, you have not learned it yet.</li>
        <li><strong>Ask it to point, not to conclude.</strong> "Where is X defined?" gets you a file path you can check. "Summarise this whole codebase" gets you a paragraph that sounds right and teaches you nothing.</li>
      </ul>

      <p>In your report, note where Claude Code was genuinely useful and where it led you wrong. We are building an LLM-assisted development practice here, and knowing the failure modes is part of the skill.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>6. Write the Current State Understanding Report</summary>
    <div class="card-body">

      <p>The deliverable for Phase 1 is a <strong>Current State Understanding Report</strong>. It is your own reference for the rest of the program, and it is how we see that you have a real grasp of the system before you start changing it.</p>
      <p>Write it as a Markdown file named <code>phase1_current_state_[firstName].md</code>. Aim for four to six pages of substance -- long enough to be genuinely useful to you in Phase 3, short enough that you had to decide what mattered.</p>

      <h3>What Makes It a Good Report</h3>
      <ul>
        <li><strong>Cite file paths.</strong> Every claim about the code should name the file it came from. This is what separates a report you can use later from an essay.</li>
        <li><strong>Your words, not the code's.</strong> Do not paste large blocks of source. Explain what it does.</li>
        <li><strong>Be specific about what you do not know.</strong> "I could not work out how X is authorised, because the check is in Y and I could not find where Y is called" is a strong entry. "Some parts were confusing" is not.</li>
      </ul>

      <h3>Report Template</h3>
      <pre class="pre-scroll"><code># Current State Understanding Report

**Name:** [Your Name]
**Phase:** 1 -- Understanding F2F and Its Repositories' Current State
**Date:** [Date]

## 1. The System in Brief

[Half a page, in your own words. What Farm2Facts does, who uses it,
the three layers, and how the user hierarchy is organised. Write it
for someone joining the project next month.]

## 2. Frontend -- farm2facts-frontend

### 2.1 Structure

[What each top-level folder in src/ is responsible for. One or two
lines each.]

### 2.2 Main Views

[What each view directory from Card 2.2 is responsible for and which
part of the running app it produces. Full descriptions for the first
five, overviews for the rest.]

### 2.3 Data and State

[Where HTTP requests are made, where the base URL comes from, how the
logged-in user and their role are stored, and how the router restricts
access. Name the files.]

## 3. Backend -- farmers-coalition

### 3.1 Structure

[What each folder in app/ is responsible for, where the API routes are
mounted, and what the main configuration files told you.]

### 3.2 Data Model

[The main tables and how they relate. Include your entity sketch.
Cover market organizations, markets, vendors and producers, and
instrument data.]

### 3.3 The Grape API

[How endpoints are declared, whether the API is versioned, how a
caller is authenticated, and what happens between a request arriving
and a row being read. Include the two or three endpoints you called
yourself in Card 3.4 and what they returned.]

## 4. How the Two Communicate

[How the frontend reaches the backend: the base URL, the request
format, and how the backend identifies who is asking.]

## 5. Feature Trace

**Feature traced:** [The screen or action you chose]

[Your diagram, embedded as an image or described in text.]

[Then the path in writing, step by step, naming the file at each step:
route, view, store or service, request, backend route, endpoint,
model, tables, response, render.]

## 6. Open Questions

[Everything you could not work out. Be specific: what you were trying
to understand, where you got to, and where you got stuck. Number them
so we can answer them individually.]

## 7. Observations

[Anything you noticed that is worth flagging: parts of the code that
look unused, data that looks stale or inconsistent, patterns that are
applied in some places but not others, or anything that struck you as
a candidate for improvement. Do not fix anything -- just record it.
Phase 2 starts from notes like these.]

## 8. Working With Claude Code

[Where it helped, where it was wrong, and what you would prompt
differently next time. A short section, three or four sentences.]</code></pre>

      <p>Sections 6 and 7 are the two we read most closely. Section 6 tells us where the program's documentation is failing you, and Section 7 is where Phase 2's investigation actually begins -- several of the things you notice here will turn into proposals a fortnight from now.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>7. Phase 1 Completion</summary>
    <div class="card-body">

      <p>Send your report to <strong>Abanish</strong> in the WISCURDS Slack channel, with the checklist below in the message. Attach the report file itself, or a link to it if you wrote it somewhere else.</p>
      <p>There is no branch and no merge request for this phase. Phase 3 is where code work starts and the issue-branch-PR flow begins.</p>

      <h3>Checklist Template</h3>
      <pre class="pre-scroll"><code>Phase 1 Completion -- [Your Name]

[ ] Read the Development Structure Overview
[ ] Clicked through the running app and listed its main sections
[ ] Mapped the top level of src/ in the frontend
[ ] Described all ten view directories from Card 2.2
[ ] Found where requests are made and how the router restricts access
[ ] Mapped app/ in the backend and read routes.rb and schema.rb
[ ] Sketched the data model and the relationships between the main tables
[ ] Read the Grape API and called at least two endpoints myself
[ ] Traced one feature end to end and drew the path
[ ] Report written and attached

Feature I traced:
[The screen or action]

My top three open questions:
1.
2.
3.

Anything that blocked me:
[What you could not get to, and why. Write "nothing" only if that is
genuinely the case.]</code></pre>

      <p>Bring your three open questions to the next weekly check-in. We would rather spend that half hour answering them than hearing that everything went fine.</p>
      <p>If you did not get through everything, send the message anyway with what you have. A partial report on time is more useful than a complete one two weeks late, and Phase 2 is built on what you learned here.</p>

    </div>
  </details>

</div>
