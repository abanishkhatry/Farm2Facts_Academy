---
layout: default
title: "Task 2.1 Guide"
permalink: /taskList/task2_1/
---

# Task 2.1 Guide

**Sprint:** Cheese Curds & Code | **Weeks:** 3, 4 & 5 | **Sub-task:** 1 -- APIs for Beginners

---

<div class="task-card-grid">

  <div class="task-card">
    <p class="card-title">1. Setup</p>
    <div class="card-body">

      <details>
        <summary>1.1 Open Your Feature Branch</summary>
        <div class="section-body">
          <p>All work for this sub-task happens in the <strong>frontend repo</strong>. Create your branch from <code>dev</code>:</p>
          <pre><code>git checkout dev
git pull
git checkout -b feat/[firstName]_task2</code></pre>
          <p>Replace <code>[firstName]</code> with your actual first name. Example: <code>feat/abanish_task2</code>.</p>
        </div>
      </details>

      <details>
        <summary>1.2 Create Your Assignment Directory</summary>
        <div class="section-body">
          <p>Inside the frontend repo, create the following directory structure:</p>
          <pre><code>task2_laser/
└── laser_[firstName]/
    ├── assignment1_api_detective.md
    ├── assignment2_postman_explorer.md
    ├── assignment3_soil_temperature.md
    └── assignment4_summary.md</code></pre>
          <p>From the root, create <code>task2_laser/</code> first, then <code>laser_[firstName]/</code> inside it. All four deliverable files go inside <code>laser_[firstName]/</code>.</p>
        </div>
      </details>

      <details>
        <summary>1.3 Committing Your Work</summary>
        <div class="section-body">
          <p>Each assignment deliverable gets its own commit. Do not bundle everything into a single commit at the end.</p>
          <pre><code>git add &lt;file&gt;
