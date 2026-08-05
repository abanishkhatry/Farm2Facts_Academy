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

**Expect this to fight you.** Standing up a Rails backend, a MySQL database, and a Vue frontend on a machine that has never had them is the least predictable part of the whole program. Version mismatches, missing system dependencies, and licensing or permission prompts are all normal here. That is not a sign you are doing it wrong.

What we ask is that you **keep a note of every problem you hit and how you got past it**, and include that note in your Phase 0 completion message. Card 2.5 covers what to write down. If something blocks you completely, say so in the message rather than going quiet -- a blocker we know about gets solved, one we do not know about does not.

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
          <p>Send that username to <strong>Abanish Khatry</strong> in the WISCURDS Slack channel, or by email at <a href="mailto:akhatry@wisc.edu">akhatry@wisc.edu</a>. Include:</p>
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

      <p>Farm2Facts is split across two repositories and you will work in both over the course of the program. In this phase you clone each one and get it running on your own machine.</p>
      <p>The setup steps are already written down. Follow the guides rather than improvising, and do the <strong>backend first</strong> -- the frontend has nothing to display without it.</p>
      <p>Budget real time for this card. It is the one part of Phase 0 that reliably takes longer than expected, and working through the problems is itself the point. Keep your notes as you go (Card 2.5).</p>

      <details>
        <summary>2.1 Start With the Student Onboarding Plan</summary>
        <div class="section-body">
          <p>Read the <a href="{{ site.baseurl }}/STUDENT_ONBOARDING_PLAN">Student Onboarding Plan</a> before you run any commands. It gives you the full picture: the Git and GitLab concepts we assume, what each repository is, and how the database fits in.</p>
          <p>Two things to take away from it specifically:</p>
          <ul>
            <li><strong>How the pieces connect.</strong> The frontend talks to the backend over HTTP; the backend talks to MySQL. You are standing up all three locally.</li>
            <li><strong>You do not touch the production database.</strong> As a developer you work against a local database, and all data reaches the frontend through the backend API.</li>
          </ul>
          <p>If you are working on a <strong>Kaufman Lab machine</strong>, read the <a href="{{ site.baseurl }}/STUDENT_ONBOARDING_PLAN#running-lab-machines">Running Lab Machines</a> section instead of the full setup guides. Those machines already have everything installed, so you only need to start MAMP and run the two servers. If your own machine is giving you trouble, a lab machine is a reasonable fallback -- note that you used one in your Phase 0 message.</p>
        </div>
      </details>

      <details>
        <summary>2.2 Set Up and Run the Backend</summary>
        <div class="section-body">
          <p>Clone <code>farmers-coalition</code>, the Rails 6.1 metrics API. Get the clone URL from the <strong>Code</strong> button on the <a href="https://git.doit.wisc.edu/at-trad/farmers-coalition" target="_blank" rel="noopener noreferrer">repo's GitLab page</a>, then:</p>
          <pre><code>git clone &lt;backend-repo-url&gt;
cd farmers-coalition
git checkout dev</code></pre>
          <p>Work from <code>dev</code>, not <code>main</code>. That is the branch all development happens against.</p>
          <p>From there, follow the <a href="{{ site.baseurl }}/docs/guides/BACKEND_GUIDE">Backend setup guide</a> end to end. It covers installing Ruby and its dependencies, configuring the database connection, and starting the Rails server.</p>
          <p>The backend is the harder of the two to set up, which is why it comes first. Expect to spend real time on the Ruby and MySQL prerequisites, and expect at least one version or dependency problem along the way.</p>
          <p><strong>Done when:</strong> <code>bin/rails server</code> runs without errors and <code>localhost:3000</code> loads in your browser. Note down any problem you hit on the way there and what fixed it.</p>
          <p>Before you move on, check <code>config/database.yml</code> and confirm it points at your <strong>local</strong> database, not a remote one. The onboarding plan shows the values it should have.</p>
        </div>
      </details>

      <details>
        <summary>2.3 Set Up and Run the Frontend</summary>
        <div class="section-body">
          <p>Clone <code>farm2facts-frontend</code>, the Vue 3 application, the same way:</p>
          <pre><code>git clone &lt;frontend-repo-url&gt;
