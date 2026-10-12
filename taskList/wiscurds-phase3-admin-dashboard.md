---
layout: default
title: "Phase 3 Task Guide -- Admin Dashboard"
permalink: /taskList/wiscurds-phase3-admin/
---

# Phase 3 Task Guide -- Project A: Admin Dashboard

**Program:** WISCURDS | **Phase:** 3 -- Data Cleaning and Feature Integration | **Team:** Aditya and Yahia

---

This is the task companion to the [Phase 3 milestone card]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-3). That card describes what the phase covers; this guide is what you actually do, in order.

Phase 3 acts on your own Phase 2 findings. You wrote the proposal; this is the part where it happens. The phase has three parts, and they run in this order:

1. **Clean the `users` table.** Delete the fully empty rows, then archive every account whose `indiv_or_org` is not one of the three valid types.
2. **Archive the orphans.** Build an archive table for each of the three biggest orphan groups, move the orphaned rows into it, then remove them from the live table.
3. **Design the foreign keys.** For every table, say what the foreign key should be, what should happen when a parent is deleted, and what currently stands in the way.

**This is the first phase where you change real data, so the rules change with it.** Up to now a mistake cost you a rewrite. From here a mistake costs rows that nobody can get back. Card 1 covers how we work in this phase, and it is not optional reading.

**Archive before you delete. Always.** Nothing in this phase is removed from a table until a copy of it exists somewhere else and you have confirmed the copy is complete. This is why Part 2 builds the archive tables before it touches anything.

**Every change ships as code.** No edits in the GUI, not even a one-row fix. A change typed into phpMyAdmin happens once, on one machine, with no record of what ran or why. The same change as a Rails migration is reviewable, repeatable, and still in the history in six months. You wrote this in your own report; now it binds you.

**Use an LLM or coding agent. We recommend it.** Writing a Rails migration you have not written before is a good use of one. The rule from the earlier phases holds and matters more here: verify everything before you run it. An agent will happily write a `DELETE` with a subtly wrong `WHERE` clause, and that one is not recoverable. Read every line of generated SQL before it touches a database, and never paste database credentials into a prompt.

Phase 3 assumes your [Phase 2 report]({{ site.baseurl }}/taskList/wiscurds-phase2-admin/) is merged. Keep `queries_used.sql` open the whole time: you will re-run most of it.

<div class="task-card-grid">

  <details class="task-card">
    <summary>1. How Phase 3 Works</summary>
    <div class="card-body">

      <p>Read this card before you write anything. The workflow here is the one you will use for every change you make to Farm2Facts from now on.</p>

      <h3>One Issue, One Branch, One Merge Request, Per Part</h3>
      <p>The three parts are three separate pieces of work. They get reviewed separately, because a reviewer checking a destructive migration should not also be reading a design document.</p>
      <table>
        <thead><tr><th>Part</th><th>Issue</th><th>Branch</th></tr></thead>
        <tbody>
          <tr><td>1. Clean the users table</td><td>File one on the GitLab board</td><td><code>feat-wis-p3-clean-users</code></td></tr>
          <tr><td>2. Archive the orphans</td><td>File one on the GitLab board</td><td><code>feat-wis-p3-archive-orphans</code></td></tr>
          <tr><td>3. Foreign key report</td><td>File one on the GitLab board</td><td><code>feat-wis-p3-foreign-key-report</code></td></tr>
        </tbody>
      </table>
      <p>Each branch comes off an up-to-date <code>dev</code> and goes back into <code>dev</code>. Part 2 depends on Part 1 being merged, so do not start Part 2 from Part 1's branch; wait for the merge, then pull <code>dev</code> again. The full process is in <a href="{{ site.baseurl }}/docs/guides/#how-we-work">How We Work</a>.</p>
      <p>All of this happens in the <strong>backend repository</strong>, <code>farmers-coalition</code>, where the migrations and models live.</p>

      <h3>Every Change Is a Migration</h3>
      <p>Rails migrations are how the database changes. They are ordinary Ruby files that Rails runs in order and keeps a record of, which is exactly the repeatability a GUI edit does not give you.</p>
      <pre><code>bin/rails generate migration RemoveTypelessUsers
