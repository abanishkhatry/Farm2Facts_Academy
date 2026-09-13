---
layout: default
title: "Phase 2 Task Guide -- Admin Dashboard"
permalink: /taskList/wiscurds-phase2-admin/
---

# Phase 2 Task Guide -- Project A: Admin Dashboard

**Program:** WISCURDS | **Phase:** 2 -- Data Source Investigation | **Team:** Aditya and Yahia

---

This is the task companion to the [Phase 2 milestone card]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-2). That card describes what the phase covers; this guide is what you actually do, in order.

Phase 2 splits into two projects. This guide is **Project A, the Admin Dashboard**, and it belongs to **Aditya and Yahia**. Project B works on the Wisconet API and has its own guide.

Your goal for this phase: by the end of it you can say what is in the Farm2Facts database, how its tables connect to each other, how the platform's identities are represented, what condition the data is actually in, and what would need cleaning before anyone builds on it.

**You are investigating, not changing.** Nothing in this phase modifies the database. No `UPDATE`, no `DELETE`, no `DROP`, no schema edits. You are building the case for what should change; the changing itself is Phase 3, and it happens through code and review rather than through a GUI. If you find something that obviously needs fixing, write it down with evidence and leave it alone.

The one piece of code you do write is in Card 8: a blank Admin Dashboard page and the navigation entry that opens it. It touches no data, and it exists so the place Phase 3 builds into is already there.

**This is one team deliverable, not two.** The two of you work on a single feature branch and produce a single report. That means agreeing up front on who investigates what and keeping each other current. As discussed during the meeting, you could further branch-off from this feature branch but all the deliverables should be within the main feature branch. Card 2 covers how to split it without standing on each other's work.

**Use an LLM or coding agent. We recommend it.** Reading an unfamiliar schema and working out what a column is for is exactly the kind of task these tools are good at, and writing SQL you have not written before is another. The same rule from Phase 1 applies: verify every claim against the actual database before it goes in the report. One addition for this phase, and it is not optional: **never paste database credentials into an agent prompt, a browser tool, or anything else.** Card 1 covers how to handle them.

Phase 2 assumes you have finished [Phase 1]({{ site.baseurl }}/taskList/wiscurds-phase1/) and understand how the backend, the frontend, and the database fit together. The schema will make far more sense if you have already read the Rails models.

