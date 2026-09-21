# PCEP Capstone: Enterprise Compliance Reporting Automation

## Problem
Participants are provided with multiple spreadsheets containing critical organizational data, including application inventories, compliance status records, identified control gaps, and corresponding stakeholder or business owner information.

The objective is to design and develop an automated solution capable of consolidating and processing these disparate spreadsheets to generate a cohesive, executive-ready compliance report. The solution should transform raw operational data into structured insights, enabling leadership to assess overall compliance posture, understand stakeholder-level performance, and identify key risk areas requiring attention.

## Objectives
Participants must design and deliver a solution that:

### 1. Consolidates Data Across Spreadsheets
- Ingest multiple Excel/CSV files containing:
  - Application list
  - Compliance status
  - Gap logs
  - Stakeholder/owner details

### 2. Generates Organizational Compliance Insights
- Compute overall compliance percentages
- Summarize compliance posture across the full application portfolio

### 3. Produces Stakeholder Level Analytics
- Break down compliance by stakeholder, business owner, or department
- Identify owners with low or high compliance performance

### 4. Identifies and Prioritizes Gaps
- Detect missing controls, exceptions, and non-compliance items
- Highlight high-risk gaps based on severity or category
- Recommend prioritized remediation areas

### 5. Visualizes Insights Using Matplotlib
Participants must produce rich visualizations such as:
- Bar charts (compliance per stakeholder)
- Heatmaps (risk or gap concentration)
- Trend lines (improvements/decline over time, if data supports it)

### 6. Auto Generate a Consulting Style Report
- Export final insights into:
  - PDF (ReportLab, FPDF, or similar)
  - HTML (for web delivery or internal portals)
- Include charts, summaries, and key findings tailored for leadership