bin/rails db:migrate</code></pre>
      <p>Two rules for every migration you write in this phase:</p>
      <ul>
        <li><strong>Write it so it can be undone.</strong> Use explicit <code>up</code> and <code>down</code> methods rather than <code>change</code> whenever the migration moves or removes data, and make <code>down</code> actually restore what <code>up</code> took away. If a migration genuinely cannot be reversed, say so in the merge request rather than leaving the reviewer to discover it.</li>
        <li><strong>Wrap move-then-delete in a transaction.</strong> A copy that succeeds followed by a delete that fails is survivable. A delete that succeeds after a copy that failed is not.</li>
      </ul>
      <p>Do not use <code>User.delete</code> or <code>Profile.delete</code> anywhere. Those are the calls that created the orphan problem in the first place, because they skip the clean-up Rails would otherwise do. In this phase you are working in migrations with explicit SQL, so you control the order yourself.</p>

      <h3>Numbers Before and After, in Every Merge Request</h3>
      <p>For every change, re-run the relevant query from <code>queries_used.sql</code> before you run the migration and again after, and put both numbers in the merge request description. A reviewer should be able to see that you moved 12,277 rows and that 12,277 rows arrived.</p>
      <p>If the before number does not match what your Phase 2 report said, stop and work out why before you continue. Data has changed since September, and Part 1 changes the Part 2 numbers on purpose.</p>

      <h3>The Dummy Database Only</h3>
      <p>Every migration in this phase runs against the dummy database, through your local backend pointed at it by its environment configuration. Nothing here runs against production. When these changes are eventually applied for real, that is a separate, supervised step.</p>

      <h3>Get Current, and Take a Backup First</h3>
      <p>Pull <code>dev</code> in <code>farmers-coalition</code> so you are working against the current code, then open the branch for Part 1:</p>
      <pre><code>git checkout dev