cd farm2facts-frontend
git checkout dev</code></pre>
          <p>Then follow the <a href="{{ site.baseurl }}/docs/guides/FRONTEND_GUIDE">Frontend setup guide</a> end to end. It covers installing the Node dependencies and running the Vue 3 development server.</p>
          <p><strong>Done when:</strong> <code>npm run serve</code> compiles and <code>localhost:8080</code> loads the app in your browser. Note down any problem you hit on the way there and what fixed it.</p>
          <p>Check the <code>.env</code> file and confirm it points at your local backend on <code>localhost:3000</code>. If the app loads but every page is empty, this is almost always why.</p>
          <p>While you are in the repo, open the <code>CLAUDE.md</code> file at the root and read it. It describes the codebase conventions you will be working within.</p>
        </div>
      </details>

      <details>
        <summary>2.4 Confirm the Two Run Together</summary>
        <div class="section-body">
          <p>Running each server on its own is not enough. Confirm they are actually talking to each other.</p>
          <p>With both servers running, open the frontend at <code>localhost:8080</code> and log in. Open your browser's developer tools, go to the <strong>Network</strong> tab, and reload the page. You should see requests going out to <code>localhost:3000</code> and coming back with data, not with connection errors.</p>
          <p>If the frontend renders but those requests fail, your setup is not finished. Check <code>.env</code> and <code>database.yml</code> first, since those are the usual causes.</p>
          <p><strong>Done when:</strong> the Network tab shows successful requests to <code>localhost:3000</code>. Note down any problem you hit on the way there and what fixed it.</p>
          <p>Take a screenshot of the running frontend and one of the running backend. You submit both in Card 4.</p>
        </div>
      </details>

      <details>
        <summary>2.5 Keep a Note of What Fought You</summary>
        <div class="section-body">
          <p>You will almost certainly hit problems in this card. Keep a short running note of each one as it happens: a version mismatch, a missing system dependency, a licensing or permission prompt, a command that failed, a step in the guide that was unclear or out of date.</p>
          <p>For each problem, two or three lines is enough:</p>
          <ul>
            <li><strong>What broke</strong> -- the step you were on and the error you got.</li>
            <li><strong>What fixed it</strong> -- or that it is still unresolved.</li>
          </ul>
          <p>Write it down while it is happening. Reconstructing it a week later never works, and the detail you skip is usually the one that helps the next person.</p>
          <p>This is not busywork. Our setup guides are living documents, and the best time to improve them is while a new developer is going through them. Anything that cost you an hour is worth a line in the guide.</p>
          <p>You submit this note as part of your Phase 0 completion message in Card 4. <strong>Send it even if nothing is fully working yet</strong> -- an honest account of where you are stuck is more useful to us than a delayed message that says everything is fine.</p>
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
        <li><strong>Slack</strong> for quick, day-to-day communication. WISCURDS has a <strong>single channel for the whole program</strong> -- it is not split into separate channels for the two projects. Everyone stays in the same channel even after the teams split in Phase 2, so you see what the other team is working on. Ask questions there rather than sitting on them.</li>
        <li><strong>Email</strong> for anything more formal or that needs a lasting record.</li>
      </ul>
      <p>Make sure you are in the WISCURDS Slack channel. If you have not been added, tell Abanish and we will add you.</p>
      <p>Setup problems are exactly what the channel is for. If you have been stuck on the same error for more than an hour, post it -- with the command you ran and the error output. Someone else is likely hitting the same thing.</p>

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
        <li><strong>Once Fall begins:</strong> we set the meeting time and frequency together, based on everyone's availability. Send Abanish the days and rough time windows you could make a recurring meeting. We need all four students' availability before the schedule can be set, so a late reply holds up everyone.</li>
      </ul>

    </div>
  </details>

  <details class="task-card">
    <summary>4. Phase 0 Completion</summary>
    <div class="card-body">

      <p>Copy the template below, fill it out, and send it as a Slack message to <strong>Abanish</strong>.</p>

      <h3>Checklist Template</h3>
      <pre class="pre-scroll"><code>Phase 0 Completion -- [Your Name]

[ ] GitLab account created under my @wisc.edu email and username shared with Abanish
[ ] Permissions granted and I can open both repositories on GitLab
[ ] Backend repo cloned locally and on the dev branch
[ ] Frontend repo cloned locally and on the dev branch
[ ] Backend runs: localhost:3000 loads
[ ] Frontend runs: localhost:8080 loads
[ ] The frontend is successfully fetching data from the backend
[ ] I am in the WISCURDS Slack channel

Screenshots attached:
[ ] Frontend running at localhost:8080, with the URL bar visible
[ ] Backend running at localhost:3000, with the URL bar visible

Trouble I ran into (from Card 2.5):
[List each problem: what broke, and what fixed it. Include anything still
unresolved, and say which machine you set up on. Write "nothing broke" only
if that is genuinely the case.]</code></pre>

      <p>Fill in the trouble section properly -- it is the part of this message we actually act on. It feeds straight back into the setup guides for the next cohort.</p>
      <p>If an item is not done, send the message anyway and say which one and why. Being stuck on setup is expected; staying quiet about it is the only real problem.</p>

    </div>
  </details>

</div>
