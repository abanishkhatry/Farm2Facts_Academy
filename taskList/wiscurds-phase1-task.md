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

**You are reading, not building.** Nothing in this phase changes application code. If you find something broken or badly written, write it down instead of fixing it. Those notes are useful later; an unplanned fix this early is not.

**You will still submit through the full Git workflow.** Your reports are committed on a feature branch cut from `dev` and delivered as merge requests, exactly the way every feature will be delivered from here on. Card 1 sets the branches up, Card 7 covers the submission. Learning that cycle on a Markdown file, where nothing can break, is far easier than learning it on your first real code change.

**You will not understand everything, and you are not supposed to.** This is a real application built over several years by people who are no longer on the project. Parts of it will be confusing, inconsistent, or apparently unused. Reading a codebase you did not write is a skill, and being able to say precisely what you do not understand is most of it. Keep a running list of open questions as you go -- that list is a graded part of the deliverable, not an admission of failure.

**Use an LLM or coding agent. We recommend it.** Getting your head around two unfamiliar repositories of this size is a genuinely complex process, and doing it unaided is slow rather than virtuous. Claude Code, or whichever coding agent you prefer, is very good at precisely this work: summarising a folder you have never opened, finding where something is defined, and explaining a framework convention you have not met before. Use one throughout this phase. What matters is that you verify what it tells you against the actual files and write your report in your own words -- Card 5 covers how to get real value out of it and the handful of ways it will mislead you if you let it.

Everyone does this phase **individually**. All four of you write your own report. The split into two project teams happens in Phase 2, and the understanding you build here is what you bring to whichever team you land on.

Phase 1 assumes both repos are running on your machine from [Phase 0]({{ site.baseurl }}/taskList/wiscurds-phase0/). If they are not, finish that first -- most of this phase depends on being able to click through the running app.

<div class="task-card-grid">

  <div class="task-card">
    <p class="card-title">1. Update Both Repos and Open Your Branch</p>
    <div class="card-body">

      <p>Do this before you read a single file. Your clones from Phase 0 are already out of date, and one of the things you are missing is the directory your reports go in.</p>

      <h3>a. Pull the latest dev in both repos</h3>
      <p>In <strong>each</strong> repository -- <code>farmers-coalition</code> and <code>farm2facts-frontend</code> -- switch to <code>dev</code> and pull:</p>
      <pre><code>git checkout dev
git pull</code></pre>
      <p>That brings down a <code>wiscurds/</code> directory at the root of both repos. That directory is where every written deliverable for this program lives, this phase and the ones after it.</p>
      <p>Pulling first also means you are reading the current state of the code rather than whatever it looked like on the day you cloned. Mapping a stale codebase is wasted work.</p>

      <h3>b. Create your feature branch in both repos</h3>
      <p>With <code>dev</code> up to date, cut your branch from it. Same branch name in both repositories:</p>
      <pre><code>git checkout -b feat-wis-p1-[firstName]</code></pre>
      <p>Replace <code>[firstName]</code> with your actual first name, lowercase. Example: <code>feat-wis-p1-abanish</code>. The name reads as: a feature branch, WISCURDS, Phase 1, yours.</p>
      <p>Confirm you are on it with <code>git branch</code> before you go any further. <strong>Never commit to <code>dev</code> or <code>main</code> directly</strong> -- that rule holds for every phase from here on, and the full branch strategy is in the <a href="{{ site.baseurl }}/docs/guides/#git-workflow-reference">Git Workflow Reference</a>.</p>

      <h3>c. Make your directories</h3>
      <p>Inside <code>wiscurds/</code> in each repo, create a folder for this phase and one for yourself inside it:</p>
      <pre><code>wiscurds/
