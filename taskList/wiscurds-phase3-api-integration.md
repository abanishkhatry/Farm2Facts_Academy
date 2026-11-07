---
layout: default
title: "Phase 3 Task Guide -- Wisconet API"
permalink: /taskList/wiscurds-phase3-api/
---

# Phase 3 Task Guide -- Project B: Wisconet API Integration

**Program:** WISCURDS | **Phase:** 3 -- Data Cleaning and Feature Integration | **Team:** Soham

---

This is the task companion to the [Phase 3 milestone card]({{ site.baseurl }}/taskList/wiscurds-key-milestones#phase-3). That card describes what the phase covers; this guide is what you actually do, in order.

Phase 2 was the investigation. This is the build. By the end of this phase, a market opening the **WISCONET** tab on its Market Profile sees the soil temperature and soil moisture from the Wisconet station nearest to it.

The phase has three parts:

1. **Resolve a market to a station.** Read the market's coordinates, then find the closest station to it.
2. **Pull the soil metrics.** Call Wisconet for that station and expose the result to the frontend.
3. **Show it in the WISCONET tab.** Fill in the placeholder you built in Phase 2.

**The Phase 2 frontend branch was deliberately left unmerged.** The empty WISCONET tab is still sitting on `feat-wis-p2-api-integration`, waiting for this. You carry on committing to that same branch rather than opening a new one, and the merge request you already have open becomes the merge request for this work too.

**Wisconet has no "nearest station" lookup.** This is the thing to understand before you start. The API will not take a zip code, a county or a pair of coordinates and tell you which station to use. It only answers questions about stations you name by their station id. Finding the right station is our job, and that is why Part 1 exists.

**Use an LLM or coding agent. We recommend it.** Distance calculations and HTTP clients are well-trodden ground and a good use of one. The usual rule holds: verify what it writes against a real response before you trust it, and never paste database credentials into a prompt.

Phase 3 assumes your [Phase 2 report]({{ site.baseurl }}/taskList/wiscurds-phase2-api/) is merged. Your section 6 recommendation is the starting point for Part 1, and if what you find now contradicts it, say so rather than quietly working around it.

<div class="task-card-grid">

  <details class="task-card">
    <summary>1. How Phase 3 Works</summary>
    <div class="card-body">

      <p>Two branches, two merge requests, across the two repositories. The parts are separated by <strong>commits</strong>, not by a branch each.</p>

      <h3>Two Branches, One Per Repository</h3>
      <table>
        <thead><tr><th>Repository</th><th>Branch</th><th>Holds</th></tr></thead>
        <tbody>
          <tr><td><code>farmers-coalition</code></td><td><code>feat-wis-p3-api-integration</code> (new, from <code>dev</code>)</td><td>Parts 1 and 2</td></tr>
          <tr><td><code>farm2facts-frontend</code></td><td><code>feat-wis-p2-api-integration</code> (already open)</td><td>Part 3</td></tr>
        </tbody>
      </table>
      <p>The frontend branch already exists and already has a merge request open. Check it out and keep going:</p>
      <pre><code>git checkout feat-wis-p2-api-integration
git pull</code></pre>
<p>Its merge request will now cover both the Phase 2 placeholder and the working tab, so update the description to say so.</p>
<p>The backend branch is new:</p>
<pre><code>git checkout dev
git pull
git checkout -b feat-wis-p3-api-integration</code></pre>
<p>One commit per finished piece of work, in the order this guide runs. You are both committing to the same two branches, so agree who is working where, and pull before you push.</p>

      <h3>What You Already Know About the API</h3>
      <p>From your Phase 2 investigation, confirmed against the live API. Everything below is verified and is yours to use rather than rediscover:</p>
      <ul>
        <li><strong>Base URL:</strong> <code>https://api.wisconet.wisc.edu</code>, with <code>/api/v1/</code> and <code>/api/v2/</code> both live. Use <strong>v2</strong>.</li>
        <li><strong>No authentication.</strong> No key, no token, no sign-up.</li>
        <li><strong><code>GET /api/v2/stations/</code></strong> returns every station as GeoJSON, including its coordinates, its <code>station_id</code>, its city and its county.</li>
        <li><strong><code>GET /api/v2/fields/</code></strong> lists every measure the network records.</li>
        <li><strong><code>GET /api/v2/stations/map</code></strong> is the one that returns readings. It takes <code>fieldlist</code> and <code>station_list</code>.</li>
        <li><strong><code>GET /api/v2/stations/{station_id}/latest</code> does not work.</strong> It returns <code>501 Not implemented</code>. Use the map endpoint instead.</li>
      </ul>

      <h3>Be a Good Citizen of Someone Else's API</h3>
      <p>Wisconet is a free public service run by the university, and we are a guest on it. Do not call it once per page load per visitor. Part 2 covers caching, and it is a requirement rather than an optimization.</p>

      <h3>Where This Runs</h3>
      <p>Against the dummy database, same as every phase so far. The Wisconet API itself is live and public, so the readings you get back are real.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>2. Part 1 -- Resolve a Market to a Station</summary>
    <div class="card-body">

      <p>Given a market profile, decide which Wisconet station is its station. Four steps.</p>

      <h3>Step 1. Pull the station list</h3>
      <p><code>GET https://api.wisconet.wisc.edu/api/v2/stations/</code> returns a GeoJSON <code>FeatureCollection</code> of around 80 stations. Each one looks like this:</p>
      <pre class="pre-scroll"><code>{
&nbsp;&nbsp;"type": "Feature",
&nbsp;&nbsp;"geometry": { "type": "Point", "coordinates": [-89.533302, 44.118801] },
&nbsp;&nbsp;"properties": {
&nbsp;&nbsp;&nbsp;&nbsp;"station_id": "HNCK",
&nbsp;&nbsp;&nbsp;&nbsp;"station_name": "Hancock",
&nbsp;&nbsp;&nbsp;&nbsp;"city": "Hancock",
&nbsp;&nbsp;&nbsp;&nbsp;"county": "Waushara County",
&nbsp;&nbsp;&nbsp;&nbsp;"region": "Central",
&nbsp;&nbsp;&nbsp;&nbsp;"elevation": 333.0,
&nbsp;&nbsp;&nbsp;&nbsp;"station_timezone": "US/Central"
&nbsp;&nbsp;}
}</code></pre>
<p><strong>GeoJSON coordinates are <code>[longitude, latitude]</code>, in that order.</strong> Reading them as latitude first puts every station in the wrong hemisphere, the code still runs, and the answers are quietly nonsense. Check this one twice.</p>
<p>The list changes rarely, so fetch it on a schedule rather than on demand. Whether you cache it or store it in a table is your call; say which you chose and why in the merge request.</p>

      <h3>Step 2. Get the market's coordinates</h3>
      <p>The <code>profiles</code> table carries <strong>latitude and longitude</strong>, so there is no geocoding step and no zip code lookup. Read the two columns straight off the profile and you have the market's position in the same form the stations use.</p>
      <p>Confirm the exact column names in the GUI before you write anything against them, then <strong>count how many market profiles actually have both values filled in</strong>. That number is how much of this feature works, and it belongs in the merge request. Count it now rather than reusing a Phase 2 figure, since Phase 3 changed the <code>users</code> and <code>profiles</code> tables.</p>
      <p>Look at the values too, not just the fill rate. Wisconsin sits near latitude 42 to 47 and longitude -87 to -93, so anything far outside that is wrong even though it is present: a zero, a swapped pair, or a positive longitude that puts the market in China. Treat those as missing rather than feeding them into Step 3.</p>

      <h3>Step 3. Find the nearest station</h3>
      <p>With a coordinate for the market and coordinates for every station, the nearest one is a distance calculation over a list of around 80. Use the haversine formula, which accounts for the curvature of the earth; at Wisconsin distances plain Pythagoras on latitude and longitude will usually agree, but not always, and it is not worth the argument.</p>
      <p>Store the result, including the <strong>distance</strong>. You will show that distance in Part 3, because a reading from eight miles away and a reading from ninety miles away are not the same claim, and the market should be able to tell which they are looking at.</p>

      <h3>Step 4. Handle the markets you cannot place</h3>
      <p>Whatever Step 2 counted, some profiles will have no coordinates or bad ones. A market with no location is a normal case here, not an error, and it has to resolve to a clean "we do not know where you are" rather than a crash or a silently wrong station.</p>
      <p>Decide what happens when the nearest station is implausibly far away, for example a market outside Wisconsin. Picking the nearest station regardless would hand a Canadian market a reading from Superior. Set a distance beyond which you return nothing, and say what you chose.</p>

      <p><strong>Done when:</strong> given a market profile, you can name its station and the distance to it, you know how many market profiles that works for, and the ones it does not work for return a clean no-answer.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>3. Part 2 -- Pull the Soil Metrics</summary>
    <div class="card-body">

      <p>Get the readings for a station and expose them to the frontend. Five steps.</p>

      <h3>Step 1. Choose the measures</h3>
      <p>Wisconet records soil temperature and soil moisture at five depths: <strong>5cm, 10cm, 20cm, 50cm and 100cm</strong>. Field names follow a fixed pattern:</p>
      <pre><code>60min_soil_temp_5cm_f_avg
60min_soil_moisture_5cm_m3m-3_avg</code></pre>
<p>Swap <code>60min</code> for <code>5min</code> or <code>daily</code>, swap the depth, and swap <code>avg</code> for <code>min</code> or <code>max</code>. Soil temperature comes in both <code>c</code> and <code>f</code>; use <code>f</code> for a US audience. Soil moisture is only in <code>m3m-3</code>, which is volumetric water content, so <code>0.05</code> means 5% water by volume.</p>
<p>Do not show all ten. Pick the shallow depths a grower would act on and say why you chose them.</p>

      <h3>Step 2. Call the map endpoint</h3>
      <p>A complete, working request:</p>
      <pre class="pre-scroll"><code>https://api.wisconet.wisc.edu/api/v2/stations/map?fieldlist=60min_soil_temp_5cm_f_avg,60min_soil_moisture_5cm_m3m-3_avg&amp;station_list=HNCK</code></pre>
      <p>It returns the station, and each requested field as an object with its unit and its observations:</p>
      <pre class="pre-scroll"><code>"60min_soil_temp_5cm_f_avg": {
&nbsp;&nbsp;"unitCode": "ud:degF",
&nbsp;&nbsp;"observations": [
&nbsp;&nbsp;&nbsp;&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"timestamp": "2026-11-07T03:00:00+00:00",
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"value": 44.6,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"qualityControl": "Z",
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"precedingValue": 45.5,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"precedingTime": "2026-11-07T02:00:00+00:00"
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;]
}</code></pre>
<p>Omit <code>station_list</code> and you get every station, which is how you would check coverage. Both <code>date</code> and the <code>aggregate_start</code> / <code>aggregate_end</code> pair are accepted if you want a range rather than the latest reading.</p>

      <h3>Step 3. Expect stations to be missing fields</h3>
      <p>Not every station has soil probes. Asking all stations for 5cm soil temperature returns 77 of the roughly 80, and <strong>the stations without it are simply absent from the response</strong> rather than present with a null.</p>
      <p>So the station nearest a market may not report soil at all, and your code has to notice an empty response rather than treat it as a reading of zero. Decide whether to fall back to the next-nearest station that does report soil, or to say nothing is available, and record the choice.</p>

      <h3>Step 4. Add an endpoint and cache it</h3>
      <p>Add one endpoint in <code>app/controllers/api/v1/</code>, following the patterns already there, that takes a profile and returns its station, the distance, and the readings. The frontend should not be calling Wisconet directly.</p>
      <p><strong>Cache the response.</strong> The readings update hourly, so there is no reason to call Wisconet more than once an hour per station, and several markets will share a station. Without a cache, a busy day means thousands of requests to a free university service for data that did not change.</p>

      <h3>Step 5. Fail quietly and visibly</h3>
      <p>Wisconet is outside our control, so assume it will be slow, down, or changed one day. Set a timeout, catch the failure, and return something the frontend can display as "readings unavailable." A third-party outage must never take down a Market Profile page, and it certainly must not take down the ones belonging to markets that have no station anyway.</p>

      <p><strong>Done when:</strong> one endpoint returns station, distance and readings for a profile, repeated calls hit the cache, a station with no soil data is handled, and Wisconet being unreachable produces a clean error rather than a broken page.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>4. Part 3 -- Show It in the WISCONET Tab</summary>
    <div class="card-body">

      <p>Fill in the placeholder tab from Phase 2, on the frontend branch you already have open. Four steps.</p>

      <h3>Step 1. Check out the branch you already have</h3>
      <pre><code>git checkout feat-wis-p2-api-integration
git pull</code></pre>
<p>Do not branch again. This is the branch holding the empty tab, and its merge request is the one that will deliver the finished feature.</p>

      <h3>Step 2. Show the readings</h3>
      <p>Soil temperature and soil moisture at the depths you chose, with their units, read from your own backend endpoint and not from Wisconet directly. Keep it plain: a few clearly labeled numbers beat a chart nobody asked for.</p>
      <p>Convert <code>m3m-3</code> into something a person reads without explanation. <code>0.05</code> shown as <code>5%</code> is kinder than <code>0.05 m3m-3</code>.</p>

      <h3>Step 3. Say where the reading came from</h3>
      <p>Every number on this tab was measured somewhere else, so the tab has to say where and when:</p>
      <ul>
        <li>The <strong>station name</strong> and its city or county.</li>
        <li>The <strong>distance</strong> from this market.</li>
        <li>The <strong>timestamp</strong> of the reading, in local time rather than the UTC the API returns.</li>
      </ul>
      <p>Without this, a market in Superior reading a Madison soil temperature has no way to know that is what happened.</p>

      <h3>Step 4. Handle the states that are not success</h3>
      <p>On current data most markets will land in one of these, so they are the main case rather than the edge case:</p>
      <ul>
        <li><strong>Loading.</strong> The request is in flight.</li>
        <li><strong>No coordinates for this market.</strong> Explain that we do not know where the market is, rather than showing an empty panel. If there is somewhere in the app to add it, say so.</li>
        <li><strong>No station near enough,</strong> or the nearest station reports no soil data.</li>
        <li><strong>Wisconet unavailable.</strong> Say the service is unavailable and that the reading is not gone.</li>
      </ul>
      <p>Then click through <strong>Summary</strong>, <strong>Management</strong>, <strong>Vendors</strong>, <strong>Accessibility</strong> and <strong>Community</strong> and confirm you did not break the tab row on your way in.</p>

      <p><strong>Done when:</strong> the WISCONET tab shows soil temperature and moisture with their station, distance and local timestamp; all four non-success states render properly; and the other tabs still work.</p>

    </div>

  </details>

  <details class="task-card">
    <summary>5. Submit</summary>
    <div class="card-body">

      <p>Two merge requests, both into <code>dev</code>.</p>
      <table>
        <thead><tr><th>Repository</th><th>Branch</th><th>Covers</th></tr></thead>
        <tbody>
          <tr><td><code>farmers-coalition</code></td><td><code>feat-wis-p3-api-integration</code></td><td>Station resolution and the metrics endpoint</td></tr>
          <tr><td><code>farm2facts-frontend</code></td><td><code>feat-wis-p2-api-integration</code></td><td>The Phase 2 placeholder and the working tab</td></tr>
        </tbody>
      </table>
      <p>The frontend one is already open. Update its title and description rather than closing it and opening another.</p>

      <h3>What Both Merge Requests Need</h3>
      <ul>
        <li><strong>How many market profiles this actually works for</strong>, as a number out of the total. This is the most important line in either description.</li>
        <li><strong>How you resolve a market to a station</strong>, and what happens when you cannot.</li>
        <li><strong>A screenshot</strong> of the working tab, for the frontend one, plus one of a market with no location so a reviewer can see that case too.</li>
        <li><strong>What you cached and for how long.</strong></li>
        <li>Both of you named, and <strong>Abanish</strong> assigned as reviewer.</li>
      </ul>

      <h3>Before You Submit</h3>
      <p>Open the <strong>Changes</strong> tab and read every line, both of you. Two things specific to this phase: no API responses with real coordinates pasted into committed fixtures without checking what is in them, and no credentials anywhere, including in a cached file you forgot to gitignore.</p>

      <p><strong>Done when:</strong> both merge requests are open or merged, a market with a known location shows real soil readings from its nearest station, and a market without one gets a clear explanation instead of a blank tab.</p>

    </div>

  </details>

</div>
