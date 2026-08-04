---
layout: default
title: "Phase 0 Task Guide"
permalink: /taskList/wiscurds-phase0/
---

# Phase 0 Task Guide

**Program:** WISCURDS | **Phase:** 0 -- Project Onboarding and Team Setup

---

This is the task companion to the [Phase 0 milestone card]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-0). That card describes what the phase covers; this guide is what you actually do, in order.

Phase 0 has one goal: by the end of it you can open both Farm2Facts repositories, have both of them cloned on your own machine, and reach the right person when you get stuck. No development work starts until all three are true.

**One note before you start.** We are still working through the **licensing required to run the repositories**, so Phase 0 stops at getting the code onto your machine. **Do not try to run either repo locally yet.** Running them is postponed until the licensing is resolved, and we will tell you in Slack when to go ahead. Nothing in this phase needs a running application.

Work through the cards in order. Card 1 gates everything else, so start it the day you read this -- granting repo permissions depends on us, not on you, and it can take a couple of days.

<div class="task-card-grid">

  <div class="task-card">
    <p class="card-title">1. GitLab Account and Repo Access</p>
    <div class="card-body">

      <p>Both Farm2Facts repositories are hosted on <strong>GitLab</strong>, not GitHub. They are private, so you cannot clone them until we add you. Do this first.</p>

      <details>
        <summary>1.1 Create Your GitLab Account</summary>
        <div class="section-body">
          <p>If you do not already have a GitLab account, create one at <a href="https://git.doit.wisc.edu" target="_blank" rel="noopener noreferrer">git.doit.wisc.edu</a>.</p>
          <p>Use your <strong>@wisc.edu email address</strong>. This is not optional -- the repos live on the UW-Madison DoIT GitLab instance, and access is granted against your university identity. A personal Gmail or a gitlab.com account will not work.</p>
          <p>If you already have an account on that instance from a class, use it. You do not need a second one.</p>
        </div>
      </details>

      <details>
        <summary>1.2 Send Us Your Username</summary>
        <div class="section-body">
          <p>Once your account exists, find your GitLab username: click your avatar in the top right, and it appears under your name as <code>@username</code>.</p>
          <p>Send that username to <strong>Abanish Khatry</strong> in the project Slack channel, or by email at <a href="mailto:akhatry@wisc.edu">akhatry@wisc.edu</a>. Include:</p>
          <ul>
            <li>Your GitLab username</li>
            <li>The @wisc.edu email the account is registered under</li>
          </ul>
          <p>We then grant you the permissions you need on both repositories. Until that is done you cannot clone or push, so send this early rather than at the end of the week.</p>
        </div>
      </details>

      <details>
        <summary>1.3 Confirm Your Access</summary>
        <div class="section-body">
          <p>After we tell you the permissions are in place, confirm it yourself rather than assuming. Open both repos while logged in:</p>
          <ul>
            <li><a href="https://git.doit.wisc.edu/at-trad/farm2facts-frontend" target="_blank" rel="noopener noreferrer">Farm2Facts Frontend</a> -- the Vue 3 data collection and reporting platform</li>
            <li><a href="https://git.doit.wisc.edu/at-trad/farmers-coalition" target="_blank" rel="noopener noreferrer">Farm2Facts Backend</a> -- the Rails 6.1 metrics API and web interface</li>
          </ul>
          <p>You should see the file tree for each, not a 404 or a permissions error. A 404 on a private GitLab repo usually means you are not a member yet, not that the page is missing -- if you get one, come back to us.</p>
          <p>While you are there, check that both repos show a <code>dev</code> branch alongside <code>main</code>. That is the branch you will work from in later phases.</p>
        </div>
      </details>

    </div>
  </div>

  <details class="task-card">
    <summary>2. Get Both Repos Onto Your Machine</summary>
    <div class="card-body">

      <p>Farm2Facts is split across two repositories and you will work in both over the course of the program. In this phase you get both of them <strong>cloned and present locally</strong>. That is the whole scope of this card.</p>
      <p><strong>You are not running either repo in this phase.</strong> We are still sorting out the licensing needed to run them, so starting the servers is postponed until that is resolved. Clone the code, look around it, and stop there. We will announce in Slack when running is unblocked, and that becomes the first thing you do at the start of Phase 1.</p>
      <p>This means you can skip the install-and-configure portions of the setup guides for now: no Ruby or Node dependency installs, no database setup, no editing <code>database.yml</code> or <code>.env</code>. Read those sections so you know what is coming, but do not execute them.</p>

      <details>
        <summary>2.1 Start With the Student Onboarding Plan</summary>
        <div class="section-body">
          <p>Read the <a href="{{ site.baseurl }}/STUDENT_ONBOARDING_PLAN">Student Onboarding Plan</a> before you run any commands. It gives you the full picture: the Git and GitLab concepts we assume, what each repository is, and how the database fits in.</p>
          <p>Two things to take away from it specifically:</p>
          <ul>
            <li><strong>How the pieces connect.</strong> The frontend talks to the backend over HTTP; the backend talks to MySQL. Later you will stand up all three locally.</li>
            <li><strong>You do not touch the production database.</strong> As a developer you work against a local database, and all data reaches the frontend through the backend API.</li>
          </ul>
          <p>The onboarding plan is written for a full local setup, which is what you will eventually do. For <strong>this phase only</strong>, read it for understanding and stop before any step that installs dependencies or starts a server.</p>
          <p>The same applies to the <a href="{{ site.baseurl }}/STUDENT_ONBOARDING_PLAN#running-lab-machines">Running Lab Machines</a> section. Even on a <strong>Kaufman Lab machine</strong>, where everything is already installed, hold off on starting MAMP and the two servers until we confirm the licensing is settled.</p>
        </div>
      </details>

      <details>
        <summary>2.2 Clone the Backend</summary>
        <div class="section-body">
          <p>Clone <code>farmers-coalition</code>, the Rails 6.1 metrics API, so the code is on your machine. Get the clone URL from the <strong>Code</strong> button on the <a href="https://git.doit.wisc.edu/at-trad/farmers-coalition" target="_blank" rel="noopener noreferrer">repo's GitLab page</a>, then:</p>
          <pre><code>git clone &lt;backend-repo-url&gt;