└── phase1/
    └── [firstName]/</code></pre>
      <p>Your report for that repo goes in that folder. Card 6 covers what goes where.</p>

      <p><strong>Done when:</strong> both repos are on <code>feat-wis-p1-[firstName]</code>, cut from an up-to-date <code>dev</code>, each with an empty <code>wiscurds/phase1/[firstName]/</code> waiting for your report.</p>

    </div>
  </div>

  <details class="task-card">
    <summary>2. Map the Frontend</summary>
    <div class="card-body">

      <p>The frontend is <a href="https://git.doit.wisc.edu/at-trad/farm2facts-frontend" target="_blank" rel="noopener noreferrer">farm2facts-frontend</a>, a Vue 3 application using Pinia for state and the MDB Vue UI Kit for components. Work in your local clone, on the branch you created in Card 1.</p>
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
          <p>Most of the app's surface area is in <code>src/views/</code>. Go through the directories below and write down what each one is responsible for and which part of the running app it produces. Connect them back to what you see in the running app -- keep it open at <code>localhost:8080</code> and click through the section a folder produces as you read it.</p>
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
          <p><strong>Done when:</strong> every directory above has a written description, and you can point to the folder responsible for any screen in the running app.</p>
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

      <p>The backend is <a href="https://git.doit.wisc.edu/at-trad/farmers-coalition" target="_blank" rel="noopener noreferrer">farmers-coalition</a>, a Rails 6.1 application with a MySQL database and a Grape API. Work in your local clone, on the branch you created in Card 1.</p>
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
          <p>Using <code>db/schema.rb</code> and the model files together, work out how the user hierarchy -- a market organization containing markets, each containing vendors and producers -- is actually stored:</p>
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
    <summary>5. Using an LLM or Coding Agent</summary>
    <div class="card-body">

      <p>We recommend working with a coding agent throughout this phase. <strong>Claude Code</strong> is what the rest of the team uses and what our examples assume, but any capable agent or LLM is fine -- what matters is that you use one, not which one.</p>
      <p>These tools are genuinely good at the task in front of you: summarising an unfamiliar folder, finding where something is defined, and explaining a framework convention you have not met before. In two repositories this size, that is hours saved.</p>
      <p>What they will not do is understand the system on your behalf. The report in Card 6 is a record of <strong>your</strong> understanding, and a report assembled from pasted answers reads exactly like one.</p>

      <h3>Prompts Worth Using</h3>
      <p>Open your agent at the root of whichever repo you are exploring, so it can read the actual files rather than guessing from what you paste in:</p>
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
        <li><strong>Verify before you believe.</strong> Any agent will occasionally describe a file that does not exist or a function that was deleted two years ago. Every claim that goes into your report should be one you have confirmed by opening the file. If you cannot find the file, the claim does not go in.</li>
        <li><strong>Write in your own words.</strong> Use what the agent gives you as a starting point, then say it yourself. If you cannot restate it without the answer in front of you, you have not learned it yet.</li>
        <li><strong>Ask it to point, not to conclude.</strong> "Where is X defined?" gets you a file path you can check. "Summarise this whole codebase" gets you a paragraph that sounds right and teaches you nothing.</li>
      </ul>

      <p>In your report, note which tool you used, where it was genuinely useful, and where it led you wrong. We are building an LLM-assisted development practice here, and knowing the failure modes is part of the skill.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>6. Write the Current State Understanding Report</summary>
    <div class="card-body">

      <p>The deliverable for Phase 1 is a <strong>Current State Understanding Report</strong>. It is your own reference for the rest of the program, and it is how we see that you have a real grasp of the system before you start changing it.</p>
      <p>Because the report covers two repositories, you write it as <strong>two files, one in each repo</strong>. Each one goes in that repo's <code>wiscurds/phase1/[firstName]/</code> folder, on the branch you created in Card 1:</p>
      <table>
        <thead><tr><th style="width:34%">Repo</th><th>File</th></tr></thead>
        <tbody>
          <tr><td><code>farm2facts-frontend</code></td><td><code>phase1_frontend_[firstName].md</code></td></tr>
          <tr><td><code>farmers-coalition</code></td><td><code>phase1_backend_[firstName].md</code></td></tr>
        </tbody>
      </table>
      <p>Splitting it this way means the person reviewing your frontend merge request is reading about the frontend, and it gives you two runs at the workflow instead of one. Aim for three to four pages per file -- long enough to be genuinely useful to you in Phase 3, short enough that you had to decide what mattered.</p>

      <h3>What Makes It a Good Report</h3>
      <ul>
        <li><strong>Cite file paths.</strong> Every claim about the code should name the file it came from. This is what separates a report you can use later from an essay.</li>
        <li><strong>Your words, not the code's.</strong> Do not paste large blocks of source. Explain what it does.</li>
        <li><strong>Be specific about what you do not know.</strong> "I could not work out how X is authorised, because the check is in Y and I could not find where Y is called" is a strong entry. "Some parts were confusing" is not.</li>
      </ul>

      <h3>The Feature Trace Goes in Both</h3>
      <p>Your trace from Card 4 crosses both repositories, so it does not belong to either one on its own. Put the <strong>diagram in both files</strong>, and in each file write up the half of the path that happens in that repo. Save the diagram image alongside the report in the same folder, for example <code>feature_trace_[firstName].png</code>, so the Markdown can point at it.</p>

      <h3>Template -- Frontend Report</h3>
      <pre class="pre-scroll"><code># Phase 1 -- Frontend Current State

