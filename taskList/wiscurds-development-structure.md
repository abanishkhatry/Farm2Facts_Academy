---
layout: default
title: "Development Structure Overview"
---

# Farm2Facts Development Structure Overview

A visual overview of how Farm2Facts is built, who uses it, and how data moves through it.

## Tech Stack and Users

<figure class="diagram">
  <img src="{{ site.baseurl }}/assets/stack.png" alt="Farm2Facts tech stack: a Vue.js frontend exchanging data with a Ruby-on-Rails backend, which exchanges data with a MySQL database. Alongside it, a list of users: market organizations, farmers markets, individual vendors, individual producers, and admins.">
</figure>

Farm2Facts runs on three layers. The **frontend** is a Vue.js application, the **backend** is a Ruby-on-Rails API, and the data itself sits in a **MySQL database**. Requests travel in both directions: the frontend asks the backend for data, the backend reads from and writes to the database, and the results come back the same way.

The people on the platform are **market organizations**, **farmers markets**, **individual vendors**, **individual producers**, and **admins**. What each of them sees depends on their role.

## Users and User Organization

<figure class="diagram">
  <img src="{{ site.baseurl }}/assets/users.png" alt="Users: individual producers and vendors, farmers markets, and market organizations. User organization: a market organization containing three farmers markets, each containing individual vendors and producers.">
</figure>

The users that interact with the platform from the outside fall into three types: **individual producers and individual vendors**, **farmers markets**, and **market organizations**.

These nest inside one another. Individual vendors and producers belong to a farmers market, and multiple farmers markets belong to a market organization. So a market organization sees data aggregated from every market underneath it, and a market sees data from its own vendors and producers.

## User Interaction and Data Flow

<figure class="diagram">
  <img src="{{ site.baseurl }}/assets/dataflow.png" alt="Data flow: vendor applications, vendor sales slips, and visitor surveys are filled in by individual producers and vendors and by farmers markets. Data flows from individual vendors and producers up to their farmers market, and from each farmers market up to the market organization.">
</figure>

Data enters the platform through **instruments**: vendor applications, vendor sales slips, visitor surveys, and others.

Individual vendors and producers fill these in at their own level. That data flows up to the **farmers market** account they belong to, which accumulates it, adds any further instruments of its own, and submits the result to the **market organization** it is associated with. That upward path is the overall flow of data within Farm2Facts.
