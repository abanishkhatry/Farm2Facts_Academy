"""Generate the LASER Program Final Review PDF.

A single retrospective document covering the whole LASER 2026 program: how each
task guide was built, what it covered, what the interns completed, and where the
program stopped. Uses the same F2F Academy palette and layout as the intern
memos (generate_memo_pdf.py) so the set reads as one family of documents.
"""

import os
from weasyprint import HTML, CSS

OUTPUT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "assets", "F2F_LASER_Program_Review.pdf"
)

# ── F2F ACADEMY COLOR PALETTE (shared with generate_memo_pdf.py) ────────────
# navDark    #1E1C1A  header/nav near-black
# charcoal   #2B2722  heading text dark charcoal-brown
# bodyBrown  #4A4540  body text medium warm brown
# cream      #F0EDE6  page background warm cream
# cardBg     #EDEAD3  card light tan background
# cardBorder #C8BFA8  card/divider warm tan border
# accent     #9B7D2E  golden-amber wheat accent
# accentBg   #F5EED8  very light amber for table headers
# lightCard  #F7F4EC  slightly lighter than cream for alternating rows

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>LASER Program 2026 &mdash; Final Review</title>
</head>
<body>

  <!-- Title block -->
  <div class="title-block">
    <h1 class="brand">F2F Academy</h1>
    <p class="subtitle">FINAL PROGRAM REVIEW &mdash; LASER 2026</p>
  </div>

  <table class="info-table">
    <tbody>
      <tr><td class="info-label">PROGRAM</td><td class="info-value">LASER &mdash; Farm2Facts Student Developer Program, 2026 cohort</td></tr>
      <tr><td class="info-label">PLATFORM</td><td class="info-value">Farm2Facts (F2F) &mdash; Vue 3 frontend, Rails 6.1 + MySQL backend</td></tr>
      <tr><td class="info-label">INTERNS</td><td class="info-value">Bright, Logan</td></tr>
      <tr><td class="info-label">PROGRAM STAFF</td><td class="info-value">Alfonso Morales, Garrett Smith, Abanish Khatry</td></tr>
      <tr><td class="info-label">MATERIALS</td><td class="info-value">F2F Academy (Jekyll site) &mdash; onboarding plan, workflow guides, sprint task guides, study materials</td></tr>
      <tr><td class="info-label">STATUS</td><td class="info-value">Program complete. Task 1 delivered in full; Task 2 delivered through sub-task 2.1, remainder paused.</td></tr>
    </tbody>
  </table>

  <!-- 1. Purpose -->
  <h2 class="h1">1.&nbsp;&nbsp;Purpose of This Document</h2>
  <p>
    This is the closing record for the LASER 2026 program. It exists so that anyone reading it
    once &mdash; a lab director, a future program lead, or the next cohort's supervisor &mdash;
    comes away with a full picture of what was built, what the interns actually did, and where
    the program stopped and why.
  </p>
  <p>
    The task cards that carried this content on the F2F Academy home page have been retired now
    that the program has wrapped. Everything they described is captured here.
  </p>

  <!-- 2. Program overview -->
  <h2 class="h1">2.&nbsp;&nbsp;Program Overview</h2>
  <p>
    LASER was an onboarding program for student developers joining Farm2Facts, a UW-Madison
    initiative that supports farmers markets by collecting vendor, attendance, and sales data
    and modeling food access across communities. The goal was not to hand the interns tickets.
    It was to take two students with no prior exposure to the codebase and move them, in
    scaffolded steps, to the point where they could contribute to a real two-repo application
    using LLM-assisted development practices.
  </p>
  <p>
    Work was organized into named sprints of roughly two weeks each. Each sprint had one task
    guide published on the F2F Academy site, and each guide was self-contained: concepts,
    instructions, file templates, submission checklist, and a closing summary of skills gained.
  </p>

  <table>
    <thead>
      <tr><th style="width:26%">Sprint</th><th style="width:14%">Weeks</th><th style="width:30%">Task Guide</th><th>Outcome</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Welcome to the Barn</strong></td>
        <td>1 &amp; 2</td>
        <td>Task 1 Guide</td>
        <td>Completed in full by both interns</td>
      </tr>
      <tr>
        <td><strong>Cheese Curds &amp; Code</strong></td>
        <td>3, 4 &amp; 5</td>
        <td>Task 2.1 Guide (APIs for Beginners)</td>
        <td>Sub-task 2.1 completed by both interns; the follow-on module was paused</td>
      </tr>
    </tbody>
  </table>

  <p>
    Both sprints ran against the live Farm2Facts frontend repository on UW-Madison's GitLab, so
    the interns were working in the same repo, on the same branching model, and through the same
    review process as the professional developers on the project.
  </p>

  <!-- 3. How the tasks were built -->
  <h2 class="h1">3.&nbsp;&nbsp;How the Tasks Were Built</h2>
  <p>
    Both task guides were written to the same template. That consistency was deliberate: once an
    intern learned how to read one guide, they could read any of them, and the mechanical parts
    of contributing (branch, directory, commits, merge request) stopped being a source of
    friction after the first sprint.
  </p>

  <h3 class="h2">3a.&nbsp;&nbsp;The Guide Template</h3>
  <p>Every guide is a stack of collapsible cards, numbered in the order the intern works through them:</p>
  <table>
    <thead>
      <tr><th style="width:28%">Card</th><th>What it does</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Setup</strong></td>
        <td>Branch off <code>dev</code> with a prescribed branch name, create a prescribed directory structure, and commit each deliverable separately with a prescribed commit message. Nothing is left to interpretation.</td>
      </tr>
      <tr>
        <td><strong>Concepts / Learning</strong></td>
        <td>The material the intern needs before starting, written into the guide itself rather than only linked out, plus an ordered list of external resources.</td>
      </tr>
      <tr>
        <td><strong>Assignments</strong></td>
        <td>One card per deliverable. Each states duration, difficulty, step-by-step instructions, and the exact questions to answer.</td>
      </tr>
      <tr>
        <td><strong>Templates</strong></td>
        <td>A fill-in-the-blank Markdown skeleton for each written deliverable, so the intern spends their effort on the thinking, not the formatting.</td>
      </tr>
      <tr>
        <td><strong>PR Creation &amp; Submission</strong></td>
        <td>A pre-submission checklist, the expected file tree, and click-by-click GitLab merge request steps. Work is not submitted until the MR is open and assigned.</td>
      </tr>
      <tr>
        <td><strong>What You Learned</strong></td>
        <td>Skills gained, grouped and tagged, so the intern can see what carries forward into the next sprint.</td>
      </tr>
    </tbody>
  </table>

  <h3 class="h2">3b.&nbsp;&nbsp;Design Decisions Behind the Template</h3>
  <ul>
    <li><strong>One deliverable, one commit.</strong> Both guides list a table of expected commits with exact messages. This taught commit hygiene by making it the only way to follow the instructions, rather than by lecturing about it.</li>
    <li><strong>Deliverables live in the repo.</strong> Written work went into <code>task1_laser/laser_[firstName]/</code> and <code>task2_laser/laser_[firstName]/</code> inside the frontend repo, not into a document folder. Reading, writing, and reviewing all happened in the same place the code lives.</li>
    <li><strong>The merge request is the finish line.</strong> Every guide closes on the MR. An intern who wrote everything but never opened the MR had not finished the task, by design.</li>
    <li><strong>Claude Code as a first-class tool, not a shortcut.</strong> Task 1 asks interns to use Claude Code to explore the codebase, then explicitly requires them to rewrite the output in their own words.</li>
    <li><strong>Warm up on something you cannot break.</strong> Task 2.1 starts on a practice API before touching the real one, so a mistake in the learning phase has no consequences.</li>
  </ul>

  <h3 class="h2">3c.&nbsp;&nbsp;Supporting Materials</h3>
  <p>The task guides did not stand alone. Each leaned on shared material published alongside them:</p>
  <ul>
    <li><strong>Student Onboarding Plan</strong> &mdash; Git and GitLab concepts, links to both repos, and database access, read before any task begins.</li>
    <li><strong>Frontend and Backend Guides</strong> &mdash; clone, configure, and run-locally walkthroughs for the Vue 3 frontend and the Rails 6.1 + MySQL backend, with separate macOS and Windows paths.</li>
    <li><strong>Workflow Guides</strong> &mdash; how we work, the Git workflow reference (branch strategy, commit rules), and the pull request guide (title format, description template, reviewer assignment).</li>
    <li><strong>Study Materials</strong> &mdash; a sprint-mapped index of readings and documentation.</li>
    <li><strong>Curriculum &amp; Task List</strong> &mdash; the sprint table linking each sprint to its guide and to related coursework (CS200, CS300, CS571 for Sprint 1).</li>
  </ul>

  <!-- 4. Task 1 -->
  <h2 class="h1">4.&nbsp;&nbsp;Task 1 &mdash; &ldquo;Welcome to the Barn&rdquo;</h2>
  <table class="info-table">
    <tbody>
      <tr><td class="info-label">SPRINT</td><td class="info-value">Welcome to the Barn</td></tr>
      <tr><td class="info-label">WEEKS</td><td class="info-value">1 &amp; 2</td></tr>
      <tr><td class="info-label">SOFT DEADLINE</td><td class="info-value">Thursday, June 25</td></tr>
      <tr><td class="info-label">BRANCH</td><td class="info-value"><code>feat/[firstName]_task1</code>, cut from <code>dev</code> in the frontend repo</td></tr>
      <tr><td class="info-label">STATUS</td><td class="info-value"><strong>Completed in full by both interns.</strong></td></tr>
    </tbody>
  </table>

  <h3 class="h2">4a.&nbsp;&nbsp;What the Task Was For</h3>
  <p>
    Task 1 answered a single question: can this person get the project running, find their way
    around it, and submit work the way the team submits work? It covered environment setup,
    codebase orientation, tooling, project context, and the full contribution workflow, and it
    produced four artifacts that made each of those visible.
  </p>

  <h3 class="h2">4b.&nbsp;&nbsp;What It Covered</h3>

  <p><strong>Card 1 &mdash; Onboarding.</strong> Four sub-sections walked the intern from zero to a working branch:</p>
  <ul>
    <li><em>1.1 Get the repos running locally</em> &mdash; read the Student Onboarding Plan, then set up the Vue 3 frontend and the Rails 6.1 backend using the per-repo guides.</li>
    <li><em>1.2 Open your feature branch</em> &mdash; branch from <code>dev</code>, then create the <code>task1_laser/laser_[firstName]/</code> directory that holds all four deliverables.</li>
    <li><em>1.3 Committing your work</em> &mdash; imperative commit messages under 72 characters, with a table giving the exact message for each of the four deliverables.</li>
    <li><em>1.4 Codebase understanding report</em> &mdash; the first substantive deliverable, described below.</li>
  </ul>

  <p><strong>The codebase overview.</strong> The intern used Claude Code to explore ten directories under <code>src/views/</code> in the frontend repo and wrote a short <em>Contains</em> and <em>Role</em> description for each, from a supplied Markdown template:</p>
  <table>
    <thead><tr><th style="width:50%">Full description required</th><th>High-level overview only</th></tr></thead>
    <tbody>
      <tr>
        <td>
          <ul class="cell-list">
            <li><code>DownloadDocuments</code></li>
            <li><code>LandingPage</code></li>
            <li><code>MarketOrg</code></li>
            <li><code>MemberResources</code></li>
            <li><code>SelectMetrics</code></li>
          </ul>
        </td>
        <td>
          <ul class="cell-list">
            <li><code>Analysis</code></li>
            <li><code>Instrument</code></li>
            <li><code>Instrument_MarketOrg</code></li>
            <li><code>Profiles</code></li>
            <li><code>Users</code></li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
    Scoping the last five to an overview was intentional. The point was a usable map of the
    frontend, not an exhaustive audit, and capping the depth kept a two-week task from becoming a
    month-long one.
  </p>

  <p><strong>Card 2 &mdash; Claude Code 101.</strong> Interns completed Anthropic's Claude Code 101 course and submitted the completion certificate. The card then went beyond the course: it explained what a <code>CLAUDE.md</code> file is and why the frontend repo has one, had the intern read the repo's existing file, and then assigned them to write their own personal <code>Claude_[firstName].md</code> reflecting their working style and what they had learned about the codebase so far. The final step was comparative: run a session against their own file, run one against the repo's file, and note the difference in how Claude behaved.</p>

  <p><strong>Card 3 &mdash; The F2F article.</strong> Interns read <em>Citizen Scientist: Farm 2 Facts Supporting Farmers Markets</em> (Ledesma et al., 2021) and wrote a 2&ndash;3 paragraph response to three questions: what problem F2F solves for market managers and why it existed before F2F; one case study from the article (South Milwaukee Downtown Market, Hope and Main, Brown Deer, or ACEFM) and what decision the collected data supported; and, as a developer, what part of the F2F system they would most want to improve. The third question deliberately connects the research context back to engineering intent.</p>

  <p><strong>Card 4 &mdash; PR creation and submission.</strong> A pre-flight checklist confirmed the branch name, the directory, and all four files. The card then explained that GitLab calls it a Merge Request but the workflow is identical to a GitHub Pull Request, and gave the six-step path through the GitLab UI, targeting <code>dev</code> and filling out every field of the description template.</p>

  <h3 class="h2">4c.&nbsp;&nbsp;Deliverables</h3>
  <table>
    <thead><tr><th style="width:38%">File</th><th>Content</th></tr></thead>
    <tbody>
      <tr><td><code>codebase_overview.md</code></td><td>Contains/Role write-up for all ten <code>src/views/</code> directories</td></tr>
      <tr><td><code>claude_code_101_certificate.pdf</code></td><td>Anthropic course completion certificate</td></tr>
      <tr><td><code>f2f_article_response.md</code></td><td>Response to the three article questions</td></tr>
      <tr><td><code>Claude_[firstName].md</code></td><td>Personal Claude Code configuration file</td></tr>
    </tbody>
  </table>
  <p>All four in <code>task1_laser/laser_[firstName]/</code>, each with its own commit, submitted as one merge request into <code>dev</code>.</p>

  <h3 class="h2">4d.&nbsp;&nbsp;Skills Established</h3>
  <table>
    <thead><tr><th style="width:26%">Area</th><th>Covered</th></tr></thead>
    <tbody>
      <tr><td>Git fundamentals</td><td>Staging and commits, <code>git status</code> / <code>git diff</code>, local vs. remote</td></tr>
      <tr><td>Git branching</td><td>Feature branch isolation, branching from <code>dev</code>, the four-level branch structure</td></tr>
      <tr><td>Pull requests</td><td>The PR as the unit of review, imperative titles, the description template</td></tr>
      <tr><td>Codebase navigation</td><td><code>src/views/</code> layout, directory-first reading, using Claude as a navigator</td></tr>
      <tr><td>CLAUDE.md</td><td>What it does, writing context prompts, comparing session outputs</td></tr>
    </tbody>
  </table>

  <h3 class="h2">4e.&nbsp;&nbsp;Result</h3>
  <p>
    <strong>Task 1 was completed in full.</strong> Both interns set up both repos locally, produced all four
    deliverables, committed them individually, and submitted merge requests into <code>dev</code>. This
    is the one sprint of the program that ran end to end exactly as designed.
  </p>

  <!-- 5. Task 2 -->
  <h2 class="h1">5.&nbsp;&nbsp;Task 2 &mdash; &ldquo;Cheese Curds &amp; Code&rdquo;</h2>
  <table class="info-table">
    <tbody>
      <tr><td class="info-label">SPRINT</td><td class="info-value">Cheese Curds &amp; Code</td></tr>
      <tr><td class="info-label">WEEKS</td><td class="info-value">3, 4 &amp; 5</td></tr>
      <tr><td class="info-label">STRUCTURE</td><td class="info-value">Module 1 &mdash; APIs for Beginners (Task 2.1). Module 2 &mdash; automated data extraction and platform integration.</td></tr>
      <tr><td class="info-label">STATUS</td><td class="info-value"><strong>Task 2.1 completed by both interns. Module 2 paused.</strong></td></tr>
    </tbody>
  </table>

  <h3 class="h2">5a.&nbsp;&nbsp;How the Sprint Was Structured</h3>
  <p>
    Task 2 was the bridge from onboarding to real feature work. It was split into two modules.
    Module 1 (Task 2.1) taught APIs from the ground up with no code required, using the Wisconet
    API &mdash; Wisconsin's statewide environmental sensor network &mdash; as the live data
    source. Module 2 was to build on that foundation with code that automates data extraction and
    feeds it into the Farm2Facts platform.
  </p>
  <p>
    Splitting the sprint this way meant the interns learned request/response mechanics against a
    read-only public API, where the worst case is a 404, before writing anything that touches the
    F2F codebase.
  </p>

  <h3 class="h2">5b.&nbsp;&nbsp;Task 2.1 &mdash; What It Covered</h3>

  <p><strong>Concepts, written into the guide.</strong> Before any assignment, the guide covered what an API is (the restaurant analogy: customer, waiter, kitchen), the REST style, and JSON. It broke a real Wisconet URL into its parts &mdash; protocol, base URL, endpoint path, action, query parameters &mdash; and gave a status code reference (200, 404, 422, 500). Only after that did it list external resources, in a required order: MuleSoft's <em>What is an API?</em>, the freeCodeCamp <em>APIs for Beginners</em> course, the first three modules of Postman API Fundamentals, the REST API Tutorial, W3Schools on JSON, and finally the Wisconet API documentation.</p>

  <p><strong>Assignment 1 &mdash; API Detective (~30 min, beginner).</strong> Browser only, no tools. Interns opened the Wisconet stations endpoint, found the station nearest their home county, built a URL for it by hand, and fetched its latest measures. Seven questions followed: station ID and county, latitude and longitude, how many fields the endpoint returned, which field name holds air temperature, whether the station has soil sensors and at how many depths, what <code>collection_frequency</code> means, and &mdash; in their own words &mdash; the difference between the station list endpoint and the latest-measures endpoint.</p>

  <p><strong>Assignment 2 &mdash; Postman Explorer (~45 min, beginner).</strong> Interns installed Postman Desktop and warmed up on JSONPlaceholder, a public practice API: fetch all users, fetch one user by ID, then filter posts by <code>userId</code> using the Params tab. They then moved to Wisconet: all stations, the ALTN (Arlington) station detail and its elevation, and ALTN's latest measures with the response time noted. All three were saved into a Postman Collection named &ldquo;Wisconet Exploration.&rdquo; The deliverable asked for a screenshot of the collection, the status code of each request, what happens with a station ID that does not exist, and a short explanation of path parameters versus query parameters.</p>

  <p><strong>Assignment 3 &mdash; Soil Temperature Deep Dive (~60 min, intermediate).</strong> The first assignment with real analytical weight. Interns learned the Wisconet field naming convention &mdash; <code>{frequency}_{measure}_{units}_{aggregation}@{depth}</code> &mdash; converted calendar dates into Unix timestamps, and built a Postman request against the measures endpoint for station HNCK pulling soil temperature at five depths (2in, 4in, 8in, 20in, 40in) across a 24-hour window. They repeated it for a second station and then switched from 5-minute readings to daily maximums to see what changed. Five questions closed it out: the readings at 2in, 8in, and 40in and what pattern appears as depth increases; which of their two stations has warmer soil at 4in and a hypothesis as to why; how many 5-minute readings a 24-hour window should produce and whether their count matches; what <code>preceding_value</code> represents; and what they would change in the field name to get hourly data.</p>

  <p><strong>Assignment 4 &mdash; Document Your Understanding (~30 min, reflection).</strong> Three parts. Part A, a one-page plain-English summary of the Wisconet API: what data it provides, how it is structured, what a soil temperature request looks like described in words, and what limitations they noticed. Part B, a hand-drawn or slide-drawn request-response flow diagram with the browser or Postman, the API server, the database, and the JSON response, every arrow labeled. Part C, a proposed use case: a tool for Wisconsin farmers built on this API, naming the user, the problem, and the endpoints it would use. Part C was written as the on-ramp into Module 2.</p>

  <h3 class="h2">5c.&nbsp;&nbsp;Task 2.1 Deliverables</h3>
  <table>
    <thead><tr><th style="width:44%">File</th><th>Content</th></tr></thead>
    <tbody>
      <tr><td><code>assignment1_api_detective.md</code></td><td>Seven answers from browser-only exploration</td></tr>
      <tr><td><code>assignment2_postman_explorer.md</code></td><td>Collection screenshot, status codes, error behavior, parameter types</td></tr>
      <tr><td><code>assignment3_soil_temperature.md</code></td><td>Multi-depth, multi-station soil temperature findings</td></tr>
      <tr><td><code>assignment4_summary.md</code></td><td>API summary, request-response diagram, proposed use case</td></tr>
    </tbody>
  </table>
  <p>
    All four in <code>task2_laser/laser_[firstName]/</code> on branch <code>feat/[firstName]_task2</code>,
    each with its own commit, submitted as one merge request into <code>dev</code>. A companion
    reference packet, <em>LASER Intern API Learning Packet &mdash; Module 1 of 2</em>, carried the same
    material in long form with a field reference and cheatsheet appendix.
  </p>

  <h3 class="h2">5d.&nbsp;&nbsp;Skills Established</h3>
  <table>
    <thead><tr><th style="width:26%">Area</th><th>Covered</th></tr></thead>
    <tbody>
      <tr><td>API fundamentals</td><td>REST architecture, HTTP methods, status codes</td></tr>
      <tr><td>JSON</td><td>Objects and arrays, key-value pairs, reading responses</td></tr>
      <tr><td>URL structure</td><td>Base URL, path parameters, query parameters</td></tr>
      <tr><td>Tooling</td><td>The browser as an API client, Postman requests, Postman Collections</td></tr>
      <tr><td>Wisconet API</td><td>Station endpoints, field naming convention, Unix timestamps</td></tr>
    </tbody>
  </table>

  <h3 class="h2">5e.&nbsp;&nbsp;Result and Pause</h3>
  <p>
    <strong>Task 2.1 was completed by both interns.</strong> They worked through the concepts and all four
    assignments, pulled live soil data from the Wisconet network at multiple depths and stations,
    and submitted their deliverables through the same branch-commit-merge-request workflow
    established in Task 1.
  </p>
  <p>
    <strong>Module 2 did not run.</strong> The sprint was paused after 2.1 because of an unresolved
    licensing issue affecting the software the integration work depended on. This was a blocker
    outside the interns' control and unrelated to their progress: the learning module had already
    landed, and the interns were ready for the code module. Rather than start work that could not
    be finished or merged, the sprint was stopped at a clean boundary &mdash; a completed,
    reviewable sub-task &mdash; and the remaining scope was set aside.
  </p>

  <!-- 6. What Module 2 was going to be -->
  <h2 class="h1">6.&nbsp;&nbsp;What Module 2 Was Scoped to Be</h2>
  <p>
    The follow-on work was fully specified before the pause, in the intern project memo
    <em>MesoNet Soil Metrics &amp; Notification System</em>. Recording it here means the scope is
    not lost if the licensing situation is resolved and the work is picked back up.
  </p>

  <h3 class="h2">6a.&nbsp;&nbsp;Feature Scope</h3>
  <ul>
    <li><strong>Data integration.</strong> Consume the MesoNet API for soil temperature, soil moisture, and rainfall near a user's farming area; surface monthly high/low summaries on both Farmer and Market/Vendor profile dashboards.</li>
    <li><strong>Threshold-based alerts.</strong> Let users set custom upper and lower bounds for soil temperature and moisture, with email notification when a threshold is crossed in either direction, plus a profile-level opt-in and customization flow.</li>
    <li><strong>Weekly digest.</strong> A scheduled cron job emailing opted-in users a soil temperature summary relevant to their region.</li>
    <li><strong>Reference data.</strong> Use readings from the Arlington Agricultural Research Station (UW-Extension, Arlington, Wisconsin) to derive sensible default threshold values.</li>
  </ul>

  <h3 class="h2">6b.&nbsp;&nbsp;Planned Assignments</h3>
  <table>
    <thead><tr><th style="width:14%">Intern</th><th style="width:22%">Focus</th><th>Responsibilities</th></tr></thead>
    <tbody>
      <tr>
        <td>Bright</td>
        <td>SWE-focused</td>
        <td>
          <ul class="cell-list">
            <li>MesoNet API integration (requests, auth, parsing)</li>
            <li>Documentation of endpoints and data models</li>
            <li>Profile integration for both user types</li>
            <li>Threshold alert logic and email triggers</li>
            <li>Cron job for the weekly digest</li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>Logan</td>
        <td>SWE + research</td>
        <td>
          <ul class="cell-list">
            <li>All SWE tasks, collaboratively with Bright</li>
            <li>Deep dive into Arlington experimental farm data via UW-Extension</li>
            <li>Research agricultural metrics and derive threshold defaults</li>
            <li>Propose new F2F platform features from those findings</li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
  <p>
    The planned timeline was three weeks: API setup and integration, then profile display and
    alerts, then cron jobs, research, and polish.
  </p>

  <!-- 7. Completion summary -->
  <h2 class="h1">7.&nbsp;&nbsp;Completion Summary</h2>
  <table>
    <thead>
      <tr><th style="width:30%">Unit</th><th style="width:20%">Status</th><th>Notes</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Task 1</strong> &mdash; Welcome to the Barn</td>
        <td><strong>Complete</strong></td>
        <td>All four deliverables submitted by both interns via merge request into <code>dev</code>. Ran exactly as designed.</td>
      </tr>
      <tr>
        <td><strong>Task 2.1</strong> &mdash; APIs for Beginners</td>
        <td><strong>Complete</strong></td>
        <td>All four assignments submitted by both interns. Live Wisconet data pulled and analyzed.</td>
      </tr>
      <tr>
        <td><strong>Task 2, Module 2</strong> &mdash; MesoNet integration</td>
        <td><strong>Paused</strong></td>
        <td>Not started. Blocked by an unresolved licensing issue affecting the software the work depended on. Scope documented and preserved.</td>
      </tr>
    </tbody>
  </table>
  <p>
    Every task that was published to the interns was completed by the interns. Nothing was left
    unfinished on their side.
  </p>

  <!-- 8. Takeaways -->
  <h2 class="h1">8.&nbsp;&nbsp;Takeaways and What Carries Forward</h2>

  <h3 class="h2">8a.&nbsp;&nbsp;What Worked</h3>
  <ul>
    <li><strong>Prescriptive setup cards removed friction.</strong> Fixing the branch name, directory structure, and commit messages in advance meant the interns spent Task 2 thinking about APIs rather than re-learning Git.</li>
    <li><strong>Deliverables as written artifacts made progress legible.</strong> Every task produced reviewable files in the repo, so completion was never ambiguous.</li>
    <li><strong>Warm-up-then-real sequencing.</strong> JSONPlaceholder before Wisconet, and browser before Postman, kept the difficulty curve gentle without lowering the ceiling.</li>
    <li><strong>Pausing at a clean boundary.</strong> Because the sprint was split into modules, the licensing block cost the program a module rather than a half-finished feature branch.</li>
  </ul>

  <h3 class="h2">8b.&nbsp;&nbsp;What to Address Next Time</h3>
  <ul>
    <li><strong>Confirm licensing and access before scoping.</strong> The single thing that stopped this program was an external dependency that was not cleared in advance. Verifying that every tool and service in a sprint's critical path is licensed and accessible should be a precondition for publishing the guide.</li>
    <li><strong>Keep a no-dependency fallback module.</strong> A parallel track that needs nothing but the public repos would have kept the interns moving through the block.</li>
  </ul>

  <h3 class="h2">8c.&nbsp;&nbsp;Reusable Assets</h3>
  <p>The following came out of LASER and are being carried into the WISCURDS program:</p>
  <ul>
    <li>The task guide template &mdash; setup, concepts, assignments, templates, submission, what you learned.</li>
    <li>The branch, directory, and commit conventions, now standard across programs.</li>
    <li>The API learning packet, reusable as standalone material for any cohort.</li>
    <li>The MesoNet project memo, holding the full unbuilt scope.</li>
    <li>The F2F Academy site structure itself: per-program blocks, collapsible task cards, and a shared core materials section.</li>
  </ul>

  <p class="footer">Farm2Facts @KaufmanLab &bull; F2F Academy &bull; LASER 2026 Final Program Review</p>