<div class="task-card-grid">

  <details class="task-card">
    <summary>1. Get Access to the Dummy Database</summary>
    <div class="card-body">

      <p>You are working against a <strong>dummy database</strong>: a copy of the platform's structure with non-production data in it. It exists so you can explore freely without any risk to real market data. Treat the credentials as seriously as production credentials anyway, because the habits you build here are the ones you will carry into real access later.</p>

      <details>
        <summary>1.1 Get Your Credentials and Open the GUI</summary>
        <div class="section-body">
          <p>Everything you need is shared with you through <strong>1Password</strong>: the username and password for the dummy database, and the <strong>link to the database GUI</strong> on the web server.</p>
          <p>You do not install anything for this phase. The GUI runs in your browser, so open the link from the 1Password item and sign in with the credentials stored alongside it. It is the same kind of interface as the phpMyAdmin you have already seen in the <a href="{{ site.baseurl }}/STUDENT_ONBOARDING_PLAN#database">Student Onboarding Plan</a>, so the navigation should feel familiar.</p>
          <p>Once you are in, open the schema in the sidebar, confirm you can see the list of tables, and click into one to browse its rows.</p>
          <p>If you cannot see the 1Password item, or the link does not let you in, tell Abanish in the WISCURDS Slack channel the same day rather than waiting. Do not ask anyone to send the credentials another way.</p>
          <h3>Rules for handling them</h3>
          <ul>
            <li><strong>Never commit them.</strong> Not in the report, not in a config file, not in a screenshot, not in a comment. Anything committed to Git is permanent even if you delete it in a later commit.</li>
            <li><strong>Never paste them into Slack, email, or a document.</strong> They live in 1Password and nowhere else.</li>
            <li><strong>Never paste them into an LLM or coding agent.</strong> If you want help with a connection problem, describe the error and redact the host and password.</li>
            <li><strong>Screenshots count.</strong> Before you put any GUI screenshot in the report, check that the URL bar, the host name, and the username are not visible in it.</li>
          </ul>
          <p><strong>Done when:</strong> both of you can open the GUI, list the tables, and read rows.</p>
        </div>
      </details>

      <details>
        <summary>1.2 Why the GUI Now and the Environment File Later</summary>
        <div class="section-body">
          <p>Worth understanding, because the tool changes in the next phase and the reason matters.</p>
          <p><strong>For this phase, use the GUI.</strong> Investigation is a visual job. You want to see the table list at a glance, click into a table and scan its rows, sort a column to spot the gaps, and see how everything connects. The GUI does all of that in a few clicks. Pointing your IDE or a terminal client at the same database is slower and shows you less, which is why we are not asking you to set that up yet.</p>
          <p><strong>From Phase 3, you stop making changes by hand.</strong> Once you are implementing rather than investigating, changes reach the database through the application: you point the backend at this database through its <strong>environment configuration</strong>, the same database settings you checked in <a href="{{ site.baseurl }}/taskList/wiscurds-phase0/">Phase 0</a>, and the changes are made in code, committed to a branch, and reviewed before they run.</p>
          <p>The reason is repeatability. A fix typed into a GUI happens once, on one machine, with no record of what was run or why. The same fix written as code is reviewable, repeatable on every environment, and still there in the history in six months when someone asks what changed. The GUI is for looking. Code is for changing.</p>
          <p>So: explore in the GUI now, and expect to leave it behind for anything that writes.</p>
        </div>
      </details>

    </div>

  </details>

  <details class="task-card">
    <summary>2. Open Your Team Branch and Split the Work</summary>
    <div class="card-body">

      <p>The report goes into the <strong>backend repository</strong>, <code>farmers-coalition</code>, since the database is the backend's concern. One branch, shared between the two of you. Card 8 has you open a branch of the same name in the frontend repo for the placeholder page, but everything up to that point happens here.</p>

      <details>
        <summary>2.1 Pull dev and Cut the Team Branch</summary>
        <div class="section-body">
          <p>Start from an up-to-date <code>dev</code>, exactly as you did in Phase 1. Your Phase 1 branch is merged and finished; do not build on it.</p>
          <pre><code>git checkout dev

git pull
git checkout -b feat-wis-p2-admin-dashboard</code></pre>

<p>One of you creates the branch and pushes it first:</p>
<pre><code>git push -u origin feat-wis-p2-admin-dashboard</code></pre>
<p>The other then checks it out rather than creating their own copy:</p>
<pre><code>git checkout dev
git pull
git checkout feat-wis-p2-admin-dashboard</code></pre>
<p>Agree between yourselves who does this first, in Slack, before either of you runs anything. Two people independently creating the same branch name is a mess to untangle.</p>
<p><strong>Done when:</strong> both of you are on <code>feat-wis-p2-admin-dashboard</code>, and it exists on GitLab.</p>
</div>
</details>

      <details>
        <summary>2.2 Create the Report Directory</summary>
        <div class="section-body">
          <p>Inside the <code>wiscurds/</code> directory you worked in during Phase 1, create a directory for this project's reports:</p>
          <pre><code>wiscurds/

└── admin_dashboard_reports/
└── database_current_state_report.md</code></pre>

