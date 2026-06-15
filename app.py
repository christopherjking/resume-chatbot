import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
#st.set_page_config(page_title="Chris King | Resume Q&A", page_icon="📊")
st.set_page_config(page_title="Chris King | Resume Q&A", page_icon="profile.png")
st.title("Chat with Chris King's Resume")
#st.write("Ask me anything about Chris's 22 years of Supply Chain and Data Analytics experience!")
st.write("Ask me anything about Chris's 22 years of Supply Chain and Data Analytics experience!")
st.write("🔗 **Connect:** [LinkedIn](https://www.linkedin.com/in/chris-king-3607684/) | [Portfolio](https://www.christopherjking.com)")

# 2. Configure the Gemini API securely
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# 3. Define the Resume Context (System Prompt)
# Paste your full resume text in this string
resume_context = """
You are an AI assistant answering questions on behalf of Chris King, a Senior Data Analytics Manager with 22 years of supply chain experience. 
Base all your answers STRICTLY on the following resume text. If a user asks a question not covered by the resume, politely explain that you only have information regarding his professional background. All your answers must be accurate.

Resume Text:

-------------------------------------------------------------------
Section - Personal Information:

Full Name: Christopher King
Preferred first name: Chris
Title: Senior Supply Chain Data Analytics Manager
Location: Naperville, IL 60540
Email: chris@christopherjking.com
Phone: 847-977-5622
LinkedIn: https://www.linkedin.com/in/chris-king-3607684
Personal Portfolio Website: https://www.christopherjking.com/




-------------------------------------------------------------------
Section - About Me Summary:

As a Senior Data Analytics Manager, I combine 22 years of hands-on supply chain experience with advanced technical proficiencies in data architecture, business intelligence strategy, and modern platform engineering (including ML and AI). My career has evolved organically from managing last-mile delivery and directing enterprise WMS implementations to architecting centralized data solutions for major retailers. Beyond the technology, I am deeply committed to people leadership and team development. I have successfully scaled and led analytics teams, including managers and analysts. By establishing structured performance frameworks, mentoring talent through their career progressions, and driving self-service analytics training, I empower both my direct reports and cross-functional partners to succeed. Whether deploying real-time operational reporting ecosystems , migrating fragmented dashboards into unified visualization architectures , or building automated data quality checks, I build scalable systems and capable teams that enable organizations to make fast, accurate decisions. 



-------------------------------------------------------------------
Section - Experience:

Experience 1:
Title: Senior Manager of Supply Chain Data Analytics
Company: Ulta Beauty
Timeframe: March 2022 - Present
Location: Bolingbrook, IL
Details:
Lead 8-person analytics team (2 managers, 6 analysts) delivering enterprise-wide data infrastructure, governance, and insights for $10B+ retail supply chain operation spanning 1,400+ stores and 6 distribution centers.

Platform Modernization & Architecture
Orchestrated complete analytics platform transformation, migrating legacy SAP HANA data lake to Google Cloud Platform while consolidating 1,600+ fragmented SQL models into unified, consumption-ready data architecture serving as single source of truth for supply chain decision-making
Redesigned reporting ecosystem, reducing 282 disparate Tableau dashboards to ~35 integrated PowerBI reports with enhanced usability and analytical depth, cutting report maintenance overhead by 87% while improving stakeholder access to actionable insights
Pioneered AI-enhanced documentation strategy using Gemini API to auto-generate metadata definitions, accelerating time-to-value for new data assets and reducing documentation backlog by 70 percent
Engineered Feature Store to standardize machine learning inputs across forecasting, inventory optimization, and network planning models, reducing feature engineering redundancy and improving model consistency

Data Governance & Quality Management
Established enterprise data governance program from ground up, implementing 800+ automated daily quality checks across critical supply chain metrics
Built comprehensive monitoring infrastructure tracking health of scheduled jobs, Python pipelines, and PowerBI refreshes, reducing data incident resolution time  and preventing downstream disruptions
Created model auditing framework to automatically detect anomalies, model drift, and potential issues before impacting business stakeholders, improving on our data downtime metric by over 3,000 percent from last year

Team Performance & Self-Service Enablement
Developed performance management framework using JIRA and Sprint methodology to track team and individual KPIs, increasing team productivity by 99 percent and improving on time delivery by 23 percent
Launched self-service analytics platform with certified data models, training curriculum, and comprehensive documentation, enabling business users to conduct independent analysis and reducing ad-hoc report requests
Cultivated analytics capability across supply chain organization through structured training programs, office hours, and documentation, democratizing data access while maintaining governance standards






Experience 2:
Title: WMS Manager
Company: Harbor Freight Tools
Timeframe: March 2021 - March 2022
Location: Joliet, IL
Details:
Drove warehouse management systems strategy for rapidly expanding retail operation, supporting launch of new 1M+ sq ft distribution center and implementation of a modern fulfillment model.
Led WMS configuration and deployment for greenfield DC partnering with Operations, Engineering, and IT to design workflows supporting both traditional replenishment and emerging direct-to-consumer fulfillment
Established real-time operational reporting platform using IBM Cognos SCI, giving floor managers immediate visibility to key operational metrics
Architected ETL pipeline feeding WMS data into SQL Server data warehouse, creating foundation for predictive analytics on labor planning, inventory positioning, and seasonal demand patterns
Built technical documentation framework in Confluence, accelerating onboarding of new system administrators and reducing knowledge-transfer dependencies




Experience 3:
Title: Warehouse Systems Advancement Manager
Company: Ulta Beauty
Timeframe: July 2017 - March 2021
Location: Bolingbrook, IL
Details:
Directed WMS evolution strategy (Manhattan 2013, 2018, 2020) supporting DC network expansion, automation integration, and continuous operational improvement across $8B retail supply chain.
Managed release pipeline for 200+ WMS enhancement initiatives spanning automation technology, labor management optimization, rate shopping and TMS systems, and omnichannel fulfillment capabilities
Expanded BI and reporting capabilities within IBM Cognos SCI, expanding visibility across essential real time operational metrics
Established agile project management framework using JIRA to prioritize development backlog, track releases, and measure ROI of system investments
Created comprehensive documentation library (technical specs, user guides, SOPs) in Confluence, standardizing institutional knowledge and reducing system-related incident escalations




Experience 4:
Title: WMS Systems Administrator
Company: Crate And Barrel
Timeframe: September 2016 - July 2017
Location: Northbrook, IL
Details:
Managed technical operations, performance optimization, and release management for Blue Yonder WMS supporting multi-DC fulfillment network for $2B+ home furnishings retailer.
Reduced WMS incident rate by 178% through proactive performance tuning, enhanced monitoring, and systematic root-cause analysis of recurring system issues
Designed and implemented SQL and MOCA solutions to resolve system bottlenecks and operational constraints, improving order processing throughput
Established structured release management process using JIRA to track enhancements, manage configuration changes, and coordinate testing
Partnered with IT and external consultants to execute system upgrades, integrations, and disaster recovery procedures




Experience 5:
Title: WMS Project Manager
Company: Crate And Barrel
Timeframe: July 2013 - September 2016
Location: Northbrook, IL
Details:
Led enterprise-wide implementation of Blue Yonder (JDA/Red Prairie) Warehouse Management System across three distribution centers, managing cross-functional teams and external consulting resources.
Successfully converted three DCs from legacy WMS to Blue Yonder platform, completing implementations on-time and on-budget while maintaining operational continuity during peak retail seasons
Directed all project lifecycle phases including requirements gathering, solution design, testing strategy, cutover planning, and post-go-live stabilization
Managed project plans, budgets, documentation, and stakeholder communications across Operations, IT, Finance, and Executive leadership




Experience 6:
Title: Assistant Home Delivery Manager
Company: Crate And Barrel
Timeframe: March 2008 - July 2013
Location: Northbrook, IL
Details:
Managed last-mile delivery operations including 3PL partner selection, contract negotiations, budgeting, and performance management for home furnishings fulfillment network.
Built carrier performance measurement framework with KPI-based scorecards tracking on-time delivery, damage rates, and customer satisfaction—reducing our return rate by 40%
Led RFP processes for carrier selection and contract renewals, negotiating agreements and managing relationships across national 3PL network





Experience 7:
Title: Home Delivery Coordinator
Company: Crate And Barrel
Timeframe: June 2006 - March 2008
Location: Northbrook, IL
Details:
Participated in corporate Home Delivery projects, RFP bid proposals, contract management, and third-party carrier relations. This included expansion into new Home Delivery markets, conversion of existing markets to new carriers, and measurement of carrier performance. 




Experience 8:
Title: Midwest Logistics Customer Service Coordinator
Company: Crate And Barrel
Timeframe: December 2005 - June 2006
Location: Naperville, IL
Details:
Managed customer service opportunities for all Midwest-regional home deliveries. Developed, deployed, and maintained carrier performance metrics. Managed test-and-learn carrier trials.




Experience 9:
Title: Home Delivery Operations Coordinator
Company: Crate And Barrel
Timeframe: October 2004 - December 2005
Location: Naperville, IL
Details:
Coordinated daily Home Delivery tasks within the distribution center while focusing on continuous-improvement initiatives. This included the development, deployment, and maintenance of internal KPI measurements. 




-------------------------------------------------------------------
Section - Skills:


Technical Skills & Core Competencies:

Data Platform, Cloud Architecture, & Business Intelligence
Google Cloud Platform (GCP) | BigQuery, Cloud Storage, Dataplex, Cloud Functions
Data Warehousing | Dimensional modeling, star schema design, data vault methodology
Legacy Systems | SAP HANA, Oracle, SQL Server, MySQL, DB2 - enterprise-scale platform transitions

Power BI | Report design, DAX, Power Query, data modeling, RLS, embedded analytics, workspace administration
Tableau | Desktop, Flow, Server, calculated fields, LOD expressions, dashboard design, performance optimization
IBM Cognos SCI | Report authoring, framework manager, real-time operational reporting
Excel/Google Sheets | Advanced formulas, pivot tables, macros, VBA, AppScript automation


Analytics Engineering,  Data Transformation & Programming
SQL | Advanced query optimization, window functions, CTEs, stored procedures, performance tuning
Python | Pandas, NumPy, requests, API integrations, ETL automation, data validation, web scraping

Feature Engineering | Feature store development, model input standardization, versioning
ETL/ELT Development | Data pipeline orchestration, incremental load strategies, error handling, data validation

MS Power Platform | Automation flows via PowerAutomate and front end app development via PowerApps

JavaScript/AppScript/HTML | Automation, custom workflows, form processing, reporting interfaces, email templates
VBA | Excel/Office automation, macro development, legacy system integration
AI LLMs | Using Gemini, Claude, Cursor, Perchance, and ChatGPT for efficient task processing

Version Control | Git fundamentals, collaborative development workflows


Data Governance & Quality Management
Data Quality Frameworks | Automated validation rules, anomaly detection, reconciliation processes
Metadata Management | Data cataloging, lineage tracking, business glossary, AI-enhanced documentation
Monitoring & Alerting | Job scheduling oversight, pipeline health checks, SLA tracking, incident response
Master Data Management | Data standardization, model certification,, reference data governance


Project Management, Program Management & Collaboration Tools
Methodologies | Agile/Scrum, Waterfall, Critical Path Method, Hybrid approaches
Certifications | Lean Project Management, Six Sigma Green Belt
Tools | JIRA (administration, workflow design, reporting), Confluence, MS Project, Smartsheet, Trello
Change Management | Stakeholder engagement, training curriculum development, adoption strategy, documentation

Documentation Platforms | Confluence, SharePoint, Google Sites, Markdown, technical writing
Presentation & Training | Executive communication, technical training design, user enablement programs
Communication | Slack, Teams, Gmail, JIRA, Outlook - building distributed team collaboration frameworks




Leadership & Strategic Competencies:

Supply Chain Experience - I have 22 years of experience in Supply Chain including ecommerce & retail transportation, final mile delivery, S&OP planning, supplier operations, omnichannel, quality assurance, distribution operations for inbound, replenishment, picking, sorting, packing, and shipping. I also have extensive experience with key Supply Chain Systems like Warehouse Management Systems (WMS - Blue Yonder & Manhattan), TMS, Rate Shopping, ASRS, Automated Picking & Sorting robotics, etc

Team Building & Development - Scaled analytics teams, mentored analysts through career progression, established performance frameworks, developed talent through comprehensive Individual Development Planning

Stakeholder Management - Translated technical capabilities into business value for leadership and cross-functional partners

Vision & Strategy - Defined multi-year roadmaps for analytics maturity, self-service enablement, and AI integration

Process Optimization - Applied Lean and Six Sigma principles to streamline analytics delivery and improve data quality






-------------------------------------------------------------------
Section - Education:


Certifications:
Six Cigma Green Belt Certified
Project Management - Lean Process Certified
Project Management - Agile Process Certified
Executive Management Certified

Education:
Bachelors Degree from North Central College - Location: Naperville - Major: Political Science | Graduation year: 2005


-------------------------------------------------------------------
Section - Special project examples:


Resume AI Chatbot
This chatbot uses Python and AI api integration to answer questions about me and my resume. 


Documentation AI Chatbot
Internally I built an AI chatbot that reviews our team's Confluence documentation, JIRA project, PowerBI catalogue, and GCP metadata to provide answers across our team's work and data products.


Automated Data Documentation
Internally I built a series of processes combining Python and AI to automate the creation of GCP metadata, PowerBI metada, lineage, and Confluence documentation to create automated data product overviews.


Automated Report Exec Summaries
Internally I built a process using Python and AI to provide weekly executive summaries of key reports with detailed insights. 


ML Forecasting Trend Data
Within the GCP landscape I built Machine Learning modelling that added forecasting logic to our Supply Chain budgeting dashboarding suite. 


Data Profiling & Reliability Platform
Combining Python, SQL, and PowerBI I built a Data Reliability and Profiling Platform to measure the accuracy of our data using the 5 pillars of Freshness, Volume, Distribution, Schema, and Lineage. 


"""

# Initialize the model with the system instructions
# Using gemini-2.5-flash as it is the current supported model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=resume_context
)

# 4. Initialize Chat Session in Streamlit Session State
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Define Custom Avatars ---
ai_icon = "profile.png"
# Using ui-avatars API to generate a user icon with your exact blue hex code (0b5394)
#user_icon = "https://ui-avatars.com/api/?name=User&background=0b5394&color=fff"
user_icon = "user.png"

# 5. Display Chat History with Custom Avatars
for message in st.session_state.messages:
    # Determine which icon to use based on the role
    avatar_to_use = user_icon if message["role"] == "user" else ai_icon
    
    with st.chat_message(message["role"], avatar=avatar_to_use):
        st.markdown(message["content"])

# 6. Handle User Input with Custom Avatars
if user_prompt := st.chat_input("Ask me anything about Chris's 22 years of Supply Chain and Data Analytics experience!..."):
    # Display user message with blue icon
    with st.chat_message("user", avatar=user_icon):
        st.markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Send message to Gemini and get response
    response = st.session_state.chat_session.send_message(user_prompt)
    
    # Display assistant response with your PNG
    with st.chat_message("assistant", avatar=ai_icon):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