</body>
</html>"""

CSS_CONTENT = """
/* ---- Page setup ---- */
@page {
  size: Letter;
  margin: 19mm 22mm 22mm 22mm;
  @bottom-center {
    content: counter(page);
    font-family: Arial, 'Helvetica Neue', sans-serif;
    font-size: 8.5pt;
    color: #9B7D2E;
  }
}

/* ---- Reset ---- */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: Arial, 'Helvetica Neue', sans-serif;
  font-size: 10.5pt;
  color: #4A4540;             /* bodyBrown */
  line-height: 1.6;
  background: #FFFFFF;
}

/* ---- Title block ---- */
.title-block {
  margin-bottom: 8pt;
  padding-bottom: 6pt;
  border-bottom: 2pt solid #C8BFA8;   /* cardBorder */
}
.brand {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 30pt;
  font-weight: 700;
  color: #2B2722;            /* charcoal */
  margin-bottom: 4pt;
}
.subtitle {
  font-size: 11pt;
  color: #9B7D2E;            /* accent */
  letter-spacing: 0.02em;
}

/* ---- Info tables ---- */
.info-table {
  width: 100%;
  border-collapse: collapse;
  margin: 12pt 0 18pt;
  font-size: 9.5pt;
}
.info-table td {
  border: 1pt solid #C8BFA8;          /* cardBorder */
  padding: 5pt 9pt;
  vertical-align: top;
}
.info-label {
  width: 22%;
  background: #F5EED8;                /* accentBg */
  color: #9B7D2E;                     /* accent */
  font-weight: 700;
}
.info-value {
  background: #FFFFFF;
  color: #4A4540;                     /* bodyBrown */
}