<p>That directory holds this project's written work for the rest of the program, so later phases add their reports alongside this one rather than scattering them. This phase produces a single file, <code>database_current_state_report.md</code>, written by both of you.</p>
<p>If you include a screenshot in the report, save the image in the same directory and reference it from the Markdown.</p>
</div>
</details>

      <details>
        <summary>2.3 Agree Who Does What</summary>
        <div class="section-body">
          <p>Two people committing to one branch and one file will collide unless you decide in advance who owns what. Spend ten minutes on this before you start Card 3.</p>
          <h3>Split by section, not by sitting</h3>
          <p>The cleanest division is to give each of you whole sections of the report to own. For example, one takes the table inventory and the relationships, the other takes the identities and the data findings, and you write the cleaning opportunities together at the end because that section needs both halves. Any split works as long as it is explicit and written down in Slack.</p>
          <h3>Rules that keep the branch clean</h3>
          <ul>
            <li><strong>Pull before you start, pull before you push.</strong> <code>git pull</code> at the beginning of every working session and again before you push. Most conflicts come from working on a stale copy for two days.</li>
            <li><strong>Commit small and often.</strong> A section at a time, pushed the same day. Sitting on a week of work in a local branch is how conflicts become painful.</li>
            <li><strong>Stay out of each other's sections.</strong> If you think your teammate's section is wrong, tell them; do not rewrite it.</li>
            <li><strong>Say what you are doing.</strong> A message in Slack saying which section you are on takes five seconds and prevents you both writing the same thing.</li>
          </ul>
          <p>If you do hit a conflict, do not delete the file and start over. Post the conflict in Slack and we will walk through resolving it. Resolving your first merge conflict with someone watching is much easier than doing it alone at midnight.</p>
        </div>
      </details>

    </div>

  </details>

  <details class="task-card">
    <summary>3. Map the Tables and How They Relate</summary>
    <div class="card-body">

      <p>This is the foundation of everything else in the phase. Before you can judge whether the data is any good, you need to know what is stored and how the pieces connect.</p>

      <details>
        <summary>3.1 Build the Table Inventory</summary>
        <div class="section-body">
          <p>Open the database in the GUI. Selecting it in the sidebar gives you the full table list, and most tools show the approximate row count and size next to each table name. That list is your starting point, so copy it into your notes before you go any further.</p>
          <p>Then work through the tables one at a time. Two views do most of the work for you:</p>
          <ul>
            <li><strong>Structure</strong> shows the columns, their types, whether they allow nulls, and which column is the primary key.</li>
            <li><strong>Browse</strong> shows actual rows, which tells you far more about what a table is for than the column names do.</li>
          </ul>
          <p>Sort the table list by row count and start at the top. The biggest tables are usually the ones that matter, and working down from them means you understand the important parts first even if you run out of time at the bottom.</p>
          <p>For each table, work out:</p>