cd farmers-coalition
git checkout dev</code></pre>
          <p>Work from <code>dev</code>, not <code>main</code>. That is the branch all development happens against.</p>
          <p><strong>Stop there.</strong> Do not install Ruby or its gems, do not set up MySQL, do not edit <code>config/database.yml</code>, and do not run <code>bin/rails server</code>. Those steps are in the <a href="{{ site.baseurl }}/docs/guides/BACKEND_GUIDE">Backend setup guide</a> and you will work through them once the licensing is resolved.</p>
          <p><strong>Done when:</strong> the <code>farmers-coalition</code> directory exists locally, is on the <code>dev</code> branch, and <code>git status</code> reports a clean working tree.</p>
          <p>Read through the guide anyway so you know what the setup will involve. Skim the repo's top-level directories too -- <code>app/</code>, <code>config/</code>, <code>db/</code> -- so the structure is not new to you in Phase 1.</p>
        </div>
      </details>

      <details>
        <summary>2.3 Clone the Frontend</summary>
        <div class="section-body">
          <p>Do the same for <code>farm2facts-frontend</code>, the Vue 3 application. Get the clone URL from the <strong>Code</strong> button on the <a href="https://git.doit.wisc.edu/at-trad/farm2facts-frontend" target="_blank" rel="noopener noreferrer">repo's GitLab page</a>, then:</p>
          <pre><code>git clone &lt;frontend-repo-url&gt;
cd farm2facts-frontend
git checkout dev</code></pre>
          <p><strong>Stop there as well.</strong> Do not run <code>npm install</code>, do not create or edit the <code>.env</code> file, and do not run <code>npm run serve</code>. The <a href="{{ site.baseurl }}/docs/guides/FRONTEND_GUIDE">Frontend setup guide</a> covers all of that for when running is unblocked.</p>
          <p><strong>Done when:</strong> the <code>farm2facts-frontend</code> directory exists locally, is on the <code>dev</code> branch, and <code>git status</code> reports a clean working tree.</p>
          <p>While you are in the repo, open the <code>CLAUDE.md</code> file at the root and read it. It describes the codebase conventions, and it costs you nothing to read without the app running.</p>
        </div>
      </details>

      <details>
        <summary>2.4 Confirm Both Clones and Hold on Running</summary>
        <div class="section-body">
          <p>You cannot verify a running application in this phase, so verify the clones instead. In each repository directory, run:</p>
          <pre><code>git remote -v