**Name:** [Your Name]
**Repo:** farm2facts-frontend
**Date:** [Date]

## 1. The System in Brief

[Half a page, in your own words. What Farm2Facts does, who uses it,
the three layers, and how the user hierarchy is organised. Write it
for someone joining the project next month.]

## 2. What the App Does

[The main sections of the running app as they appear in the
navigation, and what each one is for. One line each.]

## 3. Structure

[What each top-level folder in src/ is responsible for. One or two
lines each.]

## 4. Main Views

[What each view directory from Card 2.2 is responsible for and which
part of the running app it produces. Full descriptions for the first
five, overviews for the rest. Name the folders.]

## 5. Data and State

[Where HTTP requests are made, where the base URL comes from, how the
logged-in user and their role are stored, and how the router restricts
access. Name the files.]

## 6. Feature Trace -- Frontend Half

**Feature traced:** [The screen or action you chose]

![Feature trace](feature_trace_[firstName].png)

[The path from the click to the request leaving the browser, naming
the file at each step: route, view, what triggers the fetch, the store
or service, and the exact request that goes out. Then what comes back
and how the view renders it.]

## 7. Open Questions

[Everything about the frontend you could not work out. Be specific:
what you were trying to understand, where you got to, and where you
got stuck. Number them so we can answer them individually.]

## 8. Observations

[Anything worth flagging: code that looks unused, patterns applied in
some places but not others, anything that struck you as a candidate
for improvement. Do not fix anything -- just record it. Phase 2 starts
from notes like these.]

## 9. Working With an LLM

[Which tool you used, where it helped, where it was wrong, and what
you would prompt differently next time. Three or four sentences.]</code></pre>

      <h3>Template -- Backend Report</h3>
      <pre class="pre-scroll"><code># Phase 1 -- Backend Current State

**Name:** [Your Name]
**Repo:** farmers-coalition
**Date:** [Date]

## 1. Structure

[What each folder in app/ is responsible for, where the API routes are
mounted, and what routes.rb, schema.rb, and the Gemfile told you.]

## 2. Data Model

[The main tables and how they relate. Include your entity sketch.
Cover market organizations, markets, vendors and producers, and
instrument data. Name the tables and the models.]

## 3. The Grape API

[How endpoints are declared, whether the API is versioned, how a
caller is authenticated, and what happens between a request arriving
and a row being read.]

## 4. Endpoints I Called

[The two or three endpoints you called yourself in Card 3.4: the URL,
the status code, what came back, and how it compared to what you
expected from reading the code.]

## 5. How the Two Repos Communicate

[How the frontend reaches the backend: the base URL, the request
format, and how the backend identifies who is asking. This is the
seam between the two repositories -- describe it from the backend
side.]

## 6. Feature Trace -- Backend Half

**Feature traced:** [The same feature as your frontend report]

![Feature trace](feature_trace_[firstName].png)

[The path from the request arriving to the response going back out,
naming the file at each step: route, endpoint, model or service, the
query, and the tables the data came from.]

## 7. Open Questions

[Everything about the backend you could not work out. Be specific and
number them.]

## 8. Observations

[Anything worth flagging: data that looks stale or inconsistent,
tables that look unused, anything that struck you as a candidate for
improvement. Record it, do not fix it.]

## 9. Working With an LLM

[Which tool you used, where it helped, where it was wrong, and what
you would prompt differently next time. Three or four sentences.]</code></pre>

      <p>The Open Questions and Observations sections are the two we read most closely. Open Questions tells us where the program's documentation is failing you, and Observations is where Phase 2's investigation actually begins -- several of the things you notice here will turn into proposals a fortnight from now.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>7. Commit and Submit</summary>
    <div class="card-body">

      <p>You submit by <strong>merge request</strong>, one in each repository. Nothing is submitted until both are open and assigned.</p>
      <p>This is the part of Phase 1 that matters most for the rest of the program. From here on, every change any of us makes to Farm2Facts arrives the same way: branch off <code>dev</code>, commit the work, push, open a merge request, get it reviewed, merge. Phase 3 onward you will be doing this with code that can break things. Doing it now, with a Markdown file that cannot, is the point.</p>

      <details>
        <summary>7.1 Commit Your Work</summary>
        <div class="section-body">
          <p>In each repo, on your <code>feat-wis-p1-[firstName]</code> branch, add your files and commit:</p>
          <pre><code>git status
