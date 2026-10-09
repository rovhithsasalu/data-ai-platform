# Career Timeline

## Career summary

Integration and data engineering professional with experience building enterprise integrations, configuration-driven ETL platforms, AWS serverless services, AI assistants, and AI-assisted migration tooling. My work has included both hands-on engineering and leading solution design and migration efforts.

## TCS — WebMethods Integration Developer

**Approx. 2013–2016** — Started my career at TCS as a WebMethods integration developer. Over roughly three years, I developed **50+ integration pipelines** connecting source systems to target systems.

The work exposed me to:

- Integrating with systems such as SAP, databases, and web services.
- Data transformations and CRM-related data flows.
- Working across multiple systems and teams to deliver end-to-end integrations.

Some project specifics are difficult to recall because this work was more than ten years ago.

## Accenture — Integration, Data, Cloud, and AI

**Joined in 2016; currently there for about 10 years.** My work has progressed from WebMethods integration development into data platforms, AWS architecture, AI solutions, and platform migration leadership.

### Senior WebMethods Integration Developer

I continued building integration pipelines and also improved the tools and operational processes around them:

- Automated a previously manual, multi-step deployment process with a CI/CD solution.
- Built a utility dashboard so developers and support staff could find information about pipelines, connections, and configurations in one place.

### Data lake and configuration-driven ETL platform

As the organization invested in data lakes, I helped build an in-house data engineering platform from scratch using **Apache Spark and AWS Glue**.

- Designed a configuration-driven ETL approach: consumers supplied configuration values instead of repeatedly writing similar pipeline code.
- The platform grew to approximately **4,500 pipelines** before migration to Databricks began.
- This work gave me experience in reusable data platform design, ETL, Spark, and AWS Glue.

### AWS solutions and messaging middleware

As workloads moved from on-premises environments to the cloud, I gained hands-on AWS experience and led AWS solution work. One solution was a serverless/microservices messaging service handling **100,000+ messages per day**:

```text
Customer -> API Gateway -> SQS -> Lambda
                              (transform and route)
                                  -> Target
```

Targets included databases, web services, email, and S3. I also gained intermediate DevOps experience deploying the infrastructure stacks required to host AWS solutions.

During this period, I completed the **AWS Certified Solutions Architect – Associate** and **AWS Certified Solutions Architect – Professional** certifications.

### AI assistants using retrieval-augmented generation

I built multiple AI assistants using **RAG** to help teams find information across hundreds of documents and ask questions against that material. The goal was to put relevant knowledge at users’ fingertips.

### AI-assisted migration from SnapLogic to AWS Glue

I worked on migrating **100+ SnapLogic pipelines** to AWS Glue to reduce licensing costs and remove technical debt.

- Used AI agents to discover and understand SnapLogic pipelines.
- Mapped relevant pipeline features to AWS Glue capabilities.
- Built an ETL test solution to compare the source and migrated outputs and identify discrepancies.

### Current initiative: migration to Databricks

The team is now moving ETL pipelines to Databricks, which is a new platform for the team. I’m leading this migration effort, including solution design and exploration of **Claude Code plugins and headless agents** to support the work.

I have also been using Claude Code and developing practical skills with its skills, plugins, and hooks.

## Work I’m especially proud of

1. **Reusable ETL platform:** Helped build a configuration-driven Spark and AWS Glue platform that reached approximately 4,500 pipelines.
2. **Cloud messaging service:** Led solution work for an AWS messaging middleware service processing 100,000+ messages per day across multiple target types.
3. **AI-assisted pipeline migration:** Helped migrate 100+ SnapLogic pipelines and built output comparison testing to check migration correctness.
4. **Current Databricks migration:** Leading the team’s move of ETL workloads to a new platform, exploring agent-based tooling to improve discovery and migration.

## Impact metrics to add when available

The scale figures above are known. To make this timeline stronger for resumes and interviews, add verified measures where possible:

- CI/CD: deployment time before and after automation; deployment frequency or error reduction.
- Utility dashboard: number of users or support/developer time saved.
- ETL platform: pipeline run volume, data volume, runtime improvement, or hours of repeated code avoided.
- AWS messaging service: peak throughput, availability, processing latency, or operational effort saved.
- RAG assistants: adoption, answer/source retrieval time saved, or user feedback.
- SnapLogic migration: licensing savings, migration duration, and test coverage or discrepancy rate.
- Databricks migration: pipeline count, data volume, timeline, cost, and reliability goals.

## Raw notes (as provided)

```text
Started my career with TCS as WebMethods integration developer developed 50+ pipelines which integrates data from multiple source systems to target learning include working wirth multiple systems liek SAP, Databases, Webservices (Rest and POST),transformations, Integration involved processing CRM data and more (dont remember as its been more than 10 years)

Then after 3 years in TCS, I joined accenture on 2016 and currently in accenture over 10 years,
-->Joined as senior integration developer for webmethods, along with building integration pipelines, I have created automations like CICD where deployment process was earlier manul and multiple steps which automated complete deoyment, built utiltiy dashboard where developers/support person can check every information replated to pieplines, connections, configurations
Post taht I saw an oppertunity in Data lakes where we built inhouse data engineering puiepilien from  scratch using Spark and AWS Glue which is a full configuration based ETL Tool where consumers just have to configure values instead of creating redundant code everytime and this platform  had almost 4.5k pipelines before migration started to Databricks

While working on datalakes we had an oppertunity where everything moved from onpem tp cloud, so got to work with AWS, along with data lake, lead AWS project solutions, created a messaging middleware  servics on AWS leveraging serverless/microservices architecture where customers usedd to call our API (100k+ messages) perday, API Gateway ->SQS -> Lambda (Transform + Send to target) -->Target (DB/Webservice/Email/S3)

Meanwhile I complefed AWS CCertified Solutions aarchitect Associate and Professional

And also got some exposure on Devops(intermediate) where we deployed stack required for hosting our AWS solutions

Then got an oppertunity to work on AI as AI came in to popularity, built multiple assistants using RAG, which helped teams have data at their fingertip, ask questions which would searches through 100s of documents

Worked on  migrating 100+ Snaplogic piepkines to Glue to reduce licensing cost and elimiate tech debt using AI Agents to discover snaplogic piepline, map relavent Glue features and convert the pipeline to Glue, also built ETL test solution which would compare both outputs to make sure there are no descrepancies

Then we are at a point where moving all ETLs to Databricsk (dtaabricks is new to team moving all ETL pipelines here), leading this migration effort inluding solutiooning leveraging claude clode Plugins, headless agenents

Good exposure to claude code have been using taht for som egtime, create skills, plugins, hooks, efficiently leverage claude code
```
