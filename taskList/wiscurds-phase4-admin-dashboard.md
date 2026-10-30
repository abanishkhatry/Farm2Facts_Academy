---
layout: default
title: "Phase 4 Task Guide -- Admin Dashboard"
permalink: /taskList/wiscurds-phase4-admin/
---

# Phase 4 Task Guide -- Project A: Admin Dashboard

**Program:** WISCURDS | **Phase:** 4 -- Data Analytics and Usability Testing | **Team:** Aditya and Yahia

---

This is the task companion to the [Phase 4 milestone card]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-4). That card describes what the phase covers; this guide is what you actually do, in order.

Phase 2 told us what is in the database. Phase 3 cleaned it. Phase 4 is where the Admin Dashboard stops being a blank page and starts answering questions staff actually have: who is on this platform, who is still using it, and how much of what we hold is real.

The phase has four parts:

1. **Review the proposed visualizations.** Give your verdict on the nine proposed metrics and say what is missing.
2. **Build the metrics endpoint.** One backend endpoint that returns the numbers.
3. **Build the dashboard.** The charts, on the Admin Dashboard page you created in Phase 2.
4. **Build the archived data view.** A separate view for what Phase 3 moved out.

**Every chart reads live data only.** Phase 3 moved rows into `archived_users`, `archived_market_profiles`, `archived_sales_slips` and `archived_visitor_counts` precisely so they would stop distorting the counts. No chart in Part 3 may read an archive table. The archived rows get their own view in Part 4, and the two are never added together.

**Numbers are computed in the database, not in the browser.** The dashboard asks the API for counts and gets counts back. It does not fetch 54,962 sales slips and total them in JavaScript. If a chart is slow, fix the query or add an index, and say so in the merge request.

**Use an LLM or coding agent. We recommend it.** Chart configuration is fiddly and well-documented, which is exactly where an agent helps. The rule from the earlier phases still holds: read every query it writes before you run it, and never paste database credentials into a prompt.

Phase 4 assumes your three Phase 3 merge requests are merged. Keep `queries_used.sql` open: most of these metrics are queries you have already written.

<div class="task-card-grid">

  <details class="task-card">
    <summary>1. How Phase 4 Works</summary>
    <div class="card-body">

      <p>This phase spans both repositories, so there are two branches and two merge requests. Not five. The parts are separated by <strong>commits</strong> inside those two branches, not by branches of their own.</p>

      <h3>Two Branches, One Per Repository</h3>
      <table>
        <thead><tr><th>Repository</th><th>Branch</th><th>Holds</th></tr></thead>
        <tbody>
          <tr><td><code>farmers-coalition</code></td><td><code>feat-wis-p4-admin-dashboard</code> (new, from <code>dev</code>)</td><td>Parts 1 and 2</td></tr>
          <tr><td><code>farm2facts-frontend</code></td><td><code>feat-wis-p2-admin-dashboard</code> (already open)</td><td>Parts 3 and 4</td></tr>
        </tbody>
      </table>

      <p><strong>The frontend branch already exists.</strong> It is the one you opened in Phase 2 for the blank Admin Dashboard page, and it was deliberately left unmerged so that this phase could build on it. Do not branch again and do not open a second one. Check it out, pull it, and keep working:</p>
      <pre><code>git checkout feat-wis-p2-admin-dashboard
git pull</code></pre>
      <p>That means the frontend merge request will end up covering both the Phase 2 placeholder and the Phase 4 dashboard built on top of it. Say so in its description.</p>

      <p>The backend branch is new. Open it off an up-to-date <code>dev</code>:</p>
      <pre><code>git checkout dev
git pull
git checkout -b feat-wis-p4-admin-dashboard</code></pre>

      <h3>Split the Work by Commits</h3>
      <p>With four parts in two branches, the commits are what keeps the work reviewable. One commit per piece of finished work, with a message that says what it does:</p>
      <pre><code>Add account roster and engagement queries to the metrics endpoint