git pull
git checkout -b feat-wis-p3-clean-users</code></pre>
      <p>Before the first destructive migration runs, <strong>export a copy of the dummy database</strong> and keep it somewhere outside the repo. The GUI has an export function; a full SQL dump is fine. You are unlikely to need it, and the one time you do, it is the difference between a bad afternoon and a lost phase.</p>
      <p>Do not commit the dump. It is data, it is large, and it does not belong in Git.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>2. Part 1 -- Clean the users Table</summary>
    <div class="card-body">

      <p>This part works only in the <code>users</code> table. Five steps, in order. Record the count at every step that asks for one, because those numbers are the deliverable.</p>

      <h3>Step 1. Count the users table</h3>
      <p>Record the total number of rows in <code>users</code> before anything changes. Every later number is measured against this one.</p>

      <h3>Step 2. Delete the fully empty rows</h3>
      <p>Delete every row where <strong>all</strong> columns are NULL. The primary key is the exception, since it always has a value; every other column must be NULL for the row to qualify.</p>
      <p>Write the condition out column by column, and run it as a <code>SELECT</code> first so you can see exactly which rows match before anything is removed.</p>

      <h3>Step 3. Count the users table again</h3>
      <p>Record the new total. The drop from Step 1 should equal the number of rows your <code>SELECT</code> returned. If it does not, stop and find out why.</p>

      <h3>Step 4. Create archived_users and move the untyped accounts</h3>
      <p>Create an <code>archived_users</code> table with the same structure as <code>users</code>. In MySQL, <code>CREATE TABLE archived_users LIKE users</code> copies the columns and indexes.</p>
      <p>It holds every remaining row whose <code>indiv_or_org</code> is NULL, blank, or anything other than these three values:</p>
      <ul>
        <li>Individual Farm/Producer</li>
        <li>Individual Market</li>
        <li>Market Organization</li>
      </ul>
      <p>Check how those three are actually spelled in the column before you write the condition, and match them exactly.</p>
      <p>Copy the matching rows into <code>archived_users</code>, confirm the number that arrived equals the number you expected, then delete those rows from <code>users</code>. Copy, verify, delete, in that order and in one transaction.</p>

      <h3>Step 5. Count both tables</h3>
      <p>Record the final row count in <code>users</code> and in <code>archived_users</code>. Those two added together should equal your Step 3 total.</p>

      <p><strong>Done when:</strong> you have four recorded counts (Steps 1, 3, and the two from Step 5), the empty rows are gone, and every account left in <code>users</code> carries one of the three valid types.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>3. Part 2 -- Archive the Orphaned Rows</summary>
    <div class="card-body">

      <p>Three tables, each handled the same way: find its orphaned rows, give it an archive table, move the orphans across, then remove them from the original.</p>
      <table>
        <thead><tr><th>Live table</th><th>Archive table</th><th>Orphaned when</th></tr></thead>
        <tbody>
          <tr><td><code>profiles</code></td><td><code>archived_market_profiles</code></td><td><code>user_id</code> points at a user that does not exist</td></tr>
          <tr><td><code>sales_slips</code></td><td><code>archived_sales_slips</code></td><td><code>profile_id</code> points at a profile that does not exist</td></tr>
          <tr><td><code>visitor_counts</code></td><td><code>archived_visitor_counts</code></td><td><code>profile_id</code> points at a profile that does not exist</td></tr>
        </tbody>
      </table>
      <p>Five steps, in order. Record the count at every step that asks for one.</p>

      <h3>Step 1. Count the three tables</h3>
      <p>Record the total number of rows in <code>profiles</code>, <code>sales_slips</code> and <code>visitor_counts</code> before anything changes.</p>

      <h3>Step 2. Find the orphaned rows in each</h3>
      <p>An orphan is a row whose link column <strong>is filled</strong> but whose parent row does not exist. A row with a NULL link column is not an orphan, it is unlinked, and it stays where it is. Make that distinction explicit in your condition.</p>
      <p>Record the orphan count for each of the three tables. Your Phase 2 numbers are from September and Part 1 has changed them, so count again rather than reusing them.</p>

      <h3>Step 3. Create the three archive tables</h3>
      <p>Create each archive table with the same structure as its source. In MySQL, <code>CREATE TABLE archived_sales_slips LIKE sales_slips</code> copies the columns and indexes.</p>
      <p>Keep the original <code>id</code> values as they are, so a row can be matched back to where it came from.</p>

      <h3>Step 4. Move the orphans and delete them from the original</h3>
      <p>One table at a time, in one transaction each:</p>
      <ol>
        <li><strong>Copy</strong> the orphaned rows into the archive table.</li>
        <li><strong>Verify</strong> that the number of rows that arrived equals the count from Step 2. If it does not, stop and let the transaction roll back.</li>
        <li><strong>Delete</strong> exactly those rows from the live table, matched by <code>id</code> rather than by re-running the orphan condition.</li>
      </ol>
      <p>Do <code>sales_slips</code> first, then <code>visitor_counts</code>, then <code>profiles</code> last. Profiles are parents to many other tables, so moving them changes orphan counts elsewhere; doing them last keeps the earlier numbers stable while you work.</p>

      <h3>Step 5. Count everything again</h3>
      <p>Record the final row count in all six tables: the three live ones and the three archives. For each pair, the live table plus its archive should equal your Step 1 total, and re-running the orphan check on each live table should now return zero.</p>

      <p><strong>Done when:</strong> all six counts are recorded and reconcile, and none of the three live tables contains an orphan.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>4. Part 3 -- Design the Foreign Keys</summary>
    <div class="card-body">

      <p>No code this time. For every table, say what its foreign key should be, what should happen when the parent is deleted, and what currently stands in the way. The migrations that add the constraints get written later, from this document.</p>
      <p>Five steps, in order.</p>

      <h3>Step 1. Start from your Phase 2 table</h3>
      <p>Your Phase 2 report already lists 38 relationships with their columns, their targets, whether the Rails model describes them correctly, and how many orphans each has. That is the input. This part adds a decision to each row.</p>

      <h3>Step 2. Decide four things per relationship</h3>
      <ul>
        <li><strong>Is this a real relationship?</strong> Some are legacy. <code>markets</code> has no code writing to it, <code>users.market_id</code> is empty in all 795 rows, <code>profiles.market_id</code> is empty in 86%. A dead column does not need a constraint.</li>
        <li><strong>What does the column reference?</strong> Table and column. Usually an <code>id</code>, but not always: <code>metric_selections.metric_number</code> matches on text, and <code>contract_terms</code> uses <code>users_id</code> rather than <code>user_id</code>.</li>
        <li><strong>What happens when the parent is deleted?</strong> Step 3.</li>
        <li><strong>Should the column allow NULL?</strong> A required link is a different constraint from an optional one, and <code>sales_slips.vendor_id</code> being 95% empty tells you which kind it is.</li>
      </ul>

      <h3>Step 3. Choose the on-delete behavior for each</h3>
      <table>
        <thead><tr><th>Behavior</th><th>What happens</th><th>When it fits</th></tr></thead>
        <tbody>
          <tr><td><code>RESTRICT</code></td><td>The delete is refused while children exist</td><td>Data you must not lose silently. A profile with sales slips under it.</td></tr>
          <tr><td><code>CASCADE</code></td><td>The children are deleted too</td><td>Rows that have no meaning without their parent. Link table rows, for instance.</td></tr>
          <tr><td><code>SET NULL</code></td><td>The child's link column is emptied</td><td>Optional links, where the child survives fine without the parent.</td></tr>
        </tbody>
      </table>
      <p>Where the choice is a real argument, record the reasoning. <code>CASCADE</code> on an instrument table means deleting one profile silently removes years of a market's sales history; <code>RESTRICT</code> means the application has to handle the refusal, which is more code but no silent loss. Also say how your design changes if deletes become soft deletes, since your Phase 2 report recommends them.</p>

      <h3>Step 4. Record what blocks each one</h3>
      <p>A foreign key cannot be added while orphan rows exist; the migration fails. For each relationship, note what has to happen first:</p>
      <ul>
        <li><strong>Orphans remaining</strong> after Parts 1 and 2, with today's count.</li>
        <li><strong>Whether the column is indexed.</strong> 24 of the 38 link columns have no index, and adding one to a large table briefly locks it.</li>
        <li><strong>Whether the Rails model matches.</strong> Seven associations name columns that do not exist.</li>
        <li><strong>Suggested order.</strong> Which tables could take their constraint today, and which have to wait.</li>
      </ul>

      <h3>Step 5. Write the report</h3>
      <p>Write it as <code>foreign_key_design_report.md</code> in the directory you created in Phase 2. The report file goes <strong>inside</strong> that directory, not loose at the root of <code>wiscurds/</code>:</p>
      <pre><code>wiscurds/
