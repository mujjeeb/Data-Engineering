# Understanding Data Engineering and key concepts

## Question 1
Research and compare two popular cloud service providers and their
offerings for data engineering. Analyze the features, pricing models, and
scalability options each platform provides.

## Answer 1
​​I would compare the two most popular cloud services currently available: Amazon Web Services(AWS) and Microsoft’s Azure Cloud Services.

### Amazon Web Services: 
AWS is a cloud computing platform by Amazon that provides various services such as compute power, storage, and content delivery services. Some of its popular services for data engineering are: 
 
Amazon Simple Storage Service or Amazon S3 is a data lake that can store any volume of data from any part of the internet. Since it is an incredibly scalable, quick, and affordable option, Data engineers have the flexibility to duplicate their S3 storage across various Availability Zones with Amazon S3. Data engineers can effectively create web-based cloud solutions that expand automatically and have flexible setups owing to Amazon S3. 
AWS Glue is a fully managed ETL(extract, transform, and load) service for easily and affordably processing, improving, and migrating data between different data stores and data streams. Data engineers may interactively analyze and process the data using AWS Glue Interactive Sessions. Data engineers can visually develop, run, and monitor ETL workflows in AWS Glue Studio with a few clicks.
Amazon Redshift is a petabyte-scale data warehouse cloud service that enables you to leverage your data to discover new insights about your clients and organization. Data engineers can gain insights from data with Redshift Serverless by easily importing and querying data in the data warehouse. 

Pricing Model:
AWS offers pay-as-you-go pricing for its services. This allows customers to only pay for services used and the duration of said use. They also offer Reserved instances that allow customers to reserve services for a one-time fee.

Scalability: AWS offers scalability options such as auto-scaling and elasticity. This flexibility allows customers to scale usage based on demand.






### Azure Cloud Services:
Azure is a cloud computing platform by Microsoft that provides cloud infrastructure services for computing, storage, and networking. It also enables hybrid cloud capabilities and offers a range of higher-level services for developers and other business users. Some of its popular services for data engineering are: 
Azure Synapse Analytics is a platform that offers data warehousing, ETL pipelines, analytical tools, and visualization. Customers can efficiently process the data for warehousing and analytical purposes using Synapse Pipelines' ETL and data integration capabilities from several sources.
 Azure Databricks is a service that enables one-click installation, faster workflows, and shared collaborative, interactive workspaces for Azure users.
Azure Stream Analytics is a real-time event-processing engine designed to simultaneously analyze and process large amounts of fast streaming data from various sources. Also, you can extract information from the data stream and keep an eye out for data trends and patterns in the relationship.


Pricing Model: Azure offers pay-as-you-go pricing for its services. This allows customers to only pay for services used and the duration of said use. They also offer Reserved instances that allow customers to reserve services for a one-time fee.

Scalability:  Azure offers scalability options such as auto-scaling and elasticity. This flexibility allows customers to scale usage based on demand.


## Question 2
Select a real-world use case that exemplifies each of the 5Vs (Volume, Velocity, Variety, Veracity, and Value) of big data. Explain how data engineering techniques can be applied to address the challenges and opportunities associated with each V.

## Answer 2
Below are five real-world use case that exemplifies each of the 5V’s of big data.
Volume: This refers to the massive amount of data generated from a wide variety of sources. A great example of a business with a massive amount of data being generated is Twitter. There are about 456,000 tweets sent per day translating to about 12 Terabytes of data. Twitter uses data engineering techniques such as distributed storage systems and batch processing frameworks, stream processing frameworks. These techniques allow Twitter to analyze and respond to data in real time, providing users with up-to-date information and insights.
Velocity: This refers to the speed at which data is generated and processed. A real-world use case of an industry with a huge amount of data generated with great speed is the financial trading industry. This industry generates data with speed that have to be processed in real-time. Data engineering offers techniques such as in-memory processing, stream processing, real-time analytics, and event-driven architectures to help handle said speed.
Variety: This refers to the different types of data that can be generated. The Healthcare Industry exemplifies a real word scenario where various types of data can be generated such as health records, medical imaging, and genomic records. To process this variety the healthcare industry uses data engineering techniques such as data integration, data cleansing, data transformation, and data modeling. 
Veracity: refers to the quality and accuracy of the data. A use case example of the veracity of big data is the autonomous vehicle industry. This industry generates massive amounts of data that require both high quality and accuracy. Data engineering offers techniques such as Data Cleaning, Data validation, and Data Profiling to ensure data is of use to the industry.
Value: Refers to the usefulness of the data in creating business value. Walmart or any other E-commerce organization generates lots of data from a variety of sources such as reviews, transactions, browsing behavior, social media, etc. To extract value from this data these organizations could use data engineering techniques such as data mining, data warehousing, and machine learning.