git commit -m "Your commit message here"</code></pre>
          <h3>Expected commits for this sub-task</h3>
          <table>
            <thead>
              <tr><th>Deliverable</th><th>Commit message</th></tr>
            </thead>
            <tbody>
              <tr><td>Assignment 1</td><td><code>Add API detective browser exploration</code></td></tr>
              <tr><td>Assignment 2</td><td><code>Add Postman explorer responses and screenshots</code></td></tr>
              <tr><td>Assignment 3</td><td><code>Add soil temperature deep dive findings</code></td></tr>
              <tr><td>Assignment 4</td><td><code>Add API summary and use case proposal</code></td></tr>
            </tbody>
          </table>
        </div>
      </details>

    </div>
  </div>

  <details class="task-card">
    <summary>2. Concepts &amp; Learning Resources</summary>
    <div class="card-body">
      <p>Before starting the assignments, work through these resources in order. They build the vocabulary and mental model you will need for everything that follows.</p>

      <h3>What is an API?</h3>
      <p>An API (Application Programming Interface) is a defined way for one piece of software to talk to another. Think of it like a restaurant: you are the customer (your app), the kitchen is the server (the data source), and the waiter is the API -- taking your order and bringing back exactly what you asked for.</p>
      <p>The Wisconet API -- and most modern APIs -- follow the <strong>REST</strong> style. REST APIs work over the internet using standard URLs and return data in a format called JSON.</p>

      <h3>Anatomy of a URL</h3>
      <pre><code>https://api.wisconet.wisc.edu/api/v1/stations/HNCK/measures?fields=5min_soil_temp_f_avg@4in&amp;start_time=1719619200&amp;end_time=1719705600</code></pre>
      <table>
        <thead><tr><th>Part</th><th>What it means</th></tr></thead>
        <tbody>
          <tr><td><code>https://</code></td><td>Protocol -- always https for secure APIs</td></tr>
          <tr><td><code>api.wisconet.wisc.edu</code></td><td>Base URL -- the server's address</td></tr>
          <tr><td><code>/api/v1/stations/HNCK</code></td><td>Endpoint path -- which resource and station</td></tr>
          <tr><td><code>/measures</code></td><td>Action -- what data to retrieve</td></tr>
          <tr><td><code>?fields=…</code></td><td>Query parameters -- filters that customize the response</td></tr>
        </tbody>
      </table>

      <h3>HTTP Status Codes</h3>
      <table>
        <thead><tr><th>Code</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr><td><code>200 OK</code></td><td>Success -- data returned as expected</td></tr>
          <tr><td><code>404 Not Found</code></td><td>The endpoint or resource doesn't exist</td></tr>
          <tr><td><code>422 Unprocessable</code></td><td>Your parameters were invalid</td></tr>
          <tr><td><code>500 Internal Server Error</code></td><td>Something broke on the server side</td></tr>
        </tbody>
      </table>

      <h3>Required Resources -- Work through these in order</h3>
      <ol>
        <li><a href="https://www.youtube.com/watch?v=s7wmiS2mSXY" target="_blank" rel="noopener noreferrer">What is an API? (MuleSoft, 5 min)</a> -- watch this first</li>
        <li><a href="https://www.youtube.com/watch?v=GZvSYJDk-us" target="_blank" rel="noopener noreferrer">APIs for Beginners -- Full Course (freeCodeCamp)</a> -- watch the first 45 minutes at minimum</li>
        <li><a href="https://academy.postman.com/path/api-fundamentals-student-expert" target="_blank" rel="noopener noreferrer">Postman API Fundamentals Student Expert</a> -- complete the first 3 modules</li>
        <li><a href="https://restapitutorial.com" target="_blank" rel="noopener noreferrer">REST API Tutorial</a> -- read "What is REST" and "HTTP Methods"</li>
        <li><a href="https://www.w3schools.com/js/js_json_intro.asp" target="_blank" rel="noopener noreferrer">JSON Introduction (W3Schools)</a> -- focus on objects, arrays, and data types</li>
        <li><a href="https://api.wisconet.wisc.edu/docs" target="_blank" rel="noopener noreferrer">Wisconet API Documentation</a> -- explore this after resources 1--3</li>
      </ol>
    </div>
  </details>

  <details class="task-card">
    <summary>3. Assignment 1 -- API Detective</summary>
    <div class="card-body">
      <p><strong>Duration:</strong> ~30 minutes &nbsp;|&nbsp; <strong>Difficulty:</strong> Beginner</p>
      <p>Explore the Wisconet API using only your browser -- no tools needed. The goal is to understand what a real API response looks like.</p>

      <h3>Instructions</h3>
      <ul>
        <li>Open your browser and go to: <code>https://api.wisconet.wisc.edu/api/v1/stations/</code></li>
        <li>(Optional) Install the <strong>JSON Viewer</strong> Chrome extension for colour-coded output</li>
        <li>Scroll through the list and find the station closest to your home county. Note its <strong>station_id</strong> (4-letter code)</li>
        <li>Build a custom URL: <code>https://api.wisconet.wisc.edu/api/v1/stations/XXXX</code> (replace XXXX with your station_id)</li>
        <li>Navigate to that URL and examine the response</li>
        <li>Fetch the latest measures: <code>https://api.wisconet.wisc.edu/api/v1/stations/XXXX/latest_measures</code></li>
      </ul>

      <h3>Deliverable</h3>
      <p>Save your answers as <code>assignment1_api_detective.md</code> inside your <code>laser_[firstName]/</code> directory. Answer all seven questions:</p>
      <ol>
        <li>What is the station_id of the station you chose, and what county is it in?</li>
        <li>What are the latitude and longitude of that station?</li>
        <li>How many total fields (measures) were returned by the <code>latest_measures</code> endpoint?</li>
        <li>Find the current air temperature reading. What field name is it stored under?</li>
        <li>Does this station have soil temperature data? If yes, at how many depths?</li>
        <li>What does the <code>collection_frequency</code> field tell you about a measure?</li>
        <li>In your own words: what is the difference between the station list endpoint and the <code>latest_measures</code> endpoint?</li>
      </ol>
    </div>
  </details>

  <details class="task-card">
    <summary>4. Assignment 2 -- Postman Explorer</summary>
    <div class="card-body">
      <p><strong>Duration:</strong> ~45 minutes &nbsp;|&nbsp; <strong>Difficulty:</strong> Beginner</p>
      <p>Get comfortable using Postman to make API requests, add parameters, and read responses. Warm up on a practice API first, then move to Wisconet.</p>

      <h3>Setup</h3>
      <ul>
        <li>Download Postman Desktop at <a href="https://www.postman.com/downloads/" target="_blank" rel="noopener noreferrer">postman.com/downloads</a> (free)</li>
        <li>Create a free account and sign in</li>
        <li>Click <strong>New &rarr; HTTP Request</strong> and make sure <strong>GET</strong> is selected</li>
      </ul>

      <h3>Part A -- Warm Up with JSONPlaceholder</h3>
      <p>JSONPlaceholder is a free public practice API that always returns fake data. You cannot break anything.</p>
      <ul>
        <li>Set the URL to <code>https://jsonplaceholder.typicode.com/users</code> -- click Send. Note the status code. How many users are returned?</li>
        <li>Change the URL to <code>/users/5</code>. What is that user's name and city?</li>
        <li>Try <code>/posts?userId=3</code> using the Params tab (KEY: <code>userId</code>, VALUE: <code>3</code>). How many posts does user 3 have?</li>
      </ul>

      <h3>Part B -- Explore Wisconet</h3>
      <ul>
        <li>Get all stations: <code>https://api.wisconet.wisc.edu/api/v1/stations/</code></li>
        <li>Get the station detail for <strong>ALTN</strong> (Arlington). What is its elevation?</li>
        <li>Get ALTN's latest measures. How long did the response take (shown in Postman)?</li>
        <li>Save all three requests as a Postman Collection named <strong>"Wisconet Exploration"</strong></li>
      </ul>

      <h3>Deliverable</h3>
      <p>Save your answers as <code>assignment2_postman_explorer.md</code> inside your <code>laser_[firstName]/</code> directory. Include:</p>
      <ul>
        <li>Screenshot of your Postman Collection with all 3 saved requests (embed as an image or describe)</li>
        <li>Status code for each of the three requests</li>
        <li>What happens if you use a station_id that doesn't exist (e.g., <code>/stations/XXXX</code>)?</li>
        <li>In 2--3 sentences: what is the difference between a <strong>path parameter</strong> (like <code>/ALTN/</code>) and a <strong>query parameter</strong> (like <code>?fields=...</code>)?</li>
      </ul>
    </div>
  </details>

  <details class="task-card">
    <summary>5. Assignment 3 -- Soil Temperature Deep Dive</summary>
    <div class="card-body">
      <p><strong>Duration:</strong> ~60 minutes &nbsp;|&nbsp; <strong>Difficulty:</strong> Intermediate</p>
      <p>Use the Wisconet measures endpoint to extract real soil temperature data across different depths and stations.</p>

      <h3>Background: Field Name Format</h3>
      <p>Field names follow this pattern: <code>{frequency}_{measure}_{units}_{aggregation}@{depth}</code></p>
      <p>Examples: <code>5min_soil_temp_f_avg@4in</code>, <code>daily_soil_temp_f_max@8in</code></p>

      <h3>Instructions</h3>
      <ul>
        <li>Go to <a href="https://www.unixtimestamp.com" target="_blank" rel="noopener noreferrer">unixtimestamp.com</a>. Convert yesterday's date at 12:00 AM to a Unix timestamp -- this is your <code>start_time</code></li>
        <li>Convert today's date at 12:00 AM -- this is your <code>end_time</code></li>
        <li>In Postman, build a request to <code>https://api.wisconet.wisc.edu/api/v1/stations/HNCK/measures</code> with these Params:</li>
      </ul>
      <table>
        <thead><tr><th>KEY</th><th>VALUE</th></tr></thead>
        <tbody>
          <tr><td><code>fields</code></td><td><code>5min_soil_temp_f_avg@2in,5min_soil_temp_f_avg@4in,5min_soil_temp_f_avg@8in,5min_soil_temp_f_avg@20in,5min_soil_temp_f_avg@40in</code></td></tr>
          <tr><td><code>start_time</code></td><td>(your Unix timestamp for yesterday 12 AM)</td></tr>
          <tr><td><code>end_time</code></td><td>(your Unix timestamp for today 12 AM)</td></tr>
        </tbody>
      </table>
      <ul>
        <li>Repeat the same request for a second station of your choice</li>
        <li>Try daily summary fields: change <code>5min</code> to <code>daily</code> and <code>avg</code> to <code>max</code>. What changes?</li>
      </ul>

      <h3>Deliverable</h3>
      <p>Save your answers as <code>assignment3_soil_temperature.md</code> inside your <code>laser_[firstName]/</code> directory. Answer all five questions:</p>
      <ol>
        <li>What were the soil temperature readings at 2in, 8in, and 40in depth for HNCK? What pattern do you notice as depth increases?</li>
        <li>Compare your two stations: which has warmer soil at 4in depth? Can you hypothesize why?</li>
        <li>How many 5-minute readings should a 24-hour window produce? (Hint: 60/5 &times; 24 = ?) Does your count match?</li>
        <li>What does the <code>preceding_value</code> field represent in each observation?</li>
        <li>If you wanted hourly instead of 5-minute data, what would you change in the field name?</li>
      </ol>
    </div>
  </details>

  <details class="task-card">
    <summary>6. Assignment 4 -- Document Your Understanding</summary>
    <div class="card-body">
      <p><strong>Duration:</strong> ~30 minutes &nbsp;|&nbsp; <strong>Difficulty:</strong> Reflection</p>
      <p>Consolidate everything into a short written summary. This prepares you for Module 2, where you will write code to automate data extraction.</p>

      <h3>Part A -- API Summary (1 page max)</h3>
      <p>Write a plain-English summary answering:</p>
      <ul>
        <li>What is the Wisconet API? What kind of data does it provide?</li>
        <li>How is the API structured? (versions, endpoint categories, field naming convention)</li>
        <li>What does a typical request to get soil temperature data look like? (Describe in words -- no code needed)</li>
        <li>What limitations did you notice? (e.g., which stations have soil sensors, date formats, data coverage)</li>
      </ul>

      <h3>Part B -- Draw the Request-Response Flow</h3>
      <p>On paper or in any drawing tool (even Google Slides), draw a simple diagram showing what happens when you fetch soil temperature data. Include your browser/Postman, the API server, the database, and the JSON response coming back. Label each arrow with what is being sent or returned.</p>

      <h3>Part C -- Propose a Use Case (2--3 sentences)</h3>
      <p>If you were building a tool for Wisconsin farmers using this API, what would it do? Who is the user, what problem does it solve, and which API endpoint(s) would it use?</p>

      <h3>Deliverable</h3>
      <p>Save your response as <code>assignment4_summary.md</code> inside your <code>laser_[firstName]/</code> directory. Include Part A and Part C as written text. For Part B, either embed an image or describe the diagram in words.</p>
    </div>
  </details>

  <details class="task-card">
    <summary>7. PR Creation &amp; Submission</summary>
    <div class="card-body">
      <p>Your work is not considered submitted until a Merge Request is open, fully filled out, and assigned for review.</p>

      <h3>Before you open the MR</h3>
      <p>Confirm your feature branch matches the expected structure:</p>
      <pre><code>branch: feat/[firstName]_task2