└──&nbsp;admin_dashboard_reports/
&nbsp;&nbsp;&nbsp;&nbsp;├──&nbsp;database_current_state_report.md
&nbsp;&nbsp;&nbsp;&nbsp;└──&nbsp;foreign_key_design_report.md</code></pre>
      <p>So the full path is <code>wiscurds/admin_dashboard_reports/foreign_key_design_report.md</code>.</p>

      <p>Use this template:</p>
      <pre class="pre-scroll"><code># Foreign Key Design and Phase 3 Cleanup

**Authors:** [Name], [Name]
**Program:** WISCURDS | **Phase:** 3 -- Data Cleaning and Feature Integration
**Date:** [Date]

## 1. What We Changed

[A short record of Parts 1 and 2, so a reader can see the state of the
database before and after this phase without opening three merge
requests.]

| Change | Rows before | Rows moved or removed | Rows after |
| --- | --- | --- | --- |
| Empty user rows deleted |  |  |  |
| Untyped accounts archived |  |  |  |
| Orphaned profiles archived |  |  |  |
| Orphaned sales slips archived |  |  |  |
| Orphaned visitor counts archived |  |  |  |

[Then: the new orphans Part 1 created, and anything that did not go as
planned.]

## 2. Where the Archived Data Went

[The four archive tables, what each holds, and how someone would
restore a row if they had to.]