/* ---- Headings ---- */
.h1 {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 15.5pt;
  font-weight: 700;
  color: #2B2722;            /* charcoal */
  margin-top: 20pt;
  margin-bottom: 6pt;
  padding-bottom: 4pt;
  border-bottom: 2pt solid #C8BFA8;   /* cardBorder */
  break-after: avoid;
}
.h2 {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 12pt;
  font-weight: 700;
  color: #9B7D2E;            /* accent */
  margin-top: 13pt;
  margin-bottom: 5pt;
  break-after: avoid;
}

p { margin-bottom: 8pt; }

code {
  font-family: 'Courier New', Courier, monospace;
  font-size: 9pt;
  color: #2B2722;
  background: #F5EED8;
  padding: 0.5pt 2.5pt;
  border-radius: 2pt;
}

/* ---- Lists ---- */
ul, ol {
  padding-left: 20pt;
  margin-bottom: 10pt;
}
li { margin-bottom: 4pt; }

/* ---- Tables ---- */
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9.5pt;
  margin: 10pt 0 16pt;
}
thead { display: table-header-group; }
tr { break-inside: avoid; }
thead tr {
  background: #1E1C1A;       /* navDark */
  color: #FFFFFF;
}
th {
  padding: 6pt 9pt;
  text-align: left;
  font-weight: 700;
  border: 1pt solid #C8BFA8;
}
td {
  padding: 6pt 9pt;
  border: 1pt solid #C8BFA8;          /* cardBorder */
  color: #4A4540;                     /* bodyBrown */
  vertical-align: top;
}
tbody tr:nth-child(even) td { background: #F7F4EC; }   /* lightCard */

/* bullet lists inside table cells */
.cell-list {
  padding-left: 14pt;
  margin: 0;
}
.cell-list li { margin-bottom: 3pt; }

/* ---- Footer ---- */
.footer {
  margin-top: 26pt;
  padding-top: 8pt;
  border-top: 2pt solid #C8BFA8;      /* cardBorder */
  text-align: center;
  font-size: 9pt;
  font-style: italic;
  color: #9B7D2E;                     /* accent */
}
"""

if __name__ == "__main__":
    output = os.path.abspath(OUTPUT_PATH)
    os.makedirs(os.path.dirname(output), exist_ok=True)
    HTML(string=HTML_CONTENT).write_pdf(
        output,
        stylesheets=[CSS(string=CSS_CONTENT)],
    )
    print(f"PDF written to: {output}")