<ul>
<li><strong>What it stores</strong>, in one line and in your own words.</li>
<li><strong>Its primary key</strong>, and whether the key is a plain id or something more meaningful.</li>
<li><strong>Roughly how many rows</strong> it holds.</li>
<li><strong>Whether it looks live or dead</strong>. A table with zero rows, or one that has not been written to in years, is worth flagging now.</li>
</ul>
<p>You will not be able to guess every table from its name. When one is unclear, open the matching Rails model in <code>app/models/</code>. The model often names the relationship more clearly than the schema does, and it is the reason Phase 1 had you read them.</p>
<p>Do not write a paragraph on every table. Some will be obviously central and deserve real attention; others are lookup tables or framework bookkeeping and deserve one line.</p>
<p><strong>Done when:</strong> every table in the database has at least a one-line description and a row count.</p>
</div>
</details>

      <details>
        <summary>3.2 Map the Relationships</summary>
        <div class="section-body">
          <p>Now find how the tables point at each other. Work from the <strong>Structure</strong> view of each table, where two things tell you about relationships:</p>
          <ul>
            <li><strong>Columns ending in <code>_id</code>.</strong> A column named <code>market_id</code> is almost certainly a link to the markets table. This is the most reliable signal you have.</li>
            <li><strong>Declared foreign keys.</strong> Most GUIs show these on the Structure page or a relations view, usually as a link from the column to the table it references.</li>
          </ul>
          <p>Then check something important: <strong>not every real relationship is a declared foreign key</strong>. Rails applications often express a relationship in the model with <code>belongs_to</code> and <code>has_many</code> without ever adding a database-level constraint. So the GUI may show no foreign keys at all on a table that is clearly connected to three others.</p>
          <p>That means you need both sources:</p>
          <ul>
            <li>What the <strong>database</strong> declares, from the Structure view.</li>
            <li>What the <strong>models</strong> declare, from the <code>belongs_to</code> and <code>has_many</code> lines in <code>app/models/</code>.</li>
          </ul>
          <p>Write down, for each relationship, which table carries the reference and which one it points to, and mark whether it is declared in the database or only implied by the models. A relationship that exists in the models but not in the database is worth flagging explicitly, because it means nothing at the database level stops an orphaned row from being created. That observation feeds directly into Card 6.</p>
          <p>Finish by checking one relationship against real data: open a row in a child table, note its <code>_id</code> value, and find the matching parent row. If the parent is not there, you have found your first orphan.</p>
          <p><strong>Done when:</strong> you have a written list of the relationships between the main tables, each marked as declared or implied.</p>
        </div>
      </details>

    </div>

  </details>

  <details class="task-card">
    <summary>4. Map the Three Identities</summary>
    <div class="card-body">

      <p>Farm2Facts is organized around who the user is, and the whole platform nests: individual producers and vendors belong to a market, and markets belong to a market organization. In this card you work out how that nesting is actually stored.</p>
      <p>Keep this at a <strong>surface level</strong>. You are answering "where does this identity live and how does it connect upward", not documenting every column and permission rule.</p>

      <h3>The Three to Cover</h3>
      <p>For each of these, answer the same four questions:</p>
      <ul>
        <li><strong>Individual Producer</strong></li>
        <li><strong>Individual Market</strong></li>
        <li><strong>Market Organization</strong></li>
      </ul>

      <h3>The Four Questions</h3>
      <ol>
        <li><strong>Which table or tables represent it?</strong> Is there one table per identity, or do they share a table with a type or role column distinguishing them?</li>
        <li><strong>How does it connect upward?</strong> Which column ties a producer to its market, and a market to its organization? Follow the actual foreign key or id column.</li>
        <li><strong>What does one real row look like?</strong> Open the table and read an actual record. Which fields are filled in, and which are consistently empty?</li>
        <li><strong>How many are there?</strong> Count the rows for each identity. The proportions alone tell you something about how the platform is used.</li>
      </ol>

      <h3>Two Things to Watch For</h3>
      <ul>
        <li><strong>Vendors and producers may not be the same thing.</strong> The <a href="{{ site.baseurl }}/taskList/wiscurds-development-structure">Development Structure Overview</a> lists individual vendors and individual producers separately. Check whether the database treats them as two things or one, and say which in the report.</li>
        <li><strong>Accounts and identities may be separate.</strong> There is often a users table holding login credentials, linked to a separate table holding the market or organization it belongs to. Work out which table is the login and which is the identity, because they are easy to confuse and the difference matters in Phase 3.</li>
      </ul>

      <p>Finish this card by tracing one chain from top to bottom: pick a real market organization, find its markets, and find the producers under one of those markets. If you cannot make that trip through the data, that is a finding in itself and it goes in the report.</p>

      <p><strong>Done when:</strong> all three identities are mapped to their tables, with counts, and you have traced one complete organization to market to producer chain in real data.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>5. Look at the Data Itself</summary>
    <div class="card-body">

      <p>Cards 3 and 4 told you what the database is shaped like. This card is about what is actually sitting in it, which is a different question and usually a less flattering one.</p>
      <p>Every finding here needs a <strong>number</strong> behind it. "A lot of markets look inactive" is an impression. "Of 412 market rows, 287 have no submissions after 2022" is a finding, and it is the kind that changes what gets built.</p>

      <h3>What to Check</h3>
      <ul>
        <li><strong>Volume.</strong> Real row counts for the main tables, not the estimates from Card 3.</li>
        <li><strong>Freshness.</strong> Find the date columns and look at the spread. When was the most recent record written? How much of the data is from the last year, and how much is years old?</li>
        <li><strong>Activity.</strong> How many markets and organizations have submitted anything recently, and how many are dormant? Are there records that were created and then never used?</li>
        <li><strong>Completeness.</strong> Which columns are mostly empty? A column that is null in 90 percent of rows is either optional, abandoned, or broken, and it is worth knowing which.</li>
        <li><strong>Duplicates.</strong> Are the same market, organization, or producer represented more than once under slightly different names?</li>
        <li><strong>Orphans.</strong> Rows that point at a parent that no longer exists. Particularly likely wherever you found an implied relationship with no database constraint in Card 3.2.</li>
        <li><strong>Consistency.</strong> Do the same kinds of values follow the same format? Dates stored as text in some rows, mixed casing in names, inconsistent state or status codes, stray whitespace.</li>
      </ul>

      <h3>Getting the Numbers From the GUI</h3>
      <p>The GUI gives you most of this without writing anything. A few things to lean on:</p>
      <ul>
        <li><strong>Sorting a column</strong> is the fastest way to see the extremes. Sort by a date column to find the oldest and newest records; sort by a text column and the empty values group together at one end.</li>
        <li><strong>The search or filter view</strong> on a table lets you count rows matching a condition, which covers most completeness and activity questions.</li>
        <li><strong>The row count</strong> shown when you browse a filtered table is the number you are after. Read it off rather than counting by hand.</li>
        <li><strong>Paging through a table</strong> for a minute tells you about formatting and consistency in a way no summary does. Look at the actual values.</li>
      </ul>
      <p>Record how you got each number as you go, so the next person can repeat it. A line like "markets table, filtered to <code>created_at</code> before 2023, 287 rows" is enough.</p>

      <p><strong>Done when:</strong> you have written findings, each with a number and a note of how you got it, covering volume, freshness, completeness, duplicates, and orphans.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>6. Find the Cleaning Opportunities</summary>
    <div class="card-body">

      <p>This card turns the findings from Card 5 into a list of candidates for Phase 3. It is the part of the report we will act on, so it is worth doing carefully.</p>
      <p>A cleaning opportunity is not just "this data looks bad". It is a specific problem, the evidence that it is real, what you would do about it, and what could go wrong if you did.</p>

      <h3>Describe Each One This Way</h3>
      <ul>
        <li><strong>What is wrong.</strong> The specific problem, in one sentence.</li>
        <li><strong>Evidence.</strong> The count, where it came from, and an example row or two.</li>
        <li><strong>Why it matters.</strong> What breaks or misleads because of it. A problem with no consequence is not worth a phase of work.</li>
        <li><strong>What you would do.</strong> Delete, merge, backfill, normalize the format, add a constraint, or leave it alone and document it.</li>
        <li><strong>What could go wrong.</strong> What else points at this data, and what breaks if you change it. Deleting a row that another table still references is how a cleanup becomes an outage.</li>
      </ul>

      <h3>Two Warnings</h3>
      <ul>
        <li><strong>Do not act on any of it yet.</strong> No fixes in this phase, not even small obvious ones, and not even in the dummy database. The whole point of writing the proposal first is that someone gets to disagree with it before it happens.</li>
        <li><strong>Not everything odd is wrong.</strong> A column that is empty most of the time may be genuinely optional. A market with no recent submissions may have closed. Before you propose deleting anything, ask whether the data is telling you the truth about the real world. Where you are unsure, put it in Open Questions rather than in the proposal.</li>
      </ul>

      <p>Rank the list. Put the problems with real consequences at the top and the cosmetic ones at the bottom, and say which ones you think are worth doing in Phase 3 and which you would leave.</p>

      <p><strong>Done when:</strong> you have a ranked list of cleaning candidates, each with evidence, a proposed action, and a risk.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>7. Write the Report</summary>
    <div class="card-body">

      <p>The deliverable for this phase is one report, written by both of you, saved as:</p>
      <pre><code>wiscurds/admin_dashboard_reports/database_current_state_report.md</code></pre>
      <p>It is the reference you will work from for the rest of the program, and it is what we read when deciding what Phase 3 actually builds.</p>

      <h3>What Makes It a Good Report</h3>
      <ul>
        <li><strong>Numbers, not impressions.</strong> Every claim about the data carries a count and a note of how you got it.</li>
        <li><strong>Name real tables and columns.</strong> A reader should be able to check any statement in the report against the database in under a minute.</li>
        <li><strong>One voice.</strong> You are writing one document, not stapling two together. Read each other's sections at the end and make them sound like the same report.</li>
        <li><strong>No credentials anywhere.</strong> Check the screenshots too.</li>
      </ul>

      <h3>Report Template</h3>
      <pre class="pre-scroll"><code># Admin Dashboard -- Database Current State Report