## 3. Foreign Key Design

[One row per relationship. This is the heart of the report.]

| From table | Column | References | On delete | NULL allowed | Orphans left | Indexed | Model correct | Can add now? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

### 3.1 Reasoning for the Difficult Ones

[Not every row above needs an explanation, but some do. For each
relationship where the on-delete choice was a real decision, give the
argument in two or three sentences: what you chose, what you rejected,
and what it costs.]

### 3.2 Relationships We Recommend Dropping

[Columns that should not get a constraint because the relationship
itself is legacy. Name the evidence: empty columns, no code writing to
them, no rows.]

## 4. What Has to Happen First

[The order in which these constraints could actually be added, and what
blocks each stage.]

### 4.1 Could Be Added Today

[Relationships with zero orphans and a working index.]

### 4.2 Blocked on Cleanup

[Relationships with orphans remaining, with the count and what would
have to be done about them.]

### 4.3 Blocked on Code Changes

[Relationships where a model association or a controller would break.
Name the file.]

## 5. Soft Deletes

[How this design changes if deletes become soft deletes. Whether you
would still recommend the same on-delete behavior.]

## 6. Open Questions

[Anything you could not resolve. Number them.]</code></pre>

      <p><strong>Done when:</strong> every relationship from your Phase 2 table has a decision, and the ones that could be constrained today are separated from the ones that cannot.</p>

    </div>
  </details>

  <details class="task-card">
    <summary>5. Submit</summary>
    <div class="card-body">

      <p>Three merge requests, one per part, into <code>dev</code> in <code>farmers-coalition</code>. Open each one as that part finishes rather than saving all three for the end, because Part 2 should not start until Part 1 is merged.</p>

      <h3>What Every Merge Request Needs</h3>
      <ul>
        <li><strong>The before and after numbers</strong>, with the query label from <code>queries_used.sql</code> that produced each one.</li>
        <li><strong>What the migration does, in plain sentences.</strong> A reviewer should understand the change without reading the SQL, then read the SQL to confirm it does that.</li>
        <li><strong>Whether it is reversible</strong>, and confirmation that you tested the rollback.</li>
        <li><strong>What it affects downstream.</strong> Especially for Part 1, where orphan counts go up on purpose.</li>
        <li>Both of you named, and <strong>Abanish</strong> assigned as reviewer.</li>
      </ul>

      <h3>Read Your Own Diff First</h3>
      <p>Open the <strong>Changes</strong> tab and read every line, both of you. On a destructive migration this is not a formality. Check the <code>WHERE</code> clause in particular: a <code>DELETE</code> with a condition that is subtly wider than you meant is the single most expensive mistake available in this phase, and it looks completely normal in a diff unless someone is actually reading it.</p>

      <h3>Before You Run Anything on a Shared Database</h3>
      <p>Say in the channel when you are about to run a destructive migration against the dummy database, so that the other team is not investigating the same tables at that moment and wondering why their counts moved.</p>

      <p><strong>Done when:</strong> three merge requests are open or merged, each with its numbers, and the foreign key report is in <code>wiscurds/admin_dashboard_reports/</code>.</p>

    </div>
  </details>

</div>
