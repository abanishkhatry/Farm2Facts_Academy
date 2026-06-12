---
layout: default
title: "Task 1 Guide"
permalink: /taskList/task1/
---

# Task 1 Guide

**Sprint:** Welcome to the Barn | **Weeks:** 1 & 2

---

<div class="task-card-grid">

  <div class="task-card">
    <p class="card-title">1. Onboarding</p>
    <div class="card-body">

      <details>
        <summary>1.1 Get the Repos Running Locally</summary>
        <div class="section-body">
          <p>Start by reading through the <a href="{{ site.baseurl }}/STUDENT_ONBOARDING_PLAN">Student Onboarding Plan</a> to understand the program structure and the two repositories you will be working with. Then set up each repo locally.</p>
          <h3>a. Frontend Setup</h3>
          <p>Refer to <a href="{{ site.baseurl }}/docs/guides/FRONTEND_GUIDE">FRONTEND_GUIDE.md</a> for step-by-step instructions to clone, install dependencies, and run the Vue 3 frontend locally.</p>
          <h3>b. Backend Setup</h3>
          <p>Refer to <a href="{{ site.baseurl }}/docs/guides/BACKEND_GUIDE">BACKEND_GUIDE.md</a> for step-by-step instructions to clone, configure the database connection, and run the Rails 6.1 backend locally.</p>
        </div>
      </details>

      <details>
        <summary>1.2 Open Your Feature Branch</summary>
        <div class="section-body">
          <p>Now that you have the repos running locally, you will set up your working branch for this assignment.</p>
          <h3>a. Branch off dev in the frontend repo</h3>
          <p>All work for this assignment happens in the <strong>frontend repo</strong>. Open a terminal in that repo and create your branch from <code>dev</code>, following the <a href="{{ site.baseurl }}/docs/guides/#git-workflow-reference">branching strategy</a>:</p>
          <pre><code>git checkout dev

git pull
git checkout -b feat/[firstName]_task1</code></pre>
<p>Replace <code>[firstName]</code> with your actual first name. Example: <code>feat/abanish_task1</code>.</p>
<h3>b. Create your assignment directory</h3>
<p>Inside the frontend repo, create the following directory structure:</p>
<pre><code>task1_laser/
laser_[firstName]/</code></pre>
<p>Replace <code>[firstName]</code> with your first name. All files you produce for this assignment go inside <code>laser\_[firstName]/</code>. That includes:</p>
<ul>
<li>Your Claude Code 101 completion certificate (PDF)</li>
<li>Your F2F article response (<code>f2f_article_response.md</code>)</li>
<li>Your codebase understanding report (<code>codebase_overview.md</code>)</li>
</ul>
</div>
</details>

      <details>
        <summary>1.3 Codebase Understanding Report</summary>
        <div class="section-body">
          <p>Before writing any code, you need to build a basic map of the frontend codebase. You will use Claude Code to navigate each of the directories listed below under <code>src/views/</code>, read what is inside, and write a short description of what the folder contains and why it exists.</p>
          <p>You do not need to understand every file in detail. The goal is to know what each folder is responsible for at a high level -- what feature or screen it supports, and what kind of code lives there.</p>
          <h3>Directories to cover</h3>
          <p>Navigate to each of the following folders inside <code>src/views/</code> and write a description for each:</p>
          <ol>
            <li><code>DownloadDocuments</code></li>
            <li><code>LandingPage</code></li>
            <li><code>MarketOrg</code></li>
            <li><code>MemberResources</code></li>
            <li><code>SelectMetrics</code></li>
            <li><code>Analysis</code> -- overview only, do not dive into <code>DataAnalysis</code>, <code>GraphsView</code>, <code>InfographicsView</code>, or <code>Reports</code></li>
            <li><code>Instrument</code> -- overview only, do not describe individual sub-folders</li>
            <li><code>Instrument_MarketOrg</code> -- overview only, do not describe individual sub-folders</li>
            <li><code>Profiles</code> -- overview only, do not describe individual sub-directories</li>
            <li><code>Users</code> -- overview only, do not describe individual sub-directories</li>
          </ol>
          <h3>How to do this with Claude Code</h3>
          <p>Open Claude Code in the root of the frontend repo. For each folder, ask Claude something like:</p>
          <pre><code>What does src/views/DownloadDocuments do? Give me a brief overview of what files are in this folder and what feature it supports.</code></pre>
          <p>Use what Claude tells you as the basis for your own description. Write it in your own words -- do not paste Claude's response directly.</p>
          <h3>Output</h3>
          <p>Save your report as <code>codebase_overview.md</code> inside your <code>laser_[firstName]/</code> directory. Use the template below.</p>
          <pre><code># Frontend Codebase Overview

**Name:** [Your Name]
**Date:** [Date]

---

## DownloadDocuments

**Contains:** [What files or components are in this folder]

**Role:** [What this view does and why it exists in the app]

---

## LandingPage

**Contains:** [What files or components are in this folder]

**Role:** [What this view does and why it exists in the app]

---

## MarketOrg

**Contains:** [What files or components are in this folder]

**Role:** [What this view does and why it exists in the app]

---

## MemberResources

**Contains:** [What files or components are in this folder]

**Role:** [What this view does and why it exists in the app]