Add the onboarding funnel chart to the admin dashboard
Add the archived data view</code></pre>
      <p>Two rules that matter more now than they did in Phase 3:</p>
      <ul>
        <li><strong>Commit each part separately.</strong> A reviewer reading the branch commit by commit should be able to follow the same order this guide is written in. One commit holding the endpoint, the charts and the archive view together is not reviewable.</li>
        <li><strong>Pull before you push, every time.</strong> You are both committing to the same two branches all phase. Coordinate on who is working where before you start, and do not leave a branch broken overnight, because the other person is working on it too.</li>
      </ul>

      <h3>Live Data Only</h3>
      <p>Every query in Part 2 reads the live tables: <code>users</code>, <code>profiles</code>, <code>sales_slips</code>, <code>visitor_counts</code> and the rest. None of them reads an archive table. A count that quietly includes archived rows undoes the work you did in Phase 3 and makes the dashboard disagree with the database.</p>
      <p>Part 4 is the one place archived rows are counted, and that view says so on its face.</p>

      <h3>Still the Dummy Database</h3>
      <p>Everything in this phase runs against the dummy database through your local backend. The numbers you see are dummy numbers, and some of them are strange for that reason. That is fine: the dashboard has to survive strange data, because production has its own.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>2. Part 1 -- Review the Proposed Visualizations</summary>
    <div class="card-body">

      <p>Below are <strong>nine proposed visualizations</strong>. They are a proposal from Abanish, drawn from your Phase 2 findings, and they are not settled. What this part asks for is your report on them: for each one, should we pursue it or not, and why.</p>
      <p>You are the two people who have actually read this database. If one of these cannot be built honestly from what we hold, you will know before anyone else does, and that is the point of asking.</p>

      <table>
        <thead><tr><th>#</th><th>Visualization</th><th>Answers</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>Account roster by type and status</td><td>Who is on the platform, and how many never signed in</td></tr>
          <tr><td>2</td><td>Account engagement by recency</td><td>Who is still using it and who has gone quiet</td></tr>
          <tr><td>3</td><td>Onboarding funnel</td><td>Where accounts stop: sign-up, approval, sign-in, profile, first submission</td></tr>
          <tr><td>4</td><td>Submission volume over time, by instrument</td><td>How use has risen and fallen, and where bulk loads happened</td></tr>
          <tr><td>5</td><td>Profile completeness</td><td>How much of what we hold is real data versus blank shells</td></tr>
          <tr><td>6</td><td>Instrument adoption</td><td>Which instruments active accounts actually use</td></tr>
          <tr><td>7</td><td>Geographic coverage</td><td>Where our accounts are, and where the location data is missing</td></tr>
          <tr><td>8</td><td>Data quality flags</td><td>What still needs a human to look at it</td></tr>
          <tr><td>9</td><td>Archived data view</td><td>What Phase 3 moved out, and why</td></tr>
        </tbody>
      </table>

      <h3>Step 1. Give a verdict on each of the nine</h3>
      <p>Pursue, or do not pursue, with two or three sentences of reasoning. The question to answer for each is whether the data actually supports it. Cite your own Phase 2 numbers where they make the case, because "70% of profiles have no name, year, state or city" is a stronger argument than "completeness matters."</p>
      <p>Also note, per visualization, which tables and columns it would read and what chart form you would use.</p>

      <h3>Step 2. Say what is missing</h3>
      <p>Anything you think should be on the dashboard that is not in the nine. Same format: what it shows, who it helps, where it comes from. You spent a whole phase in this database, so this section is likely to be the most valuable part of the report.</p>

      <h3>Step 3. Say what the data cannot support</h3>
      <p>Name anything where a column is too empty or too inconsistent to chart honestly. Two from your own report, as examples of the standard:</p>
      <ul>
        <li><strong>Sales broken down by vendor.</strong> <code>sales_slips.vendor_id</code> is 95.5% empty, so such a chart would describe 4% of the data while looking authoritative.</li>
        <li><strong>Anything sourced from <code>markets</code>.</strong> No code writes to it, the last row is from 2025-07, and 81% have no name.</li>
      </ul>

      <h3>Step 4. Commit the report, then keep going</h3>
      <p>The report goes in the directory you created in Phase 2, on the backend branch:</p>
      <pre><code>wiscurds/