**Authors:** [Name], [Name]
**Program:** WISCURDS | **Phase:** 2 -- Data Source Investigation
**Database:** dummy database, read through the web GUI (credentials in 1Password)
**Date:** [Date]

## 1. Summary

[Half a page. What this database holds, how it is broadly organized, and
the three or four things a reader most needs to know about the state it
is in. Write this section last.]

## 2. How We Worked

[Which GUI you used and how you split the investigation between the two
of you. Two or three sentences. If there is anything you could not check
because the GUI made it impractical, say so here rather than leaving a
silent gap in the findings.]

## 3. Table Inventory

[One row per table, using the row counts the GUI reports. Keep
descriptions to a line.]

| Table | Rows | Primary key | What it stores | Live or dead |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

[Below the table: which tables are central, which are lookup or
framework tables, and which look unused.]

## 4. How the Tables Relate

[One row per relationship. "From" is the table that carries the
reference.]

| From | Column | To | Declared or implied |
| --- | --- | --- | --- |
|  |  |  |  |

[Then in writing: which of these exist only in the Rails models with no
constraint in the database, and what that allows to happen.]

[Then: the path you would follow to get from a market organization down
to a single producer's records.]

## 5. The Three Identities

### 5.1 Individual Producer

- **Tables:** [which table or tables represent it]
- **Connects upward by:** [the column that ties it to its market]
- **A real row:** [which fields are filled in, which are always empty]
- **How many:** [row count]

### 5.2 Individual Market

[Same four points.]

### 5.3 Market Organization

[Same four points.]

### 5.4 Notes

[Whether vendors and producers are one thing or two in this database,
how login accounts relate to these identities, and the complete
organization to market to producer chain you traced.]

## 6. Data Findings

[What condition the data is in. Every finding needs a number and a note
of how you got it, so someone else can repeat the check in the GUI.
Example of a usable "how we checked": "markets table, filtered to
created_at before 2023".]

### 6.1 Volume and Freshness

| Finding | Number | How we checked |
| --- | --- | --- |
|  |  |  |

### 6.2 Completeness

[Which columns are substantially empty. Same table shape as 6.1.]

### 6.3 Duplicates, Orphans, and Inconsistency

[Duplicate records, rows pointing at parents that do not exist, and
values stored in inconsistent formats. Same table shape as 6.1, plus an
example row or two for anything that needs seeing to be understood.]

## 7. Cleaning Opportunities

[Ranked, most consequential first.]

### Opportunity 1: [Short title]

- **What is wrong:**
- **Evidence:** [the number, and how you checked it]
- **Why it matters:**
- **Proposed action:**
- **Risk:**

### Opportunity 2: [Short title]

[Same structure. Repeat as needed.]

### Recommended for Phase 3

[Which of the above you think are worth doing, and which you would
leave alone and why.]

## 8. Open Questions

[Anything you could not resolve: a table you could not explain, data
that might be correct but looks wrong, a decision that needs someone
who knows the markets. Number them so we can answer them individually.]

## 9. Working With an LLM

[Which tool you used, where it helped, where it was wrong, and what you
would prompt differently next time. Three or four sentences.]</code></pre>

      <p>Sections 7 and 8 are the ones we read most closely. Section 7 is the proposal that decides what Phase 3 builds, and Section 8 is where you tell us what you need from us to keep moving.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>8. Add the Admin Dashboard Placeholder</summary>
    <div class="card-body">

      <p>This is the one piece of code you write in Phase 2, and it is deliberately small. Before Phase 3 puts anything real into the Admin Dashboard, the place it will live has to exist. Your job is to add an <strong>Admin Dashboard</strong> entry to the admin navigation dropdown and give it a page to open, even though that page has nothing in it yet.</p>
      <p>The value is not the feature. It is proving you can find your way around an unfamiliar frontend and ship a change through review while the change itself carries no risk. Get the workflow wrong here and it costs nothing. Get it wrong in Phase 3 and it costs a rollback.</p>

      <h3>What You Are Building</h3>
      <ul>
        <li>A new entry labelled <strong>Admin Dashboard</strong> in the admin nav bar dropdown, in the <strong>same section</strong> that currently lists <strong>Users Account</strong> and <strong>Export Data</strong>.</li>
        <li>A page for it to open. For now that page is blank, or carries the heading <strong>Admin Dashboard</strong> and nothing else.</li>
        <li>Nothing else. No data, no components, no styling work. An empty page is the correct outcome.</li>
      </ul>

      <h3>Where the Work Happens</h3>
      <p>This one is in the <strong>frontend repository</strong>, <code>farm2facts-frontend</code>, not the backend repo you have been in for the rest of this phase. Branch from <code>dev</code> exactly as before:</p>
      <pre><code>git checkout dev
git pull
git checkout -b feat-wis-p2-admin-dashboard</code></pre>
      <p>Same branch name as your backend branch, in a different repository. The team rules from Card 2.3 still apply: one of you creates and pushes it, the other checks it out rather than making their own.</p>

      <h3>Find the Placement Before You Create Anything</h3>
      <p>Do not start by making files. Start by finding the code that renders the dropdown you can already see, because the fastest way to add something to an unfamiliar codebase is to copy what is already working next to it.</p>
      <ol>
        <li>Open the running frontend, log in as an admin, and find the dropdown containing <strong>Users Account</strong> and <strong>Export Data</strong>. Note the labels exactly as they appear.</li>
        <li><strong>Search the repo for those labels.</strong> A visible string is the quickest way into frontend code you do not know. That search should land you in the component that builds the menu.</li>
        <li>Read how one existing entry is defined: its label, where it links to, and any condition controlling who can see it.</li>
        <li>Follow that link into the <strong>router</strong> and find the route definition, then the <strong>view file</strong> the route loads.</li>
      </ol>
      <p>By the end of this step you should be able to name three things: the component holding the dropdown, the route definition, and the view file it loads. Write those paths down. They go in your merge request description.</p>

      <h3>Then Build It by Copying the Pattern</h3>
      <ul>
        <li><strong>Add the entry</strong> to the dropdown in the same section as the other two, following the exact shape of the entries around it.</li>
        <li><strong>Add the route</strong>, named consistently with the existing routes rather than inventing a new convention.</li>
        <li><strong>Create the view file</strong> in the same place and the same structure as the neighbouring views. If those views are split across several files, match that; if they are one file, match that.</li>
        <li><strong>Respect the visibility rule.</strong> If the existing entries are gated so that only admins see them, yours is gated the same way. This is the one part of the card where getting it wrong actually matters.</li>
      </ul>
      <p>Resist the urge to build more than this. If you find yourself adding a table or a chart, stop: that is Phase 3 work and it needs the proposal from Card 6 approved first.</p>

      <h3>Check It Works</h3>
      <ul>
        <li>Logged in as an admin, the dropdown shows <strong>Admin Dashboard</strong> in the right section.</li>
        <li>Clicking it changes the URL and loads the page with no errors in the browser console.</li>
        <li>If the section is admin-only, log in as another user type and confirm the entry is <strong>not</strong> there.</li>
        <li><strong>Users Account</strong> and <strong>Export Data</strong> still work. A change to a shared menu is exactly the kind of thing that quietly breaks its neighbours.</li>
      </ul>

      <h3>Open the Merge Request</h3>
      <p>Same flow as the report, in the frontend repo this time:</p>
      <ol>
        <li><strong>Code &rarr; Merge requests &rarr; New merge request</strong>.</li>
        <li><strong>Source:</strong> <code>feat-wis-p2-admin-dashboard</code>. <strong>Target:</strong> <code>dev</code>.</li>
        <li>Title it <code>Add Admin Dashboard placeholder to the admin navigation</code>.</li>
        <li>In the description, name the <strong>three files</strong> you found and changed, and say plainly that the page is intentionally empty and gets filled in Phase 3. A reviewer seeing an empty page with no explanation will assume something is missing.</li>
        <li>Attach a <strong>screenshot</strong> of the dropdown with the new entry visible.</li>
        <li>Assign <strong>Abanish</strong> as the reviewer, and read the <strong>Changes</strong> tab before you submit.</li>
      </ol>
      <p>This is a separate merge request from the report one. Two repos, two branches, two merge requests, and they are reviewed independently.</p>

      <p><strong>Done when:</strong> the entry appears in the dropdown for an admin, it opens a page without errors, the other entries still work, and the merge request is open against <code>dev</code> and assigned.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>9. Commit and Submit the Report</summary>
    <div class="card-body">

      <p>This card is about the <strong>report</strong>, which lives in the backend repo. You submit it by <strong>merge request</strong> into <code>dev</code>, the same way you submitted Phase 1. One merge request for the team, from your shared branch. The frontend merge request from Card 8 is separate and travels on its own.</p>

      <details>
        <summary>9.1 Commit as You Go</summary>
        <div class="section-body">
          <p>Do not save all of this for the last day. Commit each section of the report as it becomes usable:</p>
          <pre><code>git pull

git status
git add wiscurds/admin_dashboard_reports/
git commit -m "Add table inventory to the database current state report"</code></pre>

<p><code>git status</code> before every <code>git add</code>, same as Phase 1. Two things to confirm in its output: you are on <code>feat-wis-p2-admin-dashboard</code>, and the only files listed are inside <code>wiscurds/admin_dashboard_reports/</code>. Nothing from <code>app/</code>, <code>config/</code>, or <code>db/</code> should ever appear in this phase's commits. If something does, you changed a file by accident.</p>
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
            <li><strong>Source branch:</strong> <code>feat-wis-p2-admin-dashboard</code>.</li>
            <li><strong>Target branch:</strong> <code>dev</code>. Never <code>main</code>.</li>
            <li>Title it <code>Phase 2 database current state report -- Admin Dashboard</code>.</li>
            <li>Fill out the description using the <a href="{{ site.baseurl }}/docs/guides/#pull-requests">Pull Requests guide</a>, and name both authors in it.</li>
            <li>Assign <strong>Abanish</strong> as the reviewer.</li>
          </ol>
          <p>In the description, include your <strong>top three cleaning opportunities</strong> and your <strong>open questions</strong>, so they are visible without opening the file.</p>
          <p>Open the <strong>Changes</strong> tab and read the diff before you submit. Both of you, not just whoever clicked the button.</p>
          <p><strong>Done when:</strong> one merge request is open against <code>dev</code>, assigned to Abanish, with both of you named.</p>
        </div>
      </details>

      <details>
        <summary>9.3 Respond to Review</summary>
        <div class="section-body">
          <p>Expect comments, and expect some of them to ask for a number you did not include. Commit the changes on the same branch and push again; the merge request updates itself. Reply to each comment saying what you changed.</p>
          <p>Once it is approved we merge it into <code>dev</code>, and the cleaning opportunities you proposed become the starting point for Phase 3.</p>
        </div>
      </details>

      <p>Bring your open questions to the weekly check-in rather than waiting for the review. Several of them will be questions about how the markets actually work, and those are faster to answer out loud than in a comment thread.</p>

    </div>

  </details>

</div>