---

## SelectMetrics

**Contains:** [What files or components are in this folder]

**Role:** [What this view does and why it exists in the app]

---

## Analysis

**Contains:** [Top-level files and sub-folder names only]

**Role:** [What this section of the app handles at a high level]

---

## Instrument

**Contains:** [Top-level files and sub-folder names only]

**Role:** [What this section of the app handles at a high level]

---

## Instrument_MarketOrg

**Contains:** [Top-level files and sub-folder names only]

**Role:** [What this section of the app handles at a high level]

---

## Profiles

**Contains:** [Top-level files and sub-folder names only]

**Role:** [What this section of the app handles at a high level]

---

## Users

**Contains:** [Top-level files and sub-folder names only]

**Role:** [What this section of the app handles at a high level]</code></pre>
</div>
</details>

    </div>

  </div>

  <details class="task-card">
    <summary>2. Claude Code 101</summary>
    <div class="card-body">
      <p>Work through Anthropic's Claude Code 101 course to get familiar with the CLI tool you will use throughout the program. This covers the core workflow: opening a project, running commands, and understanding how the agent reads and edits code.</p>
      <p><a href="https://anthropic.skilljar.com/claude-code-101/" target="_blank" rel="noopener noreferrer">Claude Code 101 -- Anthropic Skill Jar</a></p>
      <p>Completion is counted when you are able to show the completion certificate provided by Anthropic at the end of the Claude 101 course.</p>
    </div>
  </details>

  <details class="task-card">
    <summary>3. The F2F Article</summary>
    <div class="card-body">
      <p>Read the following article to understand the broader context of the Farm2Facts project -- what it is, who it serves, and why it matters.</p>
      <p><a href="{{ site.baseurl }}/assets/J6_Ledesma_Sustainability_2_2021.pdf" target="_blank" rel="noopener noreferrer">Citizen Scientist: Farm 2 Facts Supporting Farmers Markets (Ledesma et al., 2021)</a></p>
      <h3>Assignment</h3>
      <p>After reading the article, write a short response (2-3 paragraphs) addressing all three of the following:</p>
      <ol>
        <li>What problem does F2F solve for farmers market managers, and why did that problem exist before F2F was created?</li>
        <li>Pick one case study from the article (South Milwaukee Downtown Market, Hope and Main, Brown Deer, or ACEFM). What data did F2F collect for that market, and what decision or outcome did that data support?</li>
        <li>As a developer on this project, what part of the F2F system would you most want to improve or build on, and why?</li>
      </ol>
      <h3>Response Template</h3>
      <p>Create a file named <code>f2f_article_response.md</code> inside your <code>laser_[firstName]/</code> directory. Copy the template below into it and fill in each section.</p>
      <pre><code># F2F Article Response

**Name:** [Your Name]
**Date:** [Date]

## Question 1: The Problem F2F Solves

[Describe the problem farmers market managers faced before F2F existed.
What information were they missing? Why did that gap matter?
2-4 sentences.]

## Question 2: Case Study

**Case study chosen:** [South Milwaukee Downtown Market / Hope and Main / Brown Deer / ACEFM]

[Describe what data F2F collected for this market and what decision or
outcome that data supported. Be specific -- name the metric or program
from the article. 2-4 sentences.]

## Question 3: Developer Perspective

[Identify one part of the F2F system you would most want to improve or
build on. Explain why -- connect it to something you read in the article.
2-4 sentences.]</code></pre>
</div>

  </details>

  <details class="task-card">
    <summary>4. PR Creation &amp; Submission</summary>
    <div class="card-body">
      <p>Opening a Pull Request is the final deliverable for this assignment. Your work is not considered submitted until a PR is open, fully filled out, and assigned for review. The PR is how your supervisor reviews everything you built -- the branch, the directory structure, and all three files inside it.</p>

      <h3>Before you open the PR</h3>
      <p>Confirm your feature branch matches the expected structure:</p>
      <pre><code>feat/[firstName]_task1/

task1*laser/
laser*[firstName]/
codebase*overview.md
claude_code_101_certificate.pdf
f2f_article_response.md</code></pre>
<ul>
<li>[ ] Branch is named <code>feat/[firstName]\_task1</code> and was created from <code>dev</code></li>
<li>[ ] <code>task1_laser/laser*[firstName]/</code> directory exists in the frontend repo</li>
<li>[ ] <code>codebase_overview.md</code> is present and covers all 10 directories</li>
<li>[ ] <code>claude_code_101_certificate.pdf</code> is present</li>
<li>[ ] <code>f2f_article_response.md</code> is present and addresses all 3 questions</li>
</ul>

      <h3>Opening the PR</h3>
      <p>Once all items above are checked off, push your branch and open a PR from <code>feat/[firstName]_task1</code> into <code>dev</code>. Follow the <a href="{{ site.baseurl }}/docs/guides/#pull-requests">PR template in the Workflow Guide</a> for the title format, description fields, and reviewer assignment. Fill out every field -- an incomplete description delays review for everyone.</p>
      <p>Your PR description should make it clear what this assignment covers: the codebase overview, the Claude Code 101 certification, and the F2F article response. Link the issue if one was assigned to you.</p>
    </div>
  </details>

</div>