└──&nbsp;admin_dashboard_reports/
&nbsp;&nbsp;&nbsp;&nbsp;├──&nbsp;database_current_state_report.md
&nbsp;&nbsp;&nbsp;&nbsp;├──&nbsp;foreign_key_design_report.md
&nbsp;&nbsp;&nbsp;&nbsp;└──&nbsp;visualization_proposal_review.md</code></pre>
      <p>So the full path is <code>wiscurds/admin_dashboard_reports/visualization_proposal_review.md</code>.</p>

      <h3>Who Takes This Forward</h3>
      <p><strong>You are not contacting the Market and Research team.</strong> Abanish takes your report to them and brings back their decision. That is not your step, and waiting on it is not your step either.</p>
      <p><strong>Do not wait.</strong> Once the report is committed, move straight on to Part 2 and keep building. Some of the nine may change once that feedback comes back mid-phase, and a changed visualization is a small amount of rework against a whole phase spent waiting. Build on the assumption that the nine stand until you hear otherwise.</p>

      <p><strong>Done when:</strong> all nine have a verdict with reasoning, your additions are written up, the report is committed to the backend branch, and you have started Part 2.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>3. Part 2 -- Build the Metrics Endpoint</summary>
    <div class="card-body">

      <p>One backend endpoint that returns every number the dashboard needs, so the frontend does no arithmetic. On the backend branch. Five steps.</p>

      <h3>Step 1. Write the queries</h3>
      <p>One query per visualization, returning counts rather than rows. Most of these you already wrote in Phase 2, so start from <code>queries_used.sql</code> rather than from nothing.</p>
      <p>Two that need care:</p>
      <ul>
        <li><strong>Engagement</strong> uses the submission definition from your Phase 2 report: an account counts as having submitted if any of its profiles has a row in any instrument table. Keep the "submitted, no date" bucket, or producers will look inactive when they are not.</li>
        <li><strong>Submission volume</strong> is charted on <code>created_at</code>, not on the instrument's own <code>date</code> column. Your report found 1,060 sales slips dated before 2010 and one visitor count dated 2109, and those dates would wreck the axis.</li>
      </ul>

      <h3>Step 2. Confirm every query reads live tables only</h3>
      <p>Go through them one at a time and check that no archive table appears. This is the step people skip.</p>

      <h3>Step 3. Expose one endpoint</h3>
      <p>Follow the patterns already in <code>app/controllers/api/v1/</code>. One endpoint returning one JSON object with a key per visualization is easier to cache and easier to reason about than nine separate calls.</p>
      <p>It is an admin endpoint, so it must require authentication and must refuse a non-admin account. Check how the existing admin-only endpoints do this and do the same thing rather than inventing a second way.</p>

      <h3>Step 4. Check it against the database</h3>
      <p>Run each query in phpMyAdmin and compare it to what the endpoint returns. They have to match exactly. A dashboard that is confidently wrong is worse than no dashboard, and this is the only step that catches it.</p>

      <h3>Step 5. Time it</h3>
      <p>Record how long the endpoint takes. Some of these touch tables with 50,000-plus rows, and Phase 3 found 24 of 38 link columns have no index. If something is slow, say which query and why in the merge request.</p>

      <p><strong>Done when:</strong> the endpoint returns every number the dashboard needs, each one matches a query you ran by hand, no archive table is read anywhere, and non-admin accounts are refused.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>4. Part 3 -- Build the Dashboard</summary>
    <div class="card-body">

      <p>Fill in the Admin Dashboard page you created as a placeholder in Phase 2. This is on the frontend branch you already have open, so start by checking it out rather than creating anything. Five steps.</p>

      <h3>Step 1. Check what charting the frontend already has</h3>
      <p>Look at <code>package.json</code> before adding a dependency. The MDB Vue UI Kit we use ships a chart component, and a charting library may already be present. Adding a second one is a cost to everybody who works on this repo afterward, so if you do need a new dependency, say in the merge request what you considered and why the existing option did not work.</p>

      <h3>Step 2. Lay out the page</h3>
      <p>The headline counts at the top, the charts below. Give each chart a title that states what it shows and a one-line caption saying where the number comes from, because an admin who cannot tell what a chart counts will not trust it.</p>

      <h3>Step 3. Build the charts</h3>
      <p>One at a time, one commit each, from the endpoint. Suggested forms:</p>
      <table>
        <thead><tr><th>Visualization</th><th>Form</th></tr></thead>
        <tbody>
          <tr><td>Account roster by type and status</td><td>Stacked bar, one bar per account type</td></tr>
          <tr><td>Account engagement by recency</td><td>Grouped bar: under 12 months, 12 to 24, over 2 years, submitted but undated, never</td></tr>
          <tr><td>Onboarding funnel</td><td>Funnel: registered, approved, signed in, has a profile, submitted data</td></tr>
          <tr><td>Submission volume over time</td><td>Stacked area or multi-line by year, one series per instrument</td></tr>
          <tr><td>Profile completeness</td><td>Donut or horizontal bar: complete, partial, blank shell</td></tr>
          <tr><td>Instrument adoption</td><td>Horizontal bar: share of recently active accounts using each instrument</td></tr>
          <tr><td>Geographic coverage</td><td>Bar by state, with the country breakdown beside it</td></tr>
          <tr><td>Data quality flags</td><td>A table of counts, not a chart. These need a human to look, not a trend line.</td></tr>
        </tbody>
      </table>

      <h3>Step 4. Handle loading, empty and error states</h3>
      <p>Every chart needs three states besides the normal one: loading, no data, and the request failed. A chart that renders as a blank rectangle when the endpoint errors looks exactly like a chart reporting zero, and an admin cannot tell the difference.</p>

      <h3>Step 5. Check it on a narrow screen</h3>
      <p>Charts are the easiest thing on a page to break at tablet width. Look at it at a few sizes before you push.</p>

      <p><strong>Done when:</strong> every visualization renders with real numbers from the endpoint, each has a title and a source caption, the three non-normal states work, and nothing on the page reads an archive table.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>5. Part 4 -- Build the Archived Data View</summary>
    <div class="card-body">

      <p>Phase 3 moved rows out of the live tables. Those rows still exist and somebody will eventually ask what happened to them. This view is the answer, and it is deliberately separate from the dashboard so that archived rows can never be mistaken for live ones.</p>
      <p>Four steps, across both branches.</p>

      <h3>Step 1. Add the archive counts to the endpoint</h3>
      <p>On the backend branch, return the row count for each of the four archive tables: <code>archived_users</code>, <code>archived_market_profiles</code>, <code>archived_sales_slips</code> and <code>archived_visitor_counts</code>. Keep them under a separate key from the live metrics, so a mistake in the frontend cannot silently add the two together.</p>

      <h3>Step 2. Build the view</h3>
      <p>On the frontend branch. Reachable from the Admin Dashboard but on its own page or tab, not mixed into the charts. It needs:</p>
      <ul>
        <li><strong>How much was archived</strong>, per table and in total. A bar chart is enough.</li>
        <li><strong>Why each group was archived.</strong> Accounts with no valid <code>indiv_or_org</code> are a different case from rows orphaned by a deleted parent, and the view should say which is which.</li>
        <li><strong>When.</strong> Which Phase 3 migration moved them.</li>
      </ul>

      <h3>Step 3. Label it unmistakably</h3>
      <p>The page states at the top that these rows are archived and are not counted anywhere on the dashboard. Give it a visual treatment that differs from the live charts. Somebody will screenshot one of these without the surrounding page, and the screenshot has to be readable on its own.</p>

      <h3>Step 4. Say how a row comes back</h3>
      <p>A short note on the page, or a link to the Phase 3 report, explaining that the archive tables keep the original <code>id</code> values and that restoring a row is a migration somebody writes deliberately. This view does not delete anything and does not restore anything.</p>

      <p><strong>Done when:</strong> the four archive tables are visible with their counts and the reason each group was moved, the page is clearly marked as archived data, and no number on it appears anywhere on the live dashboard.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>6. Submit</summary>
    <div class="card-body">

      <p>Two merge requests, one per repository, both targeting <code>dev</code>. Open them when the work in that repo is finished, not part by part, since each branch carries several parts.</p>

      <table>
        <thead><tr><th>Repository</th><th>Branch</th><th>What the merge request covers</th></tr></thead>
        <tbody>
          <tr><td><code>farmers-coalition</code></td><td><code>feat-wis-p4-admin-dashboard</code></td><td>The visualization review and the metrics endpoint</td></tr>
          <tr><td><code>farm2facts-frontend</code></td><td><code>feat-wis-p2-admin-dashboard</code></td><td>The Phase 2 placeholder page, the dashboard charts, the archived data view</td></tr>
        </tbody>
      </table>

      <h3>What Both Merge Requests Need</h3>
      <ul>
        <li><strong>What it does, in plain sentences,</strong> part by part. Each branch holds several parts, so the description has to say which commits are which.</li>
        <li><strong>A screenshot</strong> of every chart, for the frontend one. Charts are quicker to review as pictures than as configuration objects.</li>
        <li><strong>The numbers,</strong> for the backend one: what each query returns, and confirmation that you checked it by hand against the database.</li>
        <li><strong>Confirmation that no live chart reads an archive table.</strong></li>
        <li>Both of you named, and <strong>Abanish</strong> assigned as reviewer.</li>
      </ul>
      <p>The frontend merge request is the one you opened the branch for back in Phase 2, so its description needs to cover the placeholder page as well as everything built on top of it.</p>

      <h3>Read Your Own Diff First</h3>
      <p>Open the <strong>Changes</strong> tab and read every line, both of you. These branches are longer-lived than the Phase 3 ones and you have both been committing to them, so the diff will contain things you did not personally write. Nothing here is destructive the way Phase 3 was, but a wrong <code>WHERE</code> clause now produces a confident, wrong number on a page that staff will believe.</p>

      <p><strong>Done when:</strong> both merge requests are open or merged, the dashboard renders its visualizations from live data, the archived view accounts for everything Phase 3 moved, and the visualization review is in <code>wiscurds/admin_dashboard_reports/</code>.</p>

    </div>
  </details>

</div>