task2_laser/
└── laser_[firstName]/
    ├── assignment1_api_detective.md
    ├── assignment2_postman_explorer.md
    ├── assignment3_soil_temperature.md
    └── assignment4_summary.md</code></pre>
      <ul>
        <li>[ ] Branch is named <code>feat/[firstName]_task2</code> and was created from <code>dev</code></li>
        <li>[ ] <code>task2_laser/laser_[firstName]/</code> directory exists in the frontend repo</li>
        <li>[ ] All 4 assignment files are present and answer every question</li>
        <li>[ ] Each deliverable has its own commit with a descriptive message</li>
      </ul>

      <h3>Opening the Merge Request on GitLab</h3>
      <ol>
        <li>In the left sidebar, go to <strong>Code</strong> &rarr; <strong>Merge requests</strong></li>
        <li>Click <strong>New merge request</strong></li>
        <li>Set <strong>Source branch</strong> to <code>feat/[firstName]_task2</code></li>
        <li>Set <strong>Target branch</strong> to <code>dev</code></li>
        <li>Click <strong>Compare branches and continue</strong></li>
        <li>Fill out the title and description using the <a href="{{ site.baseurl }}/docs/guides/#pull-requests">Pull Requests guide</a> -- fill out every field before submitting</li>
      </ol>
    </div>
  </details>

  <details class="task-card">
    <summary>What You Learned</summary>
    <div class="card-body">
      <p>Skills and concepts from this sub-task that carry forward into Module 2 and beyond.</p>
      <div class="skills-grid">
        <div>
          <p class="skill-group-label">API Fundamentals</p>
          <div class="skill-tags">
            <span class="skill-tag">REST architecture</span>
            <span class="skill-tag">HTTP methods</span>
            <span class="skill-tag">Status codes</span>
          </div>
        </div>
        <div>
          <p class="skill-group-label">JSON</p>
          <div class="skill-tags">
            <span class="skill-tag">Objects &amp; arrays</span>
            <span class="skill-tag">Key-value pairs</span>
            <span class="skill-tag">Reading responses</span>
          </div>
        </div>
        <div>
          <p class="skill-group-label">URL Structure</p>
          <div class="skill-tags">
            <span class="skill-tag">Base URL</span>
            <span class="skill-tag">Path parameters</span>
            <span class="skill-tag">Query parameters</span>
          </div>
        </div>
        <div>
          <p class="skill-group-label">Tooling</p>
          <div class="skill-tags">
            <span class="skill-tag">Browser as API client</span>
            <span class="skill-tag">Postman requests</span>
            <span class="skill-tag">Postman Collections</span>
          </div>
        </div>
        <div>
          <p class="skill-group-label">Wisconet API</p>
          <div class="skill-tags">
            <span class="skill-tag">Station endpoints</span>
            <span class="skill-tag">Field naming convention</span>
            <span class="skill-tag">Unix timestamps</span>
          </div>
        </div>
      </div>
    </div>
  </details>

</div>