git branch --show-current
git log --oneline -5</code></pre>
          <p>Check that:</p>
          <ul>
            <li>The remote points at the correct <code>git.doit.wisc.edu/at-trad/...</code> repository.</li>
            <li>The current branch is <code>dev</code>.</li>
            <li><code>git log</code> shows real commit history, which confirms the clone completed rather than stopping partway.</li>
          </ul>
          <p>Copy the output of those three commands for both repos. You submit it in Card 4 as evidence, in place of the screenshots a running setup would have produced.</p>
          <h3>What is postponed until licensing is fixed</h3>
          <p>These steps are deliberately <strong>not</strong> part of Phase 0, and you should not attempt them yet:</p>
          <ul>
            <li>Installing Ruby, gems, Node, or npm dependencies</li>
            <li>Setting up MySQL or MAMP and loading a local database</li>
            <li>Configuring <code>config/database.yml</code> or the frontend <code>.env</code></li>
            <li>Running <code>bin/rails server</code> or <code>npm run serve</code></li>
            <li>Checking frontend-to-backend requests in the browser</li>
          </ul>
          <p>We will post in Slack once the licensing is resolved. At that point work through both setup guides in full, backend first, and confirm the frontend is reaching the backend. Until then, being blocked here is expected and is not something you need to debug.</p>
        </div>
      </details>

      <details>
        <summary>2.5 Note What Fought You</summary>
        <div class="section-body">
          <p>As you clone the repos, keep a short running note of anything that did not go as described: an authentication prompt you did not expect, a missing <code>dev</code> branch, a permissions error, a step that was unclear.</p>
          <p>This is not busywork. Our setup guides are living documents, and the fastest time to improve them is while a new developer is going through them. Two or three lines per problem is enough -- what broke, and what fixed it.</p>
          <p>Keep the note going when you come back to the full setup after licensing clears, since that is where most of the friction usually is. You submit what you have so far in Card 4.</p>
        </div>
      </details>

    </div>
  </details>

  <details class="task-card">
    <summary>3. Communication and Meetings</summary>
    <div class="card-body">

      <p>You are joining a working team, not doing an assignment alone. Getting the communication set up matters as much as getting the code running.</p>

      <h3>Channels</h3>
      <p>We use two:</p>
      <ul>
        <li><strong>Slack</strong> for quick, day-to-day communication. Each project has its own dedicated channel, and that is where most conversation happens. Ask questions there rather than sitting on them.</li>
        <li><strong>Email</strong> for anything more formal or that needs a lasting record.</li>
      </ul>
      <p>Make sure you are in the project Slack channel. If you have not been added, tell Abanish and we will add you.</p>

      <h3>Who to Contact</h3>
      <p>Knowing who to ask saves you days. Match the question to the person:</p>
      <table>
        <thead>
          <tr><th>What you need</th><th>Who</th></tr>
        </thead>
        <tbody>
          <tr><td>Anything code or task related</td><td><strong>Abanish Khatry</strong> -- your focal point of contact for development</td></tr>
          <tr><td>Professional guidance</td><td><strong>Garrett Smith</strong> -- <a href="mailto:garrett.smith@wisc.edu">garrett.smith@wisc.edu</a></td></tr>
          <tr><td>Administrative matters</td><td><strong>Alfonso Morales</strong> -- <a href="mailto:morales1@wisc.edu">morales1@wisc.edu</a></td></tr>
        </tbody>
      </table>
      <p>The full contact list, including the Kaufman Lab directors, is on the <a href="{{ site.baseurl }}/">Academy home page</a>.</p>

      <h3>Meetings</h3>
      <ul>
        <li><strong>Until the Fall semester begins:</strong> we meet <strong>weekly and virtually</strong> for progress check-ins. Come with what you finished, what you are on, and what is blocking you.</li>
        <li><strong>Once Fall begins:</strong> we set the meeting time and frequency together, based on everyone's availability.</li>
      </ul>

      <h3>Your Task Here</h3>
      <ol>
        <li>Confirm you are in the project Slack channel and post a short introduction in it.</li>
        <li>Save the three contacts above somewhere you will actually look.</li>
        <li>Send Abanish your <strong>Fall availability</strong> -- the days and rough time windows you could make a recurring meeting. We need all four students' availability before we can set the Fall schedule, so a late reply holds up everyone.</li>
      </ol>

    </div>
  </details>

  <details class="task-card">
    <summary>4. Phase 0 Completion</summary>
    <div class="card-body">

      <p>Phase 0 has no pull request. The issue-branch-PR workflow starts in <a href="{{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-3">Phase 3</a>, the first phase where you write code. For now you confirm your setup directly to Abanish.</p>

      <h3>Checklist</h3>
      <p>Go through this yourself before you send anything:</p>
      <ul>
        <li>[ ] GitLab account created under my @wisc.edu email</li>
        <li>[ ] Username sent to Abanish and permissions granted</li>
        <li>[ ] I can open both repositories on GitLab and see their <code>dev</code> branches</li>
        <li>[ ] Backend repo cloned locally and on the <code>dev</code> branch</li>
        <li>[ ] Frontend repo cloned locally and on the <code>dev</code> branch</li>
        <li>[ ] I have read both setup guides, without executing the install and run steps</li>
        <li>[ ] I am in the project Slack channel and have introduced myself</li>
        <li>[ ] I have the three points of contact saved</li>
        <li>[ ] I have sent my Fall availability</li>
      </ul>

      <h3>What to Send</h3>
      <p>Post a single message to <strong>Abanish</strong> in the project Slack channel containing:</p>
      <ol>
        <li>The checklist above, with each item marked done.</li>
        <li>The <strong>verification output</strong> from Card 2.4 -- <code>git remote -v</code>, <code>git branch --show-current</code>, and <code>git log --oneline -5</code> for both repos. Paste it as text or send a screenshot of your terminal.</li>
        <li>Your <strong>notes</strong> from Card 2.5 -- what fought you and what fixed it. Write "nothing broke" if that is genuinely the case.</li>
      </ol>
      <p>No running-application screenshots this time, since running the repos is postponed until the licensing is resolved. The clone verification takes their place.</p>
      <p>If an item is not done, send the message anyway and say which one and why. A blocked step we know about gets unblocked; one we do not know about does not.</p>

      <h3>Then What</h3>
      <p>Once your clones are confirmed, move on to <a href="{{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-1">Phase 1: Understanding F2F and Its Repositories' Current State</a>. Phase 1 is about reading and understanding both codebases and their ADRs, which you can do from the cloned code without either application running.</p>
      <p>Watch Slack for the licensing update. When it lands, work through both setup guides in full before you get any deeper into the program -- every phase from <a href="{{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-3">Phase 3</a> on needs a working local environment.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>What You Learned</summary>
    <div class="card-body">
      <p>What this phase gives you that every later phase depends on.</p>
      <div class="skills-grid">
        <div>
          <p class="skill-group-label">GitLab</p>
          <div class="skill-tags">
            <span class="skill-tag">DoIT GitLab instance</span>
            <span class="skill-tag">Private repo access</span>
            <span class="skill-tag">main vs. dev</span>
          </div>
        </div>
        <div>
          <p class="skill-group-label">Cloning Repos</p>
          <div class="skill-tags">
            <span class="skill-tag">git clone</span>
            <span class="skill-tag">Checking out dev</span>
            <span class="skill-tag">Verifying a remote</span>
          </div>
        </div>
        <div>
          <p class="skill-group-label">Reading a Codebase Cold</p>
          <div class="skill-tags">
            <span class="skill-tag">Repo structure</span>
            <span class="skill-tag">CLAUDE.md</span>
            <span class="skill-tag">Setup guides</span>
          </div>
        </div>
        <div>
          <p class="skill-group-label">Working Around Blockers</p>
          <div class="skill-tags">
            <span class="skill-tag">Scoping to what is unblocked</span>
            <span class="skill-tag">Evidence in place of output</span>
            <span class="skill-tag">Tracking friction</span>
          </div>
        </div>
        <div>
          <p class="skill-group-label">Working on a Team</p>
          <div class="skill-tags">
            <span class="skill-tag">Slack vs. email</span>
            <span class="skill-tag">Escalating to the right person</span>
            <span class="skill-tag">Reporting blockers early</span>
          </div>
        </div>
      </div>
    </div>
  </details>

</div>