## Question 3
Analyze a real-world business case and propose a hybrid solution that combines OLTP and OLAP systems to meet both transactional and analytical data processing requirements. Justify your solution and discuss potential benefits and challenges.

## Answer 3 
A real-world business case for the use of a hybrid solution that combines OLTP and OLAP systems is a Food delivery service/platform such as Jumia Food. The platform needs to process large volumes of transactional data such as sales, inventory, and customer information in real-time while also conducting sophisticated data analysis to identify trends, improve marketing strategies, and optimize supply chain management.
To meet these requirements, the platform could implement a hybrid solution that combines the OLTP system for transaction data processing and provide real-time access to critical business data in combination with an OLAP data warehouse that would store historical data and enable advanced analytics, reporting, and data mining.
This Hybrid solution could use the Extract, Transform, Load (ETL) processes to transfer data from the OLTP system to the OLAP data warehouse on a regular basis.
 
Benefits of this hybrid solution include:
Increase in performance and scalability. By separating the workloads the platform can handle the transaction and analytical processing more efficiently.
Better decision-making. The Hybrid system would allow the platform to make better business decisions as they could use the historical data to track customer behavior, sales trend, and inventory management which will improve strategic decision-making.
Challenges of the Hybrid Solution:
Data Consistency and synchronization. As mentioned earlier for the system to work both systems have to be routinely synchronized. This might lead to some inconsistencies.
Maintenance and support. Supporting and maintaining multiple systems will be resource intensive.

 
## Question 4
Explain the key differences between a traditional relational database, a data warehouse, and a data lake. When would you recommend using each of these storage solutions in a data engineering project?

## Answer 4 
A Traditional Relational Database is a structured database that organizes data in rows and columns forming tables with predefined relationships between them. They are best suited for transactional processing and optimized for handling small volumes of data such as storing data for Online Transaction Processing OLTP, such as shopping carts, banking transactions, etc.
 A Data Warehouse is a centralized repository that stores large volumes of data from multiple sources. It is designed for analytical processing and handling large volumes of data with complex queries. While it also stores structured data like a traditional relational database it allows for a much larger volume of data to be stored and analyzed.It is best suited for projects that have multiple sources of data that can be combined and analyzed to help gain insights such as the E-commerce platform's need for customer purchase behavior.
A Data Lake is a centralized repository that stores structured, semi-structured and unstructured data from various sources such as social media, and IoT devices. Unlike the Data warehouse, a data lake doesn’t impose a structure on the data ingested. They are best suited for projects where the structure and the use of the data aren't well defined and are best analyzed in their raw form. An example of such a project will be a project that requires some form of machine learning.


## Question 5
Discuss the advantages and challenges of ETL in the context of data engineering.
## Answer 5 
ETL(Extract, Transform, Load) is the process of integrating data from several sources, transforming it to a predetermined format, and then loading it to a single destination system for analysis and reporting. 
This process has a few advantages in data engineeringsuch as:
Improved Data quality. By consolidating data from several sources, transforming it into a suitabale format and thenloading it into a destiantion system. This ensures that the data is consistent and accurate.
Better decision making: ETL ensures the data is been consolidated from several sources and is accurate, consistent and timely.This ensures that the insights made from this data is of great value.
Scalability and Better Accesibility: ETL is scalable and can handle larger volumes from several data sources. By consolidating the data from several sources into a destination system. Stakeholders have access to the data and can easily pull out insights that will be of value to the organization.
There are a few drawbacks to ETL such as:
Complexity: Designing, Implementing and mainatianing ETL processes requires expertise in several domains and can be arduous.
Performance: ETL responses can be resource-intensive can lead to slow response time from both the source and the destination system.
Data Quality Issues: Combining data from several sources into predetermined structure could lead to errors. These errors could lead to inaccuracies in the insights drawn from the data.