git add wiscurds/phase1/[firstName]/
git commit -m "Add Phase 1 frontend current state report for [firstName]"</code></pre>
          <p>Run <code>git status</code> before you add anything, every time. It tells you which branch you are on and exactly what you are about to commit. Two things to check in its output:</p>
          <ul>
            <li>You are on <strong><code>feat-wis-p1-[firstName]</code></strong>, not <code>dev</code>. If you are on <code>dev</code>, stop and come back to Card 1.</li>
            <li>The only files listed are <strong>yours</strong>, under <code>wiscurds/phase1/[firstName]/</code>. Nothing from <code>src/</code>, <code>app/</code>, or anyone else's folder should appear. If something does, you changed a file by accident -- undo it before committing.</li>
          </ul>
          <p>Write commit messages in the imperative, starting with a verb, under 72 characters. In the backend repo the message is the same with "backend" in place of "frontend". The full rules are in the <a href="{{ site.baseurl }}/docs/guides/#git-workflow-reference">Git Workflow Reference</a>.</p>
          <p>If you wrote your report over several sittings, several commits are better than one. A commit is a save point, not a submission.</p>
        </div>
      </details>

      <details>
        <summary>7.2 Push Your Branch</summary>
        <div class="section-body">
          <p>Your commits exist only on your machine until you push them. The first time you push a new branch, tell Git where it goes:</p>
          <pre><code>git push -u origin feat-wis-p1-[firstName]</code></pre>
          <p>After that first push, plain <code>git push</code> is enough for the rest of the phase.</p>
          <p>GitLab prints a link to open a merge request in the push output. You can use it or go through the UI in the next card -- they do the same thing.</p>
          <p><strong>Done when:</strong> your branch appears on GitLab in both repos, under <strong>Code &rarr; Branches</strong>, with your commits on it.</p>
        </div>
      </details>

      <details>
        <summary>7.3 Open Your Merge Requests</summary>
        <div class="section-body">
          <p>GitLab calls it a <strong>Merge Request (MR)</strong>. GitHub calls the same thing a Pull Request. The name differs, the workflow does not.</p>
          <p>Do this in <strong>both</strong> repositories:</p>
          <ol>
            <li>In the left sidebar, go to <strong>Code &rarr; Merge requests</strong>.</li>
            <li>Click <strong>New merge request</strong>.</li>
            <li><strong>Source branch:</strong> <code>feat-wis-p1-[firstName]</code>.</li>
            <li><strong>Target branch:</strong> <code>dev</code>. Never <code>main</code>.</li>
            <li>Click <strong>Compare branches and continue</strong>.</li>
            <li>Title it <code>Phase 1 frontend current state report -- [Your Name]</code>, or <code>backend</code> in the backend repo.</li>
            <li>Fill out the description using the <a href="{{ site.baseurl }}/docs/guides/#pull-requests">Pull Requests guide</a>. Fill in every field -- a description that says "phase 1 report" tells a reviewer nothing.</li>
            <li>Assign <strong>Abanish</strong> as the reviewer.</li>
          </ol>
          <p>Before you submit, open the <strong>Changes</strong> tab and read your own diff. Every line in it should be a line you meant to write. This habit costs thirty seconds and will save you from a bad merge more than once over the program.</p>
          <p>In your description, include your <strong>top three open questions</strong> from the report. That way they are visible to the reviewer without them having to open the file.</p>
          <p><strong>Done when:</strong> two merge requests are open, both targeting <code>dev</code>, both assigned to Abanish.</p>
        </div>
      </details>

      <details>
        <summary>7.4 Respond to Review</summary>
        <div class="section-body">
          <p>An open merge request is not a finished one. Expect comments -- that is what review is for, and on a first MR there are usually a few.</p>
          <p>When you get feedback, do not open a new branch or a new MR. Commit the changes on the <strong>same branch</strong> and push again; the MR updates itself. Reply to each comment when you have addressed it, and say what you changed.</p>
          <p>Once both MRs are approved, we merge them into <code>dev</code>. That is the end of Phase 1.</p>
        </div>
      </details>

      <p>Bring your three open questions to the next weekly check-in. We would rather spend that half hour answering them than hearing that everything went fine.</p>
      <p>If Git itself is what stopped you, say so in the WISCURDS Slack channel. Getting tangled in branches on a first merge request is completely normal and takes about five minutes to sort out together -- but only if we know about it.</p>
      <p>If you did not get through everything, open the merge requests anyway with what you have and say what is missing in the description. A partial report on time is more useful than a complete one two weeks late, and Phase 2 is built on what you learned here.</p>

    </div>
  </details>

</div>
