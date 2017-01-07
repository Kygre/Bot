'''
Created on Jan 7, 2017

@author: admin
'''
from pprint import pprint
import unittest

import ipgetter

from root.RSS import Feed_Bot, Upwork_Bot
fake_xml = '''<rss xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0" hc="a0" hcx="0">
<channel>
<title>
<![CDATA[ All Recommended jobs | upwork.com ]]>
</title>
<link>
<![CDATA[
https://www.upwork.com/ab/feed/topics/rss?orgUid=757003863698284545&amp;securityToken=4aa606ee391dec6bd271cea909cb55cfbe6f8b7cf22f9a1e3f265214784c96377651feb5902eaca5a02e2f38f4ea27b5392b5a89ca1e62910236ae039307a1f5&amp;topic=recommended&amp;userUid=757003863694090240
]]>
</link>
<description>
<![CDATA[
All Recommended jobs as of January 07, 2017 18:20 UTC
]]>
</description>
<language>en-us</language>
<pubDate>Sat, 07 Jan 2017 18:20:56 +0000</pubDate>
<copyright>© 2003-2017 Upwork Corporation</copyright>
<docs>http://blogs.law.harvard.edu/tech/rss</docs>
<generator>Upwork Corporation</generator>
<managingEditor>rss@upwork.com (Upwork Corporation)</managingEditor>
<image>
<url>https://www.upwork.com/images/rss_logo.png</url>
<title>
<![CDATA[ All Recommended jobs | upwork.com ]]>
</title>
<link>
<![CDATA[
https://www.upwork.com/ab/feed/topics/rss?orgUid=757003863698284545&amp;securityToken=4aa606ee391dec6bd271cea909cb55cfbe6f8b7cf22f9a1e3f265214784c96377651feb5902eaca5a02e2f38f4ea27b5392b5a89ca1e62910236ae039307a1f5&amp;topic=recommended&amp;userUid=757003863694090240
]]>
</link>
</image>
<item>
<title>
<![CDATA[ WordPress developer - Upwork ]]>
</title>
<link>
https://www.upwork.com/jobs/WordPress-developer_%7E0193ae71d7a5ec1834?source=rss
</link>
<description>
<![CDATA[
COMPANY DESCRIPTION<br /><br /> Exposyour is a branding, advertising, and marketing firm headquartered in Santa Clara, CA. <br /><br /> Our mission: to combine proven and innovative internet marketing solutions, to build a comprehensive, cost-effective, and powerful digital platform for all of our valued clients.<br /><br /> Our professional team includes a diverse group of web developers, online marketing experts, and digital strategists working collaboratively to satisfy our customers in every way possible. <br /><br /> Specialties: Social Media Marketing, Search Engine Optimization SEO, PPC Management &amp;amp; Optimization, Global Collaboration, Brand Development, Graphic Design/Web Design, Web Development, Client Management, Press Releases &amp;amp; Advertising.<br /><br /> JOB DESCRIPTION<br /> As the Wordpress Specialist &amp;amp; Developer you will be responsible for taking wireframes and other requirements and developing them into shippable code. Those might include core change, themes, plugins, or workflow changes.<br /><br /> Qualified candidates will:<br /> - Hit the ground running, and function best in a complex environment.<br /> - Posses Excellent Communication skills.<br /> - Work successfully while leading individual development initiatives to further projects.<br /> - Work with the team to understand existing requirements by video.<br /> - Consistently implement stable, efficient code conforming to Wordpress coding standards, working within the defined architecture.<br /> - Lead in design reviews and stakeholder demos.<br /> - Maintain a high level of organization while operating in a multi-project environment.<br /> - Ability to work under pressure on multiple projects, meeting deadlines.<br /><br /><br /> Required:<br /> - Proficiency in: PHP, Wordpress, CSS, HTML, SQL.<br /> - WordPress experience at the PHP code level (including creating and/or working with WordPress plugins and themes).<br /> - Deep understanding of the WordPress core software and its functions.<br /> - Understanding of WordPress coding best practices.<br /> - Understanding of WordPress security best practices.<br /> - Understanding of the administration and maintenance experience of a LAMP stack (Linux, Apache, MySQL or MariaDB, and PHP).<br /> - debugging and troubleshooting skills.<br /> - Enterprise level coding experience in a web scripting language (Dot Net, PHP, JSP, or another).<br /><br /> QUALIFICATIONS<br /> - Three years of Wordpress experience.<br /> - Basic Photoshop experience to assist with theme creation and work with premade themes.<br /> - UI / User Interface and front-end experience.<br /> - HTML5, JSON, JQuery, Spring Framework, Node JS, Twitter Bootstrap experience.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web &amp; Mobile Design<br /><b>Skills</b>: Adobe Photoshop, AJAX, CSS, CSS3, HTML, HTML5, JavaScript, jQuery, JQuery Mobile, MySQL Administration, PHP, Web Design, WordPress <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/WordPress-developer_%7E0193ae71d7a5ec1834?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
COMPANY DESCRIPTION<br /><br /> Exposyour is a branding, advertising, and marketing firm headquartered in Santa Clara, CA. <br /><br /> Our mission: to combine proven and innovative internet marketing solutions, to build a comprehensive, cost-effective, and powerful digital platform for all of our valued clients.<br /><br /> Our professional team includes a diverse group of web developers, online marketing experts, and digital strategists working collaboratively to satisfy our customers in every way possible. <br /><br /> Specialties: Social Media Marketing, Search Engine Optimization SEO, PPC Management &amp;amp; Optimization, Global Collaboration, Brand Development, Graphic Design/Web Design, Web Development, Client Management, Press Releases &amp;amp; Advertising.<br /><br /> JOB DESCRIPTION<br /> As the Wordpress Specialist &amp;amp; Developer you will be responsible for taking wireframes and other requirements and developing them into shippable code. Those might include core change, themes, plugins, or workflow changes.<br /><br /> Qualified candidates will:<br /> - Hit the ground running, and function best in a complex environment.<br /> - Posses Excellent Communication skills.<br /> - Work successfully while leading individual development initiatives to further projects.<br /> - Work with the team to understand existing requirements by video.<br /> - Consistently implement stable, efficient code conforming to Wordpress coding standards, working within the defined architecture.<br /> - Lead in design reviews and stakeholder demos.<br /> - Maintain a high level of organization while operating in a multi-project environment.<br /> - Ability to work under pressure on multiple projects, meeting deadlines.<br /><br /><br /> Required:<br /> - Proficiency in: PHP, Wordpress, CSS, HTML, SQL.<br /> - WordPress experience at the PHP code level (including creating and/or working with WordPress plugins and themes).<br /> - Deep understanding of the WordPress core software and its functions.<br /> - Understanding of WordPress coding best practices.<br /> - Understanding of WordPress security best practices.<br /> - Understanding of the administration and maintenance experience of a LAMP stack (Linux, Apache, MySQL or MariaDB, and PHP).<br /> - debugging and troubleshooting skills.<br /> - Enterprise level coding experience in a web scripting language (Dot Net, PHP, JSP, or another).<br /><br /> QUALIFICATIONS<br /> - Three years of Wordpress experience.<br /> - Basic Photoshop experience to assist with theme creation and work with premade themes.<br /> - UI / User Interface and front-end experience.<br /> - HTML5, JSON, JQuery, Spring Framework, Node JS, Twitter Bootstrap experience.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web &amp; Mobile Design<br /><b>Skills</b>: Adobe Photoshop, AJAX, CSS, CSS3, HTML, HTML5, JavaScript, jQuery, JQuery Mobile, MySQL Administration, PHP, Web Design, WordPress <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/WordPress-developer_%7E0193ae71d7a5ec1834?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Thu, 05 Jan 2017 23:02:56 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/WordPress-developer_%7E0193ae71d7a5ec1834?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
I need a designe who can work on an ongoing project - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/need-designe-who-can-work-ongoing-project_%7E016ade945b2231543f?source=rss
</link>
<description>
<![CDATA[
Looking for a full-time UI/UX Designer <br /><br /> 4+ years of experience in software development with focus on front-end development.<br /> Strong working knowledge of HTML5, CSS3 and JavaScript.<br /> Proficiency in Photoshop, Illustrator, visual design and wire-framing tools.<br /> Good Understanding of Client Side Scripting and JavaScript Frameworks like : Jquery.<br /> Up-to-date with the latest UI trends, techniques, and technologies.<br /> Knowledge of cross-browser compatibility issues and client-side performance consideration<br /><br /><b>Budget</b>: $300 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Design &amp; Creative &gt; Graphic Design<br /><b>Skills</b>: CSS, Graphic Design, HTML5, iPhone UI Design, jQuery, Logo Design, Mobile UI Design, Responsive Web Design, Web Design <br /><b>Country</b>: Australia<br /><a href="https://www.upwork.com/jobs/need-designe-who-can-work-ongoing-project_%7E016ade945b2231543f?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Looking for a full-time UI/UX Designer <br /><br /> 4+ years of experience in software development with focus on front-end development.<br /> Strong working knowledge of HTML5, CSS3 and JavaScript.<br /> Proficiency in Photoshop, Illustrator, visual design and wire-framing tools.<br /> Good Understanding of Client Side Scripting and JavaScript Frameworks like : Jquery.<br /> Up-to-date with the latest UI trends, techniques, and technologies.<br /> Knowledge of cross-browser compatibility issues and client-side performance consideration<br /><br /><b>Budget</b>: $300 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Design &amp; Creative &gt; Graphic Design<br /><b>Skills</b>: CSS, Graphic Design, HTML5, iPhone UI Design, jQuery, Logo Design, Mobile UI Design, Responsive Web Design, Web Design <br /><b>Country</b>: Australia<br /><a href="https://www.upwork.com/jobs/need-designe-who-can-work-ongoing-project_%7E016ade945b2231543f?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Thu, 05 Jan 2017 08:46:30 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/need-designe-who-can-work-ongoing-project_%7E016ade945b2231543f?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Experienced Manual QA Tester for Website Testing - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Experienced-Manual-Tester-for-Website-Testing_%7E01da4679bcd3897297?source=rss
</link>
<description>
<![CDATA[
Experienced QA Tester to ensure the web product looks and functions according to spec. The QA Tester will send detailed reports on test results regularly. <br /><br /> Essential Duties and Skills: <br /><br /> * strong oral/written communication skills<br /> * Devise, implement and refine best testing practices and tools for the web product. <br /> * Regression Testing <br /> * Manual Testing <br /> * UI testing - Cross-browser and device testing <br /> * Test Case/Plan &amp;amp; document creation with clarity<br /> * Develop a detailed testing plan and report with accuracy and clarity on proper protocols (including test cases, scope, test resources and timeline) with a detailed workflow to replicate an issue, how the issue occurs, where it occurs, screen images and operating system.<br /> * Coordinate the distribution and tracking of those testing assignments and ensure tracking and transparency through completion.&nbsp;&nbsp;<br /> * use of issue tracker/bug tracker software.<br /><br /> Required Qualifications: <br /><br /> * Previous QA experience testing responsive websites<br /> * Excellent communication and collaboration skills<br /> * Knowledge of development processes and environments<br /> * Perform - functional, performance, security, UI tests,<br /> * Should have experience in creating Test Plans, Test scripts, Test cases. <br /><br /> Preferred Qualifications: <br /><br /> * Automated testing experience<br /> * Experience using browser development tools for debugging<br /> * Mobile device testing experience<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; QA &amp; Testing<br /><b>Skills</b>: Functional Testing, Manual Test Execution, Performance Testing, Usability Testing, Web Testing <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Experienced-Manual-Tester-for-Website-Testing_%7E01da4679bcd3897297?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Experienced QA Tester to ensure the web product looks and functions according to spec. The QA Tester will send detailed reports on test results regularly. <br /><br /> Essential Duties and Skills: <br /><br /> * strong oral/written communication skills<br /> * Devise, implement and refine best testing practices and tools for the web product. <br /> * Regression Testing <br /> * Manual Testing <br /> * UI testing - Cross-browser and device testing <br /> * Test Case/Plan &amp;amp; document creation with clarity<br /> * Develop a detailed testing plan and report with accuracy and clarity on proper protocols (including test cases, scope, test resources and timeline) with a detailed workflow to replicate an issue, how the issue occurs, where it occurs, screen images and operating system.<br /> * Coordinate the distribution and tracking of those testing assignments and ensure tracking and transparency through completion.&nbsp;&nbsp;<br /> * use of issue tracker/bug tracker software.<br /><br /> Required Qualifications: <br /><br /> * Previous QA experience testing responsive websites<br /> * Excellent communication and collaboration skills<br /> * Knowledge of development processes and environments<br /> * Perform - functional, performance, security, UI tests,<br /> * Should have experience in creating Test Plans, Test scripts, Test cases. <br /><br /> Preferred Qualifications: <br /><br /> * Automated testing experience<br /> * Experience using browser development tools for debugging<br /> * Mobile device testing experience<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; QA &amp; Testing<br /><b>Skills</b>: Functional Testing, Manual Test Execution, Performance Testing, Usability Testing, Web Testing <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Experienced-Manual-Tester-for-Website-Testing_%7E01da4679bcd3897297?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Wed, 04 Jan 2017 23:40:55 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Experienced-Manual-Tester-for-Website-Testing_%7E01da4679bcd3897297?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Cordova / Phonegap plugin for Image crop and resize - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Cordova-Phonegap-plugin-for-Image-crop-and-resize_%7E01a7db4f1cd5b55533?source=rss
</link>
<description>
<![CDATA[
Background:<br /><br /> We are a software development company. We are developing an app for users to upload images. Before images are uploaded, they need to be cropped and resized. We have HTML5 canvas and java script functions to perform this but it consumes more memory and performance is below par
]]>
<![CDATA[
. So we need a native plugin for Android and iOS that can perform these crop and resize operations.<br /><br /> Here are the high level requirements:<br /><br /> For Crop function, we send an image object along with X, Y, Width and Height parameters. The function should return the cropped image.<br /><br /> For Resize function, we send an image object along with height and width parameters. The function should return the resized image.<br /><br /> It is okay to combine both features in one function. The plugin should work on Android 4.0+ and iOS 7.0+ platforms.<br /><br /> We are software development company ourselves but we do not have expertise in native mobile app development. We are looking for a talented developer for this project. If you&#039;re good at it, we are looking for long term association. Please respond with your skypid and examples of your phonegap / cordova projects.<br /><br /> Best.<br /><br /><b>Budget</b>: $300 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Mobile Development<br /><b>Skills</b>: Android, Android App Development, HTML5, iOS Development, iPhone App Development, Mobile App Development, PhoneGap, Swift <br /><b>Country</b>: India<br /><a href="https://www.upwork.com/jobs/Cordova-Phonegap-plugin-for-Image-crop-and-resize_%7E01a7db4f1cd5b55533?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Background:<br /><br /> We are a software development company. We are developing an app for users to upload images. Before images are uploaded, they need to be cropped and resized. We have HTML5 canvas and java script functions to perform this but it consumes more memory and performance is below par. So we need a native plugin for Android and iOS that can perform these crop and resize operations.<br /><br /> Here are the high level requirements:<br /><br /> For Crop function, we send an image object along with X, Y, Width and Height parameters. The function should return the cropped image.<br /><br /> For Resize function, we send an image object along with height and width parameters. The function should return the resized image.<br /><br /> It is okay to combine both features in one function. The plugin should work on Android 4.0+ and iOS 7.0+ platforms.<br /><br /> We are software development company ourselves but we do not have expertise in native mobile app development. We are looking for a talented developer for this project. If you&#039;re good at it, we are looking for long term association. Please respond with your skypid and examples of your phonegap / cordova projects.<br /><br /> Best.<br /><br /><b>Budget</b>: $300 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Mobile Development<br /><b>Skills</b>: Android, Android App Development, HTML5, iOS Development, iPhone App Development, Mobile App Development, PhoneGap, Swift <br /><b>Country</b>: India<br /><a href="https://www.upwork.com/jobs/Cordova-Phonegap-plugin-for-Image-crop-and-resize_%7E01a7db4f1cd5b55533?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Wed, 04 Jan 2017 13:37:22 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Cordova-Phonegap-plugin-for-Image-crop-and-resize_%7E01a7db4f1cd5b55533?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[ Quality Assurance Engineer - Upwork ]]>
</title>
<link>
https://www.upwork.com/jobs/Quality-Assurance-Engineer_%7E0149f509b0ea2541ba?source=rss
</link>
<description>
<![CDATA[
IOS Project​<br /><br /> Work with an Agile team of software development engineers to improve quality throughout the software development lifecycle<br /> &bull;    Write clear and maintainable test cases covering functional, regression and performance tests in an Agile environment<br /> &bull;    Execute manual testing efforts of iOS, Android applications and websites<br /> &bull;    Participate in design discussions with developers to ensure features are designed and implemented meeting testability requirements<br /> &bull;    Troubleshoot problems found during testing and write clear, concise, and reproducible defect reports<br /> &bull;    Work with QA team members to identify areas for automation<br /> &bull;    Write and execute scripts for automated testing of complex applications​<br /><br /> .At least 4 years of experience in the field of software testing.<br /> &bull;    Must have minimum 1-2 year experience in IOS app testing.<br /> &bull;    Must have knowledge on testing Webservices (SOAP and REST)<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; QA &amp; Testing<br /><b>Skills</b>: Mobile App Testing, QA Engineering, Software QA Testing, Web Testing <br /><b>Country</b>: India<br /><a href="https://www.upwork.com/jobs/Quality-Assurance-Engineer_%7E0149f509b0ea2541ba?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
IOS Project​<br /><br /> Work with an Agile team of software development engineers to improve quality throughout the software development lifecycle<br /> &bull;    Write clear and maintainable test cases covering functional, regression and performance tests in an Agile environment<br /> &bull;    Execute manual testing efforts of iOS, Android applications and websites<br /> &bull;    Participate in design discussions with developers to ensure features are designed and implemented meeting testability requirements<br /> &bull;    Troubleshoot problems found during testing and write clear, concise, and reproducible defect reports<br /> &bull;    Work with QA team members to identify areas for automation<br /> &bull;    Write and execute scripts for automated testing of complex applications​<br /><br /> .At least 4 years of experience in the field of software testing.<br /> &bull;    Must have minimum 1-2 year experience in IOS app testing.<br /> &bull;    Must have knowledge on testing Webservices (SOAP and REST)<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; QA &amp; Testing<br /><b>Skills</b>: Mobile App Testing, QA Engineering, Software QA Testing, Web Testing <br /><b>Country</b>: India<br /><a href="https://www.upwork.com/jobs/Quality-Assurance-Engineer_%7E0149f509b0ea2541ba?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Tue, 03 Jan 2017 10:59:17 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Quality-Assurance-Engineer_%7E0149f509b0ea2541ba?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Clojurescript developer comfortable with CSS - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Clojurescript-developer-comfortable-with-CSS_%7E01c3015a6b65563be4?source=rss
</link>
<description>
<![CDATA[
I&#039;m looking for a software engineer who can work with me to scale the prototype/MVP that I built, into a product that can be launched and marketed as a beta. I have used the following technologies to build my MVP:<br /> - Front-end is built using Clojurescript with re-frame ( a Reagent framework for building single page apps in Clojurescript).<br /> - Back-end is built using Clojure.<br /> - The website runs on Jetty with Nginx as the proxy and is hosted on AWS.<br /> - While I&#039;m only focusing on the website, eventually I plan to use ReactNative (via Clojurescript) to build the native mobile apps.<br /><br /> The back-end code for the beta is almost &amp;quot;production ready&amp;quot;. I might have to handle a few performance issues but overall, the code is good. The front-end ClojureScript code is ok as well but the weakest link is the CSS. That&#039;s where I need the most help.<br /><br /> The best candidate for this job will have the following skills:<br /> - Good knowledge of Clojure and ClojureScript. You don&#039;t have to be an expert (I&#039;m not either) but you need to know enough so that I&#039;m not spending all my time teaching you the basics of Clojure and functional programming.<br /> - Very comfortable with front-end technologies like Javascript and CSS.&nbsp;&nbsp;Even though I don&#039;t have a single line of JS in my code, being comfortable with front-end technologies is critical for this role because I&#039;m looking for someone with complimentary skills. <br /> - Ability to take mocks, assets to build a great user experience. Ability to communicate directly with UX designers would be a huge plus.<br /> - Solid understanding of how to make a responsive website. The website should be ready on Desktop and Mobile web at launch.<br /> - Back-end experience would be nice to have but I&#039;ll mostly be needing your front-end skills. Once the front-end (CSS) code is ready to go, we could collaborate on other areas of the website.<br /> - Experience with React.js would be a huge plus.<br /> - A Github profile with sample code demonstrating how comfortable you are with functional programming would also be a plus.<br /><br /> Other requirements:<br /> - I want to work with individual freelancers. No agencies please. <br /> - Fluent in English and very good written communication skills. Sorry but I don&#039;t want things lost in translation.<br /> - Location doesn&#039;t matter but considering I&#039;m in the US (Pacific), I would prefer candidates in the same time zone.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Skills</b>: Clojure, CSS, JavaScript, React.js <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Clojurescript-developer-comfortable-with-CSS_%7E01c3015a6b65563be4?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
I&#039;m looking for a software engineer who can work with me to scale the prototype/MVP that I built, into a product that can be launched and marketed as a beta. I have used the following technologies to build my MVP:<br /> - Front-end is built using Clojurescript with re-frame ( a Reagent framework for building single page apps in Clojurescript).<br /> - Back-end is built using Clojure.<br /> - The website runs on Jetty with Nginx as the proxy and is hosted on AWS.<br /> - While I&#039;m only focusing on the website, eventually I plan to use ReactNative (via Clojurescript) to build the native mobile apps.<br /><br /> The back-end code for the beta is almost &amp;quot;production ready&amp;quot;. I might have to handle a few performance issues but overall, the code is good. The front-end ClojureScript code is ok as well but the weakest link is the CSS. That&#039;s where I need the most help.<br /><br /> The best candidate for this job will have the following skills:<br /> - Good knowledge of Clojure and ClojureScript. You don&#039;t have to be an expert (I&#039;m not either) but you need to know enough so that I&#039;m not spending all my time teaching you the basics of Clojure and functional programming.<br /> - Very comfortable with front-end technologies like Javascript and CSS.&nbsp;&nbsp;Even though I don&#039;t have a single line of JS in my code, being comfortable with front-end technologies is critical for this role because I&#039;m looking for someone with complimentary skills. <br /> - Ability to take mocks, assets to build a great user experience. Ability to communicate directly with UX designers would be a huge plus.<br /> - Solid understanding of how to make a responsive website. The website should be ready on Desktop and Mobile web at launch.<br /> - Back-end experience would be nice to have but I&#039;ll mostly be needing your front-end skills. Once the front-end (CSS) code is ready to go, we could collaborate on other areas of the website.<br /> - Experience with React.js would be a huge plus.<br /> - A Github profile with sample code demonstrating how comfortable you are with functional programming would also be a plus.<br /><br /> Other requirements:<br /> - I want to work with individual freelancers. No agencies please. <br /> - Fluent in English and very good written communication skills. Sorry but I don&#039;t want things lost in translation.<br /> - Location doesn&#039;t matter but considering I&#039;m in the US (Pacific), I would prefer candidates in the same time zone.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Skills</b>: Clojure, CSS, JavaScript, React.js <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Clojurescript-developer-comfortable-with-CSS_%7E01c3015a6b65563be4?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Mon, 02 Jan 2017 20:00:29 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Clojurescript-developer-comfortable-with-CSS_%7E01c3015a6b65563be4?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[ Long term Java based web developer needed - Upwork ]]>
</title>
<link>
https://www.upwork.com/jobs/Long-term-Java-based-web-developer-needed_%7E01b2e4b71a47c24115?source=rss
</link>
<description>
<![CDATA[
A small well established recruitment software firm has an opening for a good java web developer with skills, enthusiasm and some experience in JSP scripting. They will need strong Javascript and css knowledge and be well versed in many of the techniques being used to code web applications. <br /> Th
]]>
<![CDATA[
e selected applicant will be assisting in the continued development of a long standing recruitment management web application that runs on an Apache Tomcat/MySQL platform.<br /> In addition to being a regular web app, our application has elements of desktop integration via a third party browser wrapper, so familiarity working with MS Outlook via .NET plugins would be a bonus but not essential.<br /> The application is in need of a degree of reformatting to impose a better structure and we have a long list of customer functionality requests to get through.<br /><br /> There is also a sister product for mobiles and tablets written in Jquery mobile that will occasionally need attention as well.<br /> Therefore we want someone to invest themselves in this project and look towards a long term involvement so they can gain knowledge and experience in it and take it to new places.<br /> I will setup a one month paid trial on upwork first and if things work out we can expand it.<br /> The successful applicant will be expected to work remotely but within UK business hours the majority of the time but could possibly start working on a part time basis if they have current commitments to finish off. This means we will only be considering applicants working in similar time zones. So please do not apply if you are more than 2 hours either side of GMT.<br /> Ideally we are looking for someone to ultimately become a full time member of our team.<br /> There is a small element of customer support if a client side issue can not be handled by myself, therefore the applicant must have good conversational written and spoken English, a good communicator and have strict procedural methods that he/she can use to bring order to the project.<br /> Please be warned, I do not deal with outsourcing firms, I prefer to pay developers directly for their efforts, not through a third party.<br /> The successful applicant will be working with a seasoned developer and a newly appointed designer to bring the system up to date.<br /> Please message me if you need more details.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Skills</b>: AJAX, Apache Tomcat, HTML, J2EE, Java, JavaScript, JSP, MySQL Administration <br /><b>Country</b>: United Kingdom<br /><a href="https://www.upwork.com/jobs/Long-term-Java-based-web-developer-needed_%7E01b2e4b71a47c24115?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
A small well established recruitment software firm has an opening for a good java web developer with skills, enthusiasm and some experience in JSP scripting. They will need strong Javascript and css knowledge and be well versed in many of the techniques being used to code web applications. <br /> The selected applicant will be assisting in the continued development of a long standing recruitment management web application that runs on an Apache Tomcat/MySQL platform.<br /> In addition to being a regular web app, our application has elements of desktop integration via a third party browser wrapper, so familiarity working with MS Outlook via .NET plugins would be a bonus but not essential.<br /> The application is in need of a degree of reformatting to impose a better structure and we have a long list of customer functionality requests to get through.<br /><br /> There is also a sister product for mobiles and tablets written in Jquery mobile that will occasionally need attention as well.<br /> Therefore we want someone to invest themselves in this project and look towards a long term involvement so they can gain knowledge and experience in it and take it to new places.<br /> I will setup a one month paid trial on upwork first and if things work out we can expand it.<br /> The successful applicant will be expected to work remotely but within UK business hours the majority of the time but could possibly start working on a part time basis if they have current commitments to finish off. This means we will only be considering applicants working in similar time zones. So please do not apply if you are more than 2 hours either side of GMT.<br /> Ideally we are looking for someone to ultimately become a full time member of our team.<br /> There is a small element of customer support if a client side issue can not be handled by myself, therefore the applicant must have good conversational written and spoken English, a good communicator and have strict procedural methods that he/she can use to bring order to the project.<br /> Please be warned, I do not deal with outsourcing firms, I prefer to pay developers directly for their efforts, not through a third party.<br /> The successful applicant will be working with a seasoned developer and a newly appointed designer to bring the system up to date.<br /> Please message me if you need more details.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Skills</b>: AJAX, Apache Tomcat, HTML, J2EE, Java, JavaScript, JSP, MySQL Administration <br /><b>Country</b>: United Kingdom<br /><a href="https://www.upwork.com/jobs/Long-term-Java-based-web-developer-needed_%7E01b2e4b71a47c24115?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Fri, 30 Dec 2016 10:57:45 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Long-term-Java-based-web-developer-needed_%7E01b2e4b71a47c24115?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Front-end Developer (Freelancers &amp;amp; Full Timers welcomed) - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Front-end-Developer-Freelancers-amp-Full-Timers-welcomed_%7E01ecce99c66979dceb?source=rss
</link>
<description>
<![CDATA[
Front-End Web Developer / Video Editor<br /><br /> Spuul seeks a Front-End Developer cum Video Editor with minimum 2&ndash;4 years profes-sional experience to join our Marketing team in Mumbai, India. <br /><br /> In this role the candidate will work with the Marketing team to code responsive HTML 5 pages, EDMs and also be efficient in editing video for Youtube, Facebook or advertise-ments. He/She would closely work with the Creative Head and development team in Sin-gapore.<br /><br /> Requirements<br /> &bull;    Ability to design and code responsive sites and pages in HTML 5<br /> &bull;    Level 7+ skill in Adobe Photoshop &amp;amp; Illustrator<br /> &bull; Level 8+ skill in Final Cut Pro, Adobe Premiere and Compression software<br /> &bull;    Familiar with Git - to deploy landing pages or amend HTML files<br /> &bull;    Comfortable working with JavaScript<br /> &bull;    &nbsp;&nbsp;People skills to coordinate with development team, build and deploy pages to produc-tion.<br /> &bull;    &nbsp;&nbsp;Make sure pages are well optimized ( hand code HTML5 and make sure there are no extra&nbsp;&nbsp;&nbsp;scripts that slow down pages) and load quickly on all devices<br /> &bull;    Test and make sure that pages work on all Web browsers - desktop and mobile devices<br /> &bull;    Track, measure and analyze page effectiveness with A/B testing<br /> &bull;    Ability to edit and create videos in Premiere or FCP<br /> &bull;    Upload videos to social media platforms and work with content team to get description links etc needed before upload<br /> &bull;    Familiar with posting images for Instagram, Pinterest<br /> &bull;    VERY IMPORTANT : Ability to coordinate and track everything that is done using spreadsheets (Google docs) and follow up with team to get the job done on time.<br /><br /> Apply only with<br /><br /> &bull;    3-4 URLs of HTML5 websites that are responsive and works on all mobile devices<br /> &bull;    3-4 examples of your video editing skills. Please send videos - compressed files only (360p under 4 mb)<br /> &bull;    3-4 examples demonstrating&nbsp;&nbsp;your graphics (photoshop) skills. Please send designs created in low res jpg files<br /><br /> General Qualifications Desired at Spuul<br /><br /> &bull;    General industry experience either as an employee or intern<br /> &bull;    Excellent written and verbal communication skills<br /> &bull;    Ability to work unsupervised<br /> &bull;    Desire to have fun while working hard to dent the universe<br /> &bull;    Experience in the media or online video industry a big plus<br /><br /> About Spuul<br /><br /> Spuul is a Singapore based Over the Top (OTT) video streaming service, targeted at the South Asian market and the South Asian diaspora. We take entertainment very seriously, and we&rsquo;re looking for someone who can identify problems and then help us solve them, in order to deliver unlimited, quality entertainment to our ~12 million users across the globe. <br /><br /><br /><br /><br /><br /> About The Team<br /><br /> We&#039;re about 40 of us across three locations working hard to make sure we&#039;re always ahead of the game. At Spuul, it&#039;s never &#039;just a job&#039; and life doesn&#039;t end at 5 pm. But, it doesn&#039;t begin at 9 am either! And if you think you can be a good fit, we&#039;d love for you to get to know us, so you can understand who to bother when you&#039;re facing an issue, or whom to catch when you find a mistake.<br /><br /> How We Care For Spuulers<br /><br /> Grow With Us<br /> We&rsquo;re a small team with big dreams and we&rsquo;re looking for people who aren&rsquo;t afraid to dream with us. We&rsquo;ll hire you because you know something we probably don&rsquo;t, and we&rsquo;d like you to help us fix it. We&rsquo;re a rapidly growing business in an ever-evolving industry, and we&rsquo;d like for you to be a part of this growth.<br /><br /> Your Time Is Important<br /> Whether it&rsquo;s an emergency, an occasion, or you just need a break from every day routine, our open leave policy and flexible work hours allow you to manage your personal time and business requirements such that a healthy balance is both achieved and maintained. There&rsquo;s no &lsquo;one size fits all&rsquo; recipe here, and you can decide when you&rsquo;d like some time off, and you can decide how much time you need off.<br /><br /> Only Your Work Speaks For You<br /> Just because you like wearing shorts, it doesn&rsquo;t mean you aren&rsquo;t serious about your work, contrary to popular perception. We don&rsquo;t have a dress code and we probably never will. Our CEO walks into office with his collars turned up, and you&rsquo;re free to come dressed in a three piece suit if you please! The only thing that will leave a lasting impression is every one of your contributions, no matter how big or small.<br /><br /> So when do we get to meet you?<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Skills</b>: CSS, CSS3, HTML, HTML5, JavaScript, jQuery, Web Design, Website Development <br /><b>Country</b>: Singapore<br /><a href="https://www.upwork.com/jobs/Front-end-Developer-Freelancers-amp-Full-Timers-welcomed_%7E01ecce99c66979dceb?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Front-End Web Developer / Video Editor<br /><br /> Spuul seeks a Front-End Developer cum Video Editor with minimum 2&ndash;4 years profes-sional experience to join our Marketing team in Mumbai, India. <br /><br /> In this role the candidate will work with the Marketing team to code responsive HTML 5 pages, EDMs and also be efficient in editing video for Youtube, Facebook or advertise-ments. He/She would closely work with the Creative Head and development team in Sin-gapore.<br /><br /> Requirements<br /> &bull;    Ability to design and code responsive sites and pages in HTML 5<br /> &bull;    Level 7+ skill in Adobe Photoshop &amp;amp; Illustrator<br /> &bull; Level 8+ skill in Final Cut Pro, Adobe Premiere and Compression software<br /> &bull;    Familiar with Git - to deploy landing pages or amend HTML files<br /> &bull;    Comfortable working with JavaScript<br /> &bull;    &nbsp;&nbsp;People skills to coordinate with development team, build and deploy pages to produc-tion.<br /> &bull;    &nbsp;&nbsp;Make sure pages are well optimized ( hand code HTML5 and make sure there are no extra&nbsp;&nbsp;&nbsp;scripts that slow down pages) and load quickly on all devices<br /> &bull;    Test and make sure that pages work on all Web browsers - desktop and mobile devices<br /> &bull;    Track, measure and analyze page effectiveness with A/B testing<br /> &bull;    Ability to edit and create videos in Premiere or FCP<br /> &bull;    Upload videos to social media platforms and work with content team to get description links etc needed before upload<br /> &bull;    Familiar with posting images for Instagram, Pinterest<br /> &bull;    VERY IMPORTANT : Ability to coordinate and track everything that is done using spreadsheets (Google docs) and follow up with team to get the job done on time.<br /><br /> Apply only with<br /><br /> &bull;    3-4 URLs of HTML5 websites that are responsive and works on all mobile devices<br /> &bull;    3-4 examples of your video editing skills. Please send videos - compressed files only (360p under 4 mb)<br /> &bull;    3-4 examples demonstrating&nbsp;&nbsp;your graphics (photoshop) skills. Please send designs created in low res jpg files<br /><br /> General Qualifications Desired at Spuul<br /><br /> &bull;    General industry experience either as an employee or intern<br /> &bull;    Excellent written and verbal communication skills<br /> &bull;    Ability to work unsupervised<br /> &bull;    Desire to have fun while working hard to dent the universe<br /> &bull;    Experience in the media or online video industry a big plus<br /><br /> About Spuul<br /><br /> Spuul is a Singapore based Over the Top (OTT) video streaming service, targeted at the South Asian market and the South Asian diaspora. We take entertainment very seriously, and we&rsquo;re looking for someone who can identify problems and then help us solve them, in order to deliver unlimited, quality entertainment to our ~12 million users across the globe. <br /><br /><br /><br /><br /><br /> About The Team<br /><br /> We&#039;re about 40 of us across three locations working hard to make sure we&#039;re always ahead of the game. At Spuul, it&#039;s never &#039;just a job&#039; and life doesn&#039;t end at 5 pm. But, it doesn&#039;t begin at 9 am either! And if you think you can be a good fit, we&#039;d love for you to get to know us, so you can understand who to bother when you&#039;re facing an issue, or whom to catch when you find a mistake.<br /><br /> How We Care For Spuulers<br /><br /> Grow With Us<br /> We&rsquo;re a small team with big dreams and we&rsquo;re looking for people who aren&rsquo;t afraid to dream with us. We&rsquo;ll hire you because you know something we probably don&rsquo;t, and we&rsquo;d like you to help us fix it. We&rsquo;re a rapidly growing business in an ever-evolving industry, and we&rsquo;d like for you to be a part of this growth.<br /><br /> Your Time Is Important<br /> Whether it&rsquo;s an emergency, an occasion, or you just need a break from every day routine, our open leave policy and flexible work hours allow you to manage your personal time and business requirements such that a healthy balance is both achieved and maintained. There&rsquo;s no &lsquo;one size fits all&rsquo; recipe here, and you can decide when you&rsquo;d like some time off, and you can decide how much time you need off.<br /><br /> Only Your Work Speaks For You<br /> Just because you like wearing shorts, it doesn&rsquo;t mean you aren&rsquo;t serious about your work, contrary to popular perception. We don&rsquo;t have a dress code and we probably never will. Our CEO walks into office with his collars turned up, and you&rsquo;re free to come dressed in a three piece suit if you please! The only thing that will leave a lasting impression is every one of your contributions, no matter how big or small.<br /><br /> So when do we get to meet you?<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Skills</b>: CSS, CSS3, HTML, HTML5, JavaScript, jQuery, Web Design, Website Development <br /><b>Country</b>: Singapore<br /><a href="https://www.upwork.com/jobs/Front-end-Developer-Freelancers-amp-Full-Timers-welcomed_%7E01ecce99c66979dceb?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Thu, 29 Dec 2016 13:03:52 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Front-end-Developer-Freelancers-amp-Full-Timers-welcomed_%7E01ecce99c66979dceb?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[ Front-end developer - Upwork ]]>
</title>
<link>
https://www.upwork.com/jobs/Front-end-developer_%7E017496d310d3e9dd31?source=rss
</link>
<description>
<![CDATA[
Front-End Web Developer / Video Editor<br /><br /> Spuul seeks a Front-End Developer cum Video Editor with minimum 2&ndash;4 years profes-sional experience to join our Marketing team in Mumbai, India. <br /><br /> In this role the candidate will work with the Marketing team to code responsive HTML 5 pages, EDMs and also be efficient in editing video for Youtube, Facebook or advertise-ments. He/She would closely work with the Creative Head and development team in Sin-gapore.<br /><br /> Requirements<br /> &bull;    Ability to design and code responsive sites and pages in HTML 5<br /> &bull;    Level 7+ skill in Adobe Photoshop &amp;amp; Illustrator<br /> &bull; Level 8+ skill in Final Cut Pro, Adobe Premiere and Compression software<br /> &bull;    Familiar with Git - to deploy landing pages or amend HTML files<br /> &bull;    Comfortable working with JavaScript<br /> &bull;    &nbsp;&nbsp;People skills to coordinate with development team, build and deploy pages to produc-tion.<br /> &bull;    &nbsp;&nbsp;Make sure pages are well optimized ( hand code HTML5 and make sure there are no extra&nbsp;&nbsp;&nbsp;scripts that slow down pages) and load quickly on all devices<br /> &bull;    Test and make sure that pages work on all Web browsers - desktop and mobile devices<br /> &bull;    Track, measure and analyze page effectiveness with A/B testing<br /> &bull;    Ability to edit and create videos in Premiere or FCP<br /> &bull;    Upload videos to social media platforms and work with content team to get description links etc needed before upload<br /> &bull;    Familiar with posting images for Instagram, Pinterest<br /> &bull;    VERY IMPORTANT : Ability to coordinate and track everything that is done using spreadsheets (Google docs) and follow up with team to get the job done on time.<br /><br /> Apply only with<br /><br /> &bull;    3-4 URLs of HTML5 websites that are responsive and works on all mobile devices<br /> &bull;    3-4 examples of your video editing skills. Please send videos - compressed files only (360p under 4 mb)<br /> &bull;    3-4 examples demonstrating&nbsp;&nbsp;your graphics (photoshop) skills. Please send designs created in low res jpg files<br /><br /> General Qualifications Desired at Spuul<br /><br /> &bull;    General industry experience either as an employee or intern<br /> &bull;    Excellent written and verbal communication skills<br /> &bull;    Ability to work unsupervised<br /> &bull;    Desire to have fun while working hard to dent the universe<br /> &bull;    Experience in the media or online video industry a big plus<br /><br /> About Spuul<br /><br /> Spuul is a Singapore based Over the Top (OTT) video streaming service, targeted at the South Asian market and the South Asian diaspora. We take entertainment very seriously, and we&rsquo;re looking for someone who can identify problems and then help us solve them, in order to deliver unlimited, quality entertainment to our ~12 million users across the globe. <br /><br /><br /><br /><br /><br /> About The Team<br /><br /> We&#039;re about 40 of us across three locations working hard to make sure we&#039;re always ahead of the game. At Spuul, it&#039;s never &#039;just a job&#039; and life doesn&#039;t end at 5 pm. But, it doesn&#039;t begin at 9 am either! And if you think you can be a good fit, we&#039;d love for you to get to know us, so you can understand who to bother when you&#039;re facing an issue, or whom to catch when you find a mistake.<br /><br /> How We Care For Spuulers<br /><br /> Grow With Us<br /> We&rsquo;re a small team with big dreams and we&rsquo;re looking for people who aren&rsquo;t afraid to dream with us. We&rsquo;ll hire you because you know something we probably don&rsquo;t, and we&rsquo;d like you to help us fix it. We&rsquo;re a rapidly growing business in an ever-evolving industry, and we&rsquo;d like for you to be a part of this growth.<br /><br /> Your Time Is Important<br /> Whether it&rsquo;s an emergency, an occasion, or you just need a break from every day routine, our open leave policy and flexible work hours allow you to manage your personal time and business requirements such that a healthy balance is both achieved and maintained. There&rsquo;s no &lsquo;one size fits all&rsquo; recipe here, and you can decide when you&rsquo;d like some time off, and you can decide how much time you need off.<br /><br /> Only Your Work Speaks For You<br /> Just because you like wearing shorts, it doesn&rsquo;t mean you aren&rsquo;t serious about your work, contrary to popular perception. We don&rsquo;t have a dress code and we probably never will. Our CEO walks into office with his collars turned up, and you&rsquo;re free to come dressed in a three piece suit if you please! The only thing that will leave a lasting impression is every one of your contributions, no matter how big or small.<br /><br /> So when do we get to meet you?<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Country</b>: Singapore<br /><a href="https://www.upwork.com/jobs/Front-end-developer_%7E017496d310d3e9dd31?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Front-End Web Developer / Video Editor<br /><br /> Spuul seeks a Front-End Developer cum Video Editor with minimum 2&ndash;4 years profes-sional experience to join our Marketing team in Mumbai, India. <br /><br /> In this role the candidate will work with the Marketing team to code responsive HTML 5 pages, EDMs and also be efficient in editing video for Youtube, Facebook or advertise-ments. He/She would closely work with the Creative Head and development team in Sin-gapore.<br /><br /> Requirements<br /> &bull;    Ability to design and code responsive sites and pages in HTML 5<br /> &bull;    Level 7+ skill in Adobe Photoshop &amp;amp; Illustrator<br /> &bull; Level 8+ skill in Final Cut Pro, Adobe Premiere and Compression software<br /> &bull;    Familiar with Git - to deploy landing pages or amend HTML files<br /> &bull;    Comfortable working with JavaScript<br /> &bull;    &nbsp;&nbsp;People skills to coordinate with development team, build and deploy pages to produc-tion.<br /> &bull;    &nbsp;&nbsp;Make sure pages are well optimized ( hand code HTML5 and make sure there are no extra&nbsp;&nbsp;&nbsp;scripts that slow down pages) and load quickly on all devices<br /> &bull;    Test and make sure that pages work on all Web browsers - desktop and mobile devices<br /> &bull;    Track, measure and analyze page effectiveness with A/B testing<br /> &bull;    Ability to edit and create videos in Premiere or FCP<br /> &bull;    Upload videos to social media platforms and work with content team to get description links etc needed before upload<br /> &bull;    Familiar with posting images for Instagram, Pinterest<br /> &bull;    VERY IMPORTANT : Ability to coordinate and track everything that is done using spreadsheets (Google docs) and follow up with team to get the job done on time.<br /><br /> Apply only with<br /><br /> &bull;    3-4 URLs of HTML5 websites that are responsive and works on all mobile devices<br /> &bull;    3-4 examples of your video editing skills. Please send videos - compressed files only (360p under 4 mb)<br /> &bull;    3-4 examples demonstrating&nbsp;&nbsp;your graphics (photoshop) skills. Please send designs created in low res jpg files<br /><br /> General Qualifications Desired at Spuul<br /><br /> &bull;    General industry experience either as an employee or intern<br /> &bull;    Excellent written and verbal communication skills<br /> &bull;    Ability to work unsupervised<br /> &bull;    Desire to have fun while working hard to dent the universe<br /> &bull;    Experience in the media or online video industry a big plus<br /><br /> About Spuul<br /><br /> Spuul is a Singapore based Over the Top (OTT) video streaming service, targeted at the South Asian market and the South Asian diaspora. We take entertainment very seriously, and we&rsquo;re looking for someone who can identify problems and then help us solve them, in order to deliver unlimited, quality entertainment to our ~12 million users across the globe. <br /><br /><br /><br /><br /><br /> About The Team<br /><br /> We&#039;re about 40 of us across three locations working hard to make sure we&#039;re always ahead of the game. At Spuul, it&#039;s never &#039;just a job&#039; and life doesn&#039;t end at 5 pm. But, it doesn&#039;t begin at 9 am either! And if you think you can be a good fit, we&#039;d love for you to get to know us, so you can understand who to bother when you&#039;re facing an issue, or whom to catch when you find a mistake.<br /><br /> How We Care For Spuulers<br /><br /> Grow With Us<br /> We&rsquo;re a small team with big dreams and we&rsquo;re looking for people who aren&rsquo;t afraid to dream with us. We&rsquo;ll hire you because you know something we probably don&rsquo;t, and we&rsquo;d like you to help us fix it. We&rsquo;re a rapidly growing business in an ever-evolving industry, and we&rsquo;d like for you to be a part of this growth.<br /><br /> Your Time Is Important<br /> Whether it&rsquo;s an emergency, an occasion, or you just need a break from every day routine, our open leave policy and flexible work hours allow you to manage your personal time and business requirements such that a healthy balance is both achieved and maintained. There&rsquo;s no &lsquo;one size fits all&rsquo; recipe here, and you can decide when you&rsquo;d like some time off, and you can decide how much time you need off.<br /><br /> Only Your Work Speaks For You<br /> Just because you like wearing shorts, it doesn&rsquo;t mean you aren&rsquo;t serious about your work, contrary to popular perception. We don&rsquo;t have a dress code and we probably never will. Our CEO walks into office with his collars turned up, and you&rsquo;re free to come dressed in a three piece suit if you please! The only thing that will leave a lasting impression is every one of your contributions, no matter how big or small.<br /><br /> So when do we get to meet you?<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Country</b>: Singapore<br /><a href="https://www.upwork.com/jobs/Front-end-developer_%7E017496d310d3e9dd31?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Thu, 29 Dec 2016 12:38:45 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Front-end-developer_%7E017496d310d3e9dd31?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[ Web-Based DICOM Image Viewer Updates - Upwork ]]>
</title>
<link>
https://www.upwork.com/jobs/Web-Based-DICOM-Image-Viewer-Updates_%7E016f6b889a09d09d43?source=rss
</link>
<description>
<![CDATA[
We have a DICOM Image Viewer built into our software suite.&nbsp;&nbsp;We need a developer with the following skills to modify the viewer, add a few features, and possibly even assist with a redesign of the tool, in general.&nbsp;&nbsp;This is a short-term project with defined goals and tasks, but c
]]>
<![CDATA[
ould be extended into an ongoing project for the right resource.<br /><br /> Skills Required - <br /> &bull;    DICOM<br /> &bull; JavaScript<br /> &bull;    jQuery<br /> &bull;    Bootstrap<br /> &bull;    HTML5<br /> &bull;    CSS3<br /> &bull;    Linux<br /><br /> Laravel, and PHP would be a nice addition to the skill set, but not necessary.<br /> The resource must speak English well enough to communicate with us via Skype and/or Upwork Messenger app.<br /><br /> Task List<br /> &bull;    Add support for Full Screen mode<br /> &bull;    Replace icons with SVG icon suite we had created<br /> &bull;    Adjust the viewer responsiveness for various screen sizes, including mobile devices<br /> &bull;    Add support for 3D viewing.&nbsp;&nbsp;It currently does not render 3D data sets in 3D. There are lots of plugins for this that should work with the project.<br /> &bull;    Add ability to select different performance tiers as a user setting.&nbsp;&nbsp;(Lossless JPEG vs Lossy JPEG) User could select high quality images, but be warned that it will take longer to load image sets, and may use more data on mobile devices when they switch to the setting.&nbsp;&nbsp;The lower setting will display lossy JPEGs, but be much faster, in general.<br /><br /> The next two may take some time, so we will begin with the items above, first.<br /> &bull;    Make recommendations and adjustments to the look and feel of the viewer (How can we make it sexier?&nbsp;&nbsp;We may need to find a graphic resource for this piece.)<br /> &bull;    Add ability to burn the DICOM image set off to a CD, or USB flash drive.&nbsp;&nbsp;We already have the ability to export the actual DICOM out to a folder via the viewer, but this will require making a stand alone version of our tools to burn to the CD with the DICOM data for review of the images.<br /><br /> To be considered, you MUST have previous experience on a DICOM Image viewer, preferably a web-based viewer utilizing the technology listed above.&nbsp;&nbsp;If you have the experience required, please apply by describing the relevant project or projects you have worked on, the technology involved, and copy/paste the list above with a score next to the skill rating your understanding from 0-10, 10 being an expert.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web &amp; Mobile Design<br /><b>Skills</b>: Bootstrap, CSS3, HTML5, JavaScript, jQuery, PHP <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Web-Based-DICOM-Image-Viewer-Updates_%7E016f6b889a09d09d43?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
We have a DICOM Image Viewer built into our software suite.&nbsp;&nbsp;We need a developer with the following skills to modify the viewer, add a few features, and possibly even assist with a redesign of the tool, in general.&nbsp;&nbsp;This is a short-term project with defined goals and tasks, but could be extended into an ongoing project for the right resource.<br /><br /> Skills Required - <br /> &bull;    DICOM<br /> &bull;    JavaScript<br /> &bull;    jQuery<br /> &bull;    Bootstrap<br /> &bull;    HTML5<br /> &bull;    CSS3<br /> &bull; Linux<br /><br /> Laravel, and PHP would be a nice addition to the skill set, but not necessary.<br /> The resource must speak English well enough to communicate with us via Skype and/or Upwork Messenger app.<br /><br /> Task List<br /> &bull;    Add support for Full Screen mode<br /> &bull;    Replace icons with SVG icon suite we had created<br /> &bull;    Adjust the viewer responsiveness for various screen sizes, including mobile devices<br /> &bull;    Add support for 3D viewing.&nbsp;&nbsp;It currently does not render 3D data sets in 3D. There are lots of plugins for this that should work with the project.<br /> &bull;    Add ability to select different performance tiers as a user setting.&nbsp;&nbsp;(Lossless JPEG vs Lossy JPEG) User could select high quality images, but be warned that it will take longer to load image sets, and may use more data on mobile devices when they switch to the setting.&nbsp;&nbsp;The lower setting will display lossy JPEGs, but be much faster, in general.<br /><br /> The next two may take some time, so we will begin with the items above, first.<br /> &bull;    Make recommendations and adjustments to the look and feel of the viewer (How can we make it sexier?&nbsp;&nbsp;We may need to find a graphic resource for this piece.)<br /> &bull;    Add ability to burn the DICOM image set off to a CD, or USB flash drive.&nbsp;&nbsp;We already have the ability to export the actual DICOM out to a folder via the viewer, but this will require making a stand alone version of our tools to burn to the CD with the DICOM data for review of the images.<br /><br /> To be considered, you MUST have previous experience on a DICOM Image viewer, preferably a web-based viewer utilizing the technology listed above.&nbsp;&nbsp;If you have the experience required, please apply by describing the relevant project or projects you have worked on, the technology involved, and copy/paste the list above with a score next to the skill rating your understanding from 0-10, 10 being an expert.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web &amp; Mobile Design<br /><b>Skills</b>: Bootstrap, CSS3, HTML5, JavaScript, jQuery, PHP <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Web-Based-DICOM-Image-Viewer-Updates_%7E016f6b889a09d09d43?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Wed, 28 Dec 2016 15:28:16 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Web-Based-DICOM-Image-Viewer-Updates_%7E016f6b889a09d09d43?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[ Web Developer - Upwork ]]>
</title>
<link>
https://www.upwork.com/jobs/Web-Developer_%7E0159231264442255ea?source=rss
</link>
<description>
<![CDATA[
Web Developer<br /><br /> Write well designed, testable, efficient code by using best software development practices<br /><br /> Payment 3$/Hr<br /><br /> Do Not Apply for more than amount per hour that specified, as your application will get rejected.<br /><br /> ✔ Have The Preferred Qualifications.<br /><br /> ✔ Able to work with PHP, MySQL, HTML, CSS, MooTools, jQuery, AJAX, JavaScript.<br /><br /> ✔ Able to work with WordPress, and Woocommerce &amp;quot;are extra&amp;quot;.<br /><br /> ✔ Able to deliver within the deadline or time you decide for each assignment or task that it can be finished. (As the hourly time you estimate and day for delivery of each assignment or project).<br /><br /> ✔ Only Log the time you have worked on the project or assignment.<br /> (Do not log any meetings or Skype talk or any online meeting in any instant messenger or the time you still learning something). <br /><br /> ✔ but depending on communications and quick reply and deliver tasks you will be paid weekly bonus depends on performance on the job.<br /><br /> Work assignments can be:<br /> ✔ Script Fix.<br /> ✔ Script Improvement.<br /> ✔ Script Testing، and write the testing report.<br /> ✔ Script Editing.<br /> ✔ Script Module Creation.<br /><br /><br /> Any higher than this price application will be rejected or will offer you the price within the budget limit for a trial period up to 4 weeks.<br /><br /><br /> ✔ English Test is required to pass to know you understand English well.<br /><br /><br /> The Only Independent Contractor will be approved.<br /><br /> Policy and agreement with the contractor:&nbsp;&nbsp;<br /><br /> If you able to do the job right, you will get five star rating and finish each task within the time required or the time we agree on.<br /><br /> ** Must understand and agree that non-disclosure agreement (NDA) Under no circumstance to publish the files to (Public) or file sharing websites or ideas of project to a third party or sell it under no condition all files are copyright to us which are the owner of the files even if you modify it or edit it on anyway، once this project end you must terminate any files on your computer or server or dropbox **<br /><br /> File delivery: <br /><br /> ** Files must be sent from dropbox and then terminate the files from dropbox once we confirm with you we receive it، you will attach the files by upwork message and choose option of dropbox of your account. **<br /><br /><br /> * Please write the word &#039;Web Developer&#039; when you reply to confirm you read the whole post *<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web &amp; Mobile Design<br /><b>Skills</b>: Adobe Photoshop, Bootstrap, CSS3, Graphic Design, HTML5, Java, JavaScript, jQuery, Mobile Programming, Mobile UI Design, MySQL Programming, PHP, Prototype Javascript Framework, Responsive Web Design, Search Engine Optimization (SEO), Web Design, Website Development, WordPress, Wordpress Plugin <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Web-Developer_%7E0159231264442255ea?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Web Developer<br /><br /> Write well designed, testable, efficient code by using best software development practices<br /><br /> Payment 3$/Hr<br /><br /> Do Not Apply for more than amount per hour that specified, as your application will get rejected.<br /><br /> ✔ Have The Preferred Qualifications.<br /><br /> ✔ Able to work with PHP, MySQL, HTML, CSS, MooTools, jQuery, AJAX, JavaScript.<br /><br /> ✔ Able to work with WordPress, and Woocommerce &amp;quot;are extra&amp;quot;.<br /><br /> ✔ Able to deliver within the deadline or time you decide for each assignment or task that it can be finished. (As the hourly time you estimate and day for delivery of each assignment or project).<br /><br /> ✔ Only Log the time you have worked on the project or assignment.<br /> (Do not log any meetings or Skype talk or any online meeting in any instant messenger or the time you still learning something). <br /><br /> ✔ but depending on communications and quick reply and deliver tasks you will be paid weekly bonus depends on performance on the job.<br /><br /> Work assignments can be:<br /> ✔ Script Fix.<br /> ✔ Script Improvement.<br /> ✔ Script Testing، and write the testing report.<br /> ✔ Script Editing.<br /> ✔ Script Module Creation.<br /><br /><br /> Any higher than this price application will be rejected or will offer you the price within the budget limit for a trial period up to 4 weeks.<br /><br /><br /> ✔ English Test is required to pass to know you understand English well.<br /><br /><br /> The Only Independent Contractor will be approved.<br /><br /> Policy and agreement with the contractor:&nbsp;&nbsp;<br /><br /> If you able to do the job right, you will get five star rating and finish each task within the time required or the time we agree on.<br /><br /> ** Must understand and agree that non-disclosure agreement (NDA) Under no circumstance to publish the files to (Public) or file sharing websites or ideas of project to a third party or sell it under no condition all files are copyright to us which are the owner of the files even if you modify it or edit it on anyway، once this project end you must terminate any files on your computer or server or dropbox **<br /><br /> File delivery: <br /><br /> ** Files must be sent from dropbox and then terminate the files from dropbox once we confirm with you we receive it، you will attach the files by upwork message and choose option of dropbox of your account. **<br /><br /><br /> * Please write the word &#039;Web Developer&#039; when you reply to confirm you read the whole post *<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web &amp; Mobile Design<br /><b>Skills</b>: Adobe Photoshop, Bootstrap, CSS3, Graphic Design, HTML5, Java, JavaScript, jQuery, Mobile Programming, Mobile UI Design, MySQL Programming, PHP, Prototype Javascript Framework, Responsive Web Design, Search Engine Optimization (SEO), Web Design, Website Development, WordPress, Wordpress Plugin <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Web-Developer_%7E0159231264442255ea?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Wed, 28 Dec 2016 13:00:45 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Web-Developer_%7E0159231264442255ea?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
make a web based auto bidder aplication for freelancer(.)com - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/make-web-based-auto-bidder-aplication-for-freelancer-com_%7E014971eb4deb0d971b?source=rss
</link>
<description>
<![CDATA[
We are looking for a auto biding application for freelancer(.)com. We want a script to pull the Newest jobs that are in our skills category.<br /><br /> I can place auto bids via mobile app that uses the android application or windows software.<br /><br /> Let me know if you can make that and if so a time frame and cost. <br /><br /> Thanks.<br /><br /><b>Budget</b>: $45 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Mobile Development<br /><b>Skills</b>: Android, Android App Development, iOS Development, iPhone App Development, JavaScript <br /><b>Country</b>: India<br /><a href="https://www.upwork.com/jobs/make-web-based-auto-bidder-aplication-for-freelancer-com_%7E014971eb4deb0d971b?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
We are looking for a auto biding application for freelancer(.)com. We want a script to pull the Newest jobs that are in our skills category.<br /><br /> I can place auto bids via mobile app that uses the android application or windows software.<br /><br /> Let me know if you can make that and if so a time frame and cost. <br /><br /> Thanks.<br /><br /><b>Budget</b>: $45 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Mobile Development<br /><b>Skills</b>: Android, Android App Development, iOS Development, iPhone App Development, JavaScript <br /><b>Country</b>: India<br /><a href="https://www.upwork.com/jobs/make-web-based-auto-bidder-aplication-for-freelancer-com_%7E014971eb4deb0d971b?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Tue, 27 Dec 2016 19:12:31 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/make-web-based-auto-bidder-aplication-for-freelancer-com_%7E014971eb4deb0d971b?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Live Chat Artificial Intelligence Chatbots development - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Live-Chat-Artificial-Intelligence-Chatbots-development_%7E01641541295b8e7b00?source=rss
</link>
<description>
<![CDATA[
We are needing to develop Artificial Intelligence Chatbots development using platforms such as Twilio and&nbsp;&nbsp;Slack Api.ai of google <br /> Having experience with Natrual speech language processing is a major plus<br /> We are looking to build an omni channel AI virtual asssitant live chat th
]]>
<![CDATA[
at can answer queries from multiple channels from web from facebook twitter linked in on the website on mobile and also inbound calling and outbound calling<br /> this artificial intellegence chat bot must be able to answer the phone answer complex questions use AI NLP and also make outbound calls<br /> We need the company to have good knowledge of platform as a service where you are building this not from ground scratch but platfroms like twilio tht have functionality for AI chatbot build in and youre more focued on decesion making process building for chat bots<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Scripts &amp; Utilities<br /><b>Skills</b>: API Development, Artificial Intelligence, Chatbot Development, Heroku, Lisp, Live Chat Software, Mobile App Development, Prolog, Python, Salesforce App Development, Smalltalk, Twilio API <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Live-Chat-Artificial-Intelligence-Chatbots-development_%7E01641541295b8e7b00?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
We are needing to develop Artificial Intelligence Chatbots development using platforms such as Twilio and&nbsp;&nbsp;Slack Api.ai of google <br /> Having experience with Natrual speech language processing is a major plus<br /> We are looking to build an omni channel AI virtual asssitant live chat that can answer queries from multiple channels from web from facebook twitter linked in on the website on mobile and also inbound calling and outbound calling<br /> this artificial intellegence chat bot must be able to answer the phone answer complex questions use AI NLP and also make outbound calls<br /> We need the company to have good knowledge of platform as a service where you are building this not from ground scratch but platfroms like twilio tht have functionality for AI chatbot build in and youre more focued on decesion making process building for chat bots<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Scripts &amp; Utilities<br /><b>Skills</b>: API Development, Artificial Intelligence, Chatbot Development, Heroku, Lisp, Live Chat Software, Mobile App Development, Prolog, Python, Salesforce App Development, Smalltalk, Twilio API <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Live-Chat-Artificial-Intelligence-Chatbots-development_%7E01641541295b8e7b00?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Tue, 20 Dec 2016 16:26:50 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Live-Chat-Artificial-Intelligence-Chatbots-development_%7E01641541295b8e7b00?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[ Mobile App/ software developer - Upwork ]]>
</title>
<link>
https://www.upwork.com/jobs/Mobile-App-software-developer_%7E01d7e8775f54b7b5be?source=rss
</link>
<description>
<![CDATA[
Looking for an experienced software developer with a creative vision. Experience with payment, social media, Java script, Google Maps, live video chat, and such usage is required! Looking forward to getting this beautiful project up and running.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Mobile Development<br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Mobile-App-software-developer_%7E01d7e8775f54b7b5be?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Looking for an experienced software developer with a creative vision. Experience with payment, social media, Java script, Google Maps, live video chat, and such usage is required! Looking forward to getting this beautiful project up and running.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Mobile Development<br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Mobile-App-software-developer_%7E01d7e8775f54b7b5be?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Sun, 18 Dec 2016 20:07:50 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Mobile-App-software-developer_%7E01d7e8775f54b7b5be?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Full-Stack Game Developer for Emulation Project - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Full-Stack-Game-Developer-for-Emulation-Project_%7E01ece13422c78834f6?source=rss
</link>
<description>
<![CDATA[
Your duties would include<br /> - Core stability management, fix issues that might arise with the up-time of the game server.<br /> - Overlook scripts and make sure they work appropriately. <br /> - Fix issues to game-content and environment that is reported by users.<br /><br /> We have built this software from the ground up, using the open-source &amp;quot;https://github.com/mangosone&amp;quot; so all that is required from here on is the testing, overlooking scripts, and optimizing the core stability. <br /><br /> You as a freelancer should be friendly but also professional. You should have a passion for online games, specifically &amp;quot;Massively Multiplayer Online&amp;quot; Games. You will be required to engage with the community and update our users about fixes that you&#039;ve done on a daily basis.<br /><br /> You should install the open-source and run it on your localhost to get familiar with the code if you haven&#039;t worked with it previously. I&#039;m only interested in hiring motivated and dedicated developers. This is a &amp;quot;on-going&amp;quot; project, so even though you have completed all tasks that we require we will hire you again in the future.<br /><br /> WE ARE NOT INTERESTED IN MOBILE-APP DEVELOPERS - THIS IS A SERIOUS PROJECT&nbsp;&nbsp;AND IF YOU HAVE NO PC GAME DEVELOPER EXPERIENCE, EITHER IN C, C# OR C++ USING MYSQL, SQL AND/OR LUA. THIS IS NOT A PROJECT FOR YOU AND IT&#039;S BETTER NOT WASTE OUR TIME.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Other - Software Development<br /><b>Skills</b>: C#, C++, Database Management, Lua, MySQL Programming, SQL <br /><b>Country</b>: Sweden<br /><a href="https://www.upwork.com/jobs/Full-Stack-Game-Developer-for-Emulation-Project_%7E01ece13422c78834f6?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Your duties would include<br /> - Core stability management, fix issues that might arise with the up-time of the game server.<br /> - Overlook scripts and make sure they work appropriately. <br /> - Fix issues to game-content and environment that is reported by users.<br /><br /> We have built this software from the ground up, using the open-source &amp;quot;https://github.com/mangosone&amp;quot; so all that is required from here on is the testing, overlooking scripts, and optimizing the core stability. <br /><br /> You as a freelancer should be friendly but also professional. You should have a passion for online games, specifically &amp;quot;Massively Multiplayer Online&amp;quot; Games. You will be required to engage with the community and update our users about fixes that you&#039;ve done on a daily basis.<br /><br /> You should install the open-source and run it on your localhost to get familiar with the code if you haven&#039;t worked with it previously. I&#039;m only interested in hiring motivated and dedicated developers. This is a &amp;quot;on-going&amp;quot; project, so even though you have completed all tasks that we require we will hire you again in the future.<br /><br /> WE ARE NOT INTERESTED IN MOBILE-APP DEVELOPERS - THIS IS A SERIOUS PROJECT&nbsp;&nbsp;AND IF YOU HAVE NO PC GAME DEVELOPER EXPERIENCE, EITHER IN C, C# OR C++ USING MYSQL, SQL AND/OR LUA. THIS IS NOT A PROJECT FOR YOU AND IT&#039;S BETTER NOT WASTE OUR TIME.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Other - Software Development<br /><b>Skills</b>: C#, C++, Database Management, Lua, MySQL Programming, SQL <br /><b>Country</b>: Sweden<br /><a href="https://www.upwork.com/jobs/Full-Stack-Game-Developer-for-Emulation-Project_%7E01ece13422c78834f6?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Fri, 16 Dec 2016 10:13:26 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Full-Stack-Game-Developer-for-Emulation-Project_%7E01ece13422c78834f6?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[ Mobile VoIP App - Ionic Framework - Upwork ]]>
</title>
<link>
https://www.upwork.com/jobs/Mobile-VoIP-App-Ionic-Framework_%7E01d857c594c8df9c8d?source=rss
</link>
<description>
<![CDATA[
Develope a Hybrid VoIP and Messaging App based on Ionic Framework:<br /><br /> - Javascripts / AngularJS<br /> - CSS / HTML<br /> - WebRTC (Phonertc: http://phonertc.io/)<br /> - GIT <br /><br /> Developer is required to be online via Skype at all time and work on hosted private repository, all codes must be developed in our environment and uploaded to our GIT repository server.<br /><br /> Developer will connect to our virtual machine using Remote Desktop to develope and compile.<br /><br /> Writing a guide or script to establish compiling starting from scratch is mandatory.<br /><br /> Developer must start with draft design on Objects and Classes before coding and Code must be well commented and structure. changes on final code must be updated back to draft design.<br /><br /> HIGHLIGHTS:<br /> The application will include procedure for the following:<br /> 1) Registering / Logging new users (via SMS or callerID verification).<br /> 2) Purchasing credit. (CIMB Bank, FPX Payment, Paypal, Stripe)<br /> 3) User settings page. (Change password, email, phone number, callerID, forward Number)<br /> 4) Contacts list page. Each contact can be sent an SMS message or called using the app.<br /> 5) Option to switch from Headset/Speaker/Bluetooth<br /> 6) Audio and Video calling based on opus between users<br /> 7) Option to record call in phone (auto record or in-call record button)<br /> 8) Able to select outbound CallerID (client/server code)<br /> 9) Callback Request (Client/server code)<br /><br /><b>Budget</b>: $2,000 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Mobile Development<br /><b>Skills</b>: CSS3, Git, HTML5, JQuery Mobile, VOIP Software, WebRTC <br /><a href="https://www.upwork.com/jobs/Mobile-VoIP-App-Ionic-Framework_%7E01d857c594c8df9c8d?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Develope a Hybrid VoIP and Messaging App based on Ionic Framework:<br /><br /> - Javascripts / AngularJS<br /> - CSS / HTML<br /> - WebRTC (Phonertc: http://phonertc.io/)<br /> - GIT <br /><br /> Developer is required to be online via Skype at all time and work on hosted private repository, all codes must be developed in our environment and uploaded to our GIT repository server.<br /><br /> Developer will connect to our virtual machine using Remote Desktop to develope and compile.<br /><br /> Writing a guide or script to establish compiling starting from scratch is mandatory.<br /><br /> Developer must start with draft design on Objects and Classes before coding and Code must be well commented and structure. changes on final code must be updated back to draft design.<br /><br /> HIGHLIGHTS:<br /> The application will include procedure for the following:<br /> 1) Registering / Logging new users (via SMS or callerID verification).<br /> 2) Purchasing credit. (CIMB Bank, FPX Payment, Paypal, Stripe)<br /> 3) User settings page. (Change password, email, phone number, callerID, forward Number)<br /> 4) Contacts list page. Each contact can be sent an SMS message or called using the app.<br /> 5) Option to switch from Headset/Speaker/Bluetooth<br /> 6) Audio and Video calling based on opus between users<br /> 7) Option to record call in phone (auto record or in-call record button)<br /> 8) Able to select outbound CallerID (client/server code)<br /> 9) Callback Request (Client/server code)<br /><br /><b>Budget</b>: $2,000 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Mobile Development<br /><b>Skills</b>: CSS3, Git, HTML5, JQuery Mobile, VOIP Software, WebRTC <br /><a href="https://www.upwork.com/jobs/Mobile-VoIP-App-Ionic-Framework_%7E01d857c594c8df9c8d?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Tue, 13 Dec 2016 08:14:31 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Mobile-VoIP-App-Ionic-Framework_%7E01d857c594c8df9c8d?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Telemarketers - B2B and Software Domain (Australia) - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Telemarketers-B2B-and-Software-Domain-Australia_%7E0157cebb1449ad027a?source=rss
</link>
<description>
<![CDATA[
We are a leading provider of Mobile Development &amp;amp; Mobile Testing services in the Enterprise Mobility space. You can read more about us at www.mobilepundits.com. We require an experienced cold caller (for NSW, VIC and QLD ) to call through our lists seeking potential customers.<br /><br /> We will provide a script for you to follow. Work for two hours a day (9:00 AM to 10:00 AM and any one hour between 3:00 PM to 5:00 local time) Monday to Thursday. Strong English and communication skills are a must. <br /><br /> Required experience: B2B Sales, Software Sales, Cold calling<br /><br /> Be well versed with what we do<br /> Cold call, direct email, and perform other lead generation activities.<br /> Obtain, qualify or verify customer information, including address, phone number<br /> Follow up on prospective leads.<br /> Schedule appointments for our CEO and CTO.<br /> Maintains database by entering, verifying, and backing up data.<br /> Report on a weekly basis<br /><br /> Timeline: Mar 20 to May 25<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Sales &amp; Marketing &gt; Telemarketing &amp; Telesales<br /><b>Skills</b>: Appointment Setting, Cold Calling, Records Management, Sales, Telemarketing, Telephone Handling <br /><a href="https://www.upwork.com/jobs/Telemarketers-B2B-and-Software-Domain-Australia_%7E0157cebb1449ad027a?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
We are a leading provider of Mobile Development &amp;amp; Mobile Testing services in the Enterprise Mobility space. You can read more about us at www.mobilepundits.com. We require an experienced cold caller (for NSW, VIC and QLD ) to call through our lists seeking potential customers.<br /><br /> We will provide a script for you to follow. Work for two hours a day (9:00 AM to 10:00 AM and any one hour between 3:00 PM to 5:00 local time) Monday to Thursday. Strong English and communication skills are a must. <br /><br /> Required experience: B2B Sales, Software Sales, Cold calling<br /><br /> Be well versed with what we do<br /> Cold call, direct email, and perform other lead generation activities.<br /> Obtain, qualify or verify customer information, including address, phone number<br /> Follow up on prospective leads.<br /> Schedule appointments for our CEO and CTO.<br /> Maintains database by entering, verifying, and backing up data.<br /> Report on a weekly basis<br /><br /> Timeline: Mar 20 to May 25<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Sales &amp; Marketing &gt; Telemarketing &amp; Telesales<br /><b>Skills</b>: Appointment Setting, Cold Calling, Records Management, Sales, Telemarketing, Telephone Handling <br /><a href="https://www.upwork.com/jobs/Telemarketers-B2B-and-Software-Domain-Australia_%7E0157cebb1449ad027a?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Fri, 09 Dec 2016 17:35:25 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Telemarketers-B2B-and-Software-Domain-Australia_%7E0157cebb1449ad027a?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Telemarketers - B2B and Software Domain (US East Coast) - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Telemarketers-B2B-and-Software-Domain-East-Coast_%7E015e213e7684bd848f?source=rss
</link>
<description>
<![CDATA[
We are a leading provider of Mobile Development &amp;amp; Mobile Testing services in the Enterprise Mobility space. We require an experienced cold caller (for New York City and New Jersey) to call through our lists seeking potential customers.<br /><br /> We will provide a script for you to follow.
]]>
<![CDATA[
Work for two hours a day (9:00 AM to 10:00 AM EST and any one hour between 3:00 PM to 5:00 PM EST) Monday to Thursday. Strong English and communication skills are a must. <br /><br /> Required experience: B2B Sales, Software Sales, Cold calling<br /><br /> Be well versed with what we do<br /> Cold call, direct email, and perform other lead generation activities.<br /> Obtain, qualify or verify customer information, including address, phone number<br /> Follow up on prospective leads.<br /> Schedule appointments for our CEO and CTO.<br /> Maintains database by entering, verifying, and backing up data.<br /> Report on a weekly basis<br /><br /> Timeline: Jan 16 to Mar 16<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Sales &amp; Marketing &gt; Telemarketing &amp; Telesales<br /><b>Skills</b>: Appointment Setting, Cold Calling, Records Management, Sales, Telemarketing, Telephone Handling <br /><a href="https://www.upwork.com/jobs/Telemarketers-B2B-and-Software-Domain-East-Coast_%7E015e213e7684bd848f?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
We are a leading provider of Mobile Development &amp;amp; Mobile Testing services in the Enterprise Mobility space. We require an experienced cold caller (for New York City and New Jersey) to call through our lists seeking potential customers.<br /><br /> We will provide a script for you to follow. Work for two hours a day (9:00 AM to 10:00 AM EST and any one hour between 3:00 PM to 5:00 PM EST) Monday to Thursday. Strong English and communication skills are a must. <br /><br /> Required experience: B2B Sales, Software Sales, Cold calling<br /><br /> Be well versed with what we do<br /> Cold call, direct email, and perform other lead generation activities.<br /> Obtain, qualify or verify customer information, including address, phone number<br /> Follow up on prospective leads.<br /> Schedule appointments for our CEO and CTO.<br /> Maintains database by entering, verifying, and backing up data.<br /> Report on a weekly basis<br /><br /> Timeline: Jan 16 to Mar 16<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Sales &amp; Marketing &gt; Telemarketing &amp; Telesales<br /><b>Skills</b>: Appointment Setting, Cold Calling, Records Management, Sales, Telemarketing, Telephone Handling <br /><a href="https://www.upwork.com/jobs/Telemarketers-B2B-and-Software-Domain-East-Coast_%7E015e213e7684bd848f?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Fri, 09 Dec 2016 17:31:25 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Telemarketers-B2B-and-Software-Domain-East-Coast_%7E015e213e7684bd848f?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
We search for already existing Adult cam software! - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/search-for-already-existing-Adult-cam-software_%7E0181587ea82f08206b?source=rss
</link>
<description>
<![CDATA[
Hello Freelancers, we are searching for Adult webcam software. So if you are a developer or you know good software that already exist. The person that can give us the golden tip get $50 euro and if you have a complete script we can talk about the possibilities. Please read the specs and contact us. If your tip is good enough for us we directly award the job and close it so you have 50$.<br /><br /> What do we need:<br /> - A quality coded Adult webcam software that is not stolen or re-build. <br /> - This software need to be ready for mobile phones<br /> - We don&#039;t want to pay more than $4000 for it<br /> - The adult cam site needs to be directly ready. So we don&#039;t have time for development.<br /> - Open source will be great<br /> - The software needs to have several features. <br /> - The script needs to have a model area, client and administrator area<br /> - Recommend technoligies, Java and JSP, Javascript/Ajax, CSS, MySQL, Flash/SWF<br /> ,Red5 streaming server php<br /> - Without hosting or other services that we have to pay monthly<br /><br /> We like http://tinyurl.com/hh36uzc but his service is really bad. <br /><br /> More tips are allowed. There is a lot of software but we can&#039;t compare this. If you create one by yourself let us know (as developer). If this is interesting we want to buy a license.<br /> So this is not a job that we start directly, but we want tips and pay when the right tip is there. We absolutely​ give away that $50 to the golden tip!&nbsp;&nbsp;<br /><br /><br /><br /><b>Budget</b>: $50 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Other - Software Development<br /><b>Skills</b>: PHP, Research, Software Licensing <br /><b>Country</b>: Netherlands<br /><a href="https://www.upwork.com/jobs/search-for-already-existing-Adult-cam-software_%7E0181587ea82f08206b?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Hello Freelancers, we are searching for Adult webcam software. So if you are a developer or you know good software that already exist. The person that can give us the golden tip get $50 euro and if you have a complete script we can talk about the possibilities. Please read the specs and contact us. If your tip is good enough for us we directly award the job and close it so you have 50$.<br /><br /> What do we need:<br /> - A quality coded Adult webcam software that is not stolen or re-build. <br /> - This software need to be ready for mobile phones<br /> - We don&#039;t want to pay more than $4000 for it<br /> - The adult cam site needs to be directly ready. So we don&#039;t have time for development.<br /> - Open source will be great<br /> - The software needs to have several features. <br /> - The script needs to have a model area, client and administrator area<br /> - Recommend technoligies, Java and JSP, Javascript/Ajax, CSS, MySQL, Flash/SWF<br /> ,Red5 streaming server php<br /> - Without hosting or other services that we have to pay monthly<br /><br /> We like http://tinyurl.com/hh36uzc but his service is really bad. <br /><br /> More tips are allowed. There is a lot of software but we can&#039;t compare this. If you create one by yourself let us know (as developer). If this is interesting we want to buy a license.<br /> So this is not a job that we start directly, but we want tips and pay when the right tip is there. We absolutely​ give away that $50 to the golden tip!&nbsp;&nbsp;<br /><br /><br /><br /><b>Budget</b>: $50 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Other - Software Development<br /><b>Skills</b>: PHP, Research, Software Licensing <br /><b>Country</b>: Netherlands<br /><a href="https://www.upwork.com/jobs/search-for-already-existing-Adult-cam-software_%7E0181587ea82f08206b?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Fri, 09 Dec 2016 10:55:28 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/search-for-already-existing-Adult-cam-software_%7E0181587ea82f08206b?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
GAME PROGRAMMING FOR WEB AND GAME DOWNLOADABLE APPS REQUIRED (FOR EXAMPLE, Who Want to Be A Millionnaire, Ruzzle, Scrabble, Crossword Compiler kind of games but mine have very many designs) - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/GAME-PROGRAMMING-FOR-WEB-AND-GAME-DOWNLOADABLE-APPS-REQUIRED-FOR-EXAMPLE-Who-Want-Millionnaire-Ruzzle-Scrabble-Crossword-Compiler-kind-games-but-mine-have-very-many-designs_%7E0105b3055d378ec033?source=rss
</link>
<description>
<![CDATA[
I the author of Artschiz Word-and-Number Puzzle Games, have conceptualized using Microsoft PowerPoint,&nbsp;&nbsp;a SOFTWARE for Puzzle Games (requiring accompanying HARDWARE components) containing words, numbers, pictures, graphics and video clips to make easy the playing of the proposed games which are described in further detail on Exhibit A to be shown to potential, qualified programmers​<br /><br /> 1. Program/develop&nbsp;&nbsp;software and the hardware components and, according to the specifications and instructions of the client, must have components that can easily be serviced and maintained anywhere in the world.<br /> 2. Divide work into phases (3 one-month Phases suggested by Author/creator) and deliver fully-tested, playable game sets every month<br /> 3. Program for web and downloadable apps game sets for the general public, and for students in kindergarten, pimary, secondary and tertiary educatuional levels<br /> 4. Prepare and submit to author (Client) transaction outline stating project milestones <br /> 5. The Developer shall afterward give the Client User&rsquo;s Guides (Manuals &ndash; digital and print) and ample time to ask questions and explore the software and hardware developed and their functionality until the Client understands all that there is in the use of the software and hardware so designed.<br /> 7. Be ready to add design and other industry-standard values to make the finished work internationally marketable<br /> 6. The Developer agrees to respond to any reasonable request for assistance made by the Client regarding the software and the hardware component within an agreed time frame when necessary.<br /><br /> ​<br /><br /> 1. Ability to build or, if such already exists, lease a search.game engine to generate games categories in the Client&#039;s many designs and shapes.&nbsp;&nbsp;Knowledge and skills with games like &#039;Who Wants to Be A Millionaire&#039;, Scrabble, Crossword Compiler, Ruzzle, will be useful.<br /> 2. Other knowledge and skills:<br /> a.    Array<br /> b.    Pattern matching<br /> c.    Sequence theory<br /> d.    Matrix theory<br /> e.    Regular expression<br /> f.    Java Script<br /> g.    Geometry <br /><br /><br /><b>Budget</b>: $1,000 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Game Development<br /><b>Skills</b>: C++, Game Programming, Graphic Design, JavaScript, Mobile App Development, Web Design <br /><b>Country</b>: Nigeria<br /><a href="https://www.upwork.com/jobs/GAME-PROGRAMMING-FOR-WEB-AND-GAME-DOWNLOADABLE-APPS-REQUIRED-FOR-EXAMPLE-Who-Want-Millionnaire-Ruzzle-Scrabble-Crossword-Compiler-kind-games-but-mine-have-very-many-designs_%7E0105b3055d378ec033?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
I the author of Artschiz Word-and-Number Puzzle Games, have conceptualized using Microsoft PowerPoint,&nbsp;&nbsp;a SOFTWARE for Puzzle Games (requiring accompanying HARDWARE components) containing words, numbers, pictures, graphics and video clips to make easy the playing of the proposed games which are described in further detail on Exhibit A to be shown to potential, qualified programmers​<br /><br /> 1. Program/develop&nbsp;&nbsp;software and the hardware components and, according to the specifications and instructions of the client, must have components that can easily be serviced and maintained anywhere in the world.<br /> 2. Divide work into phases (3 one-month Phases suggested by Author/creator) and deliver fully-tested, playable game sets every month<br /> 3. Program for web and downloadable apps game sets for the general public, and for students in kindergarten, pimary, secondary and tertiary educatuional levels<br /> 4. Prepare and submit to author (Client) transaction outline stating project milestones <br /> 5. The Developer shall afterward give the Client User&rsquo;s Guides (Manuals &ndash; digital and print) and ample time to ask questions and explore the software and hardware developed and their functionality until the Client understands all that there is in the use of the software and hardware so designed.<br /> 7. Be ready to add design and other industry-standard values to make the finished work internationally marketable<br /> 6. The Developer agrees to respond to any reasonable request for assistance made by the Client regarding the software and the hardware component within an agreed time frame when necessary.<br /><br /> ​<br /><br /> 1. Ability to build or, if such already exists, lease a search.game engine to generate games categories in the Client&#039;s many designs and shapes.&nbsp;&nbsp;Knowledge and skills with games like &#039;Who Wants to Be A Millionaire&#039;, Scrabble, Crossword Compiler, Ruzzle, will be useful.<br /> 2. Other knowledge and skills:<br /> a.    Array<br /> b.    Pattern matching<br /> c.    Sequence theory<br /> d.    Matrix theory<br /> e.    Regular expression<br /> f.    Java Script<br /> g.    Geometry <br /><br /><br /><b>Budget</b>: $1,000 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Game Development<br /><b>Skills</b>: C++, Game Programming, Graphic Design, JavaScript, Mobile App Development, Web Design <br /><b>Country</b>: Nigeria<br /><a href="https://www.upwork.com/jobs/GAME-PROGRAMMING-FOR-WEB-AND-GAME-DOWNLOADABLE-APPS-REQUIRED-FOR-EXAMPLE-Who-Want-Millionnaire-Ruzzle-Scrabble-Crossword-Compiler-kind-games-but-mine-have-very-many-designs_%7E0105b3055d378ec033?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Tue, 06 Dec 2016 21:23:29 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/GAME-PROGRAMMING-FOR-WEB-AND-GAME-DOWNLOADABLE-APPS-REQUIRED-FOR-EXAMPLE-Who-Want-Millionnaire-Ruzzle-Scrabble-Crossword-Compiler-kind-games-but-mine-have-very-many-designs_%7E0105b3055d378ec033?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[ Looking for Experienced SQA Engineer - Upwork ]]>
</title>
<link>
https://www.upwork.com/jobs/Looking-for-Experienced-SQA-Engineer_%7E01c2999e1c9a127563?source=rss
</link>
<description>
<![CDATA[
Credit Card Compare (www.creditcardcompare.com.au) is looking for an experienced and proven software quality assurance engineer.<br /><br /> You will play an important role in our existing development team and report to the product manager.<br /><br /> This is a unique opportunity to be part of a geographically distributed team at an established and fast-growing digital company operating in the financial services industry.<br /><br /> Experience:<br /> You have 3 - 5 years experience as a software quality assurance engineer.<br /><br /> Professional abilities:<br /> &bull; Selenium, Jenkins, and similar<br /> &bull; Python and Django<br /> &bull; CSS and Javascript<br /> &bull; NGINX and MySQL<br /> &bull; AWS (EC2, S3, CloudFront, RDS)<br /> &bull; Mercurial and Fabric<br /><br /> Personal skills:<br /> &bull; Relentlessly high standards<br /> &bull; Excellent time management<br /> &bull; Organised and dynamic<br /> &bull; Comfortable with large datasets<br /> &bull; Willing to adopt new technologies<br /><br /> What you&rsquo;ll be doing (Duties):<br /> &bull; Produce test scenarios, user stories and cases<br /> &bull; Write test scripts, preferably with Python, and automate tests to avoid introducing regressions<br /> &bull; Raise bugs with examples and steps to reproduce<br /> &bull; Recommend testing tools and technologies related to software quality, testing and deployment<br /><br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; QA &amp; Testing<br /><b>Skills</b>: Automated Testing, Mobile App Testing, Performance Testing, Software QA Testing, Software Testing, Web Testing <br /><b>Country</b>: Australia<br /><a href="https://www.upwork.com/jobs/Looking-for-Experienced-SQA-Engineer_%7E01c2999e1c9a127563?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Credit Card Compare (www.creditcardcompare.com.au) is looking for an experienced and proven software quality assurance engineer.<br /><br /> You will play an important role in our existing development team and report to the product manager.<br /><br /> This is a unique opportunity to be part of a geographically distributed team at an established and fast-growing digital company operating in the financial services industry.<br /><br /> Experience:<br /> You have 3 - 5 years experience as a software quality assurance engineer.<br /><br /> Professional abilities:<br /> &bull; Selenium, Jenkins, and similar<br /> &bull; Python and Django<br /> &bull; CSS and Javascript<br /> &bull; NGINX and MySQL<br /> &bull; AWS (EC2, S3, CloudFront, RDS)<br /> &bull; Mercurial and Fabric<br /><br /> Personal skills:<br /> &bull; Relentlessly high standards<br /> &bull; Excellent time management<br /> &bull; Organised and dynamic<br /> &bull; Comfortable with large datasets<br /> &bull; Willing to adopt new technologies<br /><br /> What you&rsquo;ll be doing (Duties):<br /> &bull; Produce test scenarios, user stories and cases<br /> &bull; Write test scripts, preferably with Python, and automate tests to avoid introducing regressions<br /> &bull; Raise bugs with examples and steps to reproduce<br /> &bull; Recommend testing tools and technologies related to software quality, testing and deployment<br /><br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; QA &amp; Testing<br /><b>Skills</b>: Automated Testing, Mobile App Testing, Performance Testing, Software QA Testing, Software Testing, Web Testing <br /><b>Country</b>: Australia<br /><a href="https://www.upwork.com/jobs/Looking-for-Experienced-SQA-Engineer_%7E01c2999e1c9a127563?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Mon, 28 Nov 2016 01:21:13 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Looking-for-Experienced-SQA-Engineer_%7E01c2999e1c9a127563?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[ Senior Software Engineer - Clojure - Upwork ]]>
</title>
<link>
https://www.upwork.com/jobs/Senior-Software-Engineer-Clojure_%7E01affe039024f23e89?source=rss
</link>
<description>
<![CDATA[
Talentica is looking for a full-stack Senior Clojure developer who will lead various aspects of the platform&rsquo;s technology and manage the implementation of the product roadmap:<br /><br /> What this role entails:<br /><br /> Developing intelligent and scalable engineering solutions from scratch<br /> Partnering with the customers to share product vision &amp;amp; goals<br /> Working on high/low-level product designs &amp;amp; roadmaps along with a team of ace developers<br /> Building products using bleeding-edge technologies on functional programming languages like Clojure, Python, Lisp, Erlang etc<br /> Building cool products for customers in Media, E-commerce, Mobile, Social networking, and lots more<br /> Experiencing Greenfield development &ndash; see a product from concept to going live &ndash; turn ideas to success! <br /><br /> What we need:<br /><br /> Have between 3 to 5 years of IT experience on working with Clojure and ClojureScript OR&nbsp;&nbsp;experience working with another LISP dialect<br /> Have a penchant for solving complex and interesting problems with functional programming techniques.<br /> A solid foundation in computer science, with strong competencies in data structures, algorithms, and software design.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web &amp; Mobile Design<br /><b>Country</b>: India<br /><a href="https://www.upwork.com/jobs/Senior-Software-Engineer-Clojure_%7E01affe039024f23e89?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Talentica is looking for a full-stack Senior Clojure developer who will lead various aspects of the platform&rsquo;s technology and manage the implementation of the product roadmap:<br /><br /> What this role entails:<br /><br /> Developing intelligent and scalable engineering solutions from scratch<br /> Partnering with the customers to share product vision &amp;amp; goals<br /> Working on high/low-level product designs &amp;amp; roadmaps along with a team of ace developers<br /> Building products using bleeding-edge technologies on functional programming languages like Clojure, Python, Lisp, Erlang etc<br /> Building cool products for customers in Media, E-commerce, Mobile, Social networking, and lots more<br /> Experiencing Greenfield development &ndash; see a product from concept to going live &ndash; turn ideas to success! <br /><br /> What we need:<br /><br /> Have between 3 to 5 years of IT experience on working with Clojure and ClojureScript OR&nbsp;&nbsp;experience working with another LISP dialect<br /> Have a penchant for solving complex and interesting problems with functional programming techniques.<br /> A solid foundation in computer science, with strong competencies in data structures, algorithms, and software design.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web &amp; Mobile Design<br /><b>Country</b>: India<br /><a href="https://www.upwork.com/jobs/Senior-Software-Engineer-Clojure_%7E01affe039024f23e89?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Fri, 25 Nov 2016 12:14:17 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Senior-Software-Engineer-Clojure_%7E01affe039024f23e89?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Uber for X Android &amp;amp; iOS App Development - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Uber-for-Android-amp-iOS-App-Development_%7E017e837bc0b117f805?source=rss
</link>
<description>
<![CDATA[
I need to build an Uber for Babysitters App.<br /><br /> Attached are the requirements - looking forward to your bids! Basing on a clone script is fine.<br /><br /> I need native iOS and Android Apps.<br /><br /> I will most likely provide screenshots that detail the functionality. <br /><br /><br /><b>Budget</b>: $3,000 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Mobile Development<br /><b>Country</b>: United Kingdom<br /><a href="https://www.upwork.com/jobs/Uber-for-Android-amp-iOS-App-Development_%7E017e837bc0b117f805?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
I need to build an Uber for Babysitters App.<br /><br /> Attached are the requirements - looking forward to your bids! Basing on a clone script is fine.<br /><br /> I need native iOS and Android Apps.<br /><br /> I will most likely provide screenshots that detail the functionality. <br /><br /><br /><b>Budget</b>: $3,000 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Mobile Development<br /><b>Country</b>: United Kingdom<br /><a href="https://www.upwork.com/jobs/Uber-for-Android-amp-iOS-App-Development_%7E017e837bc0b117f805?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Fri, 25 Nov 2016 03:48:26 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Uber-for-Android-amp-iOS-App-Development_%7E017e837bc0b117f805?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Need help resolving redirections issue on mobile version of site - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Need-help-resolving-redirections-issue-mobile-version-site_%7E0147695a214ba34b5e?source=rss
</link>
<description>
<![CDATA[
It appears that one of the (many) scripts running on my site is causing redirects when viewing the page on mobile and only with cellular data (3g/4g) - not WiFi. With WiFi enabled, no redirects.<br /><br /> So, if I visit my website through a mobile device (say, iPhone) using my cellular data (4g), it starts redirecting me to other (advertising/spam) websites.<br /><br /> I need someone to track the script that is causing this behaviour so that I can&nbsp;&nbsp;update/remove it.<br /><br /><b>Budget</b>: $40 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Skills</b>: HTML, JavaScript, Scripting, Software Debugging, Website Development <br /><b>Country</b>: Greece<br /><a href="https://www.upwork.com/jobs/Need-help-resolving-redirections-issue-mobile-version-site_%7E0147695a214ba34b5e?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
It appears that one of the (many) scripts running on my site is causing redirects when viewing the page on mobile and only with cellular data (3g/4g) - not WiFi. With WiFi enabled, no redirects.<br /><br /> So, if I visit my website through a mobile device (say, iPhone) using my cellular data (4g), it starts redirecting me to other (advertising/spam) websites.<br /><br /> I need someone to track the script that is causing this behaviour so that I can&nbsp;&nbsp;update/remove it.<br /><br /><b>Budget</b>: $40 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Skills</b>: HTML, JavaScript, Scripting, Software Debugging, Website Development <br /><b>Country</b>: Greece<br /><a href="https://www.upwork.com/jobs/Need-help-resolving-redirections-issue-mobile-version-site_%7E0147695a214ba34b5e?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Wed, 23 Nov 2016 12:52:44 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Need-help-resolving-redirections-issue-mobile-version-site_%7E0147695a214ba34b5e?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Automation Testing, Selenium, mobile testing - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Automation-Testing-Selenium-mobile-testing_%7E01c2e6cb8f74f85ef1?source=rss
</link>
<description>
<![CDATA[
Experience in software development industry for Mobile (Android &amp;amp; iOS), Web Application and API testing, write automated test scripts (Selenium).<br /><br /> Product testing (functional testing, regression testing, acceptance testing, load testing), Android and cloud-based software testing.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; QA &amp; Testing<br /><b>Skills</b>: Automated Testing, Functional Testing, Mobile App Testing, Performance Testing, Selenium, Selenium WebDriver, Software QA Testing, Software Testing, Usability Testing, Web Testing <br /><b>Country</b>: India<br /><a href="https://www.upwork.com/jobs/Automation-Testing-Selenium-mobile-testing_%7E01c2e6cb8f74f85ef1?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Experience in software development industry for Mobile (Android &amp;amp; iOS), Web Application and API testing, write automated test scripts (Selenium).<br /><br /> Product testing (functional testing, regression testing, acceptance testing, load testing), Android and cloud-based software testing.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; QA &amp; Testing<br /><b>Skills</b>: Automated Testing, Functional Testing, Mobile App Testing, Performance Testing, Selenium, Selenium WebDriver, Software QA Testing, Software Testing, Usability Testing, Web Testing <br /><b>Country</b>: India<br /><a href="https://www.upwork.com/jobs/Automation-Testing-Selenium-mobile-testing_%7E01c2e6cb8f74f85ef1?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Tue, 22 Nov 2016 06:03:25 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Automation-Testing-Selenium-mobile-testing_%7E01c2e6cb8f74f85ef1?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Automation QA engineer for application is needed (Selenium, Java) - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Automation-engineer-for-application-needed-Selenium-Java_%7E01086800cb272c6e66?source=rss
</link>
<description>
<![CDATA[
Hi, <br /> We are looking for an experienced automation engineer to start writing tests for Web application using Selenium and Java. <br /> For mobile we need Calabash/Cucumber expert.<br /><br /> What we require<br /> &bull; A suite of automated regression testing scripts to be created which we can automatically run on the test version of our web application<br /> &bull; Develop new scripts in line with new functionality<br /> &bull; Created using Selenium or another widely-adopted industry-standard <br /> automated testing tool <br /> &bull; Testing on multiple browsers, resolutions and devices<br /> &bull; Create Calabash/Cucumber scripts to run tests on iOS/Android devices<br /> &bull; Make any suggestions for later automation the site functionality if needed<br /><br /> Qualifications<br /> &bull; Minimum 4 years experience in Software Testing and Quality Assurance. This experience must include hands on experience in testing Software Products and Web Based Applications<br /> &bull; Knowledge of test processes and methodologies<br /> tools and technology<br /> &bull; Experience designing and implementing automating test cases, executing tests, monitoring results and reporting defects<br /> &bull; Ability to understand functional/technical specifications and analyze data and output logs<br /> &bull; Experience with performance and security testing will be a plus.<br /> &bull; Excellent oral and written communication skills<br /><br /> Please include within your response some unique content which demonstrates you have read this brief in full, along with your standard response. Please message us with any questions.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; QA &amp; Testing<br /><b>Skills</b>: Automated Testing, Cucumber, Java, Selenium <br /><b>Country</b>: Ukraine<br /><a href="https://www.upwork.com/jobs/Automation-engineer-for-application-needed-Selenium-Java_%7E01086800cb272c6e66?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Hi, <br /> We are looking for an experienced automation engineer to start writing tests for Web application using Selenium and Java. <br /> For mobile we need Calabash/Cucumber expert.<br /><br /> What we require<br /> &bull; A suite of automated regression testing scripts to be created which we can automatically run on the test version of our web application<br /> &bull; Develop new scripts in line with new functionality<br /> &bull; Created using Selenium or another widely-adopted industry-standard <br /> automated testing tool <br /> &bull; Testing on multiple browsers, resolutions and devices<br /> &bull; Create Calabash/Cucumber scripts to run tests on iOS/Android devices<br /> &bull; Make any suggestions for later automation the site functionality if needed<br /><br /> Qualifications<br /> &bull; Minimum 4 years experience in Software Testing and Quality Assurance. This experience must include hands on experience in testing Software Products and Web Based Applications<br /> &bull; Knowledge of test processes and methodologies<br /> tools and technology<br /> &bull; Experience designing and implementing automating test cases, executing tests, monitoring results and reporting defects<br /> &bull; Ability to understand functional/technical specifications and analyze data and output logs<br /> &bull; Experience with performance and security testing will be a plus.<br /> &bull; Excellent oral and written communication skills<br /><br /> Please include within your response some unique content which demonstrates you have read this brief in full, along with your standard response. Please message us with any questions.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; QA &amp; Testing<br /><b>Skills</b>: Automated Testing, Cucumber, Java, Selenium <br /><b>Country</b>: Ukraine<br /><a href="https://www.upwork.com/jobs/Automation-engineer-for-application-needed-Selenium-Java_%7E01086800cb272c6e66?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Sat, 19 Nov 2016 14:13:29 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Automation-engineer-for-application-needed-Selenium-Java_%7E01086800cb272c6e66?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
Education agency website design with e commerce (payment process) and multiple languages - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/Education-agency-website-design-with-commerce-payment-process-and-multiple-languages_%7E01c3a1a1b4dbc83b72?source=rss
</link>
<description>
<![CDATA[
Technical Features:<br /><br /> 1.    Host: Host papa<br /> 2.    Professionally designed Layouts and high resolution images for the site<br /> 3.    Search Engine Friendly URLs&nbsp;&nbsp;&nbsp;( meaning no numbers at the end of the web address)<br /> 4.    Must be on hostpapa during development phase<br /> 5.    Technology Used: PHP, HTML, CSS<br /> 6.    CMS: Word Press<br /> 7.    Operating System: Linux Based or others<br /> 8.    Database: MySQL or others (must be easy use)<br /> 9.    Scripting Language: Java Script and Ajax<br /> 10.    Web Server: Apache or any other easy use server (open to suggestion but it must be open and user friendly)<br /> 11.    Integrate WPML ( not just plugin) to implement multilingual functionality- <br /> &bull;    Chinese traditional<br /> &bull;    Chinese simplified <br /> &bull;    Japanese<br /> &bull; Korean<br /> &bull;    German<br /> &bull;    French<br /> &bull;    Spanish and <br /> &bull;    the capability to able to be added a new language if needed. <br /> (** http://www.toptenreviews.com/business/software/best-translation-software/ any of these kind tools which provides <br /> 12.    No extra cost omore accurate translation)<br /> 13.    Using WPML (lifetime usage license); NO GOOGLE TRANSLATOR/ NO any PLUGIN<br /> 14.    Live chat (Online consultant)<br /> 15.    SKYPE<br /> 16.    QR code for your company URL (domain URL)<br /> 17.    Tailor made images for EPIC website. <br /> 18.    Responsive: Website will full responsive which compatible to PC/Laptop, All Smart Mobiles Phones, <br /> 19.    Marketing promotion facilities (SEO) and digital marketing enabled<br /> 20.    Able to load video/e documents<br /> 21.    IT Security<br /> 22.    Online courses (trials) exercises<br /> 23.    Search function on the top for site search<br /> 24.    E-Commerce feature i.e payment gateway integration via PayPal/visa/master/bank transfer &hellip;etc. with receipt /invoice generation<br /> 25.    Others (details to be provided)<br /><br /><br /><b>Budget</b>: $250 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Skills</b>: Ecommerce Platform Development, PHP, Web Design <br /><b>Country</b>: Australia<br /><a href="https://www.upwork.com/jobs/Education-agency-website-design-with-commerce-payment-process-and-multiple-languages_%7E01c3a1a1b4dbc83b72?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Technical Features:<br /><br /> 1.    Host: Host papa<br /> 2.    Professionally designed Layouts and high resolution images for the site<br /> 3.    Search Engine Friendly URLs&nbsp;&nbsp;&nbsp;( meaning no numbers at the end of the web address)<br /> 4.    Must be on hostpapa during development phase<br /> 5.    Technology Used: PHP, HTML, CSS<br /> 6.    CMS: Word Press<br /> 7.    Operating System: Linux Based or others<br /> 8.    Database: MySQL or others (must be easy use)<br /> 9.    Scripting Language: Java Script and Ajax<br /> 10.    Web Server: Apache or any other easy use server (open to suggestion but it must be open and user friendly)<br /> 11.    Integrate WPML ( not just plugin) to implement multilingual functionality- <br /> &bull;    Chinese traditional<br /> &bull;    Chinese simplified <br /> &bull;    Japanese<br /> &bull; Korean<br /> &bull;    German<br /> &bull;    French<br /> &bull;    Spanish and <br /> &bull;    the capability to able to be added a new language if needed. <br /> (** http://www.toptenreviews.com/business/software/best-translation-software/ any of these kind tools which provides <br /> 12.    No extra cost omore accurate translation)<br /> 13.    Using WPML (lifetime usage license); NO GOOGLE TRANSLATOR/ NO any PLUGIN<br /> 14.    Live chat (Online consultant)<br /> 15.    SKYPE<br /> 16.    QR code for your company URL (domain URL)<br /> 17.    Tailor made images for EPIC website. <br /> 18.    Responsive: Website will full responsive which compatible to PC/Laptop, All Smart Mobiles Phones, <br /> 19.    Marketing promotion facilities (SEO) and digital marketing enabled<br /> 20.    Able to load video/e documents<br /> 21.    IT Security<br /> 22.    Online courses (trials) exercises<br /> 23.    Search function on the top for site search<br /> 24.    E-Commerce feature i.e payment gateway integration via PayPal/visa/master/bank transfer &hellip;etc. with receipt /invoice generation<br /> 25.    Others (details to be provided)<br /><br /><br /><b>Budget</b>: $250 <br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Skills</b>: Ecommerce Platform Development, PHP, Web Design <br /><b>Country</b>: Australia<br /><a href="https://www.upwork.com/jobs/Education-agency-website-design-with-commerce-payment-process-and-multiple-languages_%7E01c3a1a1b4dbc83b72?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Fri, 18 Nov 2016 00:01:11 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Education-agency-website-design-with-commerce-payment-process-and-multiple-languages_%7E01c3a1a1b4dbc83b72?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[ Senior Java Developer Needed - Upwork ]]>
</title>
<link>
https://www.upwork.com/jobs/Senior-Java-Developer-Needed_%7E0193a613162227eb17?source=rss
</link>
<description>
<![CDATA[
&bull;    Develop moderate to highly complex architectural designs and software solutions in support of business requirements and in accordance with predetermined software solution design standards<br /> &bull;    Assist in user requirement process, task breakdown, effort estimation and implementation of new software features in an incremental manner using agile methodologies<br /> &bull;    Produce design/functional artefacts<br /> &bull;    Constantly look for opportunities to optimize algorithms and improve the efficiency of the technology<br /> &bull;    Peer review &amp;amp; approve technical work produced by your colleagues<br /> Stay current in the field of software development and research/learn new programming platforms, tools and languages as needed. Out-of-the-box and innovative thinking is highly valued.​<br /><br /> Your technical skills and development abilities will be important to the success of the business platform/website (www.maintenancecare.com). <br /> You will seek to reach high standards of code quality through progressive development methodologies. It will be your responsibility to design, implement, test, integrate different demanding components and work closely with our Chief Technology Officer to maintain the platform. <br /> You will be required to create both functional and technical specifications in support of your designs. This person will be working within a dynamic &amp;amp; creative application development team to build web applications.<br /> This is an excellent opportunity that will provide you with a platform to really impact our business; you&rsquo;ll make sure that best practices are followed.<br /><br /> Job specifics will be discussed with the right candidate.​<br /><br /> We need someone from Canada at this time.&nbsp;&nbsp;Please check out our website to see what we do:<br /> www.MaintenanceCare.com <br /><br /> &bull;    Bachelor&rsquo;s degree in a related field and five years&rsquo; relevant experience OR Master&rsquo;s degree in a related field and three years&rsquo; relevant experience<br /> &bull;    5+ years of experience as a Java developer with mastery of J2EE framework as part of the development of new technologies (Java Web Applications, Servlets, Servlet Filters, JSP, JDBC)<br /> &bull;    Strong core java fundamentals (5+ years of experience)<br /> &bull;    Experience with build tools, preferably Ant and/or Maven <br /> * Knowledge of Unix/Linux (Debian, Mac OS) operating systems and shell scripting. <br /> * Excellent SQL programming skills and database design fundamentals <br /> * Utilizing Object Oriented Programming (OOP) principals <br /> * Knowledge of HTML / CSS, JavaScript, JSON and AJAX <br /> * Knowledge of Apache, Tomcat, JBoss or other web servers.<br /> &bull; Working knowledge developing cross-browser (Firefox, Chrome, Safari, IE, etc.) dynamic web applications using responsive web design <br /> * Familiar with various web design patterns &amp;amp; best design practices <br /> * Familiar with mobile application development (Apple and/or Android). <br /> * Self-motivated individual, enthusiastic and passionate about developing innovative software solutions <br /> * Ability to work and solve problems independently as well as in a team collaborative environment <br /> * Strong written and verbal communication skills <br /> * Team player who is also self-motivated and able to work independently <br /> * Ability to effectively communicate with technical and non-technical personnel alike<br /><br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Skills</b>: AJAX, Apache Tomcat, Core Java, CSS, Debian OS, HTML, J2EE, JavaScript, JBoss, JDBC, json, JSP, Mac OSX Administration, Object Oriented Programming (OOP), Servlet, SQL Programming, Unix, Web Design <br /><b>Country</b>: Canada<br /><a href="https://www.upwork.com/jobs/Senior-Java-Developer-Needed_%7E0193a613162227eb17?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
&bull;    Develop moderate to highly complex architectural designs and software solutions in support of business requirements and in accordance with predetermined software solution design standards<br /> &bull;    Assist in user requirement process, task breakdown, effort estimation and implementation of
]]>
<![CDATA[
new software features in an incremental manner using agile methodologies<br /> &bull;    Produce design/functional artefacts<br /> &bull; Constantly look for opportunities to optimize algorithms and improve the efficiency of the technology<br /> &bull;    Peer review &amp;amp; approve technical work produced by your colleagues<br /> Stay current in the field of software development and research/learn new programming platforms, tools and languages as needed. Out-of-the-box and innovative thinking is highly valued.​<br /><br /> Your technical skills and development abilities will be important to the success of the business platform/website (www.maintenancecare.com). <br /> You will seek to reach high standards of code quality through progressive development methodologies. It will be your responsibility to design, implement, test, integrate different demanding components and work closely with our Chief Technology Officer to maintain the platform. <br /> You will be required to create both functional and technical specifications in support of your designs. This person will be working within a dynamic &amp;amp; creative application development team to build web applications.<br /> This is an excellent opportunity that will provide you with a platform to really impact our business; you&rsquo;ll make sure that best practices are followed.<br /><br /> Job specifics will be discussed with the right candidate.​<br /><br /> We need someone from Canada at this time.&nbsp;&nbsp;Please check out our website to see what we do:<br /> www.MaintenanceCare.com <br /><br /> &bull;    Bachelor&rsquo;s degree in a related field and five years&rsquo; relevant experience OR Master&rsquo;s degree in a related field and three years&rsquo; relevant experience<br /> &bull;    5+ years of experience as a Java developer with mastery of J2EE framework as part of the development of new technologies (Java Web Applications, Servlets, Servlet Filters, JSP, JDBC)<br /> &bull;    Strong core java fundamentals (5+ years of experience)<br /> &bull;    Experience with build tools, preferably Ant and/or Maven <br /> * Knowledge of Unix/Linux (Debian, Mac OS) operating systems and shell scripting. <br /> * Excellent SQL programming skills and database design fundamentals <br /> * Utilizing Object Oriented Programming (OOP) principals <br /> * Knowledge of HTML / CSS, JavaScript, JSON and AJAX <br /> * Knowledge of Apache, Tomcat, JBoss or other web servers.<br /> &bull; Working knowledge developing cross-browser (Firefox, Chrome, Safari, IE, etc.) dynamic web applications using responsive web design <br /> * Familiar with various web design patterns &amp;amp; best design practices <br /> * Familiar with mobile application development (Apple and/or Android). <br /> * Self-motivated individual, enthusiastic and passionate about developing innovative software solutions <br /> * Ability to work and solve problems independently as well as in a team collaborative environment <br /> * Strong written and verbal communication skills <br /> * Team player who is also self-motivated and able to work independently <br /> * Ability to effectively communicate with technical and non-technical personnel alike<br /><br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Web Development<br /><b>Skills</b>: AJAX, Apache Tomcat, Core Java, CSS, Debian OS, HTML, J2EE, JavaScript, JBoss, JDBC, json, JSP, Mac OSX Administration, Object Oriented Programming (OOP), Servlet, SQL Programming, Unix, Web Design <br /><b>Country</b>: Canada<br /><a href="https://www.upwork.com/jobs/Senior-Java-Developer-Needed_%7E0193a613162227eb17?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Thu, 17 Nov 2016 18:20:50 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Senior-Java-Developer-Needed_%7E0193a613162227eb17?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[ Tester Required - Upwork ]]>
</title>
<link>
https://www.upwork.com/jobs/Tester-Required_%7E0135df6b8dcc5ea483?source=rss
</link>
<description>
<![CDATA[
You will play a key role in developing innovative software in a fast-paced, flexible environment where the team works collaboratively with multiple projects in play at one time. As a Software Tester, you will perform a variety of software test activities while learning and participating in all phases of the software development life cycle. <br /><br /> Job Responsibilities:<br /><br /> &bull;    Develop test plans and execute tests for major and minor updates to our software programs and web applications/web portals.<br /> &bull;    Perform all aspects of testing including functional, regression, load, performance and system testing.<br /> &bull;    Facilitate user acceptance testing with end-users as needed.<br /> &bull;    Create and track system defects and test resolutions to defects.<br /> &bull;    Contribute towards development and implementation of an automated testing strategy.<br /> &bull;    Participate in test strategy, test estimation and planning discussions.<br /> &bull;    Create and execute SQL scripts to be used for test validation.<br /> &bull;    Assist with technical artifacts and can engage in technical discussions (I.e. User stories, Scrum meetings, etc.).<br /> &bull;    Document, analyze and communicate test results and assist with defect management.<br /><br /> Qualifications will include:<br /> &bull;    3-5 years of experience as a Software Tester<br /> &bull;    Competent technical skills with strong attention to detail are required<br /> &bull;    Strong verbal and written communication skills with the ability to collaborate in a team environment<br /> &bull;    An independent self‐starter with natural curiosity about how software solutions work in order to solve issues<br /> &bull;    As a successful candidate, you will remain flexible in an ever‐changing environment and work well under pressure of tight deadlines<br /><br /><br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; QA &amp; Testing<br /><b>Skills</b>: Automated Testing, Functional Testing, Manual Test Execution, Mobile App Testing, Software QA Testing, Software Testing, Usability Testing, Web Testing <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Tester-Required_%7E0135df6b8dcc5ea483?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
You will play a key role in developing innovative software in a fast-paced, flexible environment where the team works collaboratively with multiple projects in play at one time. As a Software Tester, you will perform a variety of software test activities while learning and participating in all phases of the software development life cycle. <br /><br /> Job Responsibilities:<br /><br /> &bull;    Develop test plans and execute tests for major and minor updates to our software programs and web applications/web portals.<br /> &bull;    Perform all aspects of testing including functional, regression, load, performance and system testing.<br /> &bull;    Facilitate user acceptance testing with end-users as needed.<br /> &bull;    Create and track system defects and test resolutions to defects.<br /> &bull;    Contribute towards development and implementation of an automated testing strategy.<br /> &bull;    Participate in test strategy, test estimation and planning discussions.<br /> &bull;    Create and execute SQL scripts to be used for test validation.<br /> &bull;    Assist with technical artifacts and can engage in technical discussions (I.e. User stories, Scrum meetings, etc.).<br /> &bull;    Document, analyze and communicate test results and assist with defect management.<br /><br /> Qualifications will include:<br /> &bull;    3-5 years of experience as a Software Tester<br /> &bull;    Competent technical skills with strong attention to detail are required<br /> &bull;    Strong verbal and written communication skills with the ability to collaborate in a team environment<br /> &bull;    An independent self‐starter with natural curiosity about how software solutions work in order to solve issues<br /> &bull;    As a successful candidate, you will remain flexible in an ever‐changing environment and work well under pressure of tight deadlines<br /><br /><br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; QA &amp; Testing<br /><b>Skills</b>: Automated Testing, Functional Testing, Manual Test Execution, Mobile App Testing, Software QA Testing, Software Testing, Usability Testing, Web Testing <br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/Tester-Required_%7E0135df6b8dcc5ea483?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Fri, 11 Nov 2016 20:03:16 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/Tester-Required_%7E0135df6b8dcc5ea483?source=rss
</guid>
</item>
<item>
<title>
<![CDATA[
We need a group of software, web, mobile developers with good ratings and good prices - Upwork
]]>
</title>
<link>
https://www.upwork.com/jobs/need-group-software-web-mobile-developers-with-good-ratings-and-good-prices_%7E0138a689c7d5e3aecc?source=rss
</link>
<description>
<![CDATA[
Business has been great and the company has just started taking on all kinds of customers! We are expanding our software team in india and dallas, and we need the best prices you have on an hourly rate for various services you provide.<br /><br /> databases, ios and android, web, script work, etc...<br /><br /> please provide your team size, and the best prices you can provide on an hourly basis.<br /><br /> we will need anywhere from 100 - 500 hours per month of work... or, if our sales team hits their goals, you could very well be sent 10,000 hours of work.<br /><br /> we will ONLY respond to companies or freelancers who list their prices and capabilities in detail.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Other - Software Development<br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/need-group-software-web-mobile-developers-with-good-ratings-and-good-prices_%7E0138a689c7d5e3aecc?source=rss">click to apply</a>
]]>
</description>
<content:encoded>
<![CDATA[
Business has been great and the company has just started taking on all kinds of customers! We are expanding our software team in india and dallas, and we need the best prices you have on an hourly rate for various services you provide.<br /><br /> databases, ios and android, web, script work, etc...<br /><br /> please provide your team size, and the best prices you can provide on an hourly basis.<br /><br /> we will need anywhere from 100 - 500 hours per month of work... or, if our sales team hits their goals, you could very well be sent 10,000 hours of work.<br /><br /> we will ONLY respond to companies or freelancers who list their prices and capabilities in detail.<br /><br /><br /><b>Posted On</b>: January 07, 2017 18:20 UTC<br /><b>Category</b>: Web, Mobile &amp; Software Dev &gt; Other - Software Development<br /><b>Country</b>: United States<br /><a href="https://www.upwork.com/jobs/need-group-software-web-mobile-developers-with-good-ratings-and-good-prices_%7E0138a689c7d5e3aecc?source=rss">click to apply</a>
]]>
</content:encoded>
<pubDate>Mon, 07 Nov 2016 23:03:27 +0000</pubDate>
<guid>
https://www.upwork.com/jobs/need-group-software-web-mobile-developers-with-good-ratings-and-good-prices_%7E0138a689c7d5e3aecc?source=rss
</guid>
</item>
</channel>
</rss>
'''
Up_Bot = Upwork_Bot(feed=fake_xml)

import feedparser    
from pprint import pprint
class Test(unittest.TestCase):

    '''
    def test_not_my_home_ip(self):
        ip = '45.50.220.30'
        IP = ipgetter.myip()
        self.assertTrue( ip != str(IP), "Failed to hide ip %s" % IP)

    '''    
    def test_upwork_xml_parse(self):
        self.parse_dict = ['rss','channel', 'item']
        bot = Upwork_Bot(fake_xml, target= [i for i in self.parse_dict]
        # assert iterator 
        
    
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_not_my_home_ip']
    unittest.main()