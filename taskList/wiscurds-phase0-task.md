---
layout: default
title: "Phase 0 Task Guide"
permalink: /taskList/wiscurds-phase0/
---

# Phase 0 Task Guide

**Program:** WISCURDS | **Phase:** 0 -- Project Onboarding and Team Setup

---

This is the task companion to the [Phase 0 milestone card]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-0). That card describes what the phase covers; this guide is what you actually do, in order.

Phase 0 has one goal: by the end of it you can open both Farm2Facts repositories, run both of them on your own machine, and reach the right person when you get stuck. No development work starts until all three are true.

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
    <summary>2. Get Both Repos Running Locally</summary>
    <div class="card-body">

      <p>Farm2Facts is split across two repositories and you will work in both over the course of the program. In this phase you get each one running on your own machine.</p>
      <p>The setup steps are already written down. Follow the guides rather than improvising, and do not skip ahead to the frontend before the backend is up -- the frontend has nothing to display without it.</p>

      <details>
        <summary>2.1 Start With the Student Onboarding Plan</summary>
        <div class="section-body">
          <p>Read the <a href="{{ site.baseurl }}/STUDENT_ONBOARDING_PLAN">Student Onboarding Plan</a> before you run any commands. It gives you the full picture: the Git and GitLab concepts we assume, what each repository is, and how the database fits in.</p>
          <p>Two things to take away from it specifically:</p>
          <ul>
            <li><strong>How the pieces connect.</strong> The frontend talks to the backend over HTTP; the backend talks to MySQL. You are standing up all three locally.</li>
            <li><strong>You do not touch the production database.</strong> As a developer you work against a local database, and all data reaches the frontend through the backend API.</li>
          </ul>
          <p>If you are working on a <strong>Kaufman Lab machine</strong>, read the <a href="{{ site.baseurl }}/STUDENT_ONBOARDING_PLAN#running-lab-machines">Running Lab Machines</a> section instead of the full setup guides. Those machines already have everything installed, so you only need to start MAMP and run the two servers.</p>
        </div>
      </details>

      <details>
        <summary>2.2 Set Up the Backend</summary>
        <div class="section-body">
          <p>Follow the <a href="{{ site.baseurl }}/docs/guides/BACKEND_GUIDE">Backend setup guide</a> end to end. It covers cloning <code>farmers-coalition</code>, installing Ruby and its dependencies, configuring the database connection, and starting the Rails server.</p>
          <p>The backend is the harder of the two to set up, which is why it comes first. Expect to spend real time on the Ruby and MySQL prerequisites.</p>
          <p><strong>Done when:</strong> <code>bin/rails server</code> runs without errors and <code>localhost:3000</code> loads in your browser.</p>
          <p>Before you move on, check <code>config/database.yml</code> and confirm it points at your <strong>local</strong> database, not a remote one. The onboarding plan shows the values it should have.</p>
        </div>
      </details>

      <details>
        <summary>2.3 Set Up the Frontend</summary>
        <div class="section-body">
          <p>Follow the <a href="{{ site.baseurl }}/docs/guides/FRONTEND_GUIDE">Frontend setup guide</a> end to end. It covers cloning <code>farm2facts-frontend</code>, installing the Node dependencies, and running the Vue 3 development server.</p>
          <p><strong>Done when:</strong> <code>npm run serve</code> compiles and <code>localhost:8080</code> loads the app in your browser.</p>
          <p>Check the <code>.env</code> file and confirm it points at your local backend on <code>localhost:3000</code>. If the app loads but every page is empty, this is almost always why.</p>
        </div>
      </details>

      <details>
        <summary>2.4 Confirm the Two Run Together</summary>
        <div class="section-body">
          <p>Running each server on its own is not enough. Confirm they are actually talking to each other.</p>
          <p>With both servers running, open the frontend at <code>localhost:8080</code> and log in. Open your browser's developer tools, go to the <strong>Network</strong> tab, and reload the page. You should see requests going out to <code>localhost:3000</code> and coming back with data, not with connection errors.</p>
          <p>This is the point of the whole card. If the frontend renders but the Network tab is full of failed requests, your setup is not finished -- work back through <code>.env</code> and <code>database.yml</code>, and ask in Slack if you are still stuck.</p>
          <p>Take a screenshot of the running frontend and one of the running backend. You will need both in Card 4.</p>
        </div>
      </details>

      <details>
        <summary>2.5 Note What Fought You</summary>
        <div class="section-body">
          <p>As you work through the setup, keep a short running note of anything that did not go as the guide described: a version mismatch, a missing dependency, a step that was unclear, an error you had to search for.</p>
          <p>This is not busywork. Our setup guides are living documents, and the fastest time to improve them is while a new developer is going through them. Two or three lines per problem is enough -- what broke, and what fixed it.</p>
          <p>You submit this note in Card 4.</p>
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
        <li>[ ] Both repositories cloned locally</li>
        <li>[ ] Backend runs: <code>localhost:3000</code> loads</li>
        <li>[ ] Frontend runs: <code>localhost:8080</code> loads</li>
        <li>[ ] The frontend is successfully fetching data from the backend</li>
        <li>[ ] I am in the project Slack channel and have introduced myself</li>
        <li>[ ] I have the three points of contact saved</li>
        <li>[ ] I have sent my Fall availability</li>
      </ul>

      <h3>What to Send</h3>
      <p>Post a single message to <strong>Abanish</strong> in the project Slack channel containing:</p>
      <ol>
        <li>The checklist above, with each item marked done.</li>
        <li>A <strong>screenshot of the frontend running</strong> at <code>localhost:8080</code>, with the URL bar visible.</li>
        <li>A <strong>screenshot of the backend running</strong> at <code>localhost:3000</code>, with the URL bar visible.</li>
        <li>Your <strong>setup notes</strong> from Card 2.5 -- what fought you and what fixed it. Write "nothing broke" if that is genuinely the case.</li>
      </ol>
      <p>If an item is not done, send the message anyway and say which one and why. A blocked step we know about gets unblocked; one we do not know about does not.</p>

      <h3>Then What</h3>
      <p>Once your setup is confirmed, move on to <a href="{{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-1">Phase 1: Understanding F2F and Its Repositories' Current State</a>. Phase 1 assumes both repos run on your machine, so do not start it early with a half-working environment.</p>

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
          <p class="skill-group-label">Local Environment</p>
          <div class="skill-tags">
            <span class="skill-tag">Rails server</span>
            <span class="skill-tag">Vue dev server</span>
            <span class="skill-tag">Local MySQL</span>
          </div>
        </div>
        <div>
          <p class="skill-group-label">Configuration</p>
          <div class="skill-tags">
            <span class="skill-tag">database.yml</span>
            <span class="skill-tag">.env</span>
            <span class="skill-tag">Local vs. remote targets</span>
          </div>
        </div>
        <div>
          <p class="skill-group-label">Debugging Setup</p>
          <div class="skill-tags">
            <span class="skill-tag">Network tab</span>
            <span class="skill-tag">Frontend-backend requests</span>
            <span class="skill-tag">Reading error output</span>
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
